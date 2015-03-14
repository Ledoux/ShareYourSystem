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
from ShareYourSystem.Standards.Itemizers import Setter
from ShareYourSystem.Standards.Controllers import Controller
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RetrieverClass(BaseClass):

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

	def do_retrieve(self):

		#/################/#
		# Check hdf or mongo to retrieve
		#

		#debug
		'''
		self.debug(
					[
						('self.',self,[
										'ModeledHdfKeyStrsList',
										'RetrievingIndexesList'
									])
					]
				)
		'''

		#Check
		if len(self.ModelingDescriptionTuplesList)>0:
			self.RetrievingDatabaseStr='hdf'

		#debug
		'''
		self.debug(
					[
						('Ok model is done'),
						('self.',self,['ModeledHdfTablesOrderedDict','ModeledHdfKeyStrsList'])
					]
				)
		'''

		#set the RetrievedRowInt
		self.RetrievedRowInt=self.RetrievingIndexesList[1]

		#Check
		if self.RetrievingDatabaseStr=='mongo':

			#/################/#
			# Get the collection and find_one
			#

			#Definition the RetrievedMongoCollection
			self.RetrievedMongoCollection=self.ModeledMongoCollectionsOrderedDict[
				self.ModeledMongoKeyStrsList[
					self.RetrievingIndexesList[0]
				]
			]

			#debug
			'''
			self.debug(
				[
					'We retrieve mongo here',
					('self.',self,[
						'RetrievedRowInt',
					]),
					'self.RetrievedMongoCollection.find_one is ',
					str(self.RetrievedMongoCollection.find_one)
				]
			)
			'''
			
			#findOne
			self.RetrievedPickOrderedDict=collections.OrderedDict(
				self.RetrievedMongoCollection.find_one(
				{'RowInt':self.RetrievedRowInt}
			))
			#del self.RetrievedPickOrderedDict['_id']

			#debug
			'''
			self.debug(
				[
					'ok we have retrieved',
					('self.',self,['RetrievedPickOrderedDict'])
				]
			)
			'''

		#Check
		if self.RetrievingDatabaseStr=='hdf':

			#/################/#
			# Get the table and find
			#

			#debug
			'''
			self.debug(
					[
						'We hdf retrieve here'
					]
				)
			'''
			
			#Definition the RetrievedHdfTable
			self.RetrievedHdfTable=self.ModeledHdfTablesOrderedDict[
				self.ModeledHdfKeyStrsList[
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
							'We set in the controller the retrieved dict',
							('self.',self,['RetrievedPickOrderedDict'])
						]
					)
			'''

		#/################/#
		# Set in the controller
		#

		#debug
		'''
		self.debug(
				[
					'Now we set the recover dict in the controller',
					'self.RetrievedPickOrderedDict.items() is ',
					str(self.RetrievedPickOrderedDict.items())
				]
			)
		'''

		#Update
		"""
		self.ModelDeriveControllerVariable[
			Setter.SetMapStr
		](
			map(
				lambda __ItemTuple:
				(
					str(__ItemTuple[0]),
					str(__ItemTuple[1]) 
					if type(__ItemTuple[1])==unicode
					else __ItemTuple[1]
				),
				self.RetrievedPickOrderedDict.items()
			)
		)
		"""

		#Update
		self.ModelDeriveControllerVariable[
			Setter.SetMapStr
		](self.RetrievedPickOrderedDict.items())

	def propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable):

		#debug
		'''
		self.debug('Before we call the parent setModelingDescriptionTuplesList method ')
		'''

		#Hook
		BaseClass.propertize_setModelingDescriptionTuplesList(self,_SettingValueVariable)

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
			self.ModelingDescriptionTuplesList
		)

		#Init
		if self.RetrievedPickOrderedDict==None:
			self.RetrievedPickOrderedDict=collections.OrderedDict()

		#debug
		'''
		self.debug(('self.',self,['RetrievedColumnStrToGetStrOrderedDict']))
		'''
#</DefineClass>

#<DefineLocals>
Controller.ModelsClass.ManagingValueClass=RetrieverClass
#<DefineLocals>

#</DefinePrint>
RetrieverClass.PrintingClassSkipKeyStrsList.extend(
	[
		'RetrievingIndexesList',
		'RetrievedColumnStrToGetStrOrderedDict',
		'RetrievedRowInt',			
		'RetrievedHdfTable', 			
		#'RetrievedPickOrderedDict'
	]
)
#<DefinePrint>
