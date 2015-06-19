
#ImportModules
import ShareYourSystem as SYS

#Define
MyTransferer=SYS.TransfererClass(
	).transfer(
		_LateralWeightVariable=[[-1.]],
		_DoStationaryBool=True
	)

#print
print('MyTransferer is ')
SYS._print(MyTransferer) 


