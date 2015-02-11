# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Commander gather Variables to set them with an UpdateList.
The command process can be AllSetsForEach (ie a map of the update succesively for each)
or a EachSetForAll (ie each set is a map of each).

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Grasper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CommanderClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
							#'CommandingGraspVariable',
							#'CommandingUpdateVariable',
							'CommandingOrderStr'
						]

	def default_init(
				self,
				_CommandingGraspVariable=None,
				_CommandingUpdateVariable=None,	
				_CommandingOrderStr="AllUpdatesForEachGrasp",
				_CommandedGraspVariablesList=None,				
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_command(self):
		"""Collect with _GatheringKeyVariablesList and do a all sets for each with _UpdatingItemVariable"""

		#debug
		'''
		self.debug(("self.",self,['CommandingGraspVariable']))
		'''

		#Check
		if type(self.CommandingGraspVariable)!=list:
			
			self.CommandingGraspVariable=[
				self.CommandingGraspVariable
			]

		#Check
		if type(self.CommandingUpdateVariable)!=list:
			
			self.CommandingUpdateVariable=[
				self.CommandingUpdateVariable
			]

		#map a grasp
		self.CommandedGraspVariablesList=map(
				lambda __CommandingGraspVariable:
				self.grasp(
					__CommandingGraspVariable
				).GraspedAnswerVariable,
				self.CommandingGraspVariable
			)

		#Check for the order
		if self.CommandingOrderStr=="AllUpdatesForEachGrasp":

			#For each __GatheredVariable it is updating with _UpdatingItemVariable
			map(
					lambda __CommandedGraspVariable:
					__CommandedGraspVariable.set(
						SYS.MapListClass(
							self.CommandingUpdateVariable
						)
					),
					self.CommandedGraspVariablesList
				)

		elif self.CommandingOrderStr=="EachUpdateForAllGrasps":

			#For each SettingTuple it is setted in _GatheredVariablesList
			map(
					lambda __SettingVariableTuple:
					map(
						lambda __CommandedGraspVariable:
						__CommandedGraspVariable.__setitem__(
							*__SettingVariableTuple
						),
						self.CommandedGraspVariablesList
					),
					self.CommandingUpdateVariable.items() 
					if hasattr(self.CommandingUpdateVariable,'items')
					else self.CommandingUpdateVariable
				)
#</DefineClass>
