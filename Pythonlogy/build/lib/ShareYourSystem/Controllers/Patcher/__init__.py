# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Meteorer maps an append
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Controllers.Meteorer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PatcherClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'PatchingKeyStr',
								'PatchedDerivePatchersList'
							]

	def default_init(self,
						_PatchingKeyStr="Default",
						_PatchedDerivePatchersList=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_patch(self):

		#network
		self.network(
			**{
				'VisitingCollectionStrsList':['Components'],
				'RecruitingConcludeConditionTuplesList':[
					(
						'MroClassesList',
						operator.contains,
						SYS.PatcherClass
					)
				]
			}
		)

		#alias
		self.PatchedDerivePatchersList=self.NetworkedDeriveConnectersList

		#import
		from ShareYourSystem.Viewers import Boxer

		#map
		map(
				lambda __PatchedDerivePatcher:
				__PatchedDerivePatcher.collect(
						'Views',
						'Instance',
						Boxer.BoxerClass()
					).CollectingNodeVariable.box(
					),
				[self]+self.PatchedDerivePatchersList
			)

		#box
		#self['<Views>InstanceBoxer'].box()

#</DefineClass>
