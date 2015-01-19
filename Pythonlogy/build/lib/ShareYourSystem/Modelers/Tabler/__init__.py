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
BaseModuleStr="ShareYourSystem.Modelers.Tabularer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
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
									'TabledKeyStr', 										
									'TabledInt',																
									'TabledTable'
								]

	def default_init(self,
						_TabledKeyStr="", 	
						_TabledInt=-1, 			
						_TabledTable=None, 	
						**_KwargVariablesDict
						):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_table(self):

		#debug
		'''
		self.debug(('self.',self,['DatabasingSealTuplesList']))
		'''

		#<NotHook>
		#tabular first
		self.tabular()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						'We are going to look if this is a new table or not...In order to index it',
						('self.',self,[
											'DatabasedKeyStr',
											'DatabasedModelClass',
											'TabularedKeyStrsList',
											'TabularedSuffixStr',
											'TabledKeyStr'
										])
					]
				)
		'''
		
		#Get the suffix Strs of all the tables and their index
		TabledList=SYS.unzip(map(
				lambda __StrsList:
				(
					__StrsList[1],
					TablingOrderStr.join(__StrsList[2:])
				),
				map(
						lambda __TabledKeyStr:
						__TabledKeyStr.split(TablingOrderStr),
						self.TabularedKeyStrsList
					)
			),[0,1])

		#debug
		'''
		self.debug(('vars ',vars(),['TabledList']))
		'''
		
		#Unpack if it is possible
		if len(TabledList)>0:

			#Unpack
			[TabledIntsTuple,TabledSuffixStrsList]=TabledList

			#debug
			'''
			self.debug(
						[
							'There are already some tables',
							'TabledSuffixStrsList is '+str(TabledSuffixStrsList),
							"self.TabularedSuffixStr is "+str(
								self.TabularedSuffixStr)
						]
					)
			'''

			if self.TabularedSuffixStr not in TabledSuffixStrsList:

				#Increment the IndexStr
				IndexInt=max(map(int,TabledIntsTuple))+1

				#Strify
				IndexStr=str(IndexInt)

				#debug
				'''
				self.debug('IndexStr of this new table is '+str(IndexStr))
				'''
				
			else:

				#Get the already setted one
				IndexStr=self.TabularedKeyStrsList[
					TabledSuffixStrsList.index(self.TabularedSuffixStr)
					].split(TablingOrderStr)[1]

				#Intify
				IndexInt=(int)(IndexStr)

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
			[TabledIntsTuple,TabledSuffixStrsList]=[[],[]]

			#Init the list
			IndexInt=0

			#Strify
			IndexStr="0"

		#Bind with TabledKeyStr setting
		self.TabledKeyStr=TablingOrderStr+IndexStr+TablingOrderStr+self.TabularedSuffixStr

		#set the TabularedInt
		self.TabledInt=IndexInt

		#debug
		'''
		self.debug("self.TabledKeyStr is "+str(self.TabledKeyStr))
		'''
		
		#debug
		'''
		self.debug(
					[
						'Here we create the table or get it depending if it is new or not',
						'self.TabledKeyStr is '+self.TabledKeyStr,
						'self.TabularedFilePointedVariable!=None is '+str(self.TabularedFilePointedVariable!=None)
					]
				)
		'''

		#Check
		if self.TabledKeyStr!="" and self.TabularedFilePointedVariable!=None:

			#debug
			'''
			self.debug(
						[
							('self.',self,['TabledKeyStr','TabularedKeyStrsList'])
						]
					)
			'''

			#Create the Table if not already
			if self.TabledKeyStr not in self.TabularedKeyStrsList:

				#debug
				'''
				self.debug(
							[
								'The table not exists',
							]
						)
				'''

				#Create the Table in the hdf5
				self.TabledTable=self.TabularedFilePointedVariable.create_table(
											self.TabularedGroup,
											self.TabledKeyStr,
											self.DatabasedModelClass,
											self.DatabasedModelClass.__doc__ 
											if self.DatabasedModelClass.__doc__!=None 
											else "This is the "+self.DatabasedModelClass.__name__
										)

				#Append in the self.DatabasedDict['TabularedKeyStrsList']
				self.TabularedKeyStrsList.append(self.TabledKeyStr)

			else:

				#debug
				'''
				self.debug(
								[
									'The table exists',
									"self.TabularedGroup is "+str(self.TabularedGroup)
								]
							)
				'''

				#Else just get it 
				self.TabledTable=self.TabularedGroup._f_getChild(self.TabledKeyStr)

			#set the in the TablesOrderedDict
			self.TabularedOrderedDict[self.TabledKeyStr]=self.TabledTable

			#debug
			'''
			self.debug("self.TabularedOrderedDict is "+str(self.TabularedOrderedDict))
			'''
			
		#debug
		'''
		self.debug(
					[
						'Table is done here...',
						('self.',self,['TabledTable','TabularedFilePointedVariable'])
					]
				)
		'''

#</DefineClass>
