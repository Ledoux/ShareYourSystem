#<ImportSpecificModules>
import collections
import copy
import numpy
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
JoinStr='__'
JoinDeepStr='/'
#</DefineLocals>

#<DefineClass>
class JoinerClass(SYS.FeaturerClass):
	
	#<DefineHookMethods>
	def modelAfter(self,**_DatabasingVariablesDict):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					[
						"self.DatabasedDict['ModelStr'] is "+str(self.DatabasedDict['ModelStr']),
						"We are going to join..."
					]
				)

		#Definition the JoinedOrderedDict
		JoinedOrderedDict=collections.OrderedDict()

		#set in DatabasedDict
		self.DatabasedDict['JoinedOrderedDict']=JoinedOrderedDict

		#Call the join method
		self.join()

		#debug
		self.debug(
					[
						"Ok joined was done",
						"self.DatabasedDict['ModelStr'] is "+str(self.DatabasedDict['ModelStr'])
					]
				)

		#Model if there is a JoinedDatabasedDict
		if self.DatabasedDict['JoinedDatabasedDict']!={}:

			#set an alias for the DatabasedModelClass
			DatabasedModelClass=self.DatabasedDict['DatabasedModelClass']

			#Alias
			JoinedRetrievingIndexesListKeyStr=self.DatabasedDict['JoinedRetrievingIndexesListKeyStr']

			#set the columns
			DatabasedModelClass.columns[JoinedRetrievingIndexesListKeyStr]=tables.Int64Col(shape=2)
			
			#Alias
			JoinedNodifiedNodeStr=self.DatabasedDict['JoinedNodifiedNodeStr']

			#Nodify with the JoinedNodifiedNodeStr
			if JoinedNodifiedNodeStr!="":

				#debug
				self.debug('In the DatabasedModelClass we add the joined columns')

				#Alias
				JoinedNodifiedNodedStr=self.DatabasedDict['JoinedNodifiedNodedStr']
				JoinedDatabasedStr=self.DatabasedDict['JoinedDatabasedStr']

				#set the JoinedNodifiedRetrievingIndexesListKeyStrsList
				JoinedNodifiedRetrievingIndexesListKeyStrsList=map(
					lambda __NodifiedKeyStrKeyStr:
					JoinedNodifiedNodedStr+__NodifiedKeyStrKeyStr+JoinedRetrievingIndexesListKeyStr,
					self.DatabasedDict['JoinedNodifiedKeyStrsList']
				)

				#set the Cols for the joined children 
				map(
					lambda __JoinedNodifiedRetrievingIndexesListKeyStr:
					DatabasedModelClass.columns.__setitem__(
						JoinedNodifiedRetrievingIndexesListKeyStrsList,
						tables.Int64Col(shape=2)
					),
					JoinedNodifiedRetrievingIndexesListKeyStrsList
				)

		#Put them in the DatabasedDict
		LocalVars=vars()
		map(
				lambda __GettingStr:
				self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
				[
					'JoinedOrderedDict'
				]
			)

		#debug
		self.debug('End of the method')

	def rowAfter(self,**_RowingVariablesList):

		#debug
		self.debug('Start of the method')

		#debug
		DebuggingStr="self.DatabasedDict['ModelStr'] is "+str(self.DatabasedDict['ModelStr'])
		DebuggingStr+='\nWe are going to check if this model is already inserted...'
		self.debug(DebuggingStr)

		#Alias
		JoinedDatabasedDict=self.DatabasedDict['JoinedDatabasedDict']

		#Check
		if JoinedDatabasedDict!={}:

			#set JoinedRetrievingIndexesListKeyStr
			JoinedRetrievingIndexesListKeyStr=self.DatabasedDict['JoinedRetrievingIndexesListKeyStr']

			#Definition the GettingStrsList and the GettedVariablesList
			if 'ColumningTuplesList' in JoinedDatabasedDict:

				#debug
				self.debug('Check that this row is a new row in the table or not')

				#Get the GettingStrsList and GettedVariablesList
				GettingStrsList=SYS.unzip(JoinedDatabasedDict['ColumningTuplesList'],[0])
				GettedVariablesList=self.pick(GettingStrsList)

				#Check if it was already rowed
				IsRowedBoolsList=map(
						lambda __Row:
						all(
							map(
									lambda __GettingStr,__GettedVariable:
									SYS.getIsEqualBool(__Row[__GettingStr],__GettedVariable),
									GettingStrsList,
									GettedVariablesList
								)
						),
						JoinedDatabasedDict['TabularedTable'].iterrows()
					)					

				#debug
				if hasattr(self,'StructuredKeyStr'):
					self.debug('self.StructuredKeyStr is '+str(self.StructuredKeyStr))
				self.debug('IsRowedBoolsList is '+str(IsRowedBoolsList))

				#If it is rowed then set the JoinedRetrievingIndexesList
				try:
					RowInt=IsRowedBoolsList.index(True)
				except ValueError:
					RowInt=-1

				#debug
				self.debug('So the corresponding RowInt is '+str(RowInt))

				#set the RowInt
				self.DatabasedDict['JoinedOrderedDict'][JoinedRetrievingIndexesListKeyStr][1]=RowInt


			#Alias
			JoinedOrderedDict=self.DatabasedDict['JoinedOrderedDict']
			JoinedRetrievingIndexesList=self.DatabasedDict['JoinedOrderedDict'][JoinedRetrievingIndexesListKeyStr]
			JoinedNodifiedNodeStr=self.DatabasedDict['JoinedNodifiedNodeStr']

			#Give the JoinedRetrievingIndexesList to itself
			JoinedOrderedDict.__setitem__(
				JoinedRetrievingIndexesListKeyStr,
				JoinedRetrievingIndexesList
			)

			#debug
			self.debug(
						[
							'JoinedOrderedDict is now',
							SYS.represent(JoinedOrderedDict)
						]
					)

			#Give to the parent
			if JoinedNodifiedNodeStr!="":
				ParentPointer=getattr(
										self,
										JoinedNodifiedNodedStr+'ParentPointer'
							)
				if ParentPointer!=None:
					ParentPointer['App_Model_'+DatabasingStr+'Dict']['JoinedOrderedDict'][
							getattr(
									self,
									JoinedNodifiedNodedStr+'KeyStr'
									)+JoinedRetrievingIndexesListKeyStr
							]=JoinedRetrievingIndexesList

			#Update the self.RowedIdentifiedOrderedDic
			self.DatabasedDict['RowedIdentifiedOrderedDict'].update(JoinedOrderedDict)

		#debug
		self.debug('End of the method')

	def insertBefore(self,**_InsertingVariablesList):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(	
					[
						"self.DatabasedDict['ModelStr'] is "+str(self.DatabasedDict['ModelStr']),
						'self.StructuredKeyStr is '+str(self.StructuredKeyStr) if hasattr(self,"StructuredKeyStr") else ''
					]
				)

		#Definition the NotRowedTuplesList
		NotRowedTuplesList=filter(
				lambda __JoiningTuple:
				__JoiningTuple[1][0]<0 or __JoiningTuple[1][1]<0,
				self.DatabasedDict['JoinedOrderedDict'].items()
			)

		#debug
		self.debug('NotRowedTuplesList is '+str(NotRowedTuplesList))

		#Alias
		ModelStr=self.DatabasedDict['ModelStr']

		#IsNodingInsertingBool
		if 'IsNodingInsertingBool' not in _InsertingVariablesList or _InsertingVariablesList['IsNodingInsertingBool']:

			#debug
			self.debug(
						[
							'We are going to make insert all the noded children with the Model',
							'ModelStr is '+str(ModelStr)
						]
					)

			#Flush each noded children
			map(
					lambda __Variable:
					__Variable.insert(ModelStr),
					self.DatabasedDict['JoinedNodifiedOrderedDict'].values()
				)

			#debug
			self.debug(
						[
							'The noded children have inserted',
							'Now look at the joined model',
							('self.DatabasedDict',self.DatabasedDict,['JoinedModelStr'])
						]
					)

		#insert the joined model
		if self.DatabasedDict['JoinedModelStr']!="":

			#debug
			self.debug(
						[
							'Flush self with the joined model',
							'But without making the noded children inserting'
						]
					)

			#Copy the DatabasedDict
			CopiedDatabasedDict=copy.copy(self.DatabasedDict)

			#Flush
			self.insert(self.DatabasedDict['JoinedModelStr'],**{'IsNodingInsertingBool':False})

			#debug
			self.debug('Flush self with the joined model was done')
		
			#Reset the self.DatabasedDict
			self.DatabasedDict=CopiedDatabasedDict

			#set the JoinedRetrievingIndexesListKeyStr
			JoinedRetrievingIndexesListKeyStr=self.DatabasedDict['JoinedDatabasedDict']['DatabasedStr']+'RetrievingIndexesList'

			#Alias
			JoinedOrderedDict=self.DatabasedDict['JoinedOrderedDict']

			#It is going to be inserted so update the self.JoinedRetrievingIndexesList to the last row index
			if JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr][1]==-1:

				#debug
				self.debug(
							[
								'This is a new row so we just set the RowInt of the <JoinedDatabasedStr>RetrievingIndexesList',
								'To the size of the table',
								'JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr] is '+str(
									JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr])
							]
						)

				#Update the corresponding RetrievingIndexesList
				JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr][1]=self.DatabasedDict['JoinedDatabasedDict']['TabularedTable'].nrows-1

				#debug
				self.debug('Now JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr] is '+str(
					JoinedOrderedDict[JoinedRetrievingIndexesListKeyStr]))

			#Get the JoinedRetrievingIndexesList
			JoinedRetrievingIndexesListsList=map(
								lambda __InsertingVariable:
								__InsertingVariable.DatabasedDict['JoinedRetrievingIndexesList'],
								self.DatabasedDict['JoinedNodifiedOrderedDict'].values()
							)

		else:

			#set by default an empty list
			JoinedRetrievingIndexesListsList=[]

		#debug
		self.debug(
					[
						'self.StructuredKeyStr is '+str(self.StructuredKeyStr) if hasattr(self,'StructuredKeyStr') else '',
						"self.DatabasedDict['ModelStr'] is "+str(self.DatabasedDict['ModelStr']),
						'We add in the RowedIdentifiedOrderedDict the Joined JoinedRetrievingIndexesLists',
						"self.DatabasedDict['RowedIdentifiedOrderedDict'] is "+str(
								self.DatabasedDict['RowedIdentifiedOrderedDict']),
						"NotRowedTuplesList is "+str(NotRowedTuplesList),
						"JoinedRetrievingIndexesListsList is "+str(JoinedRetrievingIndexesListsList)
					]
		)

		#Alias
		RowedIdentifiedOrderedDict=self.DatabasedDict['RowedIdentifiedOrderedDict']

		#Just change the __RowInt
		map(
				lambda __NotRowedTuple:
				RowedIdentifiedOrderedDict.__setitem__(__NotRowedTuple[0],__NotRowedTuple[1]),
				NotRowedTuplesList
			)

		#debug
		self.debug('Now the RowedIdentifiedOrderedDict is '+str(RowedIdentifiedOrderedDict))

		#debug
		self.debug('End of the method')

	def retrieveAfter(self,**_RetrievingVariablesDict):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug("self.DatabasedDict['RetrievingIndexesList'] is "+str(self.DatabasedDict['RetrievingIndexesList']))

		#Alias
		RetrievedTuplesList=self.DatabasedDict['RetrievedTuplesList']

		#debug	
		DebuggedStr='RetrievedTuplesList is '+str(RetrievedTuplesList)
		self.debug(DebuggedStr)

		#Definition the RetrievingIndexesListIndexInt
		if len(RetrievedTuplesList)>0:

			#Get the Index 
			RetrievingIndexesListIndexInt=SYS.unzip(RetrievedTuplesList,[0]).index(
				self.DatabasedDict['JoinedRetrievingIndexesListKeyStr'])

			#set and retrieve for the joined model
			self.DatabasedDict['RetrievingIndexesList']=RetrievedTuplesList[RetrievingIndexesListIndexInt][1]
			self.retrieve(self.DatabasedDict['JoinedDatabasedDict']['ModelStr'])

		#debug
		self.debug('End of the method')

	def findBefore(self,**_FindingVariablesDict):

		#debug
		self.debug('Find the joined model')

		#Alias
		JoinedModelStr=self.DatabasedDict['JoinedModelStr']

		#Check that JoinedModelStr is good
		if JoinedModelStr!="":

			#Copy the DatabasedDict
			CopiedDatabasedDict=copy.copy(self.DatabasedDict)

			#debug
			self.debug(
						[
							'First we are going to find in the joined model',
							'JoinedModelStr is '+str(JoinedModelStr)
						]
					)

			#Find
			self.DatabasedDict=self.DatabasedDict['JoinedDatabasedDict']
			self.find()
			JoinedDatabasedDict=self.DatabasedDict
			self.DatabasedDict=CopiedDatabasedDict

			#debug
			self.debug(
						[
							'Find in the joined model is done',
							'JoinedModelStr is '+str(JoinedModelStr)
						]
					)

			#debug
			self.debug('Ok we have found the joined model')

			#Copy the FoundFilteredRowedDictsList
			JoinedFoundFilteredRowedDictsList=JoinedDatabasedDict['FoundFilteredRowedDictsList']

			#debug
			self.debug(
						[
							'JoinedFoundFilteredRowedDictsList is ',
							SYS.represent(JoinedFoundFilteredRowedDictsList)
						]
			)

			#Alias
			JoinedRetrievingIndexesListKeyStr=self.DatabasedDict['JoinedRetrievingIndexesListKeyStr']

			#Make the TabularedInt and the RowInt as a <JoinedModelStr>RetrievingIndexesList
			map(
					lambda __JoinedFoundFilteredRowedDict:
					__JoinedFoundFilteredRowedDict.__setitem__(
						JoinedRetrievingIndexesListKeyStr,
						[
							__JoinedFoundFilteredRowedDict['TabularedInt'],
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
											__JoinedFoundFilteredRowedDict['TabularedInt'],
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

			#set an default empty
			JoinedFindingTuplesList=[]

		#debug
		self.debug(
					[
						'Joiner findbefore is over',
						('self.DatabasedDict',self.DatabasedDict,['ModelStr','FoundRowDictsList'])
					]
				)

		#Put them in the DatabasedDict
		LocalVars=vars()
		map(
				lambda __GettingStr:
				self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
				[
					'JoinedFindingTuplesList',
				]
			)

		#debug
		self.debug('End of the method')

	def findAfter(self,**_FindingVariablesDict):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					[
						('Are we going to do a where with the FoundFilteredRowedDictsList and the '),
						('filtering JoinedFindingTuplesList?'),
						('self.DatabasedDict ',self.DatabasedDict,[
																'ModelStr',
																'FoundFilteredRowedDictsList'
																]),
						("'JoinedFindingTuplesList' in self.DatabasedDict is "+str(
							'JoinedFindingTuplesList' in self.DatabasedDict))
					]
			)

		if 'JoinedFindingTuplesList' in self.DatabasedDict:

			#debug
			self.debug(
						[
							'Ok we are going to do the where',
							"self.DatabasedDict['JoinedFindingTuplesList'] is "+str(
								self.DatabasedDict['JoinedFindingTuplesList'])
						]
					)

			#Where
			self.DatabasedDict['FoundFilteredRowedDictsList']=SYS.filterNone(SYS.where(
							self.DatabasedDict['FoundFilteredRowedDictsList'],
							self.DatabasedDict['JoinedFindingTuplesList']
							)
			)

			#debug
			self.debug('Ok the where is done.')

		#debug
		self.debug(
					[
						'After intersection',
						('self.DatabasedDict ',self.DatabasedDict,[
															'ModelStr',
															'FoundFilteredRowedDictsList'
															]
														)
					]
				)

		#debug
		self.debug('End of the method')

	def recoverBefore(self,**_LocalRecoveringVariablesDict):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					[
						('self.DatabasedDict ',self.DatabasedDict,[
															'ModelStr',
															'FoundFilteredRowedDictsList'
															]
														)
					]
				)

		#Alias
		FoundFilteredRowedDictsList=self.DatabasedDict['FoundFilteredRowedDictsList']

		#debug
		self.debug(
					[
						'Look if we have found only one FilteredRowedDict',
						'len(FoundFilteredRowedDictsList) is '+str(len(FoundFilteredRowedDictsList))
					]
				)

		if len(FoundFilteredRowedDictsList)==1:
				
			#debug
			self.debug('It is good, there is one solution !')

			#Definition a JoinedRecoveredDict
			JoinedRecoveredDict=FoundFilteredRowedDictsList[0]

			#Alias
			JoinedNodifiedOrderedDict=self.DatabasedDict['JoinedNodifiedOrderedDict']
			JoinedRetrievingIndexesListKeyStr=self.DatabasedDict['JoinedRetrievingIndexesListKeyStr']
			
			#debug
			self.debug(
						[
							'But first look if we have to recover the children first',
							"len(JoinedNodifiedOrderedDict) is "+str(
								len(JoinedNodifiedOrderedDict))
						]
					)

			#Maybe we have to recover the children before
			if len(JoinedNodifiedOrderedDict)>0:

				self.debug(
							[
								'Yes, we are going to make recover each children before'
							]
						)

				#set each Children and recover each
				JoinedNodifiedKeyStr=self.JoinedNodifiedNodedStr+'KeyStr'

				#Alias
				ModelStr=self.DatabasedDict['ModelStr']
				DatabasingStr=self.DatabasedDict['DatabasingStr']
				JoinedNodifiedNodedStr=self.DatabasedDict['JoinedNodifiedNodedStr']

				#Map a Recover
				map(
						lambda __JoinedJoiner:
						__JoinedJoiner.__setitem__(
								'/App_Model_'+DatabasingStr+'Dict/FindingTuplesList',
								[
									(
										JoinStr+JoinedRetrievingIndexesListKeyStr,
										(
											SYS.getIsEqualBool,
											JoinedRecoveredDict[
											JoinedNodifiedNodedStr+getattr(
													__JoinedJoiner,
													JoinedNodifiedNodedStr
													)+JoinedRetrievingIndexesListKeyStr
											]
										)
									)
								]
						).recover(ModelStr),
						JoinedNodifiedOrderedDict.values()
					)

				#debug
				self.debug('Ok the children are recovered')

			#debug
			self.debug(
						[
							'Maybe update first the joined model by retrieving',
							"JoinedRecoveredDict[JoinedRetrievingIndexesListKeyStr] is "+str(
								JoinedRecoveredDict[JoinedRetrievingIndexesListKeyStr]
								)
						]
					)

			#set RetrievingIndexesList in the model and retrieve
			self['App_Model_'+self.DatabasedDict['JoinedDatabasingStr']+'Dict']['RetrievingIndexesList']=JoinedRecoveredDict[
						JoinedRetrievingIndexesListKeyStr
						]
			self.retrieve(JoinedModelStr)

			#debug
			self.debug('Ok the joined model was retrieved')


			"""
			print('self.JoinedFilteredMergedRowedDictsListTuplesList is')
			SYS._print(self.JoinedFilteredMergedRowedDictsListTuplesList)
			print('AppendingGettingStrsList is ',AppendingGettingStrsList)

			#Next we have maybe to update with the joined model	
			if '/' in AppendingGettingStrsList:	

				#Definition the IndexInt of the joined model
				IndexInt=AppendingGettingStrsList.index('/')

				#Definition the JoinedFilteredMergedRowedDictsList
				JoinedFilteredMergedRowedDictsList=self.JoinedFilteredMergedRowedDictsListTuplesList[
						IndexInt][1] 

				#Definition the JoinedRetrievingIndexesList
				JoinedRetrievingIndexesList=JoinedRecoveredDict[self.JoinedRetrievingIndexesListKeyStr]

				#debug
				print('JoinedFilteredMergedRowedDictsList is ')
				SYS._print(JoinedFilteredMergedRowedDictsList)
				print('JoinedRetrievingIndexesList is ',JoinedRetrievingIndexesList)
				if hasattr(self,'StructuredKeyStr'):
					print("self['StructuredKeyStr'] is ",self.StructuredKeyStr)
				print('')

				#Take the first element of self.JoinedFilteredMergedRowedDictsTuplesList which corresponds to the Joined Model at this level	
				JoinedRowedDict=next(
						RowedDict for RowedDict in JoinedFilteredMergedRowedDictsList
						if SYS.getIsEqualBool(
							RowedDict[self.JoinedRetrievingIndexesListKeyStr],
							JoinedRetrievingIndexesList
						)
					)

				#debug
				'''
				print('JoinedRowedDict is ',JoinedRowedDict)
				print('')
				'''

				#Update
				self.update(JoinedRowedDict.items())
			"""
			
		else:

			#debug
			'''
			print('Joiner There are multiple retrieved states')
			if hasattr(self,'StructuredKeyStr'):
				print("self['StructuredKeyStr'] is ",self.StructuredKeyStr)
			print("self.DatabasedDict['FoundFilteredRowedDictsList'] is ")
			SYS._print(self.DatabasedDict['FoundFilteredRowedDictsList'])
			print('')
			'''

			#Stop the recover
			self.IsRecoveringBool=False

		#debug
		self.debug('End of the method')

	#</DefineHookMethods>
	def join(	
				self,
				_ModelStr="",
				**_JoiningVariablesDict
			):

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					[
						'_ModelStr is '+str(_ModelStr),
						'self.StructuredKeyStr is '+str(self.StructuredKeyStr) if hasattr(self,"StructuredKeyStr") else ''
					]
				)

		#Check
		if 'JoiningTuple' not in self.DatabasedDict:
			self.DatabasedDict['JoiningTuple']=("","")

		#set JoinedNodifiedNodeStr and JoinedModelStr
		JoinedNodifiedNodeStr=self.DatabasedDict['JoiningTuple'][0]
		JoinedModelStr=self.DatabasedDict['JoiningTuple'][1]

		#Put them in the DatabasedDict
		LocalVars=vars()
		map(
				lambda __GettingStr:
				self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
				[
					'JoinedNodifiedNodeStr',
					'JoinedModelStr'
				]
			)

		#set the JoiningTuple
		if 'JoiningTuple' not in _JoiningVariablesDict:

			#set to the _JoiningVariablesDict
			_JoiningVariablesDict['JoiningTuple']=self.DatabasedDict['JoiningTuple']

			#Maybe we have to structure
			if self.IsGroupedBool==False:

				#debug
				self.debug(
							[
								'Join We have to structure first',
								'self.StructuredKeyStr is '+str(self.StructuredKeyStr) if hasattr(self,"StructuredKeyStr") else ''
							]
					)
				
				#Structure
				self.structure(JoinedNodifiedNodeStr)

		#Nodify if there is the nodified objects
		if JoinedNodifiedNodeStr!="":

			#debug
			self.debug('Joiner we are going to nodify the '+str(JoinedNodifiedNodeStr))

			#Nodify
			self.nodify(JoinedNodifiedNodeStr)

			#set 
			JoinedNodifiedOrderedDict=copy.copy(self.NodifiedOrderedDict)
			JoinedNodifiedNodedStr=self.NodifiedNodedStr
			JoinedNodifiedNodingStr=self.NodifiedNodingStr

			#debug
			self.debug('self.JoinedNodifiedOrderedDict is '+str(JoinedNodifiedOrderedDict))

		else:

			#set an empty dict
			JoinedNodifiedOrderedDict=collections.OrderedDict()
			JoinedNodifiedNodedStr=""
			JoinedNodifiedNodingStr=""

		#Put them in the DatabasedDict
		LocalVars=vars()
		map(
				lambda __GettingStr:
				self.DatabasedDict.__setitem__(__GettingStr,LocalVars[__GettingStr]),
				[
					'JoinedNodifiedOrderedDict',
					'JoinedNodifiedNodedStr',
					'JoinedNodifiedNodingStr'
				]
			)

		#debug
		self.debug('We are maybe tabling the joined model ?')

		#Table maybe the joined model
		if JoinedModelStr!="":

			#set a copy of it
			LastDatabasedDict=copy.copy(self.DatabasedDict)

			#debug
			self.debug(
						[
							'We are going to table the joinedModel',
							'JoinedModelStr is '+str(JoinedModelStr)
						]
					)

			#table to configure the joined model
			self.table(JoinedModelStr)

			#debug
			self.debug(
						[
							'The joined model is tabled ok',
							'JoinedModelStr is '+str(JoinedModelStr)
						]
					)

			#Copy the DatabasedDict
			JoinedDatabasedDict=copy.copy(self.DatabasedDict)

			#Reset the DatabasedDict to the original
			self.DatabasedDict=LastDatabasedDict

		else:

			#debug
			self.debug('We dont need to table because this model has not a joined model')

			#Init an empty dict
			JoinedDatabasedDict={}

		#set a link
		self.DatabasedDict['JoinedDatabasedDict']=JoinedDatabasedDict

		#Check
		if JoinedDatabasedDict!={}:

			#debug
			self.debug('We are building the JoinedRetrievingIndexesList and give him the TabularedInt')

			#set the JoinedRetrievingIndexesListKeyStr
			JoinedRetrievingIndexesListKeyStr=JoinedDatabasedDict['DatabasedStr']+'RetrievingIndexesList'
			self.DatabasedDict['JoinedRetrievingIndexesListKeyStr']=JoinedRetrievingIndexesListKeyStr

			#set in the DatabasedDict
			self.DatabasedDict['JoinedOrderedDict'][JoinedRetrievingIndexesListKeyStr]=[JoinedDatabasedDict['TabularedInt'],-1]

			#debug
			self.debug("OK self.DatabasedDict['JoinedOrderedDict' is so "+str(
				self.DatabasedDict['JoinedOrderedDict']))
			
		#debug
		self.debug('End of the method')

		#Return self
		return self

