# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Catcher instances grasps a Variable, sets a Pointer on it that will be then collected 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Producer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Itemizers import Pointer
from ShareYourSystem.Noders import Noder
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CatcherClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CatchingCollectionStr',
								'CatchingUpdateVariable',
								'CatchingNodeKeyStr',
								'CatchingDefaultNodeKeyStrBool',
								'CatchingDerivePointerClass',
								'CatchingPointBackSetStr',
								'CatchedGraspVariable',
								'CatchedNodeKeyStr',
								'CatchedDerivePointerVariable'
							]

	def default_init(self,
						_CatchingCollectionStr="",
						_CatchingUpdateVariable=None,
						_CatchingNodeKeyStr="",
						_CatchingDefaultNodeKeyStrBool=True,
						_CatchingDerivePointerClass=Pointer.PointerClass,
						_CatchingPointBackSetStr="",
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
									'GraspingClueVariable'
								])
				)
		'''
		
		#grasp
		'''
		self.grasp(
			self.GraspingClueVariable
		)
		'''

		#link
		if type(self.GraspingClueVariable)==SYS.GraspDictClass:
			self.CatchingUpdateVariable=self.GraspingClueVariable

		#Defaut set for the collection keyStr
		if self.CatchingDefaultNodeKeyStrBool:

			#Check
			CatchedGetStr=">UnknowPath<"
			if type(self.GraspingClueVariable) in SYS.StrTypesList:
				
				#set
				CatchedGetStr=self.GraspingClueVariable

			elif type(self.GraspingClueVariable)==SYS.GraspDictClass and type(
				self.GraspingClueVariable['HintVariable']) in SYS.StrTypesList:

				#set
				CatchedGetStr=self.GraspingClueVariable['HintVariable']

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

			#set
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
				'PointingBackSetStr':self.CatchingPointBackSetStr
			}
		).point(
			self.GraspedAnswerVariable,
			'CatchToPointVariable'
		).point(
			self,
			'CatchFromPointVariable'
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
		self.CatchedDerivePointerVariable.update(
			self.CatchingUpdateVariable
		)

		

#</DefineClass>

