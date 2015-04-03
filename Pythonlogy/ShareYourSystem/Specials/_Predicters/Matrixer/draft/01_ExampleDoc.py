
#ImportModules
import ShareYourSystem as SYS

#Define
MyMatrixer=SYS.MatrixerClass(
	).matrix(
		#MatrixingNumpyVariable
		None,
		#MatrixingRowsInt
		5,
		#MatrixingColsInt
		4,
		#MatrixingStatStr
		'norm',
		#MatrixingMeanFloat
		0.,
		#MatrixingStdFloat
		1.,
		#MatrixingNormalisationInt
		1
	)

#print
print('MyMatrixer is')
SYS._print(MyMatrixer)
