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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pather"
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
							#'CommandingGetVariable',
							#'CommandingSetVariable',
							'CommandingOrderStr',
							#'CommandedValueVariablesList',
							#'CommandedSetVariablesList',
						]

	def default_init(
				self,
				_CommandingGetVariable=None,
				_CommandingSetVariable=None,	
				_CommandingOrderStr="AllSetsForEachGrasp",
				_CommandedValueVariablesList=None,
				_CommandedSetVariablesList=None,				
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_command(self):
		"""Collect with _GatheringKeyVariablesList and do a all sets for each with _UpdatingItemVariable"""

		#debug
		'''
		self.debug(("self.",self,['CommandingGetVariable']))
		'''

		#Check
		if type(self.CommandingGetVariable)!=list:
			
			self.CommandingGetVariable=[
				self.CommandingGetVariable
			]

		#Check
		if type(self.CommandingSetVariable)!=list:
			
			#Check
			if hasattr(self.CommandingSetVariable,'items'):

				#items
				self.CommandedSetVariablesList=self.CommandingSetVariable.items()

			else:

				#list
				self.CommandedSetVariablesList=[
					self.CommandingSetVariable
				]

		else:

			#alias
			self.CommandedSetVariablesList=self.CommandingSetVariable

		#map a grasp
		self.CommandedValueVariablesList=map(
				lambda __CommandingGetVariable:
				self[__CommandingGetVariable],
				self.CommandingGetVariable
			)

		#Check for the order
		if self.CommandingOrderStr=="AllSetsForEachGrasp":

			#map
			map(
					lambda __CommandedGraspVariable:
					map(
						lambda __CommandedSetVariable:
						__CommandedGraspVariable.set(
							*__CommandedSetVariable
						),
						self.CommandedSetVariablesList
					),
					self.CommandedValueVariablesList
				)

		elif self.CommandingOrderStr=="EachSetForAllGrasps":

			#map
			map(
					lambda __CommandedSetVariable:
					map(
						lambda __CommandedGraspVariable:
						__CommandedGraspVariable.set(
							*__CommandedSetVariable
						),
						self.CommandedValueVariablesList
					),
					self.CommandedSetVariablesList
				)
#</DefineClass>
