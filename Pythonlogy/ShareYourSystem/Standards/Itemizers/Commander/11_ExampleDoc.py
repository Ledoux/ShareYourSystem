
#ImportModules
import ShareYourSystem as SYS

#init
SYS.CommanderClass.CountInt=0

#define and build a chain
MyCommander=SYS.CommanderClass(
	).array(
		[['AArrayer','BArrayer'],['1Arrayer','2Arrayer']],
		#{'MyInt':'>>self.__class__.CountInt+1'}
	)

#print
print('MyCommander is ')
SYS._print(MyCommander)