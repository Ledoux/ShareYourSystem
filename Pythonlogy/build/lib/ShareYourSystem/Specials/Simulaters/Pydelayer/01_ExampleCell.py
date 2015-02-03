
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyPydelayer=SYS.PydelayerClass(
	).pydelay(
		#PydelayingKwargVariablesDict
		{
			'eqns':{
				'x' : '(foo(t) + 0.25 * x(t-tau)) / (1.0 + pow(x(t-tau),p)) -0.1*x'
				},
			'params':{
					'tau' : 5,
			    	'p'   : 10
				},
			'supportcode':'''
				double foo(t){
					return cos(t)
				}
			'''

		}
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPydelayer is '+SYS._str(
		MyPydelayer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 
