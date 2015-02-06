

#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Define
PopulationUnitsInt=3

#Definition an instance
MyExpresser=SYS.ExpresserClass(
	).express(
		_MapBool=True,
		_SpecificTagVariablesArray=np.array(
					[[{} for __Int1 in xrange(PopulationUnitsInt)] for __Int2 in xrange(PopulationUnitsInt)]
				),
		_RowTagVariablesArray=np.array(
				[
					{},
					{'TransferFunctionStr':'tanh'}
				]
			),
		_ColTagVariablesArray=np.array(
				[
					{'SymbolStr':'x'+str(__Int)}
					for __Int in xrange(PopulationUnitsInt) 
				]
			),
		_TheoryBool=True
	)

MyExpresser.store()


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
			zip(
				xrange(len(MyExpresser['ExpressedPreExpressionStrsList'])),
				MyExpresser['ExpressedPreExpressionStrsList']
				)
		]
	)

#Print