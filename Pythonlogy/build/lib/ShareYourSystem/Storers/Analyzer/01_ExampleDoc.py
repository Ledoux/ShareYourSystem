
#ImportModules

import ShareYourSystem as SYS,Classer
from ShareYourSystem.Storers import Analyzer

@Classer.ClasserClass()
class SumerClass(Analyzer.AnalyzerClass):

	#Definition
	RepresentingKeyStrsList=[
									'SumingFirstInt',
									'SumingSecondInt',
									'SumedTotalInt'
								]
								
	def default_init(self,
						_SumingFirstInt=0,
						_SumingSecondInt=0,
						_SumedTotalInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)
						
	@Triggerer.TriggererClass(**{
									'TriggeringConditionTuplesList':[
										('SettingKeyVariable',(SYS.getIsInListBool,[
											'SumingFirstInt',
											'SumingSecondInt'
										]))
									]
								}
							)
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Definition of an instance and analyze it
MySumer=SumerClass().update(
	[
		('SumingFirstInt',1),
		('SumingSecondInt',3)
	]
).analyze()

#Definition the AttestedStr
SYS._attest(
	[
		'MySumer is '+SYS._str(
		MySumer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MySumer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

