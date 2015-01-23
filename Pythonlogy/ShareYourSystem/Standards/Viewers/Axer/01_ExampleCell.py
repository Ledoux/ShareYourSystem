
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Ploters import Figurer,Paneler,Axer

#Definition an instance
MyFigurer=Figurer.FigurerClass().push(
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
		'MyFigurer is '+SYS._str(
		MyFigurer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print

