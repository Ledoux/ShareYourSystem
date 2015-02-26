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
					self.ControllingModelClassVariable=SYS.ModelerClass

				#alias
				self.TeamedValueVariable.ManagingValueClass=self.ControllingModelClassVariable

#</DefineClass>


#</DefinePrint>
ControllerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ControllingModelClassVariable',
		'ControllingViewClassVariable'
	]
)
#<DefinePrint>

