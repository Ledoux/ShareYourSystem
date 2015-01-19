# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Joiner instances helps to flush in joined databases, get the corresponding
RetrieveIndexesLists if it was already flushed, and then flush locally
depending if it is a new row compared to all JoinedRetrieveIndexesListsList

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Merger"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Featurer=BaseModule
import collections
import tables
from ShareYourSystem.Modelers import Modeler
#</ImportSpecificModules>

#<DefineLocals>
JoinStr='__'
JoinDeepStr='/'
#</DefineLocals>

#<DefineFunctions>
def getJoinedRetrieveIndexesListWithInstanceVariableAndDeriveDatabaser(
	_InstanceVariable,_DeriveDatabaser):

	#Table
	_DeriveDatabaser.table().pick(['TabledInt',-1])

	#set the JoinedRetrieveIndexesListKeyStr
	return [_DeriveDatabaser.TabledInt,-1]
#<DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':[
		'model',
		'tabular',
		'join',
		'flush'
	]
})
class JoinerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'JoiningCollectionStr',
								'JoiningCatchStr',
								'JoiningAttentionStr',
								'JoiningFindBeforeBool',
								'JoinedCatchCollectionOrderedDict',
								'JoinedCatchDeriveJoinersList',
								'JoinedRetrieveIndexesListGetStrsList',
								'JoinedRetrieveIndexesListColumnStrsList',
								'JoinedFlushIndexIntsList'
							]

	def default_init(self,
						_JoiningCollectionStr="",
						_JoiningCatchStr="",
						_JoiningAttentionStr="",
						_JoiningFindBeforeBool=True,
						_JoinedAttentionCollectionOrderedDict=None,
						_JoinedCatchCollectionOrderedDict=None,
						_JoinedCatchDeriveJoinersList=None,
						_JoinedRetrieveIndexesListGetStrsList=None,
						_JoinedRetrieveIndexesListColumnStrsList=None,
						_JoinedFlushIndexIntsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def mimic_database(self):

		#debug
		'''
		self.debug('We join first')
		'''

		#<NotHook>
		#join first
		self.join()
		#</NotHook>
		
		#debug
		'''
		self.debug('Add in the DatabasingSealTuplesList')
		'''
		
		#set
		if len(self.JoinedRetrieveIndexesListColumnStrsList)>0:
			self.DatabasingSealTuplesList=map(
				lambda __JoinedRetrieveIndexesListGetStr,__JoinedRetrieveIndexesListColumnStr:
				(
					__JoinedRetrieveIndexesListGetStr,
					__JoinedRetrieveIndexesListColumnStr,
					tables.Int64Col(shape=2)
				),
				self.JoinedRetrieveIndexesListGetStrsList,
				self.JoinedRetrieveIndexesListColumnStrsList
			)+self.DatabasingSealTuplesList

		#debug
		'''
		self.debug(
					[	
						('self.',self,['DatabasingSealTuplesList']),
						'Now call the parent model method'
					]
				)
		'''

		#<NotHook>
		#then database 
		BaseClass.database(self)
		#</NotHook>

	def mimic_row(self):

		#debug
		'''
		self.debug('Maybe we have to join first')
		'''

		#<NotHook>
		#table and join first
		self.table()
		self.join()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						("We are going to check if is already flushed in the joined databases..."),
						('self.',self,['JoinedCatchDeriveJoinersList'])
					]
				)
		'''

		#set
		self.JoinedFlushIndexIntsList=map(
					lambda __JoinedDeriveDatabaserPointer:
					__JoinedDeriveDatabaserPointer.row().RowedIndexInt,
					self.JoinedCatchDeriveJoinersList
				)

		#debug
		'''
		self.debug(('self.',self,[
									'JoinedFlushIndexIntsList',
									'JoinedRetrieveIndexesListGetStrsList'

								]))
		'''

		#set the modeled int in the retrieve tuples
		map(
				lambda __JoinedRetrieveIndexesListGetStr,__JoinedFlushIndexInt:
				getattr(
					self.NodePointDeriveNoder,
					__JoinedRetrieveIndexesListGetStr
					).__setitem__(
						1,
						__JoinedFlushIndexInt
				),
				self.JoinedRetrieveIndexesListGetStrsList,
				self.JoinedFlushIndexIntsList
			)

		#debug
		'''
		self.debug([
						('Before updating the RowingGetStrsList'),
						#('self.',self,['NodePointDeriveNoder'])
						('model first to set the DatabasedGetStrToColumStr')
					]
				)
		'''

		#Model first to set the DatabasedGetStrToColumStr
		#self.model()

		#Add in the RowingGetStrsList
		self.RowingGetStrsList=self.JoinedRetrieveIndexesListGetStrsList+self.RowingGetStrsList

		#debug
		'''
		self.debug('Now row with Featurer')
		'''

		#<NotHook>
		#row then
		BaseClass.row(self)
		#</NotHook>

		#debug
		'''
		self.debug('Ok row is over for joining')
		'''

	def mimic_flush(self):

		#<NotHook>
		#row first
		self.row()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						'First setSwitch and make flush the catched databases',
						('self.',self,[
											'JoiningCatchStr',
											'JoiningCollectionStr'
									])
					]
				)
		'''
		
		#Flush the post joined databases
		self.JoinedFlushIndexIntsList=map(
			lambda __JoinedCatchDeriveJoinerPointer:
			__JoinedCatchDeriveJoinerPointer.CatchToPointVariable.flush(),
			self.JoinedCatchCollectionOrderedDict.values(),
		)

		#switch first
		self.transmit(
			[
				('setSwitch',{
						'LiargVariablesList':[],
						'KwargVariablesDict':
						{
							'_ClassVariable':"Joiner",
							'_DoStrsList':['Flush']
						}
					}
				)
			],
			[self.JoiningCatchStr+self.JoiningCollectionStr]
		)

		#debug
		'''
		self.debug('Now we can flush here')
		'''

		#<NotHook>
		#flush then
		BaseClass.flush(self)
		#</NotHook>
		
	def mimic_retrieve(self):

		#debug
		'''
		self.debug(('self.',self,['RetrievingIndexesList']))
		'''

		#<NotHook>
		#retrieve first
		BaseClass.retrieve(self)
		#</NotHook>

		#Retrieve in the joined databases
		self.JoinedFlushIndexIntsList=map(
					lambda __JoinedRetrieveIndexesListGetStr,__JoinedDeriveDatabaserPointer:
					__JoinedDeriveDatabaserPointer.retrieve(
						getattr(
							self.NodePointDeriveNoder,
							__JoinedRetrieveIndexesListGetStr
						)
					),
					self.JoinedRetrieveIndexesListGetStrsList,
					self.JoinedCatchDeriveJoinersList
				)

	def mimic_find(self):

		#<NotHook>
		#table first
		self.table()
		#</NotHook>

		#debug
		'''
		self.debug(('self.',self,['FindingConditionTuplesList']))
		'''

		#
		if self.JoiningFindBeforeBool:

			#Find in the joined databases
			JoinedFindFilterRowDictsListsList=map(
					lambda __JoinedDeriveDatabaserPointer:
					__JoinedDeriveDatabaserPointer.find().FoundFilterRowDictsList,
					self.JoinedCatchDeriveJoinersList
				)

			#debug
			'''
			self.debug('JoinedFindFilterRowDictsListsList is '+str(JoinedFindFilterRowDictsListsList))
			'''

			#Just keep the retrieve lists
			JoinedFindFilterRetrieveListsList=map(
						lambda __JoinedFindFilterRowDictsList:
						map(
								lambda __JoinedFindFilterRowDict:
								[
									__JoinedFindFilterRowDict['TabledInt']
									if 'TabledInt' in __JoinedFindFilterRowDict else 0,
									__JoinedFindFilterRowDict['RowInt']
								],
								__JoinedFindFilterRowDictsList
							),
						JoinedFindFilterRowDictsListsList
			)

			#debug
			'''
			self.debug('JoinedFindFilterRetrieveListsList is '+str(JoinedFindFilterRetrieveListsList))
			'''

			#Map
			JoinedFindingConditionTuplesList=map(
					lambda __JoinedRetrieveIndexesListColumnStr,__JoinedFindFilterRetrieveList:
					(
						__JoinedRetrieveIndexesListColumnStr,
						(
							SYS.getIsInListBool,
							__JoinedFindFilterRetrieveList
						)
					),
					self.JoinedRetrieveIndexesListColumnStrsList,
					JoinedFindFilterRetrieveListsList
				)

			#debug
			'''
			self.debug('JoinedFindingConditionTuplesList is '+str(JoinedFindingConditionTuplesList))
			'''

			#Add to the finding condition tuples
			self.FindingConditionTuplesList+=JoinedFindingConditionTuplesList

			#Call the parent method
			Featurer.FeaturerClass.find(self)

		else:
			
			#Call the parent method
			BaseClass.find(self).FoundFilterRowDictsList

	def do_join(	
				self
			):

		#<NotHook>
		#model first
		self.model()
		#</NotHook>

		#Check
		if self.JoiningCollectionStr=="":
			self.JoiningCollectionStr=self.NetworkCollectionStr
		if self.JoiningCatchStr=="":
			self.JoiningCatchStr=self.NetworkCatchStr
		if self.JoiningAttentionStr=="":
			self.JoiningAttentionStr=self.NetworkAttentionStr

		#debug
		'''
		self.debug(
					('self.',self,[
									'JoiningCollectionStr',
									'JoiningCatchStr',
									'JoiningAttentionStr'
								])
				)
		'''
		#set
		JoinedAttentionCollectionOrderedDictKeyStr=self.JoiningAttentionStr+self.JoiningCollectionStr+"CollectionOrderedDict"

		#check
		if hasattr(
			self,
			JoinedAttentionCollectionOrderedDictKeyStr
		):

			#get
			self.JoinedAttentionCollectionOrderedDict=getattr(
				self,
				JoinedAttentionCollectionOrderedDictKeyStr
			)

		#set
		JoinedCatchCollectionOrderedDictKeyStr=self.JoiningCatchStr+self.JoiningCollectionStr+"CollectionOrderedDict"

		#check
		if hasattr(self,JoinedCatchCollectionOrderedDictKeyStr):

			#get
			self.JoinedCatchCollectionOrderedDict=getattr(
				self,
				JoinedCatchCollectionOrderedDictKeyStr
			)

			#model and link all the catched joiners
			self.JoinedCatchDeriveJoinersList=map(
					lambda __JoinedCatchDeriveJoiner:
					#__JoinedCatchDeriveJoiner.__setitem__(
					#	'FlushIsBool',
					#	False
					#).CatchToPointVariable.model(
					#),
					__JoinedCatchDeriveJoiner.CatchToPointVariable.model(),
					self.JoinedCatchCollectionOrderedDict.values()
				)

			#debug
			'''
			self.debug(('self.',self,['JoinedCatchCollectionOrderedDict']))
			'''

			#set
			self.JoinedRetrieveIndexesListColumnStrsList=map(
					lambda __JoinedCatchDeriveJoiner:
					"Join"+''.join(
						[
							__JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.NodeKeyStr
							if __JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.NodeKeyStr!="" 
							else 'Top'+__JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.__class__.NameStr,
							__JoinedCatchDeriveJoiner.ModeledSuffixStr
						]
					)+"RetrieveIndexesList",
					self.JoinedCatchDeriveJoinersList,
				)

			#debug
			'''
			self.debug(('self.',self,['JoinedRetrieveIndexesListColumnStrsList']))
			'''

			#set
			self.JoinedRetrieveIndexesListGetStrsList=map(
					lambda __JoinedCatchDeriveJoiner:
					"Joined"+''.join(
						[
							self.ModeledPointDeriveStorerVariable.NodeKeyStr
							if self.ModeledPointDeriveStorerVariable.NodeKeyStr!="" 
							else 'Top'+self.ModeledPointDeriveStorerVariable.__class__.NameStr,
							self.ModeledSuffixStr,
							'To',
							__JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.NodeKeyStr
							if __JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.NodeKeyStr!="" 
							else 'Top'+__JoinedCatchDeriveJoiner.ModeledPointDeriveStorerVariable.__class__.NameStr,
							__JoinedCatchDeriveJoiner.ModeledSuffixStr
						]
					)+"RetrieveIndexesList",
					self.JoinedCatchDeriveJoinersList,
				)
			
			#debug
			'''
			self.debug(
						[
							('self.',self,['JoinedRetrieveIndexesListGetStrsList']),
							'Table the joined databases'
						]
					)
			'''

			#Table all the joined databasers and init the corresponding JoinedRetrieveIndexesList in the NodePointDeriveNoder
			self.ModeledPointDeriveStorerVariable.update(
				zip(
						self.JoinedRetrieveIndexesListGetStrsList,
						map(
							lambda __JoinedCatchDeriveJoiner:
							[
								__JoinedCatchDeriveJoiner.table()['TabledInt'],
								-1
							],
							self.JoinedCatchDeriveJoinersList
						)
					)
			)

			#debug
			'''
			self.debug(
						('self.',self,[
										'JoinedRetrieveIndexesListColumnStrsList',
										'JoinedRetrieveIndexesListGetStrsList'
									])
			)
			'''
#</DefineClass>

