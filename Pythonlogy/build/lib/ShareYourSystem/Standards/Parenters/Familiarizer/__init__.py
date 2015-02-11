# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Familiarizer defines Child ordered dicts with <DoStr> as KeyStr. 
The items inside are automatically setted with Familiarized<DoStr><TypeStr> and have 
a Pointer to the parent InstanceVariable. This is the beginning for buiding high
arborescent and (possibly circular) structures of objects.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Filterer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Standards.Itemizers import Pather
from ShareYourSystem.Standards.Parenters import Parenter
#</ImportSpecificModules>

#<DefineLocals>
class FamilyDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.FamilyDictClass=FamilyDictClass
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class FamiliarizerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'FamiliarizingKeyStr',
								'FamiliarizedDeriveParenterVariable'
							]

	def default_init(self,
				_FamiliarizingKeyStr="",							
				_FamiliarizedDeriveParenterVariable=None, 																		
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.FamilyDict=FamilyDictClass()

		##########################
		#init some parent attributes
		#

		self.ParentPointDeriveParenter=None
		self.ChildKeyStr=""

		##########################
		#init some family attributes from the parent 
		#

		self.FamilyPointDeriveFamiliarizer=None
		self.FamilyKeyStr=""

	
	def do_familiarize(self):

		#debug
		'''
		self.debug(("self.",self,['FamiliarizingKeyStr']))
		'''

		#Get the FamiliarizedStr
		if self.FamiliarizingKeyStr!="":
		
			#set the Familiarized OrderedDict and KeyStr
			FamiliarizedDeriveParenterVariableKeyStr=self.FamiliarizingKeyStr

			#try to get
			try:

				#get
				self.FamiliarizedDeriveParenterVariable=self.FamilyDict[
					FamiliarizedDeriveParenterVariableKeyStr
				]
			
			except KeyError:

				#set
				self.__setattr__(
									FamiliarizedDeriveParenterVariableKeyStr,
									Parenter.ParenterClass()
								)

				#get
				self.FamiliarizedDeriveParenterVariable=getattr(
					self,
					FamiliarizedDeriveParenterVariableKeyStr
				)

				#set an alias with the FamiliarizingKeyStr
				self.__setattr__(
					self.FamiliarizingKeyStr,
					self.FamiliarizedDeriveParenterVariable
				)

				#set
				self.FamilyDict[
					FamiliarizedDeriveParenterVariableKeyStr
				]=self.FamiliarizedDeriveParenterVariable

			

#</DefineClass>

