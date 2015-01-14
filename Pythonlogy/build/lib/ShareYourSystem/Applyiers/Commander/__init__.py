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
BaseModuleStr="ShareYourSystem.Noders.Attentioner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CommanderClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
							#'CommandingUpdateList',
							#'CommandingVariablesList',
							'CommandingOrderStr',
							'CommandingGatherIsBool'
						]

	def default_init(self,
				_CommandingUpdateList=None,	
				_CommandingVariablesList=None, 
				_CommandingOrderStr="AllSetsForEach",				
				_CommandingGatherIsBool=True,
				**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_command(self):
		"""Collect with _GatheringKeyVariablesList and do a all sets for each with _UpdatingItemVariable"""

		#Check
		if self.CommandingGatherIsBool:

			#Get the GatheredVariablesList
			self.gather()

			#debug
			'''
			self.debug(
							('self.',self,[
									'CommandingUpdateList',
									'GatheringVariablesList',
									'GatheredVariablesList'
									]
							)
						)
			'''

			#Check
			if len(self.GatheredVariablesList)>0:

				#Just keep the values
				self.CommandingVariablesList=SYS.flat(SYS.unzip(self.GatheredVariablesList,[1]))

		#debug
		'''
		self.debug(("self.",self,['CommandingVariablesList']))
		'''

		#Check for the order
		if self.CommandingOrderStr=="AllSetsForEach":

			#For each __GatheredVariable it is updating with _UpdatingItemVariable
			map(
					lambda __CommandedVariable:
					__CommandedVariable.update(self.CommandingUpdateList),
					self.CommandingVariablesList
				)

		elif self.CommandingOrderStr=="EachSetForAll":

			#For each SettingTuple it is setted in _GatheredVariablesList
			map(
					lambda __SettingVariableTuple:
					map(
						lambda __CommandedVariable:
						__CommandedVariable.__setitem__(*__SettingVariableTuple),
						self.CommandingVariablesList
						),
					self.CommandingUpdateList.items() 
					if hasattr(self.CommandingUpdateList,'items')
					else self.CommandingUpdateList
				)

		#Return self
		#return self 
#</DefineClass>
