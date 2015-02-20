
#ImportModules
import ShareYourSystem as SYS

#init
SYS.CommanderClass.CountInt=0
SYS.CommanderClass.GrabList=[]

#define and build a chain
MyCommander=SYS.CommanderClass(
	).array(
		[['ACommander','BCommander'],['1Commander','2Commander']],
		{'MyInt':'>>SYS.set(self.__class__,"CountInt",self.__class__.CountInt+1)'}
	).command(
		{
			'ConditionTuplesList':[(type,SYS.operator.eq,SYS.CommanderClass)]
		},
		{
			'execute':{
				'SetValueVariable':">>self.__class__.GrabList.append(self)",
				'ConditionTuplesList':[
					('MyInt',SYS.operator.lt,3)
				]
			}
		}
	)

#print
print('MyCommander is GrabList')
SYS._print(MyCommander.GrabList)





