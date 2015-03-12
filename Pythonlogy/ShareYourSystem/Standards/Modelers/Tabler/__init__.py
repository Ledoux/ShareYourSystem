# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Tabler defines TablesClass instances able to set in a hdf5 structure
a table at a certain node, taking in account the order of already created tables.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Modeler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
TablingOrderStr='xx'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['table']})
class TablerClass(
					BaseClass,
				):
	
	def default_init(self,
						_TabledMongoDeriveNoderVariable=None,
						_TabledHdfGroupVariable=None,
						_TabledMongoTopClientVariable=None,
						_TabledMongoLocalDatabaseVariable=None,
						_TabledHdfTopFileVariable=None,
						_TabledMongoSuffixStr="",
						_TabledHdfSuffixStr="",
						_TabledHdfKeyStrsList=None,
						_TabledMongoKeyStrsList=None,
						_TabledMongoCollectionsOrderedDict=None,
						_TabledHdfTablesOrderedDict=None,
						_TabledMongoKeyStr="", 	
						_TabledHdfKeyStr="", 
						_TabledMongoIndexInt=-1, 	
						_TabledHdfIndexInt=-1, 			
						_TabledMongoCollection=None, 	
						_TabledHdfTable=None, 
						**_KwargVariablesDict
						):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_table(self):

		#debug
		'''
		self.debug(('self.',self,['ModelingDescriptionTuplesList']))
		'''

		#debug
		'''
		self.debug(
					[
						'We are going to look if this is a new table or not...',
						'In order to index it',
						('self.',self,[
											'ModeledKeyStr',
											'ModeledDescriptionClass',
										]
						)
					]
				)
		'''

		#Check
		if self.ModelingMongoBool:

			#debug
			'''
			self.debug(
					'We tabular mongo here'
				)
			'''

			#set
			self.TabledMongoSuffixStr=self.ModelTagStr+'Collection'

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'PymongoneClientVariable',
							'TabledMongoSuffixStr'
						]
					)
				]
			)
			'''

			#Check
			if self.ModelDeriveControllerVariable.PymongoneClientVariable==None:

				#debug
				'''
				self.debug('We have to pymongo first...')
				'''

				#pymongo
				self.ModelDeriveControllerVariable.pymongo()

			#Link
			self.TabledMongoTopClientVariable=self.ModelDeriveControllerVariable.PymongoneClientVariable
			
			#Check
			if self.TabledMongoTopClientVariable!=None:

				#debug
				'''
				self.debug(
							[	
								'Looking for names of collections here',
								('self.',self,[
									'TabledMongoTopClientVariable'
									]),
							]
						)
				'''

				#set
				self.TabledMongoDatabaseKeyStr=self.ModelDeriveControllerVariable.ControlModelStr

				#set
				self.ModelDeriveControllerVariable.PymongoingDatabaseKeyStr=self.TabledMongoDatabaseKeyStr

				#set
				self.TabledMongoLocalDatabaseVariable=self.TabledMongoTopClientVariable[
						self.TabledMongoDatabaseKeyStr
				]

				#debug
				'''
				self.debug(
						[
							('self.',self,[
								'TabledMongoDatabaseKeyStr',
								'TabledMongoLocalDatabaseVariable'
								]),
							"id(self.TabledMongoLocalDatabaseVariable) is "+str(
								id(self.TabledMongoLocalDatabaseVariable))
						]
					)
				'''

				#set
				self.TabledMongoLocalDatabaseVariable.__dict__[
					'ParentDerivePymongoer'
				]=self.ModelDeriveControllerVariable

				#alias
				self.ModelDeriveControllerVariable.Database=self.TabledMongoLocalDatabaseVariable

				#debug
				'''
				self.debug(
							[	
								('self.',self,[
									'TabledMongoLocalDatabaseVariable'
									]),
								"'ParentDerivePymongoer' in self.TabledMongoLocalDatabaseVariable.__dict__",
								'ParentDerivePymongoer' in self.TabledMongoLocalDatabaseVariable.__dict__
							]
						)
				'''

				#Get and sort
				self.TabledMongoKeyStrsList=map(
					str,
					sorted(
						filter(
								lambda __KeyStr:
								__KeyStr.endswith(
									self.TabledMongoSuffixStr
								),
								self.TabledMongoLocalDatabaseVariable.collection_names()
							)
						)
				)
				
				#debug
				'''
				self.debug(
					[	
						('self.',self,[
							'TabledMongoKeyStrsList'
							])
					]
				)
				'''
				
				#update
				self.TabledMongoCollectionsOrderedDict.update(
					map(
							lambda __TabledKeyStr:
							(
								__TabledKeyStr,
								self.TabledMongoLocalDatabaseVariable[
									__TabledKeyStr
								]
							),
							self.TabledMongoKeyStrsList
						)
				)

				#debug
				'''
				self.debug(("self.",self,[
											'TabledMongoSuffixStr',
											'TabledMongoKeyStrsList'
											]))
				'''

			#debug
			'''
			self.debug(
						[
							'TabledMongoKeyStrsList',
							'TabledMongoSuffixStr',
							'TabledMongoKeyStr'
						]
					)
			'''

			#Get the suffix Strs of all the tables and their index
			TabledMongoList=SYS.unzip(map(
					lambda __StrsList:
					(
						__StrsList[1],
						TablingOrderStr.join(__StrsList[2:])
					),
					map(
							lambda __TabledMongoKeyStr:
							__TabledMongoKeyStr.split(TablingOrderStr),
							self.TabledMongoKeyStrsList
						)
				),[0,1]
			)

			#debug
			'''
			self.debug(('vars ',vars(),['TabledHdfList']))
			'''
			
			#Unpack if it is possible
			if len(TabledMongoList)>0:

				#Unpack
				[TabledMongoIndexIntsTuple,TabledMongoSuffixStrsList]=TabledMongoList

				#debug
				'''
				self.debug(
							[
								'There are already some tables',
								'TabledMongoSuffixStrsList is '+str(TabledMongoSuffixStrsList),
								"self.TabledMongoSuffixStr is "+str(
									self.TabledMongoSuffixStr)
							]
						)
				'''

				if self.TabledMongoSuffixStr not in TabledMongoSuffixStrsList:

					#Increment the IndexStr
					TabledMongoIndexInt=max(map(int,TabledMongoIndexIntsTuple))+1

					#Strify
					TabledMongoIndexStr=str(TabledMongoIndexInt)

					#debug
					'''
					self.debug('IndexStr of this new table is '+str(IndexStr))
					'''
					
				else:

					#Get the already setted one
					TabledMongoIndexStr=self.TabledMongoKeyStrsList[
							TabledMongoSuffixStrsList.index(self.TabledMongoSuffixStr)
						].split(TablingOrderStr)[1]

					#Intify
					TabledMongoIndexInt=(int)(TabledMongoIndexStr)

					#debug
					'''
					self.debug('IndexStr of this not new table is '+str(IndexStr))
					'''

			else:

				#debug
				'''
				self.debug('There are no tables here')
				'''

				#set to empty lists 
				[TabledMongoIndexIntsTuple,TabledMongoSuffixStrsList]=[[],[]]

				#Init the list
				TabledMongoIndexInt=0

				#Strify
				TabledMongoIndexStr="0"

			#Bind with TabledHdfKeyStr setting
			self.TabledMongoKeyStr=TablingOrderStr+TabledMongoIndexStr+TablingOrderStr+self.TabledMongoSuffixStr

			#set the TabledInt
			self.TabledMongoIndexInt=TabledMongoIndexInt

			#debug
			'''
			self.debug("self.TabledMongoKeyStr is "+str(self.TabledMongoKeyStr))
			'''
			
			#debug
			'''
			self.debug(
						[
							'Here we create the collection or get it depending if it is new or not',
							'self.TabledMongoKeyStr is '+self.TabledMongoKeyStr,
							'self.TabledTopFileVariable!=None is '+str(self.TabledTopFileVariable!=None)
						]
					)
			'''

			#Check
			if self.TabledMongoKeyStr!="" and self.TabledMongoLocalDatabaseVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'TabledMongoKeyStr',
									'TabledMongoKeyStrsList'
									]
								),
								'self.TabledMongoLocalDatabaseVariable.collection_names() is ',
								str(self.TabledMongoLocalDatabaseVariable.collection_names())
							]
						)
				'''
				
				#Create the collection if not already
				if self.TabledMongoKeyStr not in self.TabledMongoKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The collection not exists',
								]
							)
					'''

					#Create the collections
					self.TabledMongoCollection=self.TabledMongoLocalDatabaseVariable.create_collection(
						self.TabledMongoKeyStr
					)

					#Append
					self.TabledMongoKeyStrsList.append(self.TabledMongoKeyStr)

				else:

					#debug
					'''
					self.debug(
						[
							'The collection exists',
						]
					)
					'''

					#Else just get it 
					self.TabledMongoCollection=self.TabledMongoLocalDatabaseVariable[
						self.TabledMongoKeyStr
					]
					

				
				
				#set the in the TabledMongoCollectionsOrderedDict
				self.TabledMongoCollectionsOrderedDict[
					self.TabledMongoKeyStr
				]=self.TabledMongoCollection

				#debug
				'''
				self.debug("self.TabledMongoCollectionsOrderedDict is "+str(self.TabledMongoCollectionsOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for mongo...',
							('self.',self,[
								'TabledMongoCollection',
								'TabledMongoTopDatabaseVariable'
								]
							)
						]
					)
			'''


		#Check
		if self.ModelingHdfBool:

			#debug
			'''
			self.debug('We tabular for hdf here...')
			'''
			
			#set
			self.TabledHdfSuffixStr=self.ModelTagStr+'Table'

			#Check
			if self.ModelDeriveControllerVariable.HdformatedFileVariable==None:

				#Check
				if self.ModelDeriveControllerVariable.HdformatingFileKeyStr=='':

					#set
					self.ModelDeriveControllerVariable.HdformatingFileKeyStr=self.ModelDeriveControllerVariable.ControlModelStr+'.hdf5'

				#debug
				'''
				self.debug(
					[
						'We have to hdformat first...',
						'self.ModelDeriveControllerVariable.HdformatingFileKeyStr is ',
						self.ModelDeriveControllerVariable.HdformatingFileKeyStr
					]
				)
				'''

				#Hdformat
				self.ModelDeriveControllerVariable.hdformat()
				
			#Set
			self.ModelDeriveControllerVariable.HdfGroupPathStr=self.ModelDeriveControllerVariable.ControlModelStr

			#Link
			self.TabledHdfTopFileVariable=self.ModelDeriveControllerVariable.HdformatedFileVariable
			
			#debug
			'''
			self.debug(('self.',self,[
										'TabledHdfTopFileVariable'
									]))
			'''
			
			#/#################/#
			# Check for all the tables alreday defined here
			#

			#Check
			if self.TabledHdfTopFileVariable!=None:

				#debug
				'''
				self.debug(
							[	
								'Looking for names of tables here',
								('self.',self,['HdfGroupPathStr'])
							]
						)
				'''

				#Definition Tabled attributes
				self.TabledHdfGroupVariable=self.TabledHdfTopFileVariable.getNode(
					self.ModelDeriveControllerVariable.HdfGroupPathStr
				)

				#debug
				'''
				self.debug(
							[
								('looking for tables with the same suffix Str as : '),
								('self.',self,['TabledHdfSuffixStr'])
							]
						)
				'''

				#Get and sort
				self.TabledHdfKeyStrsList=sorted(
					filter(
							lambda __KeyStr:
							__KeyStr.endswith(self.TabledHdfSuffixStr),
							self.TabledHdfGroupVariable._v_leaves.keys()
						)
				)
				
				self.TabledHdfTablesOrderedDict.update(
					map(
							lambda __TabledKeyStr:
							(
								__TabledKeyStr,
								self.TabledHdfGroupVariable._f_getChild(
									__TabledKeyStr
								)
							),
							self.TabledHdfKeyStrsList
						)
				)

				#debug
				'''
				self.debug(("self.",self,[
											'TabledHdfSuffixStr',
											'TabledHdfKeyStrsList'
											]))
				'''	

			#/################/#
			# Refind all the names of the tables
			#

			#debug
			'''
			self.debug(
						('self.',self,[
							'TabledHdfKeyStrsList',
							'TabledHdfSuffixStr',
							'TabledHdfKeyStr'
						])
					)
			'''

			#Get the suffix Strs of all the tables and their index
			TabledHdfList=SYS.unzip(map(
					lambda __StrsList:
					(
						__StrsList[1],
						TablingOrderStr.join(__StrsList[2:])
					),
					map(
							lambda __TabledHdfKeyStr:
							__TabledHdfKeyStr.split(TablingOrderStr),
							self.TabledHdfKeyStrsList
						)
				),[0,1]
			)

			#debug
			self.debug(('vars ',vars(),['TabledHdfList']))
			
			#/##################/#
			# Find if there are already some tables here and deduce the index of the table
			#

			#Unpack if it is possible
			if len(TabledHdfList)>0:

				#Unpack
				[TabledHdfIndexIntsTuple,TabledHdfSuffixStrsList]=TabledHdfList

				#debug
				'''
				self.debug(
							[
								'There are already some tables',
								'TabledHdfSuffixStrsList is '+str(TabledHdfSuffixStrsList),
								"self.TabledHdfSuffixStr is "+str(
									self.TabledHdfSuffixStr)
							]
						)
				'''

				if self.TabledHdfSuffixStr not in TabledHdfSuffixStrsList:

					#Increment the IndexStr
					TabledHdfIndexInt=max(map(int,TabledHdfIndexIntsTuple))+1

					#Strify
					TabledHdfIndexStr=str(TabledHdfIndexInt)

					#debug
					'''
					self.debug('IndexStr of this new table is '+str(IndexStr))
					'''
					
				else:

					#Get the already setted one
					TabledHdfIndexStr=self.TabledHdfKeyStrsList[
							TabledHdfSuffixStrsList.index(self.TabledHdfSuffixStr)
						].split(TablingOrderStr)[1]

					#Intify
					TabledHdfIndexInt=(int)(TabledHdfIndexStr)

					#debug
					'''
					self.debug('IndexStr of this not new table is '+str(IndexStr))
					'''

			else:

				#debug
				'''
				self.debug('There are no tables here')
				'''

				#set to empty lists 
				[TabledHdfIndexIntsTuple,TabledHdfSuffixStrsList]=[[],[]]

				#Init the list
				TabledHdfIndexInt=0

				#Strify
				TabledHdfIndexStr="0"

			#/##################/#
			# set the table key str
			#

			#debug
			self.debug(
					[
						'We set the table key str',
						('self.',self,['TabledHdfKeyStr'])
					]
				)

			#Bind with TabledHdfKeyStr setting
			self.TabledHdfKeyStr=TablingOrderStr+TabledHdfIndexStr+TablingOrderStr+self.TabledHdfSuffixStr

			#set the TabledInt
			self.TabledHdfIndexInt=TabledHdfIndexInt

			#debug
			'''
			self.debug("self.TabledHdfKeyStr is "+str(self.TabledHdfKeyStr))
			'''
			
			#debug
			'''
			self.debug(
						[
							'Here we create the table or get it depending if it is new or not',
							('self.',self,[
								'TabledHdfKeyStr',
								'TabledHdfTopFileVariable'
								])
						]
					)
			'''
			
			#Check
			if self.TabledHdfKeyStr!="" and self.TabledHdfTopFileVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'TabledHdfKeyStr',
									'TabledHdfKeyStrsList'
								])
							]
						)
				'''
				
				#Create the Table if not already
				if self.TabledHdfKeyStr not in self.TabledHdfKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The table not exists',
								]
							)
					'''

					#Create the Table in the hdf5
					self.TabledHdfTable=self.TabledHdfTopFileVariable.create_table(
						self.TabledHdfGroupVariable,
						self.TabledHdfKeyStr,
						self.ModeledDescriptionClass,
						self.ModeledDescriptionClass.__doc__ 
						if self.ModeledDescriptionClass.__doc__!=None 
						else "This is the "+self.ModeledDescriptionClass.__name__
					)

					#Append
					self.TabledHdfKeyStrsList.append(
						self.TabledHdfKeyStr
					)

				else:

					#debug
					'''
					self.debug(
									[
										'The table exists',
										"self.TabledGroupVariable is "+str(self.TabledGroupVariable)
									]
								)
					'''

					#Else just get it 
					self.TabledHdfTable=self.TabledHdfGroupVariable._f_getChild(
						self.TabledHdfKeyStr
					)

				#set the in the TablesOrderedDict
				self.TabledHdfTablesOrderedDict[
					self.TabledHdfKeyStr
				]=self.TabledHdfTable

				#debug
				'''
				self.debug("self.TabledHdfTablesOrderedDict is "+str(
					self.TabledHdfTablesOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for hdf...',
							('self.',self,[
								'TabledHdfTable',
								'TabledHdfTopFileVariable'
								]
							)
						]
					)
			'''

	def mimic_model(self):

		#call the tabular method
		BaseClass.model(self)

		#debug
		'''
		self.debug('We have modeled here, now table')
		'''
		
		#table
		self.table()

#</DefineClass>


#</DefinePrint>
TablerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'TabledMongoDeriveNoderVariable',	
		'TabledHdfGroupVariable', 
		'TabledHdfTopFileVariable',
		'TabledMongoTopClientVariable',
		'TabledMongoLocalDatabaseVariable',									
		#'TabledMongoSuffixStr',
		#'TabledHdfSuffixStr',																
		'TabledMongoKeyStrsList',
		'TabledHdfKeyStrsList', 	
		'TabledMongoCollectionsOrderedDict',												
		'TabledHdfTablesOrderedDict',
		'TabledMongoKeyStr', 	
		'TabledHdfKeyStr', 
		#'TabledMongoIndexInt', 	
		#'TabledHdfIndexInt', 			
		'TabledMongoCollection', 	
		'TabledHdfTable' 
	]
)
#<DefinePrint>