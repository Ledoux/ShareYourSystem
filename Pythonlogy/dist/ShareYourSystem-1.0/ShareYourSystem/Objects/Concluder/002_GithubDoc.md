
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


A Concluder

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Conditioner"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConcluderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ConcludingTestVariable',
									'ConcludingConditionTuplesList',
									'ConcludedConditionIsBoolsList',
									'ConcludedIsBool'
								]

	def default_init(self,
				_ConcludingTestVariable=None,
				_ConcludingConditionTuplesList=None,
				_ConcludedConditionIsBoolsList=None,
				_ConcludedIsBool=True,
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_conclude(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['ConcludingConditionTuplesList']))
		'''
		
		#Apply __getitem__
		self.ConcludedConditionIsBoolsList=map(
				lambda __ConcludingConditionTuple:
				self.condition(
						self.ConcludingTestVariable[
							__ConcludingConditionTuple[0]
						] if type(
							__ConcludingConditionTuple[0])
						in SYS.StrTypesList else __ConcludingConditionTuple[0],
						__ConcludingConditionTuple[1],
						__ConcludingConditionTuple[2]
					).ConditionedIsBool,
				self.ConcludingConditionTuplesList
			)

		#all
		self.ConcludedIsBool=all(self.ConcludedConditionIsBoolsList)

		#Return self
		#return self
#</DefineClass>

```

<small>
View the Concluder sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Objects/Concluder" target="_blank">Github</a>
</small>

