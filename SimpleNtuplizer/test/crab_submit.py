from CRABClient.UserUtilities import config

config = config()

#config.General.workArea                 = './'
config.General.workArea                 =  'crab_PFcluster'
#config.General.workArea                 =  'crab_PFcluster_v1'

config.General.transferLogs             = False

config.JobType.pluginName               = 'Analysis'
config.JobType.psetName                 = 'runAnalyzer.py'
config.JobType.allowUndistributedCMSSW  = True

#config.Data.inputDBS                    = 'global'
config.Data.inputDBS                    = 'phys03'
config.Data.splitting                   = 'FileBased'
config.Data.unitsPerJob                 = 100

#config.Site.storageSite                 = 'T3_US_FNALLPC'
config.Site.storageSite                 = 'T2_CH_CERN'
#config.Data.outLFNDirBase = '/store/group/phys_egamma/PFClusterCalibration/150_V0_2017/FlatTrees'
#config.Data.outLFNDirBase = '/store/group/phys_egamma/PFClusterCalibration/150_V0_2017/FlatTrees/v1'
config.Data.outLFNDirBase = '/store/group/phys_egamma/PFClusterCalibration/150_V2_2016UL_SJ/FlatTrees/'

if __name__ == '__main__':

    datasets = {
        #'PFClusterPU10To300' : '/DoublePhotonNoMaterial_FlatPt-10To300/shilpi-crab_DoublePhotonNoMaterial_FlatPt-10To300_0to70PU-9c112e244c41f1eee1e8bf19070f2b2a/USER',
        #'PFClusterPU0To10' : '/DoublePhotonNoMaterial_FlatPt-0p01To10/shilpi-crab_DoublePhotonNoMaterial_FlatPt-0p0To10_0to70PU-9c112e244c41f1eee1e8bf19070f2b2a/USER',
        #'PFClusterPU10To300noPU' : '/DoublePhotonNoMaterial_FlatPt-10To300/shilpi-crab_DoublePhotonNoMaterial_FlatPt-10To300_noPU-9c112e244c41f1eee1e8bf19070f2b2a/USER',
        #'PFClusterPU0To10noPU' : '/DoublePhotonNoMaterial_FlatPt-0p01To10/shilpi-crab_DoublePhotonNoMaterial_FlatPt-0p0To10_noPU-9c112e244c41f1eee1e8bf19070f2b2a/USER'


        'PFClusterPU10To300' : '/DoublePhotonNoMaterial_FlatPt-10To300/shilpi-crab_DoublePhotonNoMaterial_FlatPt-10To300_0to70PU-ad6375b0703b017ba138c501a5e17ec8/USER',
        'PFClusterPU0To10' : '/DoublePhotonNoMaterial_FlatPt-0p01To10/shilpi-crab_DoublePhotonNoMaterial_FlatPt-0p0To10_0to70PU-ad6375b0703b017ba138c501a5e17ec8/USER',
        'PFCluster10To300noPU' : '/DoublePhotonNoMaterial_FlatPt-10To300/shilpi-crab_DoublePhotonNoMaterial_FlatPt-10To300_noPU-ad6375b0703b017ba138c501a5e17ec8/USER',
        'PFCluster0To10noPU' : '/DoublePhotonNoMaterial_FlatPt-0p01To10/shilpi-crab_DoublePhotonNoMaterial_FlatPt-0p0To10_noPU-ad6375b0703b017ba138c501a5e17ec8/USER'
       
        }

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    for name, dataset in datasets.iteritems():
        config.General.requestName = name
        config.Data.inputDataset = dataset
        submit(config)
