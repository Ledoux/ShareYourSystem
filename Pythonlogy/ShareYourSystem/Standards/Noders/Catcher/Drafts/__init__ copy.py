# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Catcher instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Producer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer
from ShareYourSystem.Standards.Noders import Noder
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CatcherClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CatchingGraspClueVariable',
								'CatchingCollectionStr',
								'CatchingUpdateVariable',
								'CatchingNodeKeyStr',
								'CatchingDefaultNodeKeyStrBool',
								'CatchingDerivePointerClass',
								'CatchingPointBackBool',
								'CatchedGraspVariable',
								'CatchedNodeKeyStr',
								'CatchedDerivePointerVariable'
							]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_CatchingGraspClueVariable="",
						_CatchingCollectionStr="",
						_CatchingUpdateVariable=None,
						_CatchingNodeKeyStr="",
						_CatchingDefaultNodeKeyStrBool=True,
						_CatchingDerivePointerClass=Pointer.PointerClass,
						_CatchingPointBackBool=False,
						_CatchedGraspVariable=None,
						_CatchedNodeKeyStr="",
						_CatchedDerivePointerVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_catch(self):
		
		#debug
		'''
		self.debug(
					('self.',self,[
									'CollectingCollectionStr',
									'CatchingGraspClueVariable'
								])
				)
		'''
		
		#grasp
		self.grasp(
			self.CatchingGraspClueVariable
		)

		#Defaut set for the collection keyStr
		if self.CatchingDefaultNodeKeyStrBool:

			#Check
			CatchedGetStr=">UnknowPath<"
			if type(self.CatchingGraspClueVariable) in SYS.StrTypesList:
				CatchedGetStr=self.CatchingGraspClueVariable

			elif hasattr(self.GraspedAnswerVariable,'parent'):

				#Get the up
				CatchedUpNodeKeyStrsList=(self.parent(
					).ParentedPathStr+'/'+self.NodeKeyStr).split('/')
				CatchedUpNodeKeyStrsList.reverse()
				CatchedUpPathStr='/'.join(CatchedUpNodeKeyStrsList[:-1])

				#Get the down
				CatchedDownNodeKeyStrsList=(self.GraspedAnswerVariable.parent(
					).ParentedPathStr+'/'+self.GraspedAnswerVariable.NodeKeyStr).split('/')
				CatchedDownPathStr='/'.join(CatchedDownNodeKeyStrsList[1:])

				#Get the top
				CatchedTopStr=CatchedUpNodeKeyStrsList[-1]

				if CatchedUpNodeKeyStrsList[-1]==CatchedDownNodeKeyStrsList[0]:

					#set
					CatchedGetStr=CatchedUpPathStr+'>'+CatchedTopStr+'<'+CatchedDownPathStr					


			#debug
			'''
			self.debug('CatchedGetStr is '+CatchedGetStr)
			'''

			#set
			'''
			self.CollectingNodeKeyStr=self.GraspedAnswerVariable.__class__.NameStr.join(
				NodeKeyStr.split(
					Noder.NodingSuffixGetStr)[-1].split(self.GraspedAnswerVariable.__class__.NameStr
					)[:-1]
				)
			'''

			'''
			CatchedNodeKeyStr=CatchedGetStr.split(
					Noder.NodingSuffixGetStr
			)[-1]
			'''

			'''
			#Check
			if self.GraspedAnswerVariable.NodePointDeriveNoder!=None:
				if self.GraspedAnswerVariable.NodePointDeriveNoder.NodeKeyStr=="":
					CatchedPrefixStr='Top'+self.GraspedAnswerVariable.NodePointDeriveNoder.__class__.NameStr
				else:
					CatchedPrefixStr=self.GraspedAnswerVariable.NodePointDeriveNoder.NodeKeyStr
			else:
				CatchedPrefixStr=""

			#set
			self.CatchedNodeKeyStr=CatchedPrefixStr+'_'+CatchedGetStr
			'''

			self.CatchedNodeKeyStr=CatchedGetStr

		else:

			#Look for one
			self.CatchedNodeKeyStr=self.CatchingNodeKeyStr
			
		#adapt the 
		self.CatchedNodeKeyStr=self.CatchedNodeKeyStr.replace('/','_')

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchingCollectionStr',
									'CatchedNodeKeyStr'
								])
					)
		'''

		#Check
		if self.CatchingCollectionStr=="":
			self.CatchingCollectionStr=self.CollectingCollectionStr

		#init
		self.CatchedDerivePointerVariable=self.CatchingDerivePointerClass(
			**{
				'PointingBackBool':self.CatchingPointBackBool
			}
		).point(
			self.GraspedAnswerVariable,
			'CatchToPointVariable'
		)

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchedDerivePointerVariable'
								])
					)
		'''
		
		#collect and update
		self.collect(
					self.CatchingCollectionStr,
					self.CatchedNodeKeyStr,
					self.CatchedDerivePointerVariable
				)

		#set
		self.CatchedDerivePointerVariable.update(self.CatchingUpdateVariable)

#</DefineClass>

