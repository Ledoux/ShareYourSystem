#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Printer

#Definition of an instance Printer and make it print hello
MyPrinter=Printer.PrinterClass()._print('hello')
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyPrinter is '+SYS._str(MyPrinter)
	]
) 

#Print

