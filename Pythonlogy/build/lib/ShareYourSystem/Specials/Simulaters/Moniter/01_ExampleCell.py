#ImportModules
import ShareYourSystem as SYS

#Definition of a Moniter instance
MyMoniter=SYS.MoniterClass(
	).set(
		'MoniteringTrackTuplesList',
		[
			#TypeStr #VariableStr #IndexIntsList #ClockStr
			('State','v',[0,1],'Record')
		]
	)
		
#Define
print('MyMoniter is ')
SYS._print(MyMoniter)



