
#ImportModules
import ShareYourSystem as SYS

#array original
MyArrayer=SYS.ArrayerClass(
	).array(
		[
			["AArrayer","BArrayer"],
			[
				{
					'#key':'1Arrayer',
					'#map@set':{'MyStr':"hello"}
				},
				{
					'#key':'2Arrayer',
					'#map@set':{'MyInt':2}
				}
			]
		]
	)

#Definition the AttestedStr
print('MyArrayer is ')
SYS._print(MyArrayer)

