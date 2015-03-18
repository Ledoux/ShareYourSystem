#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	)['#map@set'](
			[
				('-Models',[
						('|Parameter',[
							('ModelKeyStrsList',['MultiplyingFirstFloat','MultiplyingSecondFloat'])
						]),
						('|Result',[
							('ModelKeyStrsList',['MultipliedTotalFloat']),
							('ParentingTriggerVariable',['<->/^/|Parameter'])
						])
					]
				)
			]
		)


print(MyParenter['/-Models/|Result'].ParentingTriggerVariable)
print(MyParenter['/-Models/|Parameter'].ParentingTriggerVariable)


#print
print('MyParenter is ')
SYS._print(MyParenter)


