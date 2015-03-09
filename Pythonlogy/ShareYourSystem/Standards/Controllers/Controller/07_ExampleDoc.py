
#ImportModules
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	)['#map@set'](
		{
			'/-Views/|Run':{
				'-Panels':{
					'#map@set':[
						('|First',{'MyStr':"hello"})
					]
				}
			}
		}
	)

#print
print('MyController is ')
SYS._print(MyController)


#MyController.set('!/-Views/|Run',''