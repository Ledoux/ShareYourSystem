# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Folderer is a quick object helping for getting the FolderedDirKeyStrsList
at a specified directory or in the current one by default

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import json
import os
import sys
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FoldererClass(BaseClass):
	"""
		FoldererClass ...

	"""

	def default_init(self,
						_FolderingPathStr="",
						_FolderingMkdirBool=False,
						_FolderedDirKeyStrsList=None,	
						_FolderedModuleStr="",
						_FolderedParentModuleStr="",
						_FolderedNameStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_folder(self,**_KwargVariablesDict):

		#Get the current
		FolderedCurrentPathStr=os.getcwd()

		#set
		if self.FolderingPathStr=="":
			self.FolderingPathStr=FolderedCurrentPathStr+'/'

		#debug
		'''
		print('self.FolderingPathStr is '+self.FolderingPathStr)
		print('FolderedCurrentPathStr is '+FolderedCurrentPathStr)
		print('')
		'''
			
		#Check
		if self.FolderingPathStr!="":

			#Add the '/' if not in the end
			if self.FolderingPathStr[-1]!="/":
				self.FolderingPathStr+="/"

			#Build intermediar pathes
			if os.path.isdir(self.FolderingPathStr)==False:

				#Check
				if self.FolderingMkdirBool:

					#debug
					'''
					print('We are going to build the intermediar folder')
					print('self.FolderingPathStr is ',self.FolderingPathStr)
					print('')
					'''

					#Definition
					FolderingPathStrsList=self.FolderingPathStr.split('/')
					FolderedRootPathStr=FolderingPathStrsList[0]
					for _PathStr in FolderingPathStrsList[1:]:

						#debug
						'''
						print('FolderedRootPathStr is ',FolderedRootPathStr)
						print('')
						'''

						#Mkdir if it doesn't exist
						if FolderedRootPathStr!="" and os.path.isdir(FolderedRootPathStr)==False:
							os.popen('mkdir '+FolderedRootPathStr)

						#Add the following
						FolderedRootPathStr+='/'+_PathStr

					#Mkdir if it doesn't exist
					if os.path.isdir(FolderedRootPathStr)==False:
						os.popen('mkdir '+FolderedRootPathStr)

		#Recheck
		if os.path.isdir(self.FolderingPathStr):

			#set
			self.FolderedDirKeyStrsList=os.listdir(self.FolderingPathStr)

			#Check
			if '__init__.py' in self.FolderedDirKeyStrsList:

				#set maybe FolderedModuleStr and FolderedParentModuleStr if we are located in the SYS path
				if 'ShareYourSystem' in self.FolderingPathStr:

					#set
					self.FolderedModuleStr='ShareYourSystem'+self.FolderingPathStr.split(
						'ShareYourSystem')[-1].replace('/','.')

					#Remove the ossibly last dot
					if self.FolderedModuleStr[-1]=='.':
						self.FolderedModuleStr=self.FolderedModuleStr[:-1]

					#set
					if '.' in self.FolderedModuleStr:

						#set
						self.FolderedNameStr=self.FolderedModuleStr.split('.')[-1]

						#debug
						'''
						self.debug(('self.',self,['FolderingPathStr','FolderedNameStr']))
						'''
						
						#set the parent
						self.FolderedParentModuleStr=self.FolderedNameStr.join(
							self.FolderedModuleStr.split(self.FolderedNameStr)[:-1]
						)
						if len(self.FolderedParentModuleStr
							)>0 and self.FolderedParentModuleStr[-1]=='.':
							self.FolderedParentModuleStr=self.FolderedParentModuleStr[:-1]
					else:
						self.FolderedModuleStr=self.FolderedModuleStr

			else:

				#set
				self.FolderedModuleStr=""
				self.FolderedParentModuleStr=""


#</DefineClass>

#</DefinePrint>
FoldererClass.PrintingClassSkipKeyStrsList.extend(
	[
		'FolderingPathStr',
		'FolderingMkdirBool',
		'FolderedDirKeyStrsList',	
		'FolderedModuleStr',
		'FolderedParentModuleStr',
		'FolderedNameStr'
	]
)
#<DefinePrint>