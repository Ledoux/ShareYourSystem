
#ImportModules
import ShareYourSystem as SYS

#produce
MyArrayer=SYS.ArrayerClass().array(
		["Sections","Subsections"],
		[
			["A","B"],['1','2']
		],
		[SYS.ArrayerClass,SYS.NoderClass],
		[{'MySectionInt':3},None]
	).array()

#Definition the AttestedStr
SYS._attest(
	[
		'MyProducer is '+SYS._str(
		MyArrayer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print
