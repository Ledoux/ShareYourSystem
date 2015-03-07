# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Viewer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	def default_init(self, 
						_ViewDeriveControllerVariable=None,
						_ViewTagStr="",
						_ViewedFigureVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):

		pass
		
	"""
	def propertize_setParentKeyStr(self,_SettingValueVariable):

		#call the parent base
		BaseClass.propertize_setParentKeyStr(self,_SettingValueVariable)

		#debug
		'''
		self.debug(
			[
				'We know the ParentKeyStr',
				'We model here',
			]
		)
		'''

		#/#################/#
		# Give some things from the controller
		#

		#get the parent-parent Teamer
		if self.ParentDeriveTeamerVariable!=None:
			if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable!=None:
				self.ViewDeriveControllerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#Link set
		self.ViewTagStr=self.ManagementTagStr+'View'

		#debug
		'''
		self.debug(
				[
					'We have setted the ViewDeriveControllerVariable',
					('self.',self,[
						'ViewDeriveControllerVariable',
						'ViewTagStr'
					])
				]
			)
		'''

		#view
		self.view()
	"""

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(
			self,
			_SettingValueVariable
		)

		#/##################/#
		# Find the first top Controller
		#

		self.debug(
			[
				'We have parented',
				('self.',self,['ParentedDeriveTeamersList'])
			]
		)
		

#</DefineClass>

#</DefinePrint>
ViewerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ViewDeriveControllerVariable',
		'ViewTagStr',
	]
)
#<DefinePrint>
