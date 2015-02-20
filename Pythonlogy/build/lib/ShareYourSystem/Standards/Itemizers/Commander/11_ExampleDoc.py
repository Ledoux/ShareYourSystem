
#ImportModules
import ShareYourSystem as SYS

#init
SYS.CommanderClass.CountInt=0

#define and build a chain
MyCommander=SYS.CommanderClass(
	).array(
		[['ACommander','BCommander'],['1Commander','2Commander']],
		{'MyInt':'>>SYS.set(self.__class__,"CountInt",self.__class__.CountInt+1)'}
		#{'MyStr':"kk"}
	)

#print
print('MyCommander is ')
SYS._print(MyCommander)






