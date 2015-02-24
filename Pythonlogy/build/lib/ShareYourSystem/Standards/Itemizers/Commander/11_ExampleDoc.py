
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
			'#filter':[(0,str.endswith,'Commander')],
			'#scan':'>>self.__dict__.items()',
			'#modify':'>>dict(self.GettedValueVariable).values()'
		},
		{
			'execute':{
				'#value:#get':">>self.__class__.GrabList.append(self)",
				'#if':[
					('MyInt',SYS.operator.lt,2)
				]
			}
		}
	)


#print
print('MyCommander is GrabList')
SYS._print(MyCommander.GrabList)





