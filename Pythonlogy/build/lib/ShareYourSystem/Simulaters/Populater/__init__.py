# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Populater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineClass>
@DecorationClass()
class PopulaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'PopulatingUnitsInt',
								'PopulatingEventCollectionStr',
								'PopulatingStateCollectionStr',
								'PopulatedEventDeriveMonitersList',
								'PopulatedStateDeriveMonitersList',
								'PopulatedPreviousDerivePopulaterVariable',
								'PopulatedStartUnitInt',
								'PopulatedEndUnitInt'
							]

	def default_init(self,
						_PopulatingUnitsInt=0,
						_PopulatingEventCollectionStr='Spikome',
						_PopulatingStateCollectionStr='Variablome',
						_PopulatedEventDeriveMonitersList=None,
						_PopulatedStateDeriveMonitersList=None,
						_PopulatedPreviousDerivePopulaterVariable=None,
						_PopulatedStartUnitInt=0,
						_PopulatedEndUnitInt=0,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#node for init
		self.node(self.PopulatingEventCollectionStr)
		self.node(self.PopulatingStateCollectionStr)

	def do_populate(self):	

		#debug
		self.debug(('self.',self,[
								'PopulatingEventCollectionStr',
								'PopulatingStateCollectionStr'
								]))

		#link
		self.PopulatedEventDeriveMonitersList=getattr(
				self,
				self.PopulatingEventCollectionStr+'CollectionOrderedDict'
			).values()
		self.PopulatedStateDeriveMonitersList=getattr(
				self,
				self.PopulatingStateCollectionStr+'CollectionOrderedDict'
			).values()

		#Check
		if self.NetworkIndexInt>0:
			self.PopulatedPreviousDerivePopulaterVariable=self.NetworkPointDeriveNetworker.NetworkedDeriveConnectersList[
				self.NetworkIndexInt-1
			]
		else:
			self.PopulatedPreviousDerivePopulaterVariable=self

		#sum
		self.PopulatedStartUnitInt=self.PopulatedPreviousDerivePopulaterVariable.PopulatedEndUnitInt
		self.PopulatedEndUnitInt=self.PopulatedStartUnitInt+self.PopulatingUnitsInt


#</DefineClass>
