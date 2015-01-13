#<ImportSpecificModules>
import ShareYourSystem as SYS
#</ImportSpecificModules>

SimulatingDynamic=SYS.SimulatingDynamicClass().__setitem__(
                    'TestingAttestFunctionStrsList',
                    [
                      #'attest_default', 
                      'attest_output',
                      #'attest_store',
                      #'attest_scan'
                    ]
                  )
#SimulatingDynamic.attest()
#SimulatingDynamic.test()
SimulatingDynamic.output().plotSimulation()