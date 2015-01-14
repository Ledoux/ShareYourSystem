
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


A Gatherer is able to pick several times and flat all the results in a one dimension of ItemTuplesList

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Picker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'DoingGetBool':True})
class GathererClass(BaseClass):
	
	def default_init(self,
				_GatheringVariablesList=None,
				_GatheredVariablesList=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_gather(self):
		"""Reduce a map of pick for GatheringVariable being a List or __getitem__ for GatheringVariable being a GettingVariable"""

		#debug
		'''
		self.debug("self.GatheringVariablesList is "+str(self.GatheringVariablesList))
		'''
		
		#Debug
		'''
		for __GatheringVariable in self.GatheringVariablesList:

			if type(__GatheringVariable)==list:

				#Debug 
				print('This is a list')
				print('')

				Variable=zip(
							__GatheringVariable,
							self.pick(__GatheringVariable)
						)
			

			else:

				#Debug 
				print('This is not a list')
				print('')

				Variable=[
					(
						__GatheringVariable,
						self[__GatheringVariable]
					)
				]

			#Debug
			print('l.63 Gatherer')
			print('Variable is ',Variable)
			print('')
		'''


		#Definition the PickedOrGettedVariablesList
		PickedOrGettedVariablesList=map(
						lambda __GatheringVariable:
						zip(
							__GatheringVariable,
							self.pick(__GatheringVariable)
						)
						if type(__GatheringVariable)==list
						else [
								(
									__GatheringVariable,
									self[__GatheringVariable]
								)
							],
						self.GatheringVariablesList
		)

		#debug
		'''
		self.debug(('vars ',vars(),['PickedOrGettedVariablesList']))
		'''

		#Reduce
		if len(PickedOrGettedVariablesList)>0:
			self.GatheredVariablesList=reduce(
						operator.__add__,
						PickedOrGettedVariablesList
					)
		else:
			self.GatheredVariablesList=[]

		#debug
		'''
		self.debug('End of the method')
		'''

		#Return the reduce
		return self.GatheredVariablesList
#</DefineClass>

```

<small>
View the Gatherer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Applyiers/Gatherer)
</small>

