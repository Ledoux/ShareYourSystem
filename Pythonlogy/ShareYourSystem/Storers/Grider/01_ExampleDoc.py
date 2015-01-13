
#ImportModules

import ShareYourSystem as SYS,Classer
from ShareYourSystem.Functers import Outputer
from ShareYourSystem.Objects import Scanner

#Define a Multiplier class
@Classer.ClasserClass()
class MultiplierClass(Scanner.ScannerClass):

	#Definition
	RepresentingKeyStrsList=[
									'MultiplyingFirstInt',
									'MultiplyingSecondInt',
									'MultipliedTotalInt'
								]
								
	def default_init(self,
						_MultiplyingFirstInt=0,
						_MultiplyingSecondInt=0,
						_MultipliedTotalInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		Scanner.ScannerClass.__init__(self,**_KwargVariablesDict)
		
		#analyze	
		self.analyze(
			['MultiplyingFirstInt','MultiplyingSecondInt'],
			['MultipliedTotalInt']
		)

	@Outputer.OutputerClass()
	def do_multiply(self):
		
		#debug
		'''
		self.debug(('self.',self,['MultiplyingFirstInt','MultiplyingSecondInt']))
		'''

		#set the MultipliedTotalInt
		self.MultipliedTotalInt=self.MultiplyingFirstInt*self.MultiplyingSecondInt

MyMultiplier=MultiplierClass().scan(
		[
			('MultiplyingFirstInt',[0,1,2]),
			('MultiplyingSecondInt',[2,4]),
		]
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyMultiplier is '+SYS._str(
		MyMultiplier,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyMultiplier.hdfview().hdfclose().HdformatedStr
	]
) 

#Print
