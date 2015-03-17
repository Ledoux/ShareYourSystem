# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Joiner instances helps to insert in joined databases, get the corresponding
RetrieveIndexesLists if it was already inserted, and then insert locally
depending if it is a new row compared to all JoinedRetrieveIndexesListsList

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Featurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Featurer=BaseModule
import collections
import tables
from ShareYourSystem.Functers import Argumenter,Hooker,Switcher
from ShareYourSystem.Standards.Modelers import Modeler
#</ImportSpecificModules>

#<DefineLocals>
JoinStr='__'
JoinDeepStr='/'
#</DefineLocals>

#<DefineFunctions>
def getJoinedRetrieveIndexesListWithInstanceVariableAndDeriveDatabaserPointer(
	_InstanceVariable,_DeriveDatabaserPointer):

	#Table
	_DeriveDatabaserPointer.table()

	#set the JoinedRetrieveIndexesListKeyStr
	return [_DeriveDatabaserPointer.TabledInt,-1]

#<DefineFunctions>

#<DefineClass>
@DecorationClass()
class JoinerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'JoiningDownGetKeyStrsList',
									'JoinedDownDeriveJoinersList',
									'JoinedRetrieveIndexesListGetStrsList',
									'JoinedRetrieveIndexesListColumnStrsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_JoiningDownGetKeyStrsList=[],
						_JoinedDownDeriveJoinersList=None,
						_JoinedRetrieveIndexesListGetStrsList=[],
						_JoinedRetrieveIndexesListColumnStrsList=[],
						_JoinedInsertIndexIntsList=[],
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
	def model(self,**_KwargVariablesDict):

		#<NotHook>
		#database and join first
		self.database()
		self.join()
		#</NotHook>
		
		#debug
		self.debug('Add in the ModelingDescriptionTuplesList')

		#set
		self.ModelingDescriptionTuplesList+=map(
				lambda __JoinedRetrieveIndexesListGetStr,__JoinedRetrieveIndexesListColumnStr:
				(
					__JoinedRetrieveIndexesListGetStr,
					__JoinedRetrieveIndexesListColumnStr,
					tables.Int64Col(shape=2)
				),
				self.JoinedRetrieveIndexesListGetStrsList,
				self.JoinedRetrieveIndexesListColumnStrsList
			)

		#debug
		self.debug(('self.',self,['ModelingDescriptionTuplesList']))

		#<NotHook>
		#join and model first
		Featurer.FeaturerClass.model(self)
		#</NotHook>

	#@Hooker.HookerClass(**{
	#	'HookingAfterVariablesList':[
	#			{'CallingMethodStr':'table'}
	#		]
	#	,
	#	'HookingBeforeVariablesList':[
	#			{'CallingVariable':Featurer.FeaturerClass.row}
	#		]
	#	}	
	#)
	def row(self,**_KwargsVariablesDict):

		#<NotHook>
		#table first
		self.table()
		#</NotHook>

		#debug
		self.debug(
					[
						("We are going to check if is already inserted in the joined databases..."),
						('self.',self,['JoinedDownDeriveJoinersList'])
					]
				)

		#set
		self.JoinedInsertIndexIntsList=map(
					lambda __JoinedDeriveDatabaserPointer:
					__JoinedDeriveDatabaserPointer.row().RowedIndexInt,
					self.JoinedDownDeriveJoinersList
				)

		#debug
		self.debug(('self.',self,[
									'JoinedInsertIndexIntsList',
									'JoinedRetrieveIndexesListGetStrsList'

								]))

		#set the modeled int in the retrieve tuples
		map(
				lambda __JoinedRetrieveIndexesListGetStr,__JoinedInsertIndexInt:
				getattr(
					self.NodedDatabaseParentPointer,
					__JoinedRetrieveIndexesListGetStr
					).__setitem__(
						1,
						__JoinedInsertIndexInt
				),
				self.JoinedRetrieveIndexesListGetStrsList,
				self.JoinedInsertIndexIntsList
			)

		#Add in the RowingKeyStrsList
		self.RowingKeyStrsList+=self.JoinedRetrieveIndexesListGetStrsList

		#debug
		self.debug('Now row with Featurer')

		#<NotHook>
		#row then
		Featurer.FeaturerClass.row(self)
		#</NotHook>

		#debug
		self.debug('Ok row is over')

	#@Hooker.HookerClass(**{
	#	'HookingAfterVariablesList':[
	#		{'CallingMethodStr':'row'}
	#	],
	#	'HookingBeforeVariablesList':[
	#		{'CallingVariable':Featurer.FeaturerClass.insert}
	#	]
	#}
	#)
	def insert(self,**_KwargVariablesDict):

		#<NotHook>
		#row first
		self.row()
		#</NotHook>

		#debug
		self.debug('First make insert the joined databases')

		#Insert the joined databases
		self.JoinedInsertIndexIntsList=map(
					lambda __JoinedDeriveDatabaserPointer:
					__JoinedDeriveDatabaserPointer.insert(),
					self.JoinedDownDeriveJoinersList
				)

		#debug
		self.debug('Now we can insert')

		#<NotHook>
		#insert then
		Featurer.FeaturerClass.insert(self)
		#</NotHook>

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[
	#	{'CallingVariable':Featurer.FeaturerClass.retrieve}]
	#	}
	#)
	def retrieve(self,**_KwargVariablesDict):

		

		#debug
		self.debug("self.",self,['RetrievingIndexesList','RetrievedTuplesList'])

		#Definition the RetrievingIndexesListIndexInt
		if len(self.RetrievedTuplesList)>0:

			#Get the Index 
			RetrievingIndexesListIndexInt=SYS.unzip(self.RetrievedTuplesList,[0]).index(
				self.JoinedRetrievingIndexesListKeyStr)

			#set and retrieve for the joined model
			self.RetrievingIndexesList=self.RetrievedTuplesList[RetrievingIndexesListIndexInt][1]
			self.JoinedDeriveDatabaserPointer.retrieve()

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Featurer.FeaturerClass.find}]})
	def find(self,**_KwargVariablesDict):

		#Check that JoiningDatabaseKeyStr is good
		if JoiningDatabaseKeyStr!="":

			#Find
			self.JoinedDeriveDatabaserPointer.find()

			#debug
			self.debug('Ok we have found the joined model')

			#Copy the FoundFilteredRowedDictsList
			JoinedFoundFilteredRowedDictsList=self.JoinedDeriveDatabaserPointer['FoundFilteredRowedDictsList']

			#debug
			self.debug(
						[
							'JoinedFoundFilteredRowedDictsList is ',
							SYS.represent(JoinedFoundFilteredRowedDictsList)
						]
			)

			#Alias
			JoinedRetrievingIndexesListKeyStr=self.ModeledDict['JoinedRetrievingIndexesListKeyStr']

			#Make the TabledInt and the RowInt as a <JoiningDatabaseKeyStr>RetrievingIndexesList
			map(
					lambda __JoinedFoundFilteredRowedDict:
					__JoinedFoundFilteredRowedDict.__setitem__(
						JoinedRetrievingIndexesListKeyStr,
						[
							__JoinedFoundFilteredRowedDict['TabledInt'],
							__JoinedFoundFilteredRowedDict['RowInt'],
						]
					),
					JoinedFoundFilteredRowedDictsList
				)

			#set the JoinedFindingTuplesList
			JoinedFindingTuplesList=[
						(
							JoinedRetrievingIndexesListKeyStr,
							(
								SYS.getIsInListBool,
								map(
										lambda __JoinedFoundFilteredRowedDict:
										[
											__JoinedFoundFilteredRowedDict['TabledInt'],
											__JoinedFoundFilteredRowedDict['RowInt'],
										],
										JoinedFoundFilteredRowedDictsList
									)
							)
					)
				]

			#debug
			self.debug(
						[
							'JoinedFindingTuplesList is',
							SYS.represent(JoinedFindingTuplesList)
						]
					)

		else:

			#set a default empty
			JoinedFindingTuplesList=[]

		#debug
		self.debug(
					[
						('self.ModeledDict',self.ModeledDict,['ModelStr','FoundRowDictsList'])
					]
				)

		#Put them in the ModeledDict
		LocalVars=vars()
		map(
				lambda __GettingStr:
				self.ModeledDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
				[
					'JoinedFindingTuplesList',
				]
			)

	def findAfter(self,**_FindingVariablesDict):

		#debug
		self.debug(
					[
						('Are we going to do a where with the FoundFilteredRowedDictsList and the '),
						('filtering JoinedFindingTuplesList?'),
						('self.ModeledDict ',self.ModeledDict,[
																'ModelStr',
																'FoundFilteredRowedDictsList'
																]),
						("'JoinedFindingTuplesList' in self.ModeledDict is "+str(
							'JoinedFindingTuplesList' in self.ModeledDict))
					]
			)

		if 'JoinedFindingTuplesList' in self.ModeledDict:

			#debug
			self.debug(
						[
							'Ok we are going to do the where',
							"self.ModeledDict['JoinedFindingTuplesList'] is "+str(
								self.ModeledDict['JoinedFindingTuplesList'])
						]
					)

			#Where
			self.ModeledDict['FoundFilteredRowedDictsList']=SYS.filterNone(SYS.where(
							self.ModeledDict['FoundFilteredRowedDictsList'],
							self.ModeledDict['JoinedFindingTuplesList']
							)
			)

			#debug
			self.debug('Ok the where is done.')

		#debug
		self.debug(
					[
						'After intersection',
						('self.ModeledDict ',self.ModeledDict,[
															'ModelStr',
															'FoundFilteredRowedDictsList'
															]
														)
					]
				)

		#debug
		self.debug('End of the method')

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[
		{'CallingVariable':Featurer.FeaturerClass.recover}]})
	def recover(self,**_LocalRecoveringVariablesDict):

		#debug
		self.debug(
					[
						('self.',self,[
											'ModelingModelStr',
											'FoundFilteredRowedDictsList'
											]
										)
					]
				)

		#debug
		self.debug(
					[
						'Look if we have found only one FilteredRowedDict',
						'len(self.FoundFilteredRowedDictsList) is '+str(len(self.FoundFilteredRowedDictsList))
					]
				)

		if len(self.FoundFilteredRowedDictsList)==1:
				
			#debug
			self.debug('It is good, there is one solution !')

			#Definition a JoinedRecoveredDict
			JoinedRecoveredDict=self.FoundFilteredRowedDictsList[0]

			#Alias
			JoinedRetrievingIndexesListKeyStr=self.ModeledDict['JoinedRetrievingIndexesListKeyStr']
				
		else:

			#debug
			self.debug('There are multiple found states')

			#Stop the recover
			self.RecoveringIsBool=False

	#@Switcher.SwitcherClass()
	@Argumenter.ArgumenterClass()
	def join(	
				self,
				_DatabaseKeyStr=None,
				**_KwargVariablesDict
			):

		#Init
		if self.JoinedDownDeriveJoinersList==None:
			self.JoinedDownDeriveJoinersList=[]

		#Check
		if hasattr(self,'NodedDatabaseParentPointer'):
				
			#debug
			self.debug('Look for the Joined databases...')

			#Get with the good names
			'''
			JoinedList=SYS._filter(
							lambda __DeriveDatabaser:
							__DeriveDatabaser.__class__.NameStr.join(
								__DeriveDatabaser.NodedDatabaseKeyStr.split(
									__DeriveDatabaser.__class__.NameStr)[:-1]
								)==self.JoiningDatabaseKeyStr,
							self.NodedDatabaseParentPointer['<Database>']
						)
			'''

			#set
			self.JoinedDownDeriveJoinersList=map(
				self.NodedDatabaseParentPointer.NodedDatabaseOrderedDict.__getitem__,
				self.JoiningDownGetKeyStrsList
			)

			#set
			self.JoinedRetrieveIndexesListColumnStrsList=map(
					lambda __JoiningDatabaseKeyStr:
					'Joined'+__JoiningDatabaseKeyStr+'RetrieveIndexesList',
					self.JoiningDownGetKeyStrsList
				)

			self.JoinedRetrieveIndexesListGetStrsList=map(
					lambda __JoiningDatabaseKeyStr:
					'Joined'+self.ModelingKeyStr+'To'+__JoiningDatabaseKeyStr+'RetrieveIndexesList',
					self.JoiningDownGetKeyStrsList
				)
			
			#Table all the joined databasers and init the corresponding JoinedRetrieveIndexesList in the NodedDatabaseParentPointer
			self.NodedDatabaseParentPointer.update(
				zip(
						self.JoinedRetrieveIndexesListGetStrsList,
						map(
							lambda __JoinedDeriveDatabaserPointer:
							getJoinedRetrieveIndexesListWithInstanceVariableAndDeriveDatabaserPointer(
								self,
								__JoinedDeriveDatabaserPointer
							),
							self.JoinedDownDeriveJoinersList
						)
					)
			)

			#debug
			self.debug(('self.',self,[
										'JoinedRetrieveIndexesListColumnStrsList',
										'JoinedRetrieveIndexesListGetStrsList'
									]))
#</DefineClass>

