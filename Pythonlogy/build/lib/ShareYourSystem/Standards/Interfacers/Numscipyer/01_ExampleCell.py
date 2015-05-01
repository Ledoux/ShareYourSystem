
#ImportModules
import ShareYourSystem as SYS

#Build a norm dense matrix
MyNumscipyer=SYS.NumscipyerClass(
	).numscipy(
		_SizeTuple=(3,2)
	)

#print
print('MyNumscipyer is ')
SYS._print(MyNumscipyer)

#Build a sparse binary matrix
MyNumscipyer=SYS.NumscipyerClass(
	).numscipy(
		_ProbabilityFloat=0.5,
		_SizeTuple=(10,10)
	)

#print
print('MyNumscipyer.NumscipiedRandomFloatsArray is ')
SYS._print(MyNumscipyer.NumscipiedRandomFloatsArray)

