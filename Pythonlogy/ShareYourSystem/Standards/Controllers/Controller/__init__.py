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
from ShareYourSystem.Standards.Itemizers import Parenter
#</ImportSpecificModules>

#<DefineLocals>
class ModelsParenterClass(Parenter.ParenterClass):pass
class ViewsParenterClass(Parenter.ParenterClass):pass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ControllerClass(BaseClass):

	def default_init(self,
				_ControlTagStr="Top",
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
		
	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/##################/#
		# Set the ControlTagStr
		#

		#debug
		'''
		self.debug(
				[
					'We have parented',
					'we set the control path str',
					('self.',self,[
							'ParentedTotalPathStr',
							'ManagementTagStr'
						])
				]
			)
		'''
		
		#Check
		if self.ManagementTagStr!='':

			#get
			self.ControlTagStr=(
					self.ParentedTotalPathStr+'/'+self.ManagementTagStr
				).replace('/','_')

		#remove
		if self.ControlTagStr[0]=='_':
			self.ControlTagStr=self.ControlTagStr[1:]

		#/##################/#
		# Special Model control case
		#

		#Create a group in the hdf5 file if it is with hdf
		self.HdformatedFileVariable=self.ParentTopDeriveTeamerVariable.HdformatedFileVariable
#</DefineClass>

#<DefineLocals>

#Set
#SYS.ManagerClass.ManagingValueClass=ControllerClass
ControllerClass.TeamingClassesDict={
	'Models':ModelsParenterClass,
	'Views':ViewsParenterClass
}
#<DefineLocals>

#</DefinePrint>
ControllerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'ControlTagStr',
		'ControllingMethodStr',
		'ControllingManagingKeyStr',
		'ControllingModelClassVariable',
		'ControllingViewClassVariable',
		'ControlledDeriveManagerVariable'
	]
)
#<DefinePrint>



