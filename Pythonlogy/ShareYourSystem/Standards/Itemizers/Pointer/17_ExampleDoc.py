
#ImportModules
import ShareYourSystem as SYS

#array original
MyPointer=SYS.PointerClass(
	).set(
		'-Neurons',
		{
			'|E':{
				'array':[
					[
						['-Connections'],
						['|Postlets<->Prelets'],
						['|#direct:_^_|E','|#direct:_^_|I']
					],
					[
						{},
						{},
						{
							'SynapsingBrianKwargVariablesDict':{'pre':'ge+=1.62*mV'},
							'SynapsingProbabilityVariable':0.02
						}
					]
				]
			},
			'|I':{}
		}
	).get('?v')

#print
print('MyPointer is ')
SYS._print(MyPointer)


