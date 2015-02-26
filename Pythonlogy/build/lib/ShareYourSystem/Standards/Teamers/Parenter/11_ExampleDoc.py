
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
						'&PostConnections':{
							'$EtoI':{
								'ParentingTriggerVariable':
								{
									'<->/^/^/$I/&PreConnections':None
									#'MyInt':0
								}
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

