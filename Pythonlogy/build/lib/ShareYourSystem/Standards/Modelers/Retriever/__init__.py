# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Retriever instances can retrieve InsertedVariablesList given their 
IndexInt of their corresponding table and their RowInt 
(ie their index of their inserted line).

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Inserter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RetrieverClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
							'RetrievingIndexesList',
							'RetrievedColumnStrToGetStrOrderedDict',
							'RetrievedRowInt',			
							'RetrievedHdfTable', 			
							'RetrievedPickOrderedDict'
						]

	def default_init(self,
						_RetrievingIndexesList=None,
						_RetrievingDatabaseStr='mongo',
						_RetrievedColumnStrToGetStrOrderedDict=None,
						_RetrievedRowInt=-1,			
						_RetrievedHdfTable=None, 			
						_RetrievedPickOrderedDict=None,		
						**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def setModelingSealTuplesList(self,_SettingValueVariable):

		#debug
		'''
		self.debug('Before we call the parent setModelingSealTuplesList method ')
		'''

		#Hook
		BaseClass.setModelingSealTuplesList(self,_SettingValueVariable)

		#Bind with RetrievedColumnStrToGetStrOrderedDict setting
		if self.RetrievedColumnStrToGetStrOrderedDict==None:
			self.RetrievedColumnStrToGetStrOrderedDict=collections.OrderedDict()

		#map
		map(
			lambda __ModelingColumnTuple:
			self.RetrievedColumnStrToGetStrOrderedDict.__setitem__(
				__ModelingColumnTuple[1],
				__ModelingColumnTuple[0]
			),
			self.ModelingSealTuplesList
		)

		#Init
		if self.RetrievedPickOrderedDict==None:
			self.RetrievedPickOrderedDict=collections.OrderedDict()

		#debug
		'''
		self.debug(('self.',self,['RetrievedColumnStrToGetStrOrderedDict']))
		'''
		
	ModelingSealTuplesList=property(
									BaseClass.ModelingSealTuplesList.fget,
									setModelingSealTuplesList,
									BaseClass.ModelingSealTuplesList.fdel,
									BaseClass.ModelingSealTuplesList.__doc__
								)
	
	def do_retrieve(self):

		#debug
		'''
		self.debug(
					[
						('self.',self,[
										'TabularedHdfKeyStrsList',
										'RetrievingIndexesList'
									])
					]
				)
		'''

		#table first
		self.table()

		#Check
		if len(self.ModelingSealTuplesList)>0:
			self.RetrievingDatabaseStr='hdf'

		#debug
		'''
		self.debug(
					[
						('Ok table is done'),
						('self.',self,['TabularedHdfTablesOrderedDict','TabularedHdfKeyStrsList'])
					]
				)
		'''

		#set the RetrievedRowInt
		self.RetrievedRowInt=self.RetrievingIndexesList[1]

		#Check
		if self.RetrievingDatabaseStr=='mongo':

			#Definition the RetrievedMongoCollection
			self.RetrievedMongoCollection=self.TabularedMongoCollectionsOrderedDict[
				self.TabularedMongoKeyStrsList[
					self.RetrievingIndexesList[0]
				]
			]

			#debug
			self.debug(('self.',self,['RetrievedMongoCollection']))

			#findOne
			self.RetrievedPickOrderedDict=self.RetrievedMongoCollection.find_one(
				{'RowInt':self.RetrievedRowInt}
			)

		#Check
		if self.RetrievingDatabaseStr=='hdf':

			#Definition the RetrievedHdfTable
			self.RetrievedHdfTable=self.TabularedHdfTablesOrderedDict[
				self.TabularedHdfKeyStrsList[
					self.RetrievingIndexesList[0]
				]
			]

			#debug
			'''
			self.debug(('self.',self,['RetrievedRowInt','RetrievedHdfTable']))
			'''

			#Definition the RetrievedRowsList
			for __RetrievedRow in self.RetrievedHdfTable.iterrows():
				if __RetrievedRow['RowInt']==self.RetrievedRowInt:

					#debug
					'''
					self.debug('self.RetrievedHdfTable.colnames is '+str(self.RetrievedHdfTable.colnames))
					'''

					#set
					map(
						lambda __ColumnStr:
						self.RetrievedPickOrderedDict.__setitem__(
							self.RetrievedColumnStrToGetStrOrderedDict[__ColumnStr],
							__RetrievedRow[__ColumnStr]
							) if __ColumnStr in self.RetrievedColumnStrToGetStrOrderedDict else None
						,
						self.RetrievedHdfTable.colnames
					)

					#debug
					'''
					self.debug('RetrievedPickOrderedDict is setted')
					'''

			#debug
			'''
			self.debug(
						[
							('self.',self,['RetrievedPickOrderedDict'])
						]
					)
			'''

			#Update
			self.ModeledPointDeriveControllerVariable.update(
				self.RetrievedPickOrderedDict.items(),
				#**{'RestrictingIsBool':True}
			)
			self.ModeledPointDeriveControllerVariable.RestrictingIsBool=False


#</DefineClass>
