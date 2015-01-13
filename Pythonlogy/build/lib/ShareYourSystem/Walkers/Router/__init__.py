# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Router

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Mobilizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RouterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'RoutingPickKeyVariablesList',
									'RoutedVariablesOrderedDict'
								]

	def default_init(self,
				_RoutingPickKeyVariablesList=None,
				_RoutedVariablesOrderedDict=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_route(self):
			
		#debug
		'''
		self.debug(('self.',self,['WalkingSocketDict','WalkedTopOrderedDict']))
		'''

		#Init
		if 'RouteTopOrderedDict' not in self.WalkedTopOrderedDict:
			self.WalkedTopOrderedDict['RouteTopOrderedDict']=self.WalkingSocketDict['TopVariable'].RoutedVariablesOrderedDict

		#Init
		if 'PickKeyVariablesList' not in self.WalkedTopOrderedDict:
			self.WalkedTopOrderedDict['PickKeyVariablesList']=self.WalkingSocketDict['TopVariable'].RoutingPickKeyVariablesList

		#Pick and set in the dict
		RouteVariablesOrderedDict=collections.OrderedDict()
		map(
				lambda __PickKeyVariable,__PickValueVariable:
				RouteVariablesOrderedDict.update(
					{__PickKeyVariable:__PickValueVariable}
				),
				self.WalkedTopOrderedDict['PickKeyVariablesList'],
				self.pick(self.WalkedTopOrderedDict['PickKeyVariablesList'])
			)

		#debug
		'''
		self.debug(
			(
				'self.WalkedTopOrderedDict ',
				self.WalkedTopOrderedDict,
				[
					'RouteTopOrderedDict',
					'TopIntsList'
				]
			)
		)
		'''

		#set
		Pather.setWithPathVariableAndKeyVariable(
			self.WalkedTopOrderedDict['RouteTopOrderedDict'],
			self.WalkedTopOrderedDict['TopIntsList'],
			RouteVariablesOrderedDict
		)

		#debug
		'''
		self.debug(
					[
						'After set...',
						(
							'self.WalkedTopOrderedDict ',
							self.WalkedTopOrderedDict,
							['RouteTopOrderedDict']
						)
					]
				)
		'''
		

#</DefineClass>
