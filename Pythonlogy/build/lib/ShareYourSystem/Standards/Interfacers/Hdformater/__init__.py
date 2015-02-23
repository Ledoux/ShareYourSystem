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
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Writer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import importlib
import os
import sys
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['hdformat']
})
class HdformaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'HdformatingFileKeyStr',
								'HdformatingModuleStr',
								'HdformatedFileVariable',
								'HdformatedConsoleStr'
							]

	def default_init(self,
			_HdformatingFileKeyStr="", 
			_HdformatingModuleStr="tables",			
			_HdformatedFileVariable=None, 
			_HdformatedFilePathStr="",		
			_HdformatedConsoleStr="", 			
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_hdformat(self):

		#debug
		self.debug(('self.',self,[
									'HdformatingFileKeyStr'
								]))
		
		#Check
		if self.HdformatedFileVariable==None:

			#folder first
			self.folder()

			#set
			self.HdformatedFilePathStr=self.FolderingPathStr+self.HdformatingFileKeyStr
			
			#Maybe we have to import
			if self.HdformatingModuleStr not in sys.modules:

				#debug
				'''
				self.debug('We import first the hdf module')
				'''

				#Import
				importlib.import_module(self.HdformatingModuleStr)

			#Check
			if self.HdformatingFileKeyStr!="":

				#Check for first write
				if os.path.isfile(self.HdformatedFilePathStr)==False:

					#debug
					'''
					self.debug('We create the file first')
					'''

					#Create the file 
					self.HdformatedFileVariable=sys.modules[self.HdformatingModuleStr].File(
										self.HdformatedFilePathStr,'w')
						
					#Close it
					self.HdformatedFileVariable.close()

				if self.HdformatedFileVariable==None or ( 
					(self.HdformatingModuleStr=='tables' and self.HdformatedFileVariable.isopen==0
						) or (self.HdformatingModuleStr=='h5py' and self.HdformatedFileVariable.mode=='c') ):

					#debug
					'''
					self.debug('We open the file')
					'''

					#Open the HdformatedFileVariable
					self.HdformatedFileVariable=sys.modules[self.HdformatingModuleStr].File(
						self.HdformatedFilePathStr,'r+')

	def hdfview(self):

		#debug
		'''
		self.debug(('self.',self,['HdformatingFilePathStr']))
		'''

		if self.HdformatedFilePathStr!="":
		
			#set the HdformatedConsoleStr
			self.HdformatedConsoleStr=os.popen(
				SYS.h5lsPathStr+' -dlr '+self.HdformatedFilePathStr
			).read()
		
		#Return self
		return self.HdformatedConsoleStr

	def mimic_close(self):

		#Close the HdformatedFileVariable
		if self.HdformatedFileVariable!=None:
			self.HdformatedFileVariable.close()

#</DefineClass>
