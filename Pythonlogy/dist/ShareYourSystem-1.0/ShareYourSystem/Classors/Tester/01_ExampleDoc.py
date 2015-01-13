#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Tester
from ShareYourSystem.Tutorials import Decrementer

#Attest the module
Decrementer.DecrementerClass().setAttest(
	Tester.TesterClass.DeriveClassor.AttestingFolderPathStr
)
Decrementer.test()

#Print

