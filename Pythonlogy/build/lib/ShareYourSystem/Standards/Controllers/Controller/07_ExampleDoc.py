
#ImportModules
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	)['#map@set'](
		{
			'/-Views/|Run':{
				'-Panels':{
					'|A':{
						'-Plots':{
							'|0':{
								'MyStr':"hello"
							}
						}
					}
				}
			}
		}
	)

#print
print('MyController is ')
SYS._print(MyController)

