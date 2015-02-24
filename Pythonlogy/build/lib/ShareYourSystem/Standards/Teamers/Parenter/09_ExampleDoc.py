
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyParenter=SYS.ParenterClass(
	).array(
		[
			['&Neurons'],
			[
				{
					'#key':"$E",
					'#map@set':{
						'&Connections':{
							'$EtoI':{

							}
						}
					}
				}
			]	
		]
	)

"""
	.command(
		'+&.values+$.values',
		'#call:parent',
		_AfterWalkBool=True
	).command(
		'+&.values+$.values',
		{
			'#bound:recruit':lambda _InstanceVariable:_InstanceVariable[
					'/Top/NeuronsDict'
				].__setitem__(
					_InstanceVariable.ManagementKeyStr,
					_InstanceVariable
				) 
				if _InstanceVariable['/^/ParentKeyStr']=="Neurons"
				else None,
			'/Top/LayersDict.__setitem__':{
				'#value:#map@get':["/~/ManagementKeyStr",">>self"],
				'#if':[
					('/~/^/ParentKeyStr',SYS.operator.eq,"#direct:Layers")
				]
			}
		}
	)
"""

#print
print('MyParenter is ')
SYS._print(MyParenter)

