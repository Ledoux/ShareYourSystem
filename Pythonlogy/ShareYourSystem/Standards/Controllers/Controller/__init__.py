# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Controller

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Hdformater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ControllerClass(BaseClass):

	def default_init(self,
				_ControlModelStr="Top",
				_ControllingMethodStr="",
				_ControllingManagingKeyStr="",
				_ControllingModelClassVariable=None,
				_ControllingViewClassVariable=None,
				_ControlledDeriveManagerVariable=None,
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_control(self):
		
		#debug
		'''
		self.debug(
				[
					'We control here'
				]
			)
		'''

		#Check
		if self.ControllingMethodStr=='insert':
			
			#get
			self.ControlledDeriveManagerVariable=self.TeamDict[
				'Models'][self.ControllingManagingKeyStr]

			#insert and row
			self.ControlledDeriveManagerVariable.insert()
			self.ControlledDeriveManagerVariable.setSwitch('row')
			

	def mimic_team(self):

		#/##################/#
		# If it is an ask for update the models then gve to the child manager the 
		# modeler classes for instancing

		#call the base method
		BaseClass.team(self)

		#Check
		if self.TeamingKeyStr=='Models':

			#Check
			if self.TeamedIsBool==False:

				#debug
				'''
				self.debug('we create models here')
				'''
				
				#Check
				if self.ControllingModelClassVariable==None:
					self.ControllingModelClassVariable=SYS.HierarchizerClass

				#alias
				self.TeamedValueVariable.ManagingValueClass=self.ControllingModelClassVariable

		if self.TeamingKeyStr=='Views':

			#Check
			if self.TeamedIsBool==False:

				#debug
				'''
				self.debug('we create models here')
				'''
				
				#Check
				if self.ControllingViewClassVariable==None:
					self.ControllingViewClassVariable=SYS.FigurerClass

				#alias
				self.TeamedValueVariable.ManagingValueClass=self.ControllingViewClassVariable


	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/##################/#
		# Special Model control case
		#

		#get
		self.ControlModelStr=(
				self.ParentedTotalPathStr+'/'+self.ManagementTagStr
			).replace('/','_')

		#remove
		if self.ControlModelStr[0]=='_':
			self.ControlModelStr=self.ControlModelStr[1:]

		#Create a group in the hdf5 file if it is with hdf
		self.HdformatedFileVariable=self.ParentTopDeriveTeamerVariable.HdformatedFileVariable
			

#</DefineClass>

#Set
SYS.ManagerClass.ManagingValueClass=ControllerClass

#</DefinePrint>
ControllerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'ControlModelStr',
		'ControllingMethodStr',
		'ControllingManagingKeyStr',
		'ControllingModelClassVariable',
		'ControllingViewClassVariable',
		'ControlledDeriveManagerVariable'
	]
)
#<DefinePrint>

