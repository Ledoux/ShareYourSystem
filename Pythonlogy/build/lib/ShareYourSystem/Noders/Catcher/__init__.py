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
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Itemizers import Pointer
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CatcherClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'CatchingGetVariable',
									'CatchingCollectionStr',
									'CatchingNodeKeyStr',
									'CatchingDefaultNodeKeyStrBool',
									'CatchingNodeClass',
									'CatchingPointBackBool',
									'CatchedGetVariable',
									'CatchedNodeKeyStr',
									'CatchedPointVariable'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_CatchingGetVariable="",
						_CatchingCollectionStr="",
						_CatchingNodeKeyStr="",
						_CatchingDefaultNodeKeyStrBool=True,
						_CatchingNodeClass=Pointer.PointerClass,
						_CatchingPointBackBool=False,
						_CatchedGetVariable=None,
						_CatchedNodeKeyStr="",
						_CatchedPointVariable=None,
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
									'CatchingGetVariable'
								])
				)
		'''
		
		#get by checking if it is already getted
		if type(self.CatchingGetVariable) in SYS.StrTypesList:
			self.CatchedGetVariable=self[self.CatchingGetVariable]
		else:
			self.CatchedGetVariable=self.CatchingGetVariable

		#Defaut set for the collection keyStr
		if self.CatchingDefaultNodeKeyStrBool:

			#Check
			CatchedGetStr=">UnknowPath<"
			if type(self.CatchingGetVariable) in SYS.StrTypesList:
				CatchedGetStr=self.CatchingGetVariable
			else:

				#Get the up
				CatchedUpNodeKeyStrsList=(self.parent(
					).ParentedPathStr+'/'+self.NodeKeyStr).split('/')
				CatchedUpNodeKeyStrsList.reverse()
				CatchedUpPathStr='/'.join(CatchedUpNodeKeyStrsList[:-1])

				#Get the down
				CatchedDownNodeKeyStrsList=(self.CatchingGetVariable.parent(
					).ParentedPathStr+'/'+self.CatchingGetVariable.NodeKeyStr).split('/')
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
			self.CollectingNodeKeyStr=self.CatchedGetVariable.__class__.NameStr.join(
				NodeKeyStr.split(
					Noder.NodingSuffixGetStr)[-1].split(self.CatchedGetVariable.__class__.NameStr
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
			if self.CatchedGetVariable.NodePointDeriveNoder!=None:
				if self.CatchedGetVariable.NodePointDeriveNoder.NodeKeyStr=="":
					CatchedPrefixStr='Top'+self.CatchedGetVariable.NodePointDeriveNoder.__class__.NameStr
				else:
					CatchedPrefixStr=self.CatchedGetVariable.NodePointDeriveNoder.NodeKeyStr
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
		self.CatchedPointVariable=self.CatchingNodeClass(
			**{
				'PointingBackBool':self.CatchingPointBackBool
			}
		).point(
			self.CatchedGetVariable,
			'PointVariable'
		)

		#debug
		'''
		self.debug(
					('self.',self,[
									'CatchedPointVariable'
								])
					)
		'''
		
		#store
		self.collect(
					self.CatchingCollectionStr,
					self.CatchedNodeKeyStr,
					self.CatchedPointVariable
				)

#</DefineClass>

