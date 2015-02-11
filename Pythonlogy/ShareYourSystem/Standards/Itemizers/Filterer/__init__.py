# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Filterer pick and 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FiltererClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'FilteringGraspVariable',
									'FilteringGetKeyVariable',
									'FilteredGraspVariable',
									'FilteredGetValueVariable'
								]

	def default_init(self,
				_FilteringGraspVariable=None,
				_FilteringGetKeyVariable=None,
				_FilteredGraspVariable=None,
				_FilteredGetValueVariable=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_filter(self):
			
		#debug
		'''
		self.debug(('self.',self,[
									'ConcludingConditionTuplesList',
									'FilteringGraspVariable'
								])
				)
		'''
		
		#Get
		self.FilteredGraspVariable=self.grasp(
			self.FilteringGraspVariable
		).GraspedAnswerVariable

		#Check
		if self.conclude(
			self.FilteredGraspVariable
		).ConcludedIsBool:

			#debug
			'''
			self.debug(
					(
						'self.',self,[
										'FilteringGetKeyVariable',
										'ConcludedConditionIsBoolsList',
									]+SYS.unzip(
										self.ConcludingConditionTuplesList,[0]
									)
					)
				)
			'''
			
			#Pick
			self.FilteredGetValueVariable=self.__getitem__(
					self.FilteringGetKeyVariable
				)


#</DefineClass>
