# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Catcher instances grasps a Variable, sets a To Pointer on this latter Variable,
also a Pointer on the source Catcher, give a CatchKeyStr, and makes collect this
grapsed Variables.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Arrayer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer
from ShareYourSystem.Standards.Noders import Noder
import collections
import copy
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
									'CatchingCollectionStr',
									'GraspingClueVariable'
								])
				)
		'''
		
		#link
		if type(self.GraspingClueVariable)==SYS.GraspDictClass:
			self.CatchingUpdateVariable=copy.deepcopy(self.GraspingClueVariable)

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchingUpdateVariable'
								])
				)
		'''

		#Defaut set for the collection keyStr
		self.CatchedNodeKeyStr=""
		if self.CatchingDefaultNodeKeyStrBool:

			#Check
			CatchedGetStr=">UnknowPath<"
			if type(self.GraspingClueVariable) in SYS.StrTypesList:
				
				#set
				CatchedGetStr=self.GraspingClueVariable

			elif type(self.GraspingClueVariable)==SYS.GraspDictClass and type(
				self.GraspingClueVariable['HintVariable']
				) in SYS.StrTypesList:

				#set
				CatchedGetStr=self.NodeKeyStr+self.GraspingClueVariable['HintVariable']

			elif hasattr(self.GraspedAnswerVariable,'parent'):

				#Get the up
				CatchedUpNodeKeyStrsList=(self.parent(
					).ParentedNodePathStr+'/'+self.NodeKeyStr).split('/')
				CatchedUpNodeKeyStrsList.reverse()
				CatchedUpPathStr='/'.join(CatchedUpNodeKeyStrsList[:-1])

				#Get the down
				CatchedDownNodeKeyStrsList=(self.GraspedAnswerVariable.parent(
					).ParentedNodePathStr+'/'+self.GraspedAnswerVariable.NodeKeyStr).split('/')
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
									'CatchingDerivePointerClass'
								])
					)
		'''

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
		).__setitem__(
			'CatchKeyStr',self.CatchedNodeKeyStr
		)

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchingCollectionStr',
									'CatchedNodeKeyStr',
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

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchingUpdateVariable'
								])
				)
		'''

		#set
		self.CatchedDerivePointerVariable.update(
			self.CatchingUpdateVariable
		)

		

#</DefineClass>

