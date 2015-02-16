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
BaseModuleStr="ShareYourSystem.Standards.Objects.Conditioner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
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
									'ConcludingTypesList',
									'ConcludedConditionIsBoolsList',
									'ConcludedIsBool'
								]

	def default_init(self,
				_ConcludingTestVariable=None,
				_ConcludingConditionTuplesList=None,
				_ConcludingTypesList=[type(len),type(type)],
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
		
		#map condition
		self.ConcludedConditionIsBoolsList=map(
				lambda __ConcludingConditionTuple:
				self.condition(
						__ConcludingConditionTuple[0],
						__ConcludingConditionTuple[1],
						__ConcludingConditionTuple[2],
						self.ConcludingTestVariable
					).ConditionedIsBool,
				self.ConcludingConditionTuplesList
			)

		#all
		self.ConcludedIsBool=all(self.ConcludedConditionIsBoolsList)
#</DefineClass>
