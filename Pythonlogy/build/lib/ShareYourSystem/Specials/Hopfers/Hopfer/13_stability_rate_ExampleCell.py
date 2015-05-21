

#ImportModules
import ShareYourSystem as SYS

#Define
MyHopfer=SYS.HopferClass(
	).hopf(
		_LateralWeigthVariable=[[-1.]],
		_DelayTimeVariable=0.,
		_DoStabilityBool=True
	)

#print
print('MyHopfer is ')
SYS._print(MyHopfer) 


"""
import numpy as np

print(np.ndarray.__div__)
"""

"""
#ImportModules
import ShareYourSystem as SYS

#Define
MyHopfer=SYS.HopferClass(
	).hopf(
		_LateralWeigthVariable=[
			[0.,0.],
			[0.,-0.1]
		],
		_DelayTimeVariable=[
			[0.,0.],
			[0.,0.]
		],
		_DecayTimeVariable=[
			0.,
			0.
		],
		_RiseTimeVariable=0.,
		_DoStabilityBool=True
	)

#print
print('MyHopfer is ')
SYS._print(MyHopfer) 
"""

