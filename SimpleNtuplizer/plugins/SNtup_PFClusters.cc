#include "SimpleNtuplizer.h"

namespace {
  typedef reco::PFCluster::EEtoPSAssociation::value_type EEPSPair;
}

void SimpleNtuplizer::setPFVariables(const edm::Event& iEvent,
				     const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  ////clear all teh vector elements
  nClus_pf        = 0;
  clusrawE_pf     = -99;
  cluscorrE_pf    = -99;
  clusPt_pf       = -99;
  clusEta_pf      = -99;
  clusRho_pf      = -99;
  clusPhi_pf      = -99;
  clusLayer_pf    = -99;
  clusPS1_pf      = -99;
  clusPS2_pf      = -99;
  nvtx_pf         = -99;
  genEnergy_pf    = -99;
  genPt_pf        = -99;
  genEta_pf       = -99;
  genPhi_pf       = -99;
  genStatusFlag_pf= -99;
  ietamod20_pf      = -999;
  iphimod20_pf      = -999;
  tgtvar_pf         = -999;
  nlgtgtvar_pf      = -999;
  nhits_pf          = -999;

  edm::Handle<reco::PFClusterCollection> clustersH;
  iEvent.getByToken(pfLabel_,clustersH);

  //edm::Handle<reco::PFCluster::EEtoPSAssociation> clusterpairH;
  //iEvent.getByToken(pspfLabel_,clusterpairH);

  edm::Handle<edm::ValueMap<reco::GenParticleRef> > clustergenH;
  iEvent.getByToken(genpfLabel_,clustergenH);

  edm::Handle<edm::ValueMap<int> > clusSize;
  iEvent.getByToken(clusSizeLabel_,clusSize);

  edm::Handle<edm::ValueMap<float> > clusPS1;
  iEvent.getByToken(ps1Label_,clusPS1);

  edm::Handle<edm::ValueMap<float> > clusPS2;
  iEvent.getByToken(ps2Label_,clusPS2);

  edm::Handle<reco::VertexCollection> vertices;
  if(doVertex) {
    iEvent.getByToken(vtxToken_, vertices);
    if (vertices->empty()) nPV_ = 0;
    else nvtx_pf = vertices->size();
  }

  // Selective Readout Flags
  edm::Handle<EBSrFlagCollection> ebSrFlags;
  iEvent.getByToken(ebSrFlagToken_, ebSrFlags );
  edm::Handle<EESrFlagCollection> eeSrFlags;
  iEvent.getByToken(eeSrFlagToken_, eeSrFlags );

  ///needed for reading the SR flag
  edm::ESHandle<EcalTrigTowerConstituentsMap> hTriggerTowerMap =
    iSetup.get<IdealGeometryRecord>().getHandle(eTTmapToken_);
  triggerTowerMap_ = hTriggerTowerMap.product();

  //electronics map
  edm::ESHandle< EcalElectronicsMapping > ecalmapping =
    iSetup.get<EcalMappingRcd>().getHandle(ecalmappingToken_);
  elecMap_ = ecalmapping.product();

  ///rho
  edm::Handle< double > rhoH;
  iEvent.getByToken(rhoToken_,rhoH);
  rho_pf = *rhoH;

  if (clustersH.isValid()) {
    // double size = (*clustersH).size();

    size_t iP(0);
    for (auto&& pfc : *clustersH) {

      ///raw energy
      clusrawE_pf = pfc.energy();

      ///corrected energy
      cluscorrE_pf = pfc.correctedEnergy();

      ///pt
      clusPt_pf = pfc.pt();

      ///layer number
      int layerNum = 0;

      PFLayer::Layer layer = pfc.layer();
      if(layer==PFLayer::PS2) layerNum = -12;
      if(layer==PFLayer::PS1) layerNum = -11;
      if(layer==PFLayer::ECAL_ENDCAP) layerNum = -2;
      if(layer==PFLayer::ECAL_BARREL) layerNum = -1;
      if(layer==PFLayer::NONE) layerNum = 0;
      if(layer==PFLayer::HCAL_BARREL1) layerNum = 1;
      if(layer==PFLayer::HCAL_BARREL2) layerNum = 2;

      if(layer==PFLayer::HCAL_ENDCAP) layerNum = 3;
      if(layer==PFLayer::HF_EM) layerNum = 11;
      if(layer==PFLayer::HF_HAD) layerNum = 12;
      if(layer==PFLayer::HGCAL) layerNum = 13;

      clusLayer_pf = layerNum;

      ///position
      auto const & crep = pfc.position();
      double eta = crep.eta();
      double phi = crep.phi();
      double rho = crep.rho();

      clusEta_pf = eta;
      clusPhi_pf = phi;
      clusRho_pf = rho;

      ///ieta, iphi
      //find seed crystal indices
      bool iseb = (pfc.layer()) == (PFLayer::ECAL_BARREL);

      if (iseb) {
	EBDetId ebseed(pfc.seed());
	clusIetaIx_pf = ebseed.ieta();
	clusIphiIy_pf = ebseed.iphi();
      } else {
	EEDetId eeseed(pfc.seed());
	clusIetaIx_pf = eeseed.ix();
	clusIphiIy_pf = eeseed.iy();
      }

      Int_t signiEtaSeed = clusIetaIx_pf > 0 ? +1 : -1;

      ietamod20_pf = abs(clusIetaIx_pf)<=25 ? (clusIetaIx_pf-signiEtaSeed) : (clusIetaIx_pf-26*signiEtaSeed)%20 ;

      iphimod20_pf  = (clusIphiIy_pf-1)%20;

      auto clusterref = edm::Ref<reco::PFClusterCollection>(clustersH, iP++);

      if(!iseb) {

	clusPS1_pf = (*clusPS1)[clusterref];
	clusPS2_pf = (*clusPS2)[clusterref];

      }//if(!iseb)


      ////SR flags
      if(iseb){

	EBSrFlagCollection::const_iterator srf
	  = ebSrFlags->find(readOutUnitOf((EBDetId) pfc.seed()));

	clusFlag_pf = srf->value();
      }

      if(!iseb){
	EESrFlagCollection::const_iterator srf
	  = eeSrFlags->find(readOutUnitOf((EEDetId)pfc.seed()));

	clusFlag_pf = srf->value();
      }

      // gen matching
      //auto clusterref = edm::Ref<reco::PFClusterCollection>(clustersH, iP++);
      auto genpart = (*clustergenH)[clusterref];
      genEnergy_pf = genpart->energy();
      genPt_pf = genpart->pt();
      genEta_pf = genpart->eta();
      genPhi_pf = genpart->phi();


      ////https://github.com/cms-sw/cmssw/blob/CMSSW_9_1_X/DataFormats/HepMCCandidate/interface/GenParticle.h#L65-L103
      UShort_t tmpStatusFlag = 0;
      if (genpart->fromHardProcessFinalState()) setbit(tmpStatusFlag, 0);
      if (genpart->isPromptFinalState())        setbit(tmpStatusFlag, 1);
      if (genpart->isHardProcess()) setbit(tmpStatusFlag, 2);
      if (genpart->fromHardProcessDecayed()) setbit(tmpStatusFlag, 3);
      if (genpart->isPromptDecayed()) setbit(tmpStatusFlag, 4);

      genStatusFlag_pf = tmpStatusFlag;

      clusSize_pf = (*clusSize)[clusterref];


      ///tgtvar_pf
      tgtvar_pf    = log(genEnergy_pf/clusrawE_pf);
      nlgtgtvar_pf = genEnergy_pf/clusrawE_pf;
      if(!iseb)
	{
	  tgtvar_pf    = log( genEnergy_pf/(clusrawE_pf+clusPS1_pf+clusPS2_pf) );
	  nlgtgtvar_pf =  genEnergy_pf/(clusrawE_pf+clusPS1_pf+clusPS2_pf) ;
	}

      nhits_pf = clusSize_pf;

      nClus_pf++;

      pfTree_->Fill();
    }//for (reco::PFClusterCollection::const_iterator pfc=(....))



  }//if (clustersH.isValid())
  else{
    cout<<"Handle not found!!!"<<endl;
  }


}//void SimpleNtuplizer::setPFVariables

EcalTrigTowerDetId SimpleNtuplizer::readOutUnitOf(const EBDetId& xtalId) const{
  return triggerTowerMap_->towerOf(xtalId);
}

EcalScDetId SimpleNtuplizer::readOutUnitOf(const EEDetId& xtalId) const{
  const EcalElectronicsId& EcalElecId = elecMap_->getElectronicsId(xtalId);
  int iDCC= EcalElecId.dccId();
  int iDccChan = EcalElecId.towerId();
  const bool ignoreSingle = true;
  const std::vector<EcalScDetId> id = elecMap_->getEcalScDetId(iDCC, iDccChan, ignoreSingle);
  return id.size()>0?id[0]:EcalScDetId();
}
