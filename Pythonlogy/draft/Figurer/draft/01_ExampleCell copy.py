
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Ploters import Ploter,Axer,Paneler,Figurer

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


#Print

