# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Tabularer helps to define names for setting Tables in a hdf5 structure,
given the names of predefined models.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Modeler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import importlib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(
	**{'ClassingSwitchMethodStrsList':['tabular']}
)
class TabularerClass(
					BaseClass
				):
		
	def default_init(self,
					_TabularedMongoDeriveNoderVariable=None,
					_TabularedHdfGroupVariable=None,
					_TabularedMongoTopClientVariable=None,
					_TabularedMongoLocalDatabaseVariable=None,
					_TabularedHdfTopFileVariable=None,
					_TabularedMongoSuffixStr="",
					_TabularedHdfSuffixStr="",
					_TabularedHdfKeyStrsList=None,
					_TabularedMongoKeyStrsList=None,
					_TabularedMongoCollectionsOrderedDict=None,
					_TabularedHdfTablesOrderedDict=None,
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_tabular(self):
		""" """

		#debug
		'''
		self.debug(
				[
					('self.',self,[
							'ModelingDescriptionTuplesList',
							'ModeledDescriptionClass',
							'WatchModelWithModelerBool',
							'WatchModelWithJoinerBool'
						]),
					'self.model is '+SYS._str(self.model)
				]
			)
		'''

		#debug
		'''
		self.debug(
					[
						('self.',self,[
							'ModelDeriveControllerVariable'
							]
						)
					]
				)
		'''
		
		#Check
		if self.ModelDeriveControllerVariable!=None:

			#debug
			'''
			self.debug(('self.',self,['ModelTagStr']))
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
				self.TabularedMongoSuffixStr=self.ModelTagStr+'Collection'

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'PymongoneClientVariable',
								'TabularedMongoSuffixStr'
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
				self.TabularedMongoTopClientVariable=self.ModelDeriveControllerVariable.PymongoneClientVariable
				
				#Check
				if self.TabularedMongoTopClientVariable!=None:

					#debug
					'''
					self.debug(
								[	
									'Looking for names of collections here',
									('self.',self,[
										'TabularedMongoTopClientVariable'
										]),
								]
							)
					'''

					#set
					self.TabularedMongoDatabaseKeyStr=self.ModelDeriveControllerVariable.ControlModelStr

					#set
					self.ModelDeriveControllerVariable.PymongoingDatabaseKeyStr=self.TabularedMongoDatabaseKeyStr

					#set
					self.TabularedMongoLocalDatabaseVariable=self.TabularedMongoTopClientVariable[
							self.TabularedMongoDatabaseKeyStr
					]

					#debug
					'''
					self.debug(
							[
								('self.',self,[
									'TabularedMongoDatabaseKeyStr',
									'TabularedMongoLocalDatabaseVariable'
									]),
								"id(self.TabularedMongoLocalDatabaseVariable) is "+str(
									id(self.TabularedMongoLocalDatabaseVariable))
							]
						)
					'''

					#set
					self.TabularedMongoLocalDatabaseVariable.__dict__[
						'ParentDerivePymongoer'
					]=self.ModelDeriveControllerVariable

					#alias
					self.ModelDeriveControllerVariable.Database=self.TabularedMongoLocalDatabaseVariable

					#debug
					'''
					self.debug(
								[	
									('self.',self,[
										'TabularedMongoLocalDatabaseVariable'
										]),
									"'ParentDerivePymongoer' in self.TabularedMongoLocalDatabaseVariable.__dict__",
									'ParentDerivePymongoer' in self.TabularedMongoLocalDatabaseVariable.__dict__
								]
							)
					'''

					#Get and sort
					self.TabularedMongoKeyStrsList=map(
						str,
						sorted(
							filter(
									lambda __KeyStr:
									__KeyStr.endswith(
										self.TabularedMongoSuffixStr
									),
									self.TabularedMongoLocalDatabaseVariable.collection_names()
								)
							)
					)
					
					#debug
					'''
					self.debug(
						[	
							('self.',self,[
								'TabularedMongoKeyStrsList'
								])
						]
					)
					'''
					
					#update
					self.TabularedMongoCollectionsOrderedDict.update(
						map(
								lambda __TabularedKeyStr:
								(
									__TabularedKeyStr,
									self.TabularedMongoLocalDatabaseVariable[
										__TabularedKeyStr
									]
								),
								self.TabularedMongoKeyStrsList
							)
					)

					#debug
					'''
					self.debug(("self.",self,[
												'TabularedMongoSuffixStr',
												'TabularedMongoKeyStrsList'
												]))
					'''

			#Hdf case
			if self.ModelingHdfBool:

				#debug
				'''
				self.debug('We tabular for hdf here...')
				'''
				
				#set
				self.TabularedHdfSuffixStr=self.ModelTagStr+'Table'

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
				self.TabularedHdfTopFileVariable=self.ModelDeriveControllerVariable.HdformatedFileVariable
				
				#debug
				'''
				self.debug(('self.',self,[
											'TabularedHdfTopFileVariable'
										]))
				'''
				
				#/#################/#
				# Check for all the tables alreday defined here
				#

				#Check
				if self.TabularedHdfTopFileVariable!=None:

					#debug
					'''
					self.debug(
								[	
									'Looking for names of tables here',
									('self.',self,['HdfGroupPathStr'])
								]
							)
					'''

					#Definition Tabulared attributes
					self.TabularedHdfGroupVariable=self.TabularedHdfTopFileVariable.getNode(
						self.ModelDeriveControllerVariable.HdfGroupPathStr
					)

					#debug
					'''
					self.debug(
								[
									('looking for tables with the same suffix Str as : '),
									('self.',self,['TabularedHdfSuffixStr'])
								]
							)
					'''

					#Get and sort
					self.TabularedHdfKeyStrsList=sorted(
						filter(
								lambda __KeyStr:
								__KeyStr.endswith(self.TabularedHdfSuffixStr),
								self.TabularedHdfGroupVariable._v_leaves.keys()
							)
					)
					
					self.TabularedHdfTablesOrderedDict.update(
						map(
								lambda __TabularedKeyStr:
								(
									__TabularedKeyStr,
									self.TabularedHdfGroupVariable._f_getChild(
										__TabularedKeyStr
									)
								),
								self.TabularedHdfKeyStrsList
							)
					)

					#debug
					'''
					self.debug(("self.",self,[
												'TabularedHdfSuffixStr',
												'TabularedHdfKeyStrsList'
												]))
					'''	

	def mimic_model(self):

		#model first
		BaseClass.model(self)

		#debug
		self.debug(
			[
				'We have modeled here, now tabular'
			]
		)
		
		#tabular then
		self.tabular()

#</DefineClass>

#</DefinePrint>
TabularerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'TabularedMongoDeriveNoderVariable',	
		'TabularedHdfGroupVariable', 
		'TabularedHdfTopFileVariable',
		'TabularedMongoTopClientVariable',
		'TabularedMongoLocalDatabaseVariable',									
		#'TabularedMongoSuffixStr',
		#'TabularedHdfSuffixStr',																
		'TabularedMongoKeyStrsList',
		'TabularedHdfKeyStrsList', 	
		'TabularedMongoCollectionsOrderedDict',												
		'TabularedHdfTablesOrderedDict'
	]
)
#<DefinePrint>
