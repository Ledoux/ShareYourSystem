# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Rower helps to set rowed lines in a Databaser from pointed attributes,
ready then to be inserted in a table.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Tabler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
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
								'RowedHdfColumnStrsList',	
								'RowedMongoPickOrderedDict',																									
								'RowedHdfPickOrderedDict',
								'RowedMongoIsBoolsList',
								'RowedHdfIsBoolsList',
								'RowedMongoIsBool',
								'RowedHdfIsBool',
								'RowedMongoIndexInt',
								'RowedHdfIndexInt'
							]

	def default_init(
					self,
					_RowingGetStrsList={
							'DefaultingSetType':property,
							'PropertizingInitVariable':[],
							'PropertizingDocStr':''
					},
					_RowedGetStrToColumnStrOrderedDict=None,
					_RowedHdfColumnStrsList=None,
					_RowedMongoPickOrderedDict=None, 																
					_RowedHdfPickOrderedDict=None,
					_RowedMongoIsBoolsList=None,	 
					_RowedHdfIsBoolsList=None,	
					_RowedMongoIsBool=False,
					_RowedHdfIsBool=False,
					_RowedMongoIndexInt=-1,
					_RowedHdfIndexInt=-1,
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
					(
						_DatabasingSealTuple[0],
						_DatabasingSealTuple[1]
					),
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


		#Check
		if self.DatabasingHdfBool:

			#debug
			'''
			self.debug(
							[
								'bind with RowedHdfColumnStrsList setting',
								('self.',self,['RowedGetStrToColumnStrOrderedDict'])
							]
						)
			'''
			
			#Bind with 
			self.RowedHdfColumnStrsList=map(
					lambda __RowingGetStr:
					self.RowedGetStrToColumnStrOrderedDict[__RowingGetStr],
					_SettingValueVariable
				)

			#debug
			'''
			self.debug(('self.',self,['RowedHdfColumnStrsList']))
			'''

	def do_row(self):
		""""""
	
		#table then
		self.table()
		
		#Check	
		if self.ModeledPointDeriveControllerVariable!=None:
			
			#debug
			'''
			self.ModeledPointDeriveControllerVariable.debug('ParentSpeaking...')
			'''

			#Check
			if self.DatabasingHdfBool:

				#Update
				self.RowedHdfPickOrderedDict.update(
					zip(
						self.RowedHdfColumnStrsList,
						self.ModeledPointDeriveControllerVariable.pick(
							self.RowingGetStrsList
						)
					)
				)

				#debug
				'''
				self.debug(('self.',self,[
										'RowedHdfPickOrderedDict',
										'TabledHdfTable'
									]))
				'''

				#Check if it was already rowed
				self.RowedHdfIsBoolsList=map(
						lambda __Row:
						all(
							map(
									lambda __RowedItemTuple:
									SYS.getIsEqualBool(
														__Row[__RowedItemTuple[0]],
														__RowedItemTuple[1]
													),
									self.RowedHdfPickOrderedDict.items()
								)
							),
						self.TabledHdfTable.iterrows()
					)

				#debug
				'''
				self.debug(('self.',self,['RowedHdfIsBoolsList']))
				'''

				#set
				if len(self.RowedHdfIsBoolsList)==0:
					self.RowedHdfIsBool=False
				else:
					self.RowedHdfIsBool=any(self.RowedHdfIsBoolsList)

				#Init to the len of the table
				self.RowedHdfIndexInt=self.TabledHdfTable.nrows

				#But maybe find a last index
				if self.RowedHdfIsBool: 
					if len(self.RowedHdfIsBoolsList)>0:
						self.RowedHdfIndexInt=self.RowedHdfIsBoolsList.index(True)

				#debug
				'''
				self.debug(('self.',self,['RowedHdfIsBool','RowedHdfIndexInt']))
				'''

			#Check
			if self.DatabasingMongoBool:

				#Update
				self.RowedMongoPickOrderedDict.update(
					zip(
						self.RowingGetStrsList,
						self.ModeledPointDeriveControllerVariable.pick(
							self.RowingGetStrsList
						)
					)
				)

				#debug
				self.debug(('self.',self,[
										'RowedMongoPickOrderedDict',
										'TabledMongoCollection'
									]))

				#Define
				RowedCursor=self.TabledMongoCollection.find()

				#debug
				self.debug('list(RowedCursor) is '+SYS._str(list(RowedCursor)))

				#Check if it was already rowed
				self.RowedMongoIsBoolsList=map(
						lambda __Row:
						all(
							map(
									lambda __RowedItemTuple:
									SYS.getIsEqualBool(
														__Row[__RowedItemTuple[0]],
														__RowedItemTuple[1]
													),
									self.RowedMongoPickOrderedDict.items()
								)
						),
						RowedCursor
					)

				#debug
				'''
				self.debug(('self.',self,['RowedHdfIsBoolsList']))
				'''

				#set
				if len(self.RowedMongoIsBoolsList)==0:
					self.RowedMongoIsBool=False
				else:
					self.RowedMongoIsBool=any(self.RowedMongoIsBoolsList)

				#Init to the len of the table
				self.RowedMongoIndexInt=RowedCursor.count()

				#But maybe find a last index
				if self.RowedMongoIsBool: 
					if len(self.RowedMongoIsBoolsList)>0:
						self.RowedMongoIndexInt=self.RowedMongoIsBoolsList.index(True)

				#debug
				'''
				self.debug(('self.',self,['RowedMongoIsBool','RowedMongoIndexInt']))
				'''
		
#</DefineClass>
