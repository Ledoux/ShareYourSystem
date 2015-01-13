#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Moniter

#Definition of a Moniter instance
MyMoniter=Moniter.MoniterClass().update(
		[
			('MoniteringTrackTuplesList',
				[
					#TypeStr #VariableStr #IndexIntsList #ClockStr
					('State','v',[0,1],'Record')
				]
			)

		]
	)
		
#Definition the AttestedStr
SYS._attest(
					[
						'MyMoniter is '+SYS._str(MyMoniter)
					]
				) 

#Print

