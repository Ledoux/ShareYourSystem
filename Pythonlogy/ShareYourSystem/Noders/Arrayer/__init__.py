# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Arrayer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Producer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import itertools
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ArrayerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
								'ArrayingCollectionStrsList',
								'ArrayingNodeKeyStrsListsList',
								'ArrayingCollectionClassesList',
								'ArrayingUpdateVariablesList',
								'ArrayedDeriveNodersListsList'
							]

	def default_init(self,
						_ArrayingCollectionStrsList=None,
						_ArrayingNodeKeyStrsListsList=None,
						_ArrayingCollectionClassesList=None,
						_ArrayingUpdateVariablesList=None,
						_ArrayedDeriveNodersListsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_array(self):
		
		#init
		self.ProducedDeriveNodersList=[self]

		#map
		self.ArrayedDeriveNodersListsList=map(
				lambda __ArrayingCollectionStr,__ArrayingNodeKeyStrsList,__ArrayingCollectionClass,__ArrayingUpdateVariable:
				self.__setitem__(
					'ProducedDeriveNodersList',
					SYS.flat(
						map(
							lambda __ProducedDeriveNoder:
							__ProducedDeriveNoder.produce(
								__ArrayingCollectionStr,
								__ArrayingNodeKeyStrsList,
								__ArrayingCollectionClass,
								__ArrayingUpdateVariable
							).ProducedDeriveNodersList,
							self.ProducedDeriveNodersList,
						)
					)
				).ProducedDeriveNodersList,
				self.ArrayingCollectionStrsList,
				self.ArrayingNodeKeyStrsListsList,
				self.ArrayingCollectionClassesList,
				self.ArrayingUpdateVariablesList
			)

#</DefineClass>

