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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Filterer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineLocals>
class ParentDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.ParentDictClass=ParentDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass(
	**{'ClassingSwitchMethodStrsList':['parent']}
)
class ParenterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ParentingChildKeyStr',
								'ParentingChildValueVariable'
							]

	def default_init(self,
				_ParentingChildKeyStr=None,
				_ParentingChildValueVariable=None,
				**_KwargVariablesDict):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#Init a ParentDict
		self.ParentDict=ParentDictClass()

		#Init
		self.FamilyKeyStr=""

		#point
		self.point(
				None,
				'FamilyPointDeriveFamiliarizer'
			)

	def do_parent(self):

		##########################
		#give some parent attributes
		#

		#set
		self.ParentDict[
			self.ParentingChildKeyStr
		]=self.ParentingChildValueVariable	

		#set
		self.ParentingChildValueVariable.point(
				self,
				'ParentPointDeriveParenter'
			)
		
		#set
		'''
		self.ParentingChildValueVariable.__setattr__(
			'ParentDict',
			self.ParentDict
		)
		'''

		#set
		self.ParentingChildValueVariable.__setattr__(
			'ChildKeyStr',
			self.ParentingChildKeyStr
		)

		##########################
		#give some family attributes
		#

		#set
		self.ParentingChildValueVariable.__setattr__(
			'FamilyKeyStr',
			self.FamilyKeyStr
		)

		#set 
		self.ParentingChildValueVariable.point(
				self.FamilyPointDeriveFamiliarizer,
				'FamilyPointDeriveFamiliarizer'
			)
		

#</DefineClass>

