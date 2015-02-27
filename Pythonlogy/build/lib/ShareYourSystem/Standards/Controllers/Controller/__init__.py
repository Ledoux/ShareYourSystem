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
BaseModuleStr="ShareYourSystem.Standards.Teamers.Parenter"
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
				_ControllingModelClassVariable=None,
				_ControllingViewClassVariable=None,
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_control(self):
		pass

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
		if self.HdformatedFileVariable!=None:

			#debug
			'''
			self.debug(
						[
							'UppestGroupedParentVariable.HdfGroupPathStr is '+UppestGroupedParentVariable.HdfGroupPathStr,
							('self.',self,[
										'ParentedNodePathStr',
										'NodedKeyStr'
									])
						]
					)
			'''

			#set the HdfGroupPathStr
			if self.ParentedTopDeriveParenterVariable==self:
				self.HdfGroupPathStr="/"
			else:
				self.HdfGroupPathStr=getHdfGroupPathStrWithPathStrsList(
					[
						self.ParentedTopDeriveParenterVariable.HdfGroupPathStr,
						self.ParentedNodePathStr,
						self.NodeKeyStr
					]
				)

			#debug
			'''
			self.debug(('self.',self,['HdfGroupPathStr']))
			'''
			
			#Check if the Path exists
			if self.HdfGroupPathStr not in self.HdformatedFileVariable:

				#set all the intermediate Paths before
				PathStrsList=self.HdfGroupPathStr.split('/')[1:]
				ParsingChildPathStr="/"

				#set the PathStr from the top to the down (integrativ loop)
				for __ChildPathStr in PathStrsList:

					#Go deeper
					NewParsingChildPathStr=ParsingChildPathStr+__ChildPathStr

					#Create the group if not already
					if NewParsingChildPathStr not in self.HdformatedFileVariable:
						if self.HdformatingModuleStr=="tables":
							self.HdformatedFileVariable.create_group(
								ParsingChildPathStr,__ChildPathStr)
						elif self.HdformatingModuleStr=="h5py":
							Group=self.HdformatedFileVariable[ParsingChildPathStr]
							Group.create_group(__ChildPathStr)
					
					#Prepare the next group	
					ParsingChildPathStr=NewParsingChildPathStr+'/'

#</DefineClass>

#Set
SYS.ManagerClass.ManagingValueClass=ControllerClass

#</DefinePrint>
ControllerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'ControlModelStr',
		'ControllingModelClassVariable',
		'ControllingViewClassVariable'
	]
)
#<DefinePrint>

