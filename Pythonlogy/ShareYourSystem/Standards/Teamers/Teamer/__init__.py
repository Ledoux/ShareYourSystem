# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Teamer defines Child ordered dicts with <DoStr> as KeyStr. 
The items inside are automatically setted with Teamed<DoStr><TypeStr> and have 
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
from ShareYourSystem.Standards.Teamers import Manager
#</ImportSpecificModules>

#<DefineLocals>
TeamPrefixStr='*'
class TeamDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.TeamDictClass=TeamDictClass
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class TeamerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'TeamingKeyStr',
								'TeamingManageVariable',
								'TeamedDeriveParenterVariable'
							]

	def default_init(self,
				_TeamingKeyStr="",		
				_TeamingManageVariable=None,					
				_TeamedDeriveParenterVariable=None, 																		
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TeamDict=TeamDictClass()

		##########################
		#init some parent attributes
		#

		self.ParentPointDeriveParenter=None
		self.ChildKeyStr=""

		##########################
		#init some family attributes from the parent 
		#

		self.TeamPointDeriveTeamer=None
		self.TeamKeyStr=""

	
	def do_familiarize(self):

		#debug
		'''
		self.debug(("self.",self,['TeamingKeyStr']))
		'''

		#Get the TeamedStr
		if self.TeamingKeyStr!="":
		
			#set the Teamed OrderedDict and KeyStr
			TeamedDeriveParenterVariableKeyStr=self.TeamingKeyStr

			#try to get
			try:

				#get
				self.TeamedDeriveParenterVariable=self.TeamDict[
					TeamedDeriveParenterVariableKeyStr
				]
			
			except KeyError:

				#set
				self.__setattr__(
									TeamedDeriveParenterVariableKeyStr,
									Parenter.ParenterClass()
								)

				#get
				self.TeamedDeriveParenterVariable=getattr(
					self,
					TeamedDeriveParenterVariableKeyStr
				)

				#set an alias with the TeamingKeyStr
				self.__setattr__(
					self.TeamingKeyStr,
					self.TeamedDeriveParenterVariable
				)

				#set
				self.TeamDict[
					TeamedDeriveParenterVariableKeyStr
				]=self.TeamedDeriveParenterVariable

			
	def mimic_set(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		self.debug(('self.',self,['SettingKeyVariable']))

		#Check
		if type(
			self.SettingKeyVariable
		)==str and self.SettingKeyVariable.startswith(TeamPrefixStr):

			#split
			SplitList=self.SettingKeyVariable.split(Pather.PathPrefixStr)

			#
			'''
			if len(SplitList)>1:
				self.TeamingKeyStr=SplitList[0]
			'''

			else:

				#debug
				self.debug('We family here')

				#family
				self.familiarize(
					SYS.deprefix(
						self.SettingKeyVariable,
						TeamPrefixStr
					)
				)

				#Stop the setting
				OutputDict["HookingIsBool"]=False 

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			return BaseClass.set(self)


#</DefineClass>

