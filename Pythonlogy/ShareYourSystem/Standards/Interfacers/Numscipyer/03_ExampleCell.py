
#ImportModules
import ShareYourSystem as SYS

#Build a norm dense matrix
MyNumscipyer=SYS.NumscipyerClass(
	).numscipy(
		_SizeTuple=(5,5),
		_SymmetryFloat=0.,
		_EigenvalueBool=True
	)

#print
print('MyNumscipyer.NumscipiedRandomFloatsArray is ')
SYS._print(MyNumscipyer.NumscipiedRandomFloatsArray)

MyNumscipyer.view(
	).pyplot(
	)
