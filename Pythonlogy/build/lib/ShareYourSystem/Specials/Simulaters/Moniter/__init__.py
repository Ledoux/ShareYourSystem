# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

A Moniter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MoniterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'MoniteringRecordTimeIndexIntsArray',
								'MoniteringSampleTimeIndexIntsArray',
								'MoniteringVariableStr',
								'MoniteringVariableIndexIntsArray',
								'MoniteringDerivePopulaterVariable',
								'MoniteredTempVariablesArray',
								'MoniteredTotalVariablesArray'
							]
	
	def default_init(self,
						_MoniteringRecordTimeIndexIntsArray=None,
						_MoniteringSampleTimeIndexIntsArray=None,
						_MoniteringVariableStr="IntegratedMonitPreFloatsArray",
						_MoniteringVariableIndexIntsArray=None,
						_MoniteringDerivePopulaterVariable=None,
						_MoniteredTempVariablesArray=None,
						_MoniteredTotalVariablesArray=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_monit(self):

		#Check
		if self.MoniteringDerivePopulaterVariable==None:
			self.MoniteringDerivePopulaterVariable=self.NodePointDeriveNoder

		#debug
		'''
		self.debug(('self.',self,[
								'MoniteringSampleTimeIndexIntsArray',
								'MoniteringVariableIndexIntsArray',
								'MoniteringVariableStr'
							]))
		'''

		#debug
		'''
		import numpy as np
		MoniteredTempCompleteVariablesArray=getattr(
				self.MoniteringDerivePopulaterVariable,
				self.MoniteringVariableStr
			)
		self.debug('np.shape(MoniteredTempCompleteVariablesArray) is '+str(
			np.shape(MoniteredTempCompleteVariablesArray)
			)
		)
		'''

		#pick
		self.MoniteredTempVariablesArray=getattr(
				self.MoniteringDerivePopulaterVariable,
				self.MoniteringVariableStr
			)[
				self.MoniteringVariableIndexIntsArray,
				self.MoniteringSampleTimeIndexIntsArray
			]

		#debug
		'''
		self.debug(
					[
						('self.',self,[
								'MoniteringVariableIndexIntsArray',
								'MoniteringRecordTimeIndexIntsArray',	
								'MoniteredTempVariablesArray'
																]),
						'np.shape(self.MoniteredTotalVariablesArray) is '+str(
							np.shape(self.MoniteredTotalVariablesArray))
					]
				)
		'''

		#set
		VariableLengthInt=len(self.MoniteringVariableIndexIntsArray)
		self.MoniteredTotalVariablesArray[
			self.MoniteringVariableIndexIntsArray,
			self.MoniteringRecordTimeIndexIntsArray
		]=self.MoniteredTempVariablesArray

		#debug
		'''
		self.debug(('self.',self,['MoniteredTotalVariablesArray']))
		'''
		
#</DefineClass>