#</DefineClass>

#<DefineAttestingFunctions>
def attest_join():

	#Build Hdf groups
	Joiner=SYS.JoinerClass().hdformat().update(
								[
									(
										'App_Structure_ChildJoiner1',
										SYS.JoinerClass().update(
										[
											('App_Model_ParameterizingDict',
														{
															'ColumningTuplesList':
															[
																('MyIntsList',tables.Int64Col(shape=2))
															]
														}
											),
											('MyIntsList',[2,4]),
											('App_Model_ResultingDict',
														{
															'ColumningTuplesList':
															[
																('MyInt',tables.Int64Col())
															]
														}
											),
											('MyInt',1)
										])
									),
									('App_Model_ParameterizingDict',
														{
															'ColumningTuplesList':
															[
																('MyStr',tables.StrCol(10)),
															]
														}
									),
									('MyStr',"hello")
								]	
							).walk(
										[
											'StructuredOrderedDict.items()'
										],
										**{
												'BeforeUpdateList':
												[
													('parentize',{'ArgsVariable':"Structure"}),
													('group',{'ArgsVariable':""}),
													('model',{'ArgsVariable':"Parameter"}),
													('table',{'ArgsVariable':""}),
													('row',{'ArgsVariable':""}),
													('insert',{'ArgsVariable':""})
												]
											}
									).update(
										[
											
											('App_Model_ResultingDict',
												{
													'ColumningTuplesList':
													[
														('MyFloat',tables.Float32Col()),
														('MyFloatsList',tables.Float32Col(shape=3))
													],
													'JoiningTuple':("Structure","Parameter")
												}
											),
											('MyFloat',0.1),
											('MyFloatsList',[2.3,4.5,1.1])
										]
									).model("Result"		
									).table(
									).row(
									).insert("Result"
									).hdfclose()

	#Return the object itself
	return "Objects is : \n"+SYS.represent(
		Joiner
		)+'\n\n\n'+SYS.represent(os.popen('/usr/local/bin/h5ls -dlr '+Joiner.HdformatingPathStr
		).read())
#</DefineAttestingFunctions>
