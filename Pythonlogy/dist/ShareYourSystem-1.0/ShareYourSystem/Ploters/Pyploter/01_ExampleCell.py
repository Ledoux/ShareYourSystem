
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Ploters import Paneler,Axer,Ploter,Pyploter

#Definition an instance
MyPyploter=Pyploter.PyploterClass().push(
	[
		(
			'First',Paneler.PanelerClass().push(
					[
						('First',Axer.AxerClass().push(
								[
									('First',Ploter.PloterClass())
								],
								**{'CollectingCollectionStr':'Plotome'}
							)
						),
						('Second',Axer.AxerClass()),
					],
					**{'CollectingCollectionStr':'Axome'}
				)
		),
		(
			'Second',Paneler.PanelerClass().push(
					[
						('First',Axer.AxerClass())
					],
					**{'CollectingCollectionStr':'Axome'}
				)
		)
	],
**{'CollectingCollectionStr':'Panelome'}
).figure()


#Definition the AttestedStr
SYS._attest(
	[
		'MyPyploter is '+SYS._str(
		MyPyploter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
