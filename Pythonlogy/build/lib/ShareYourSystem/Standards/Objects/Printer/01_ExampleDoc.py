#ImportModules
import ShareYourSystem as SYS

#Definition of an instance Printer and make it print hello
MyPrinter=SYS.PrinterClass()._print('hello')
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyPrinter is '+SYS._str(MyPrinter)
	]
) 

#Print

