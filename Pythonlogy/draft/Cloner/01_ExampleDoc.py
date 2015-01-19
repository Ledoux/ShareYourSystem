#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Cloner

#Definition of an instance Cloner 
MyCloner=Cloner.ClonerClass()
MyCloner.MyInt=1

#clone
MyFirstCloner=MyCloner.clone()
MyFirstCloner.MyInt=2
	
#Definition the AttestedStr
SYS._attest(
					[
						'MyCloner is '+SYS._str(MyCloner),
						'MyFirstCloner is '+SYS._str(MyFirstCloner)
					]
				) 

#Print

