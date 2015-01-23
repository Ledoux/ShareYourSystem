#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Tutorials import Incrementer

#Attest the module
Incrementer.IncrementerClass().setAttest(
	Attester.AttesterClass.DeriveClassor.AttestingFolderPathStr
)

#Definition the AttestedStr
SYS._attest(
	[
'Attests file is written and is '+open(
	Attester.AttesterClass.DeriveClassor.AttestingFolderPathStr+'attest_increment.txt'
).read()
	]
) 

#Print
