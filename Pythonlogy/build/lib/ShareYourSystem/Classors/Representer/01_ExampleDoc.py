#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Representer,Attester

#Represent a dict
Dict={
	'ParentDict':
		{
		'ChildDict':
			{
				'MyInt':0
			},
		'MyStr':'hello'
		}
	}

#Represent a TuplesList
TuplesList=[
				(
					'ParentTuplesList',
					[
						(
							'ChildDict',
							{
								'MyInt':0
							}
						)
					]
				),
				('MyStr','hello')
			]

#Definition the AttestedStr
SYS._attest(
	[
		'Dict is'+Representer.represent(Dict),
		'TuplesList is'+Representer.represent(TuplesList)
	]
) 

#Print
