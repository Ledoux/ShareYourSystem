
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


Merger instances help for reloading rowed variables from
different tables but with different shaping variables. 
The results is a list of rowed items from merged tables.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Shaper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
Shaper=BaseModule
from ShareYourSystem.Databasers import Tabler,Rower,Recoverer
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MergerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'MergingConditionTuplesList',									
									'MergedRowedDictsList'
								]

	def default_init(self,
					_MergingConditionTuplesList=None, 		
					_MergedRowedDictsList=None,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_find(self):

		#<NotHook>
		#merge first
		self.merge()
		#</NotHook>

		#Bound the FoundRowDictsList with the MergedRowedDictsList one
		self.FoundRowDictsList=self.MergedRowedDictsList

		#<NotHook>
		#find then
		BaseClass.find(self)
		#</NotHook>

	def do_merge(self):

		#debug
		'''
		self.debug(
					('self.',self,[
										'ModeledKeyStr',
										'MergingConditionTuplesList',
										'TabularedKeyStrsList'
									])
				)
		'''

		#Debug
		'''
		print(

				map(
							lambda __TabularedKeyStr:
						__TabularedKeyStr.split(Shaper.ShapingJoiningStr),
						self.TabularedKeyStrsList
					)
			)
		'''
		
		#Bind with MergedShapingDictsList setting
		MergedShapingDictsList=map(
								lambda __StrsList:
								dict(
									map(
											lambda __ShapingStr:
											SYS.getUnSerializedTuple(
												self.NodePointDeriveNoder,
												__ShapingStr.split(
													Shaper.ShapingTuplingStr
												)
											)
											#Remove the suffix and the prefix
											,__StrsList[1:-1] if len(__StrsList)>2 else []
										)
								),
								map(
									lambda __TabularedKeyStr:
									__TabularedKeyStr.split(Shaper.ShapingJoiningStr),
									self.TabularedKeyStrsList
								)
						)

		#debug
		'''
		self.debug('MergedShapingDictsList is '+str(MergedShapingDictsList))
		'''

		#Bind with MergedFilteredShapingDictsList
		MergedFilteredShapingDictsList=SYS.where(
									MergedShapingDictsList,
									self.MergingConditionTuplesList
									)

		#debug
		'''
		self.debug('MergedFilteredShapingDictsList is '+str(MergedFilteredShapingDictsList))
		'''

		#Bind with MergedTablesList setting
		MergedTablesList=SYS.filterNone(
									map(
											lambda __Table,__MergedFilteredShapingDict:
											__Table
											if __MergedFilteredShapingDict!=None
											else None,
											self.TabularedOrderedDict.values(),
											MergedFilteredShapingDictsList
									))
								
		MergedRowedDictsListsList=map(
				lambda __MergedTable:
				map(
						lambda __RowedDict:
						dict(__RowedDict,**{
								'TabledInt':int(
												__MergedTable.name.split(Tabler.TablingOrderStr)[1]
											)
							}
						),
						Rower.getRowedDictsListWithTable(__MergedTable)
					),
				MergedTablesList
			)

		#debug
		'''
		self.debug('MergedRowedDictsListsList is '+str(MergedRowedDictsListsList))
		'''
		
		#Reduce
		if len(MergedRowedDictsListsList)>0:
			self.MergedRowedDictsList=reduce(operator.__add__,MergedRowedDictsListsList)

#</DefineClass>

```

<small>
View the Merger sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Databasers/Merger" target="_blank">Github</a>
</small>

