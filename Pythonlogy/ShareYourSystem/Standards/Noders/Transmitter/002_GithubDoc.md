
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Transmitter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Networker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class TransmitterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'TransmittingUpdateList',
								'TransmittingCollectionStrsList',
								'TransmittedVariablesList',
								'TransmittingSelfIsBool'
							]

	def default_init(self,
			_TransmittingUpdateList=None,
			_TransmittingCollectionStrsList=None,
			_TransmittingSelfIsBool=True,
			_TransmittedVariablesList=None,
			**_KwargVariablesDict
		):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_transmit(self):

		#debug
		'''
		self.debug(('self.',self,['TransmittingSelfIsBool']))
		'''
		
		#Check
		if self.TransmittingSelfIsBool:

			#update
			self.update(self.TransmittingUpdateList)

		#map
		self.TransmittedVariablesList=SYS.flat(
			map(
				lambda __TransmittingCollectionStr:
				map(
					lambda __DeriveNoderPointer:
					__DeriveNoderPointer.CatchToPointVariable,
					getattr(
						self,
						__TransmittingCollectionStr+'CollectionOrderedDict'
					).values()
				) if hasattr(self,__TransmittingCollectionStr+'CollectionOrderedDict')
				else [],
				self.TransmittingCollectionStrsList
			)
		)

		#command
		self.command(
						self.TransmittingUpdateList,
						self.TransmittedVariablesList,
						_GatherIsBool=False
					)

		#Return self
		#return self

#</DefineClass>


```

<small>
View the Transmitter sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Noders/Transmitter" target="_blank">Github</a>
</small>

