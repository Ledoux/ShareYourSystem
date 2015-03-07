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
SYS.addDo("Viewer","View","Viewing","Viewed")
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	def default_init(self, 
						_ViewDeriveControllerVariable=None,
						_ViewFirstDeriveViewerVariable=None,
						_ViewedHtmlStr="",
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):

		pass
			
	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(
			self,
			_SettingValueVariable
		)

		#/##################/#
		# Find the first top Controller
		#

		#find
		self.debug(
			[
				'We have parented',
				('self.',self,['ParentedDeriveTeamersList'])
			]
		)

		#Check
		if len(self.ParentedDeriveTeamersList)>0:

			#index
			IndexInt=map(type,self.ParentedDeriveTeamersList).index(SYS.Controller)

			#set
			self.ViewDeriveControllerVariable=self.ParentedDeriveTeamersList[IndexInt]

			#set
			if IndexInt>0:

				#get
				self.ViewFirstDeriveViewerVariable=self.ParentedDeriveTeamersList[IndexInt-1]

			else:

				#get
				self.ViewFirstDeriveViewerVariable=self

		else:

			#alias
			self.ViewFirstDeriveViewerVariable=self
	
#</DefineClass>

#</DefinePrint>
ViewerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ViewDeriveControllerVariable',
		'ViewFirstDeriveViewerVariable',
		'ViewedHtmlStr'
	]
)
#<DefinePrint>
