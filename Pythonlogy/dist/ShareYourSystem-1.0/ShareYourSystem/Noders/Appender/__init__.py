# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Appender append by doing a set in a NodedOrderedDict thanks to the <AppendedNodeCollectionStr><AppendedNodeKeyStr>

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Noder"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections

from ShareYourSystem.Applyiers import Updater
Noder=BaseModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AppenderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'AppendingCollectionVariable',
									'AppendedNodeCollectionStr', 
									'AppendedNodeKeyStr'
								]

	def default_init(self,
						_AppendingCollectionVariable=None, 				
						_AppendedNodeCollectionStr="",								
						_AppendedNodeKeyStr="",	
						**_KwargVariablesDict
					):
	
		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_append(self):
		""" """
		
		#debug
		'''
		self.debug('self.AppendingCollectionVariable is '+str(self.AppendingCollectionVariable))
		'''

		#TuplesList Case
		if SYS.getIsTuplesListBool(self.AppendingCollectionVariable):

			#debug
			'''
			self.debug('This is a tuples list')
			'''

			#Definition the KeyStrsList
			AppendedKeyStrsList=SYS.unzip(self.AppendingCollectionVariable,[0])

			#Look for an AppendingNodeCollectionStr
			try:
				NodeCollectionStrIndexInt=AppendedKeyStrsList.index(
					"NodeCollectionStr"
				)
				self.AppendedNodeCollectionStr=self.AppendingCollectionVariable[
					NodeCollectionStrIndexInt
				][1]
				
				'''
				#self.AppendedKeyStrKeyStr='Noded'+self.AppendedNodeCollectionStr+'KeyStr'
				try:
					AppendedKeyStrIndexInt=AppendedKeyStrsList.index(
						self.AppendedKeyStrKeyStr
					)
					self.AppendedKeyStr=self.AppendingCollectionVariable[KeyStrIndexInt][1]
				except:
					pass
				'''
				NodeKeyStrIndexInt=AppendedKeyStrsList.index(
					"NodeKeyStr"
				)
				self.AppendedNodeKeyStr=self.AppendingCollectionVariable[
					NodeKeyStrIndexInt
				][1]

			except:
				pass

		else:

			#Objects Case
			if "AppenderClass" in map(
							lambda __Class:
							__Class.__name__,
							type(self.AppendingCollectionVariable).__mro__
							):

				#debug
				'''
				self.debug('This is a derived object from an Appender')
				'''

				#set
				AppendedDict=self.AppendingCollectionVariable.__dict__

			#dict Case
			elif type(self.AppendingCollectionVariable) in [dict,collections.OrderedDict]:
				AppendedDict=self.AppendingCollectionVariable

			try:

				#set
				self.AppendedNodeCollectionStr=AppendedDict["NodeCollectionStr"]
				self.AppendedNodeKeyStr=AppendedDict[
						'NodeKeyStr'
				]
			
			except:
				pass

		#Init the SettingVariable and Add the NodifyingStr
		AppendedSettingKeyVariable=Noder.NodingPrefixGetStr+self.AppendedNodeCollectionStr+Noder.NodingSuffixGetStr+self.AppendedNodeKeyStr

		#debug
		self.debug([
						('self.',self,[
											'AppendedNodeCollectionStr',
											'AppendedNodeKeyStr'
										])
					]
				)

		#Then set
		if AppendedSettingKeyVariable!=Noder.NodingPrefixGetStr+Noder.NodingSuffixGetStr:
			self.__setitem__(
								AppendedSettingKeyVariable,
								self.AppendingCollectionVariable
							)

		#Return self
		#return self

#</DefineClass>
