# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Parenter completes the list of grand-parent nodes that 
a child node could have. It acts only at one level.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Distinguisher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Functers import Argumenter
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ParenterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									#'ParentingNodeStr'
								]

	def default_init(self,
				_ParentingNodeStr="",
				_ParentedDeriveNodersList=None,
				_ParentedNodePathStr="",
				**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_parent(self):

		#debug
		'''
		self.debug(('self.',self,['ParentingNodeStr']))
		'''
		
		#Nodify
		self.node(self.ParentingNodeStr)

		#debug
		'''
		self.debug(('self.',self,['NodePointDeriveNoder']))
		'''

		#Check of a parent pointer
		if self.NodePointDeriveNoder!=None:

			#debug
			'''
			self.debug('We are going to node the parent pointer')
			'''

			#Nodify the parent
			self.NodePointDeriveNoder.node(self.ParentingNodeStr)

			#set the GrandParentPointersList
			#GrandParentPointersListKeyStr=self.NodedPrefixStr+"GrandParentPointersList"
			GrandParentPointersListKeyStr='ParentedDeriveNodersList'
			try:
				setattr(
							self,
							GrandParentPointersListKeyStr,
							[self.NodePointDeriveNoder]+getattr(self.NodePointDeriveNoder,GrandParentPointersListKeyStr)
						)
			except AttributeError:
				self.NodePointDeriveNoder.__setattr__(GrandParentPointersListKeyStr,[])
				setattr(
							self,
							GrandParentPointersListKeyStr,
							[self.NodePointDeriveNoder]+getattr(self.NodePointDeriveNoder,GrandParentPointersListKeyStr)
						)
			self.ParentedDeriveNodersList=getattr(self,GrandParentPointersListKeyStr)

			#set the GrandParentKeyStrsList
			GrandParentKeyStrsListKeyStr=self.NodedPrefixStr+"GrandParentKeyStrsList"
			self.__setattr__(
								GrandParentKeyStrsListKeyStr,
								map(
										lambda __GrandParentPointer:
										getattr(__GrandParentPointer,self.NodedKeyStrKeyStr),
										self.ParentedDeriveNodersList
									)
						)

			#set the PathStrsList
			PathStrsListKeyStr=self.NodedPrefixStr+"PathStrsList"
			PathStrsList=[getattr(self,self.NodedKeyStrKeyStr)]+copy.copy(
									getattr(self,GrandParentKeyStrsListKeyStr)
								)
			self.__setattr__(
								PathStrsListKeyStr,
								PathStrsList
							)
			getattr(self,PathStrsListKeyStr).reverse()

			#set the PathStr
			PathStrKeyStr=self.NodedPrefixStr+"PathStr"
			PathStr=Pather.PathingPrefixStr.join(getattr(self,PathStrsListKeyStr))
			self.__setattr__(
								PathStrKeyStr,
								PathStr
							)
			self.ParentedNodePathStr=PathStr

		#Return self
		#return self

#</DefineClass>

