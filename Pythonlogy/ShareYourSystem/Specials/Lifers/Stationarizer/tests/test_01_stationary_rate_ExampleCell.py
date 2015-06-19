
#ImportModules
import ShareYourSystem as SYS

#Define
MyStationarizer=SYS.StationarizerClass(
	).stationarize(
		_LateralWeightVariable=[[-1.]],
		_ConstantTimeVariable=[20.,10.]
	)

#print
print('MyStationarizer is ')
SYS._print(MyStationarizer) 


