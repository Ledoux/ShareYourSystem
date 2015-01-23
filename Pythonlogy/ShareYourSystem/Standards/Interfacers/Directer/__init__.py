# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Directer is a walker through the folders of the harddrive, 
assuring a call of _DirectingCallbackFunction at each level.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Killer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DirecterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'DirectingCallbackFunction',
									'DirectingLiargVariablesList',
									'DirectingFilterFunctionPointer'
								]

	def default_init(self,
						_DirectingCallbackFunction=None,
						_DirectingLiargVariablesList=None,
						_DirectingFilterFunctionPointer=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass()
	def do_direct(self):

		#Call the folder method before
		self.folder()

		#debug
		'''
		print('Directer l.62')
		print('self.FolderingPathStr is ',self.FolderingPathStr)
		print('')
		'''
		
		#Definition the call back function if not already
		if self.DirectingCallbackFunction==None:

			#Definition a test function
			def test(_LiargVariablesList,_FolderPathStr,_DirKeyStrsList):
				pass
				print(_LiargVariablesList,_FolderPathStr,_DirKeyStrsList)

			#set
			self.DirectingCallbackFunction=test

		'''
		#Call the function
		try:
			self.DirectingCallbackFunction(
								self.DirectingLiargVariablesList,
								self.FolderingPathStr,
								self.FolderedDirKeyStrsList,
								**_KwargVariablesDict
								)
		except:
			self.DirectingCallbackFunction(
								self.DirectingLiargVariablesList,
								self.FolderingPathStr,
								self.FolderedDirKeyStrsList
								)
		'''

		#Walk with os
		os.path.walk(
						self.FolderingPathStr,
						self.DirectingCallbackFunction,
						self.DirectingLiargVariablesList
					)

		"""
		#Do it Manually

		#Call the function
		try:
			self.DirectingCallbackFunction(
								self.DirectingLiargVariablesList,
								self.FolderingPathStr,
								self.FolderedDirKeyStrsList,
								**_KwargVariablesDict
								)
		except:
			self.DirectingCallbackFunction(
								self.DirectingLiargVariablesList,
								self.FolderingPathStr,
								self.FolderedDirKeyStrsList
								)

		#Filter the folders to walk
		DirectedFolderKeyStrsList=SYS._filter(
						lambda __FolderedDirKeyStr:
						os.path.isdir(self.FolderingPathStr+__FolderedDirKeyStr),
						self.FolderedDirKeyStrsList
			)

		#debug
		'''
		print('After first filter DirectedFolderKeyStrsList is ',DirectedFolderKeyStrsList)
		print('')
		'''

		#Filter again maybe
		if self.DirectingFilterFunctionPointer!=None:
			DirectedFolderKeyStrsList=SYS._filter(
						lambda __DirectedFolderKeyStr:
						self.DirectingFilterFunctionPointer(
							self,__DirectedFolderKeyStr),
						DirectedFolderKeyStrsList
			)

		#debug
		'''
		print('After second DirectedFolderKeyStrsList is ',DirectedFolderKeyStrsList)
		print('')
		'''

		#Map a recursive direct
		'''
		map(	
				lambda __DirectedFolderKeyStr:
				self.__class__().direct(
								self.DirectingCallbackFunction,
								self.DirectingLiargVariablesList,
								**{
								'FolderingPathStr':
									self.FolderingPathStr+__DirectedFolderKeyStr+'/'
								}
							),
				DirectedFolderKeyStrsList
			)
		'''

		"""

		#Return self
		#return self	

#</DefineClass>

