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
BaseModuleStr="ShareYourSystem.Standards.Modelers.Databaser"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import importlib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['tabular']})
class TabularerClass(
					BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
									'TabularingDatabaseStr',
									'TabularedGroupVariable', 
									'TabularedDeriveNoderVariable',	
									'TabularedTopFileVariable',									
									'TabularedSuffixStr',																
									'TabularedKeyStrsList', 													
									'TabularedTablesOrderedDict',
									'TabularedCollectionsOrderedDict'
								]

	def default_init(self,
					_TabularingDatabaseStr='hdf',
					_TabularedGroupVariable=None,
					_TabularedDeriveNoderVariable=None,
					_TabularedTopFileVariable=None,
					_TabularedTopDatabaseVariable=None,
					_TabularedSuffixStr="",
					_TabularedKeyStrsList=None,
					_TabularedTablesOrderedDict=None,
					_TabularedCollectionsOrderedDict=None,
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
							'DatabasingSealTuplesList',
							'DatabasedModelClass',
							'WatchModelWithModelerBool',
							'WatchModelWithJoinerBool'
						]),
					'self.model is '+SYS._str(self.model)
				]
			)
		'''
		
		#<NotHook>
		#database first
		self.database()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						('self.',self,['DatabasingSealTuplesList','DatabasedModelClass']),
						('self.DatabasedPointDeriveStorer!=None is '+str(self.DatabasedPointDeriveStorer!=None))
					]
				)
		'''
		
		#Maybe we have to hdformat first
		if self.ModeledPointDeriveStorerVariable!=None:

			#set 
			self.GroupedPathStr=self.ModeledPointDeriveStorerVariable.GroupedPathStr

			#debug
			'''
			self.debug(('self.',self,['ModeledSuffixStr']))
			'''
			
			#set
			self.TabularedSuffixStr='Model'.join(
				self.ModeledSuffixStr.split('Model')[:-1]
			)+'Table'
					
			#Hdf case
			if self.TabularingDatabaseStr=='hdf':

				#Check
				if self.ModeledPointDeriveStorerVariable.HdformatedFileVariable==None:

					#debug
					'''
					self.debug('We have to hdformat first...')
					'''

					#Hdformat
					self.ModeledPointDeriveStorerVariable.hdformat()
					#self.ModeledPointDeriveStorerVariable.structure()
				
				#Link
				self.TabularedTopFileVariable=self.ModeledPointDeriveStorerVariable.HdformatedFileVariable
				
				#debug
				'''
				self.debug(('self.',self,[
											'HdformatedTopFileVariable',
											'DatabasingSealTuplesList',
											'DatabasedModelClass'
										]))
				'''
				
				#Check
				if self.TabularedTopFileVariable!=None:

					#debug
					'''
					self.debug(
								[	
									'Looking for names of tables here',
									('self.',self,['GroupedPathStr'])
								]
							)
					'''

					#Definition Tabulared attributes
					self.TabularedGroupVariable=self.TabularedTopFileVariable.getNode(
						self.GroupedPathStr
					)

					#debug
					'''
					self.debug(
								[
									('looking for tables with the same suffix Str as : '),
									('self.',self,['TabularedSuffixStr'])
								]
							)
					'''

					#Get and sort
					self.TabularedKeyStrsList=sorted(
						filter(
								lambda __KeyStr:
								__KeyStr.endswith(self.TabularedSuffixStr),
								self.TabularedGroupVariable._v_leaves.keys()
							)
					)
					
					self.TabularedTablesOrderedDict.update(
						map(
								lambda __TabularedKeyStr:
								(
									__TabularedKeyStr,
									self.TabularedGroupVariable._f_getChild(__TabularedKeyStr)
								),
								self.TabularedKeyStrsList
							)
					)

					#debug
					'''
					self.debug(("self.",self,[
												'TabularedSuffixStr',
												'TabularedKeyStrsList'
												]))
					'''

			#Check
			elif self.TabularingDatabaseStr=='mongo':

				#Check
				if self.ModeledPointDeriveStorerVariable.PymongoneDatabaseVariable==None:

					#debug
					'''
					self.debug('We have to pymongo first...')
					'''

					#pymongo
					self.ModeledPointDeriveStorerVariable.pymongo()
					#self.ModeledPointDeriveStorerVariable.structure()

				#Link
				self.TabularedTopDatabaseVariable=self.ModeledPointDeriveStorerVariable.PymongoneDatabaseVariable
				
				#debug
				'''
				self.debug(('self.',self,[
											'HdformatedTopDatabaseVariable',
											'DatabasingSealTuplesList',
											'DatabasedModelClass'
										]))
				'''
				
				#Check
				if self.TabularedTopDatabaseVariable!=None:

					#debug
					self.debug(
								[	
									'Looking for names of collections here',
									('self.',self,['GroupedPathStr'])
								]
							)

					#get
					self.TabularedDeriveNoderVariable=self.TabularedTopDatabaseVariable.ParentDerivePymongoer[
						self.GroupedPathStr
					]


					#Get and sort
					self.TabularedKeyStrsList=sorted(
						filter(
								lambda __KeyStr:
								__KeyStr.endswith(self.TabularedSuffixStr),
								self.TabularedDeriveNoderVariable.MongosCollectionOrderedDict.keys()
							)
					)
					
					self.TabularedCollectionsOrderedDict.update(
						map(
								lambda __TabularedKeyStr:
								(
									__TabularedKeyStr,
									self.TabularedGroupVariable._f_getChild(
										__TabularedKeyStr
									)
								),
								self.TabularedKeyStrsList
							)
					)

					#debug
					'''
					self.debug(("self.",self,[
												'TabularedSuffixStr',
												'TabularedKeyStrsList'
												]))
					'''


		
#</DefineClass>
