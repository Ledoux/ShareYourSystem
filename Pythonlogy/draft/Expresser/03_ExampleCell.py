

#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyExpresser=SYS.ExpresserClass(
	).express(
		_SymbolStr='c',
		_MapBool=True,
		_SpecificTagVariablesArray=np.array(
					[
						[{},{'DelayFloat':1.}],
						[{'TransferFunctionStr':'cos'},{}]
					]
				),
		_RowTagVariablesArray=np.array(
				[
					{},
					{'TransferFunctionStr':'tanh'}
				]
			),
		_ColTagVariablesArray=np.array(
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
