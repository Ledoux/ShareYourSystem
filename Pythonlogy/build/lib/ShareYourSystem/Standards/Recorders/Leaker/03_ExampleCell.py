#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyLeaker=SYS.LeakerClass(
	).mapSet(
		{
			'LeakingUnitsInt':3,
			'-Interactions':{
				'|/':{
				
				}
			}
		}	
	).leak(
	)
	
#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 

