

#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyExpresser=SYS.ExpresserClass(
	).express(
		_ExpressingSymbolStr='c',
		_ExpressingMapBool=True,
		_ExpressingSpecificTagVariablesArray=np.array(
					[
						[{},{'DelayFloat':1.}],
						[{'TransferFunctionStr':'cos'},{}]
					]
				),
		_ExpressingRowTagVariablesArray=np.array(
				[
					{},
					{'TransferFunctionStr':'tanh'}
				]
			),
		_ExpressingColTagVariablesArray=np.array(
				[
					{'SymbolStr':'c0'},
					{'SymbolStr':'c1'}
				]
			)
	)

#Definition the AttestedStr
'''
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
'''

#print
SYS._print(
		[
			"MyExpresser['ExpressedPreExpressionStrsList'] is ",
			MyExpresser['ExpressedPreExpressionStrsList']
		]
	)

#Print
