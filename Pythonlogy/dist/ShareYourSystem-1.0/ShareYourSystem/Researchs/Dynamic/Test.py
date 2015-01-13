#<ImportSpecificModules>
import ShareYourSystem as SYS
#</ImportSpecificModules>

Dynamic=SYS.DynamicClass().__setitem__(
                    'TestingAttestFunctionStrsList',
                    [
                      #'attest_default', 
                      'attest_output',
                      #'attest_store',
                      #'attest_scan'
                    ]
                  )
#Dynamic.attest()
#Dynamic.test()

#print(SYS.Dynamic.getNotAutaptedTuple((10,10)))
#print(len(SYS.Dynamic.getSelectedSymetricConnections(100,45)))

"""
import itertools

print(list(itertools.product([0,1,2],[0,1,2])))
"""

'''
import numpy as np
#a=np.diag(np.diag(np.array([[1.,2.,3.],[3.,4.,7.],[1.,1.,1.]])))
#print(a)

import matplotlib.pyplot
x=np.arange(-10.,10.,0.1)
matplotlib.pyplot.plot(x,np.tanh(x))
matplotlib.pyplot.plot([0.,0.],[-1.1,1.1],'--',color="black")
matplotlib.pyplot.plot([-10.,10.],[0.,0.],'--',color="black")
matplotlib.pyplot.ylim([-1.1,1.1])
matplotlib.pyplot.show()
'''