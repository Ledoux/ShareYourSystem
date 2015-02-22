# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Filterer pick and condition

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
									'FilteringGetVariable',
									'FilteredGraspVariable',
									'FilteredGetValueVariable'
								]

	def default_init(self,
				_FilteringGraspVariable=None,
				_FilteringGetVariable=None,
				_FilteredGraspVariable=None,
				_FilteredGetValueVariable=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_filter(self):
			
		#debug
		'''
		self.debug(('self.',self,[
									'ConcludingConditionVariable',
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
										'FilteringGetVariable',
										'ConcludedConditionIsBoolsList',
									]+SYS.unzip(
										self.ConcludingConditionVariable,[0]
									)
					)
				)
			'''

			#Check
			if type(self.FilteringGetVariable)!=list:

				#get
				self.FilteredGetValueVariable=self.__getitem__(
						self.FilteringGetVariable
					)

			else:

				#map get
				self.FilteredGetValueVariable=self['map*get'](
						self.FilteringGetVariable
					)


#</DefineClass>
