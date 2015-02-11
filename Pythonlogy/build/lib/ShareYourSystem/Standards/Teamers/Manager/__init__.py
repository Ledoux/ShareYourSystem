# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Manager completes the list of grand-manage nodes that 
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
ManagementPrefixStr="$"

class ManagementDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the manage init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.ManagementDictClass=ManagementDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ManagerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ManagingUpdateVariable'
							]

	def default_init(self,
				_ManagingUpdateVariable=None,
				**_KwargVariablesDict):	

		#Call the manage init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#Init the DeriveTeamersManagementDict
		self.DeriveTeamersManagementDict=ManagementDictClass()

		#Init
		self.TeamKeyStr=""

		#point
		self.point(
				None,
				'TeamPointDeriveTeamer'
			)

	def do_manage(self):

		#debug
		self.debug(
			('self.',self,[
					'ManagingUpdateVariable'
				])
		)

		#set
		if self.ManagingUpdateVariable.items():

			filter(
					lambda __ItemTuple:
					__ItemTuple.startswith(
						ManagementPrefixStr
					),
					self.ManagingUpdateVariable.items()
				)



		self.ManagementDict[
			self.ManagingKeyStr
		]=self.ManagingValueVariable

		##########################
		#give some manage attributes
		#

		#set
		self.ManagingValueVariable.point(
				self,
				'ManagementPointDeriveManager'
			)
		
		#set
		'''
		self.ManagingValueVariable.__setattr__(
			'ManagementDict',
			self.ManagementDict
		)
		'''

		#set
		self.ManagingValueVariable.__setattr__(
			'ManagementKeyStr',
			self.ManagingKeyStr
		)

		##########################
		#give some family attributes
		#

		#set
		'''
		self.ManagingValueVariable.__setattr__(
			'TeamKeyStr',
			self.TeamKeyStr
		)
		'''

		#set 
		self.ManagingValueVariable.point(
				self.TeamPointDeriveTeamer,
				'TeamPointDeriveTeamer'
			)
		
	def mimic_set(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		self.debug(('self.',self,['SettingKeyVariable']))

		#Check
		if type(
			self.SettingKeyVariable
		)==str and self.SettingKeyVariable.startswith(ManagementPrefixStr):

			#debug
			self.debug('We manage here')

			#manage
			self.manage(
				SYS.deprefix(
					self.SettingKeyVariable,
					ManagementPrefixStr
				),
				self.SettingValueVariable
			)

			#Stop the setting
			OutputDict["HookingIsBool"]=False 

		#Call the manage get method
		if OutputDict['HookingIsBool']:
			return BaseClass.set(self)

#</DefineClass>

