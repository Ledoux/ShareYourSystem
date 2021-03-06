# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Joiner instances helps to insert in Hierarchized databases, get the corresponding
RetrieveIndexesLists if it was already inserted, and then insert locally
depending if it is a new row compared to all HierarchizedRetrieveIndexesListsList

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Joiner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import tables

from ShareYourSystem.Functers import Imitater,Switcher
from ShareYourSystem.Standards.Objects import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class HierarchizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'HierarchizingNodeStr',
									'HierarchizingDatabaseNodeStr',
									'HierarchizingDatabaseKeyStr',
									'HierarchizedNodeVariablesList',
									'HierarchizedDeriveDatabasersList',
									'HierarchizedKeyStrsList',
									'HierarchizedRetrieveIndexesListColumnStrsList',
									'HierarchizedRetrieveIndexesListGetStrsList',
									'HierarchizedInsertIndexIntsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_HierarchizingNodeStr="Component",
						_HierarchizingDatabaseNodeStr="",
						_HierarchizingDatabaseKeyStr="",
						_HierarchizedNodeVariablesList=None,
						_HierarchizedDeriveDatabasersList=None,
						_HierarchizedKeyStrsList=None,
						_HierarchizedRetrieveIndexesListColumnStrsList=None,
						_HierarchizedRetrieveIndexesListGetStrsList=None,
						_HierarchizedInsertIndexIntsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{
	#						'HookingAfterVariablesList':[
	#							{'CallingMethodStr':'join'},
	#							{'CallingVariable':Featurer.FeaturerClass.model}
	#						]
	#					}
	#)
	@Switcher.SwitcherClass()
	#@Argumenter.ArgumenterClass()
	@Imitater.ImitaterClass()
	def model(self):

		#debug
		'''
		self.debug(('self.',self,['HierarchizingNodeStr']))
		'''

		#<NotHook>
		#hierarchy first
		self.hierarchize()
		#</NotHook>
		
		#debug
		'''
		self.debug('Add in the ModelingDescriptionTuplesList')
		'''
		
		#set
		if len(self.HierarchizedRetrieveIndexesListColumnStrsList)>0:
			self.ModelingDescriptionTuplesList=map(
				lambda __HierarchizedRetrieveIndexesListGetStr,__HierarchizedRetrieveIndexesListColumnStr:
				(
					__HierarchizedRetrieveIndexesListGetStr,
					__HierarchizedRetrieveIndexesListColumnStr,
					tables.Int64Col(shape=2)
				),
				self.HierarchizedRetrieveIndexesListGetStrsList,
				self.HierarchizedRetrieveIndexesListColumnStrsList
			)+self.ModelingDescriptionTuplesList

		#debug
		'''
		self.debug(('self.',self,['ModelingDescriptionTuplesList']))
		'''

		#<NotHook>
		#call the base model method then
		BaseClass.model(self)
		#</NotHook>
	
		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	@Switcher.SwitcherClass()
	#@Argumenter.ArgumenterClass()
	@Imitater.ImitaterClass()
	def table(self):

		#debug
		'''
		self.debug(('self.',self,[
									'HierarchizingNodeStr',
								]))
		'''

		#<NotHook>
		#database firstand hierarchy first
		self.database()
		self.hierarchize()
		#/<NotHook>

		#Check
		if self.HierarchizingNodeStr!="":

			#structure first in the parent pointer and then table
			if self.NodePointDeriveNoder!=None:

				#Check
				if self.HdformatedFileVariable==None:

					#debug
					self.debug(
							[
								'We have to structure first'
							]
						)

					#structure by also tabling at the same time
					self.NodePointDeriveNoder.structure(
						**{
							'ParentingNodeStr':self.HierarchizingNodeStr
						}
					)

					#Table all the Hierarchized databasers and init the corresponding HierarchizedRetrieveIndexesList in the NodePointDeriveNoder
					self.NodePointDeriveNoder.update(
						zip(
								self.HierarchizedRetrieveIndexesListGetStrsList,
								map(
									lambda __HierarchizedDeriveDatabaser:
									[
										__HierarchizedDeriveDatabaser.table(
											).TabledInt,
										-1
									],
									self.HierarchizedDeriveDatabasersList
								)
							)
					)

		
		#<NotHook>
		BaseClass.table(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	#@Argumenter.ArgumenterClass()
	@Imitater.ImitaterClass()	
	def row(self):

		#<NotHook>
		#table first
		self.table()
		#</NotHook>

		#set
		self.HierarchizedInsertIndexIntsList=map(
					lambda __HierarchizedDeriveDatabaser:
					__HierarchizedDeriveDatabaser.row().RowedIndexInt,
					self.HierarchizedDeriveDatabasersList
				)

		#debug
		'''
		self.debug(('self.',self,[
									'RowedHierarchyInsertIndexIntsList',
									'HierarchizedRetrieveIndexesListGetStrsList'

								]))
		'''

		#set the modeled int in the retrieve tuples
		map(
				lambda __HierarchizedRetrieveIndexesListGetStr,__RowedHierarchyInsertIndexInt:
				getattr(
					self.NodePointDeriveNoder,
					__HierarchizedRetrieveIndexesListGetStr
					).__setitem__(
						1,
						__RowedHierarchyInsertIndexInt
				),
				self.HierarchizedRetrieveIndexesListGetStrsList,
				self.HierarchizedInsertIndexIntsList
			)
	

		#debug
		'''
		self.debug([
						('Before updating the RowingKeyStrsList'),
						#('self.',self,['NodePointDeriveNoder'])
						('model first to set the ModeledGetStrToColumStr')
					]
				)
		'''

		#debug
		'''
		self.debug(('self.',self,['RowingKeyStrsList']))
		'''

		#Add in the RowingKeyStrsList
		self.RowingKeyStrsList=self.HierarchizedRetrieveIndexesListGetStrsList+self.RowingKeyStrsList

		#debug
		'''
		self.debug(
					[
						'Now row with Featurer',
						('self.',self,['RowingKeyStrsList'])
					]
				)
		'''

		#<NotHook>
		#row then
		BaseClass.row(self)
		#</NotHook>

		#debug
		'''
		self.debug('Ok row is over for hierarchizing')
		'''

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	#@Argumenter.ArgumenterClass()
	@Imitater.ImitaterClass()
	def insert(self):
				
		#<NotHook>
		#row first
		self.row()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						'First make insert the Hierarchized databases',
						('self.',self,['HierarchizedNodeVariablesList'])
					]
				)
		'''

		#Insert the Hierarchized databases
		self.HierarchizedInsertIndexIntsList=map(
					lambda __HierarchizedDeriveDatabaser:
					__HierarchizedDeriveDatabaser.insert(),
					self.HierarchizedDeriveDatabasersList
				)

		#debug
		'''
		self.debug(
					[
						'First make insert the Hierarchized databases',
						('self.',self,['HierarchizedNodeVariablesList'])
					]
				)
		'''

		#debug
		'''
		self.debug('Now we can insert')
		'''

		#<NotHook>
		#insert then
		BaseClass.insert(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	@Imitater.ImitaterClass()
	def retrieve(self):

		#debug
		'''
		self.debug(('self.',self,['RetrievingIndexesList']))
		'''

		#<NotHook>
		#retrieve first
		BaseClass.retrieve(self)
		#</NotHook>

		#Retrieve in the joined databases
		self.HierarchizedInsertIndexIntsList=map(
					lambda __HierarchizedRetrieveIndexesListGetStr,__HierarchizedDeriveDatabaserPointer:
					__HierarchizedDeriveDatabaserPointer.retrieve(
						getattr(
							self.NodePointDeriveNoder,
							__HierarchizedRetrieveIndexesListGetStr
						)
					),
					self.HierarchizedRetrieveIndexesListGetStrsList,
					self.HierarchizedDeriveDatabaserPointersList
				)

	@Switcher.SwitcherClass()
	#@Argumenter.ArgumenterClass()
	def do_hierarchize(	
				self
			):

		#debug
		'''
		self.debug(('self.',self,['HierarchizingNodeStr']))
		'''

		if self.HierarchizingDatabaseNodeStr=="":
			self.HierarchizingDatabaseNodeStr=self.ModelingNodeStr

		#Init a default value
		if self.HierarchizingDatabaseKeyStr=="":
			self.HierarchizingDatabaseKeyStr=self.ModeledCollectionKeyStr

		#Check
		if self.HierarchizingNodeStr!="":

			#Check
			if self.NodePointDeriveNoder!=None:
					
				#debug
				'''
				self.debug('Look for the hierarchized variables...')
				'''

				#set
				self.HierarchizedNodeVariablesList=self.NodePointDeriveNoder[
						Noder.NodingPrefixGetStr+self.HierarchizingNodeStr+Noder.NodingSuffixGetStr
					]

				#debug
				'''
				self.debug(('self.',self,['HierarchizedNodeVariablesList']))
				'''

				#set
				self.HierarchizedDeriveDatabasersList=map(
					lambda __HierarchizedNodeVariable:
					SYS._filter(
							lambda __NodedDatabaser:
							getattr(
								__NodedDatabaser,
								'Noded'+self.HierarchizingDatabaseNodeStr+'KeyStr'
								).startswith(
								self.HierarchizingDatabaseKeyStr
							),
							getattr(
									__HierarchizedNodeVariable,
									'Noded'+self.HierarchizingDatabaseNodeStr+'OrderedDict'
							).values()
					)[0],
					self.HierarchizedNodeVariablesList
				)

				#debug
				'''
				self.debug(('self.',self,['HierarchizedDeriveDatabasersList']))
				'''

				#set
				self.HierarchizedKeyStrsList=map(
					lambda __HierarchizedVariable:
					getattr(
						__HierarchizedVariable,
						self.NodePointDeriveNoder.NodedKeyStrKeyStr
					),
					self.HierarchizedNodeVariablesList
				)

				#debug
				'''
				self.debug(('self.',self,['HierarchizedKeyStrsList']))
				'''

				#set
				self.HierarchizedRetrieveIndexesListColumnStrsList=map(
						lambda __HierarchizedKeyStr:
						'Hierarchized'+__HierarchizedKeyStr+'RetrieveIndexesList',
						self.HierarchizedKeyStrsList
					)

				#set
				self.HierarchizedRetrieveIndexesListGetStrsList=map(
						lambda __HierarchizedKeyStr:
						'Hierarchized'+self.ModelingNodeStr+self.ModeledCollectionKeyStr+'To'+__HierarchizedKeyStr+'RetrieveIndexesList',
						self.HierarchizedKeyStrsList
					)
				
				#debug
				'''
				self.debug(('self.',self,[
											'HierarchizedRetrieveIndexesListColumnStrsList',
											'HierarchizedRetrieveIndexesListGetStrsList'
										]))
				'''

		#<NotHook>
		#Return self
		#return self
		#</NotHook>


#</DefineClass>

