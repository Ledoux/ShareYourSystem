# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Hdformater instance maps an apply and so "grinds" a MappingArgDictsList 
to a method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Walker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import os
import sys
from ShareYourSystem.Functers import Argumenter,Alerter,Hooker,Switcher
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class HdformaterClass(BaseClass):
	
	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
			_HdformatingModuleStr="tables",
			_HdformatingPathStr="", 			
			_HdformatedFileVariable=None, 		
			_HdformatedStr="", 			
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Alerter.AlerterClass()		
	@Switcher.SwitcherClass()
	@Argumenter.ArgumenterClass()
	def hdformat(self,_ModuleStr=None,_PathStr=None,*_LiargVariablesList,**_KwargVariablesDict):

		#set the HdformatingPathStr
		if self.HdformatingPathStr=="" and os.getcwd().split('/')[-1]==self.__class__.NameStr:
			self.HdformatingPathStr=os.getcwd()+'/'+self.__class__.NameStr+'.hdf5'

		#debug
		'''
		self.debug(('self.',self,['HdformatingPathStr']))
		'''
	
		#Check
		if self.HdformatingPathStr!="":

			#Maybe we have to import
			if self.HdformatingModuleStr not in sys.modules:
				importlib.import_module(self.HdformatingModuleStr)

			#Check for first write
			if os.path.isfile(self.HdformatingPathStr)==False:

				#Create the file 
				self.HdformatedFileVariable=sys.modules[self.HdformatingModuleStr].File(
									self.HdformatingPathStr,'w')
					
				#Close it
				self.HdformatedFileVariable.close()

			if self.HdformatedFileVariable==None or ( 
				(self.HdformatingModuleStr=='tables' and self.HdformatedFileVariable.isopen==0
					) or (self.HdformatingModuleStr=='h5py' and self.HdformatedFileVariable.mode=='c') ):

				#Open the HdformatedFileVariable
				self.HdformatedFileVariable=sys.modules[self.HdformatingModuleStr].File(
					self.HdformatingPathStr,'r+')

		#Return self
		return self

	def hdfview(self):

		#debug
		'''
		self.debug(('self.',self,['HdformatingPathStr']))
		'''

		#set the HdformatedStr
		self.HdformatedStr=os.popen(
										'/usr/local/bin/h5ls -dlr '+self.HdformatingPathStr
								).read()
		
		#Return self
		return self

	def hdfclose(self):

		#Close the HdformatedFileVariable
		if self.HdformatedFileVariable!=None:
			self.HdformatedFileVariable.close()

		#Return self
		return self
	#</DefineHookMethods>

#</DefineClass>

