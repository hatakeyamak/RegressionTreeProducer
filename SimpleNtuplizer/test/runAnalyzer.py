import FWCore.ParameterSet.Config as cms

from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("EenTest")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1 )

process.load('Configuration/EventContent/EventContent_cff')
process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")

#process.GlobalTag = GlobalTag(process.GlobalTag, '113X_mcRun3_2021_realistic_v10', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '120X_mcRun3_2021_realistic_v6', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 

#file_input_list = open('list_input_files_using_my_db.txt', 'r')
file_input_list = open('list_input_files1.txt', 'r')
lines_input_files = file_input_list.readlines()
#
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        lines_input_files
    )
)

readFiles.extend([
	#'/store/mc/Run3Summer21MiniAOD/DoublePhotonNoMaterial_FlatPt-0p01To10/MINIAODSIM/NoPUExt21ZM_Ext21ZM_NoMaterial_120X_mcRun3_2021_realistic_v5-v3/260000/14240a35-21a5-4cee-90be-23799fc683a0.root'
])

#process.source = cms.Source(
#    "PoolSource",
#	fileNames = readFiles,
#    secondaryFileNames = secFiles
#)
#
########################################
# Define the analyzer
########################################

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("tree_noPU.root"),
				   closeFileFast = cms.untracked.bool(True)
)


process.een_analyzer = cms.EDAnalyzer(
    'SimpleNtuplizer',
    vertices            = cms.InputTag("offlineSlimmedPrimaryVertices", ""),
    electrons           = cms.InputTag("slimmedElectrons", ""),
    photons             = cms.InputTag("slimmedPhotons", ""),
    superClustersEB     = cms.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALBarrel"),
    superClustersEE     = cms.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALEndcapWithPreshower"),
    pfLabel             = cms.InputTag("particleFlowClusterECALMatchedToPhotons"),
    rho                 = cms.InputTag("fixedGridRhoFastjetAll", ""),
    genparticles        = cms.InputTag("prunedGenParticles", ""),
    PUInfoInputTag      = cms.InputTag("slimmedAddPileupInfo", ""),
    genEvtInfoInputTag  = cms.InputTag("generator", ""),
    ecalrechitsEB       = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    ecalrechitsEE       = cms.InputTag("reducedEgamma","reducedEERecHits"),
    ebSrFlagCollection  = cms.InputTag("ecalDigis"),
    eeSrFlagCollection  = cms.InputTag("ecalDigis"),
    ps1Label             = cms.InputTag("particleFlowClusterECALMatchedToPhotons","PS1"),
    ps2Label             = cms.InputTag("particleFlowClusterECALMatchedToPhotons", "PS2"),
    
    doElectronTree      = cms.bool(False),
    doPhotonTree        = cms.bool(False),
    doSuperClusterTree  = cms.bool(False),
    doPFClusterTree     = cms.bool(True),
    doVertex            = cms.bool(True),
    doTagAndProbe       = cms.bool(False),
    saveUnmatched       = cms.bool(False),
    isData              = cms.bool(False)

    )

'''
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('try.root'),
                               outputCommands = cms.untracked.vstring('keep *_particleFlowCluster*_*_*')
)
'''
    
process.load('RecoEgamma.EgammaMCTools.pfClusterMatchedToPhotonsSelector_cfi')
process.particleFlowClusterECALMatchedToPhotons = process.pfClusterMatchedToPhotonsSelector.clone()
process.particleFlowClusterECALMatchedToPhotons.genParticleTag = cms.InputTag("prunedGenParticles")
process.particleFlowClusterECALMatchedToPhotons.recHitsEBLabel = cms.InputTag("reducedEgamma","reducedEBRecHits")
process.particleFlowClusterECALMatchedToPhotons.recHitsEELabel = cms.InputTag("reducedEgamma","reducedEERecHits")


process.p = cms.Path(process.particleFlowClusterECALMatchedToPhotons * process.een_analyzer)
#process.output_step = cms.EndPath(process.out)
