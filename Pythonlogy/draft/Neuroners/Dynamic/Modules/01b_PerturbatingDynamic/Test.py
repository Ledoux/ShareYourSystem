#<ImportSpecificModules>
import ShareYourSystem as SYS
#</ImportSpecificModules>

PerturbatingDynamic=SYS.PerturbatingDynamicClass().__setitem__(
                    'TestingAttestFunctionStrsList',
                    [
                      #'attest_default', 
                      'attest_output',
                      #'attest_store',
                      #'attest_scan'
                    ]
                  )
#PerturbatingDynamic.attest()
PerturbatingDynamic.output().plot().show()
#PerturbatingDynamic.test()

#SYS.Dynamic.getNotAutaptingTuplesListWithConnectionsIntAndPairsInt(1000*1000,149850)
