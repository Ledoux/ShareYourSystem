
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Itemizers import Executer

#Definition and update with an exec Str
MyExecuter=Executer.ExecuterClass()

MySecondInt=MyExecuter.__setitem__(
	'MySecondInt',
	'Exec_self.SettingValueVariable=1+1'
).MySecondInt

#Exec is also possible in a getting
GettedValueVariable=MyExecuter['Exec_self.GettedValueVariable=self.MySecondInt-1']
		
#Definition the AttestedStr
SYS._attest(
	[
		'MySecondInt is  '+str(MySecondInt),
		'GettedValueVariable is '+str(GettedValueVariable)
	]
) 

#Print

