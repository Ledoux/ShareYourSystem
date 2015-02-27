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
BaseModuleStr="ShareYourSystem.Standards.Modelers.Tabularer"
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
	
	#Definition
	RepresentingKeyStrsList=[
					'TabledMongoKeyStr', 	
					'TabledHdfKeyStr', 
					'TabledMongoIndexInt', 	
					'TabledHdfIndexInt', 			
					'TabledMongoCollection', 	
					'TabledHdfTable' 
		]

	def default_init(self,
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

		#tabular first
		self.tabular()

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
						[
							'TabularedMongoKeyStrsList',
							'TabularedMongoSuffixStr',
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
							self.TabularedMongoKeyStrsList
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
								"self.TabularedMongoSuffixStr is "+str(
									self.TabularedMongoSuffixStr)
							]
						)
				'''

				if self.TabularedMongoSuffixStr not in TabledMongoSuffixStrsList:

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
					TabledMongoIndexStr=self.TabularedMongoKeyStrsList[
							TabledMongoSuffixStrsList.index(self.TabularedMongoSuffixStr)
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
			self.TabledMongoKeyStr=TablingOrderStr+TabledMongoIndexStr+TablingOrderStr+self.TabularedMongoSuffixStr

			#set the TabularedInt
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
							'self.TabularedTopFileVariable!=None is '+str(self.TabularedTopFileVariable!=None)
						]
					)
			'''

			#Check
			if self.TabledMongoKeyStr!="" and self.TabularedMongoLocalDatabaseVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'TabledMongoKeyStr',
									'TabularedMongoKeyStrsList'
									]
								),
								'self.TabularedMongoLocalDatabaseVariable.collection_names() is ',
								str(self.TabularedMongoLocalDatabaseVariable.collection_names())
							]
						)
				'''
				
				#Create the collection if not already
				if self.TabledMongoKeyStr not in self.TabularedMongoKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The collection not exists',
								]
							)
					'''

					#Create the collections
					self.TabledMongoCollection=self.TabularedMongoLocalDatabaseVariable.create_collection(
						self.TabledMongoKeyStr
					)

					#Append
					self.TabularedMongoKeyStrsList.append(self.TabledMongoKeyStr)

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
					self.TabledMongoCollection=self.TabularedMongoLocalDatabaseVariable[
						self.TabledMongoKeyStr
					]
					

				
				
				#set the in the TabularedMongoCollectionsOrderedDict
				self.TabularedMongoCollectionsOrderedDict[
					self.TabledMongoKeyStr
				]=self.TabledMongoCollection

				#debug
				'''
				self.debug("self.TabularedMongoCollectionsOrderedDict is "+str(self.TabularedMongoCollectionsOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for mongo...',
							('self.',self,[
								'TabledMongoCollection',
								'TabularedMongoTopDatabaseVariable'
								]
							)
						]
					)
			'''


		#Check
		if self.ModelingHdfBool:

			#debug
			'''
			self.debug(
						('self.',self,[
							'TabularedHdfKeyStrsList',
							'TabularedHdfSuffixStr',
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
							self.TabularedHdfKeyStrsList
						)
				),[0,1]
			)

			#debug
			'''
			self.debug(('vars ',vars(),['TabledHdfList']))
			'''
			
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
								"self.TabularedHdfSuffixStr is "+str(
									self.TabularedHdfSuffixStr)
							]
						)
				'''

				if self.TabularedHdfSuffixStr not in TabledHdfSuffixStrsList:

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
					TabledHdfIndexStr=self.TabularedHdfKeyStrsList[
							TabledHdfSuffixStrsList.index(self.TabularedHdfSuffixStr)
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

			#Bind with TabledHdfKeyStr setting
			self.TabledHdfKeyStr=TablingOrderStr+TabledHdfIndexStr+TablingOrderStr+self.TabularedHdfSuffixStr

			#set the TabularedInt
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
							'self.TabledHdfKeyStr is '+self.TabledHdfKeyStr,
							'self.TabularedHdfTopFileVariable!=None is '+str(self.TabularedHdfTopFileVariable!=None)
						]
					)
			'''

			#Check
			if self.TabledHdfKeyStr!="" and self.TabularedHdfTopFileVariable!=None:

				#debug
				'''
				self.debug(
							[
								('self.',self,[
									'TabledHdfKeyStr',
									'TabularedHdfKeyStrsList'
								])
							]
						)
				'''
				
				#Create the Table if not already
				if self.TabledHdfKeyStr not in self.TabularedHdfKeyStrsList:

					#debug
					'''
					self.debug(
								[
									'The table not exists',
								]
							)
					'''

					#Create the Table in the hdf5
					self.TabledHdfTable=self.TabularedHdfTopFileVariable.create_table(
						self.TabularedHdfGroupVariable,
						self.TabledHdfKeyStr,
						self.ModeledDescriptionClass,
						self.ModeledDescriptionClass.__doc__ 
						if self.ModeledDescriptionClass.__doc__!=None 
						else "This is the "+self.ModeledDescriptionClass.__name__
					)

					#Append
					self.TabularedHdfKeyStrsList.append(
						self.TabledHdfKeyStr
					)

				else:

					#debug
					'''
					self.debug(
									[
										'The table exists',
										"self.TabularedGroupVariable is "+str(self.TabularedGroupVariable)
									]
								)
					'''

					#Else just get it 
					self.TabledHdfTable=self.TabularedHdfGroupVariable._f_getChild(
						self.TabledHdfKeyStr
					)

				#set the in the TablesOrderedDict
				self.TabularedHdfTablesOrderedDict[
					self.TabledHdfKeyStr
				]=self.TabledHdfTable

				#debug
				'''
				self.debug("self.TabularedHdfTablesOrderedDict is "+str(
					self.TabularedHdfTablesOrderedDict))
				'''
				
			#debug
			'''
			self.debug(
						[
							'Table is done here for hdf...',
							('self.',self,[
								'TabledHdfTable',
								'TabularedHdfTopFileVariable'
								]
							)
						]
					)
			'''



#</DefineClass>
