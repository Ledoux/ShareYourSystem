
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Storers import Grider

#Define a Multiplier class
@Classer.ClasserClass()
class MultiplierClass(Grider.GriderClass):

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
		Grider.GriderClass.__init__(self,**_KwargVariablesDict)
		
	def do_multiply(self):
		
		#set the MultipliedTotalInt
		self.MultipliedTotalInt=self.MultiplyingFirstInt*self.MultiplyingSecondInt


MyMultiplier=MultiplierClass().grid(
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
