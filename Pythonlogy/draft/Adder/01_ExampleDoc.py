
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Adder

#Definition an Tree instance
MyAdder=Adder.AdderClass()+[
	[
		('NodeCollectionStr','Tree'),
		('NodeKeyStr','MyTuplesList'),
		('MyStr','Hello')
	],
	{
		'NodeCollectionStr':'Tree',
		'NodeKeyStr':'MyDict',
		'MyOtherStr':'Bonjour'
	},
	Adder.AdderClass().update(
			[
				('NodeCollectionStr','Tree'),
				('NodeKeyStr','MyChildAppender')
			]
		)
]
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyAdder is '+SYS._str(
		MyAdder,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

