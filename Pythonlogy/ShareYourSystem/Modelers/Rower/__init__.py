# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Rower helps to set rowed lines in a Databaser from pointed attributes,
ready then to be flushed in a table.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Tabler"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
#</ImportSpecificModules>

#<DefineFunctions>
def getRowedDictsListWithTable(_Table):
	return map(
			lambda __Row:
			dict(
				zip(
					_Table.colnames,
					map(
						lambda __ColumnStr:
						__Row[__ColumnStr],
						_Table.colnames
					)
				)
			),
			_Table.iterrows()
		)
#</DefineFunctions>


#<DefineClass>
@DecorationClass(
	#**{'ClassingSwitchMethodStrsList':["row"]}
)
class RowerClass(
					BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
								'RowingGetStrsList',
								'RowedGetStrToColumnStrOrderedDict',
								'RowedColumnStrsList',																										
								'RowedPickOrderedDict',
								'RowedIsBoolsList',
								'RowedIsBool',
								'RowedIndexInt'
							]

	def default_init(
					self,
					_RowingGetStrsList={
							'DefaultingSetType':property,
							'PropertizingInitVariable':[],
							'PropertizingDocStr':''
					},
					_RowedGetStrToColumnStrOrderedDict=None,
					_RowedColumnStrsList=None,																
					_RowedPickOrderedDict=None, 
					_RowedIsBoolsList=None,	
					_RowedIsBool=False,
					_RowedIndexInt=-1,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def setDatabasingSealTuplesList(self,_SettingValueVariable):

		#debug
		'''
		self.debug(
					[
						'Before setting DatabasingSealTuplesList',
						('self.',self,['DatabasingSealTuplesList']),
						'_SettingValueVariable is '+str(_SettingValueVariable)
					]
				)
		'''

		#set
		self._DatabasingSealTuplesList=_SettingValueVariable

		#debug
		'''
		self.debug(
					[
						'After',
						('self.',self,['DatabasingSealTuplesList']),
						'We bind with RowedGetStrToColumnStrOrderedDict setting',
					]
				)
		'''

		#Bind with RowedGetStrToColumnStrOrderedDict setting
		self.RowedGetStrToColumnStrOrderedDict=collections.OrderedDict(
				map(
					lambda _DatabasingSealTuple:
					(_DatabasingSealTuple[0],_DatabasingSealTuple[1]),
					self._DatabasingSealTuplesList
					)
				)

		#debug
		'''
		self.debug(
					[
						('self.',self,['RowedGetStrToColumnStrOrderedDict'])
					]
				)
		'''

	DatabasingSealTuplesList=property(
									BaseClass.DatabasingSealTuplesList.fget,
									setDatabasingSealTuplesList,
									BaseClass.DatabasingSealTuplesList.fdel,
									BaseClass.DatabasingSealTuplesList.__doc__
								)

	def setRowingGetStrsList(self,_SettingValueVariable):
		
		#debug
		'''
		self.debug('_SettingValueVariable '+str(_SettingValueVariable))
		'''

		#set
		self._RowingGetStrsList=_SettingValueVariable

		#debug
		'''
		self.debug(
						[
							'bind with RowedColumnStrsList setting',
							('self.',self,['RowedGetStrToColumnStrOrderedDict'])
						]
					)
		'''
		
		#Bind with 
		self.RowedColumnStrsList=map(
				lambda __RowingGetStr:
				self.RowedGetStrToColumnStrOrderedDict[__RowingGetStr],
				_SettingValueVariable
			)

		#debug
		'''
		self.debug(('self.',self,['RowedColumnStrsList']))
		'''

	#@Alerter.AlerterClass()
	#@Hooker.HookerClass(**{'HookingBeforeVariablesList':[{'CallingMethodStr':"table"}]})
	def do_row(self):
		""""""
	
		#<NotHook>
		#table then
		self.table()
		#</NotHook>
		
		#Check	
		if self.NodePointDeriveNoder!=None:
			
			#debug
			'''
			self.NodePointDeriveNoder.debug('ParentSpeaking...')
			'''

			#Update
			self.RowedPickOrderedDict.update(
				zip(
					self.RowedColumnStrsList,
					self.NodePointDeriveNoder.pick(self.RowingGetStrsList)
				)
			)

			#debug
			'''
			self.debug(('self.',self,[
									'RowedPickOrderedDict',
									'TabledTable'
								]))
			'''

			#Check if it was already rowed
			self.RowedIsBoolsList=map(
					lambda __Row:
					all(
						map(
								lambda __RowedItemTuple:
								SYS.getIsEqualBool(
													__Row[__RowedItemTuple[0]],
													__RowedItemTuple[1]
												),
								self.RowedPickOrderedDict.items()
							)
						),
					self.TabledTable.iterrows()
				)

			#debug
			'''
			self.debug(('self.',self,['RowedIsBoolsList']))
			'''

			#set
			if len(self.RowedIsBoolsList)==0:
				self.RowedIsBool=False
			else:
				self.RowedIsBool=any(self.RowedIsBoolsList)

			#Init to the len of the table
			self.RowedIndexInt=self.TabledTable.nrows

			#But maybe find a last index
			if self.RowedIsBool: 
				if len(self.RowedIsBoolsList)>0:
					self.RowedIndexInt=self.RowedIsBoolsList.index(True)

			#debug
			'''
			self.debug(('self.',self,['RowedIsBool','RowedIndexInt']))
			'''
		
#</DefineClass>
