
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyParenter=SYS.ParenterClass(
	).array(
		[
			['-Neurons'],
			[
				{
					'#key':"|E",
					'#map@set':{
						'-Posts':{
							'|EtoI':{
								'ParentingTriggerVariable':
								[
									'<->/^/^/|I/-PreConnections'
								]
							}
						}
					}
				}
			]	
		]
	).parent(
		_DownBool=True
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

