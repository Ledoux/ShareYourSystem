
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyExpresser=SYS.ExpresserClass(
	).express(
		#ExpressingInputFloat,
		0.5,
		#ExpressingVariableStr,
		'x',
		#ExpressingDelayFloat,
		5.,
		#ExpressingTransferFunctionStr,
		'tanh',
		#ExpressingOutputFloat,
		2.
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyExpresser is '+SYS._str(
		MyExpresser,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
