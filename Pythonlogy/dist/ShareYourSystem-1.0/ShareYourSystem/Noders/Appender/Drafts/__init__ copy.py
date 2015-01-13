# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Appender append by doing a set in a NodedOrderedDict thanks to the <AppendedNodeStr><AppendedNodeKeyStr>

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
									#'AppendingCollectionVariable',
									#'AppendingCollectionVariable', 				
									#'AppendedNodeStr',				
									#'AppendedNodedStr',					
									#'AppendedKeyStr',					
									#'AppendedKeyStrKeyStr',			
									#'AppendedDict',						
									#'AppendedSettingKeyVariable',	
								]

	def default_init(self,
						_AppendingCollectionVariable=None, 				
						_AppendedNodeStr="",								
						_AppendedKeyStr="",					
						_AppendedKeyStrKeyStr="",			
						_AppendedDict=None,						
						_AppendedSettingKeyVariable="",			
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
			KeyStrsList=SYS.unzip(self.AppendingCollectionVariable,[0])

			#Look for an AppendingNodeCollectionStr
			try:
				NodeStrIndexInt=KeyStrsList.index("AppendingNodeCollectionStr")
				self.AppendedNodeStr=self.AppendingCollectionVariable[NodeStrIndexInt][1]
				self.AppendedKeyStrKeyStr='Noded'+self.AppendedNodeStr+'KeyStr'
				try:
					KeyStrIndexInt=KeyStrsList.index(self.AppendedKeyStrKeyStr)
					self.AppendedKeyStr=self.AppendingCollectionVariable[KeyStrIndexInt][1]
				except:
					pass
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
				self.AppendedDict=self.AppendingCollectionVariable.__dict__

			#dict Case
			elif type(self.AppendingCollectionVariable) in [dict,collections.OrderedDict]:
				self.AppendedDict=self.AppendingCollectionVariable

			try:

				#debug
				'''
				self.debug(('self.',self,['AppendedDict']))
				'''

				#set
				self.AppendedNodeStr=self.AppendedDict["AppendingNodeCollectionStr"]
				self.AppendedKeyStrKeyStr='Noded'+self.AppendedNodeStr+'KeyStr'
				self.AppendedKeyStr=self.AppendedDict[self.AppendedKeyStrKeyStr]
			
			except:
				pass

		#Init the SettingVariable and Add the NodifyingStr
		self.AppendedSettingKeyVariable=Noder.NodingPrefixGetStr+self.AppendedNodeStr+Noder.NodingSuffixGetStr+self.AppendedKeyStr

		#debug
		'''
		self.debug([
						('self.',self,[
											'AppendedSettingKeyVariable',
											'AppendedKeyStrKeyStr',
											'AppendedNodeStr',
											'AppendedKeyStr',
											'AppendingCollectionVariable'
										])
					]
				)
		'''

		#Then set
		if self.AppendedSettingKeyVariable!=Noder.NodingPrefixGetStr+Noder.NodingSuffixGetStr:
			return self.__setitem__(
										self.AppendedSettingKeyVariable,
										self.AppendingCollectionVariable
									)

		#Return self
		return self

#</DefineClass>
