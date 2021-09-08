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
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_0.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_1.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_10.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_100.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_101.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_102.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_103.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_104.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_105.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_106.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_107.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_108.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_109.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_11.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_12.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_13.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_14.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_15.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_16.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_17.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_18.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_19.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_2.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_20.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_21.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_22.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_23.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_24.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_25.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_26.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_27.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_28.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_29.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_3.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_30.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_31.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_32.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_33.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_34.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_35.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_36.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_37.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_38.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_39.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_4.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_40.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_41.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_42.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_43.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_44.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_45.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_46.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_47.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_48.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_49.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_5.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_50.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_51.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_52.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_53.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_54.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_55.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_56.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_57.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_58.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_59.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_6.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_60.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_61.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_62.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_63.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_64.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_65.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_66.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_67.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_68.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_69.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_7.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_70.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_71.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_72.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_73.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_74.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_75.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_76.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_77.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_78.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_79.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_8.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_80.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_81.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_82.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_83.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_84.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_85.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_86.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_87.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_88.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_89.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_9.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_90.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_91.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_92.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_93.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_94.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_95.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_96.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_97.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_98.root',
'file:/eos/cms//store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/MINIAOD/EGM-Run3Summer21MiniAOD-00013_99.root'
        #'file:/afs/cern.ch/work/j/jordanm/public/forShilpi/PPD-Run3Summer21MiniAOD-00001.root'
        # 'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/EGM-Run3Summer21MiniAOD-00013_0.root',
        # 'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/EGM-Run3Summer21MiniAOD-00013_1.root',
        # 'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/EGM-Run3Summer21MiniAOD-00013_2.root',
        # 'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/EGM-Run3Summer21MiniAOD-00013_3.root',
        # 'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/EGM-Run3Summer21MiniAOD-00013_4.root'
        #'file:/afs/cern.ch/user/h/hatake/work/public/PF/CMSSW_11_3_2_EGMPFClusterRegression/src/RegressionTreeProducer/SimpleNtuplizer/test/DoublePho_mini.root'
        #'file:../../../MCProd/DoublePho_mini.root'
        #'file:/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/MINIAOD/EGM-Run3Summer21MiniAOD-00013_1.root'
    )
    )

########################################
# Define the analyzer
########################################

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("/eos/cms/store/group/phys_pf/Run3PreparationSamples/EGMRegession/DoublePhotonNoMaterialNoPU/tree/tree_orig.root"),
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
#process.p = cms.Path(process.particleFlowClusterECALMatchedToPhotons)
#process.output_step = cms.EndPath(process.out)
