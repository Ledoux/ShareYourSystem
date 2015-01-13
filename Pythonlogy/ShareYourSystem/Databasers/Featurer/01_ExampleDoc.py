
#ImportModules
import tables
import operator

import ShareYourSystem as SYS,Classer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Objects import Structurer
from ShareYourSystem.Databasers import Featurer,Joiner

#Define a Sumer class
@Classer.ClasserClass()
class SumerClass(Structurer.StructurerClass):

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
		Structurer.StructurerClass.__init__(self,**_KwargVariablesDict)
						
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

#Definition of a Sumer instance and configure a results and parameters models
MySumer=SumerClass().update(
			[
				('HdformatingFileKeyStr','Sums.hdf5'),
				(
					'<Database>ParametersFeaturer',
					Featurer.FeaturerClass().update(
						[
							(
								'Attr_ModelingSealTuplesList',
								[
									('SumingFirstInt','SumingFirstInt',tables.Int64Col()),
									('SumingSecondInt','SumingSecondInt',tables.Int64Col())
								]
							),
							('FeaturingAllBool',True)
						]
					)
				),
				(
					'<Database>ResultsJoiner',
					Joiner.JoinerClass().update(
						[
							(
								'Attr_ModelingSealTuplesList',
								[
									('SumedTotalInt','SumedTotalInt',tables.Int64Col())
								]
							),
							('JoiningDownGetKeyStrsList',["ParametersFeaturer"])
						]
					)
				)
			]
		)

#Update and store
MySumer.update(
	[
		('SumingFirstInt',1),
		('SumingSecondInt',3)
	]
)['<Database>ParametersFeaturer'].flush()

#Update and store
MySumer.update(
	[
		('SumingFirstInt',2),
		('SumingSecondInt',4)
	]
)['<Database>ParametersFeaturer'].flush()

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

