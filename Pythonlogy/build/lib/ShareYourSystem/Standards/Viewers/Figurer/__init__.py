# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Figurer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Viewers.Viewer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo("Figurer","Figure","Figuring","Figured")
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Setter
#</ImportSpecificModules>

#<DefineLocals>
FigurePlotKeyStr='#plot'
FigureBarKeyStr='#bar'
FigureScatterKeyStr='#scatter'
FigureAxesKeyStr='#axes'
FigureMpld3KeyStr='#mpld3.plugins.'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class FigurerClass(BaseClass):
	
	def default_init(self,
						_FigurePyplotVariable=None,
						_FigureCartoonVariable=None,
						_FigureTooltipVariable=None,
						_FiguringGridIntsTuple=(10,10),
						_FiguringSubGridIntsTuple=None,
						_FiguringAnchorIntsTuple=(0,0),
						_FiguringShapeIntsTuple=(1,1),
						_FiguringDrawVariable=None,
						_FiguredTeamTagStr="",
						_FiguredDeriveTeamerVariablesList=None,
						_FiguredPanelDeriveTeamerVariable=None,
						_FiguredAxesVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		self.ManagingValueClass=self.__class__

	def do_figure(self):	

		#/###################/#
		# First we get the children figurers and check what they are
		#

		#debug
		'''
		self.debug(
				[
					'We figure here',
					('self.',self,['ViewFirstDeriveViewerVariable'])
				]
			)
		'''

		#filter
		FiguredTeamTagStrsList=SYS._filter(
			lambda __KeyStr:
			__KeyStr in ['Panels','Axes','Plots'],
			self.TeamDict.keys()
		)

		#Check
		if len(FiguredTeamTagStrsList)==1:

			#filter
			self.FiguredTeamTagStr=FiguredTeamTagStrsList[0]

			#get
			self.FiguredDeriveTeamerVariablesList=self.TeamDict[
				self.FiguredTeamTagStr
			].ManagementDict.values()

		#debug
		'''
		self.debug(
				[
					('self.',self,[
							'FiguredTeamTagStr',
							#'FiguredDeriveTeamerVariablesList'
						])
				]
			)
		'''

		#/###################/#
		# do something before descending a figure call
		#

		if self.FiguredTeamTagStr=='Panels':

			#debug
			'''
			self.debug(
					[
						'I am the top figurer...'
					]
				)
			'''

		elif self.FiguredTeamTagStr=='Axes':

			#debug
			'''
			self.debug(
					[
						'I am a Panel...'
					]
				)
			'''

		elif self.FiguredTeamTagStr=='Plots':

			#debug
			'''
			self.debug(
					[
						'I am an Axes..'
					]
				)
			'''

			#get the parent panel
			self.FiguredPanelDeriveTeamerVariable=self.ParentDeriveTeamerVariable

			#init
			from matplotlib import pyplot
			self.FiguredAxesVariable=pyplot.subplot2grid(
					self.ViewFirstDeriveViewerVariable.FiguringGridIntsTuple, 
					self.FiguringAnchorIntsTuple, 
					rowspan=self.FiguringShapeIntsTuple[0],
					colspan=self.FiguringShapeIntsTuple[1]
				)

			#link
			self.FiguredAxesVariable._figure=self.FigurePyplotVariable

		else:

			#debug
			'''
			self.debug(
					[
						'I dont have such panels axes plots...',
						'So I can be a plot or the top one axe one plot figurer'
					]
				)
			'''

			#Check
			if self!=self.ViewFirstDeriveViewerVariable:


				#debug
				'''
				self.debug(
						[
							'I am Plot..',
							'I set my FiguredAxesVariables corresponding to my parent one'
						]
					)
				'''

				#get the one of the parent
				self.FiguredAxesVariable=self.ParentedDeriveTeamerVariable.FiguredAxesVariable

			else:

				#debug
				self.debug(
						[
							'I am the top figurer but with just one axes..',
							('self.',self,['FiguringGridIntsTuple'])
						]
					)

				#Set the size of the grid to this just one plot
				self.FiguringGridIntsTuple=(1,1)

				#get the parent panel
				self.FiguredPanelDeriveTeamerVariable=self.ParentDeriveTeamerVariable

				#init
				from matplotlib import pyplot
				self.FiguredAxesVariable=pyplot.subplot2grid(
						self.FiguringGridIntsTuple, 
						self.FiguringAnchorIntsTuple, 
						rowspan=self.FiguringShapeIntsTuple[0],
						colspan=self.FiguringShapeIntsTuple[1]
					)

				#link
				self.FiguredAxesVariable._figure=self.FigurePyplotVariable			

		#/###################/#
		# map a figure into them
		#

		#map
		map(
				lambda __FiguredDeriveTeamerVariable:
				__FiguredDeriveTeamerVariable.figure(),
				self.FiguredDeriveTeamerVariablesList
			)

		#/###################/#
		# if there axes setted then applythe draw set variable 
		#

		#Check
		if self.FiguredAxesVariable!=None:

			#debug
			'''
			self.debug(
					[
						'There are axes so command the figuring draw variable',
						('self.',self,['FiguringDrawVariable'])
					]
				)
			'''

			#commad self
			self.command('/',self.FiguringDrawVariable)

		#/###################/#
		# now do something here depending on the Tag
		#

		if self.FiguredTeamTagStr=='Panels':

			#debug
			'''
			self.debug(
					[
						'I am the top figurer...'
					]
				)
			'''

		elif self.FiguredTeamTagStr=='Axes':

			#debug
			'''
			self.debug(
					[
						'I am a Panel...'
					]
				)
			'''

		else:

			#debug
			'''
			self.debug(
					[
						'I am an Axes..'
					]
				)
			'''

	def mimic_team(self):

		#call the base method
		BaseClass.team(self)

		#debug
		self.debug(
				[
					'We have team and check now for a Panels, Axes, or Plots',
					('self.',self,[
						'TeamingKeyStr',
						'TeamedValueVariable'
					])
				]
			)

		#Check
		if self.TeamingKeyStr in ['Panels','Axes','Plots']:

			#set
			self.TeamedValueVariable.ManagingValueClass=SYS.FigurerClass

			#map mute
			map(
					lambda __KeyStr:
					self.TeamedValueVariable.set('!|'+__KeyStr,SYS.FigurerClass),
					self.TeamedValueVariable.ManagementDict.keys()
				)


	def mimic_view(self):

		#import mpld3
		import mpld3

		#fig to html
		self.ViewedHtmlStr=mpld3.fig_to_html(
			self.FigurePyplotVariable,
			template_type="simple"
		)

		#call the base method
		BaseClass.view(self)


	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the parent method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#debug
		'''
		self.debug(
				[
					'We have parented !',
					('self.',self,['ViewFirstDeriveViewerVariable'])
				]
			)
		'''

		#/###############/#
		# If it is the top then init the figure
		#

		#Check
		if self.ViewFirstDeriveViewerVariable==self:

			#debug
			'''
			self.debug(
					[
						'We init a figure'
					]
				)
			'''

			#import pyplot
			from matplotlib import pyplot

			#subplots
			self.FigurePyplotVariable = pyplot.figure()

		else:

			#debug
			'''
			self.debug(
					[
						'We just do an alias'
					]
				)
			'''

			#alias
			self.FigurePyplotVariable=self.ViewFirstDeriveViewerVariable.FigurePyplotVariable

		#figure
		self.figure()

	def mimic_set(self):

		#Check
		if self.SettingKeyVariable in [
											FigurePlotKeyStr,
											FigureScatterKeyStr,
											FigureBarKeyStr
										]:

			#debug
			'''
			self.debug(
					[
						'before plot',
						('self.',self,[
							#'ViewDeriveControllerVariable',
							'SettingValueVariable'
						])
					]
				)
			'''

			#init
			FigurePlotArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.ViewDeriveControllerVariable
				)

			#debug
			'''
			self.debug(
					[
						'We plot here',
						'FigurePlotArgumentDict is',
						SYS._str(FigurePlotArgumentDict)
					]
				)
			'''

			#plot
			self.FigureCartoonVariable=self.FiguredAxesVariable.plot(
					*FigurePlotArgumentDict['LiargVariablesList'],
					**FigurePlotArgumentDict['KwargVariablesDict']
				)

			#return 
			return {'HookingIsBool':False}

		elif self.SettingKeyVariable==FigureAxesKeyStr:

			#debug
			'''
			self.debug(
					[
						'before axes',
						('self.',self,['ViewDeriveControllerVariable'])
					]
				)
			'''

			#map
			ArgumentTuplesList=map(
					lambda __ItemTuple:
					(
						__ItemTuple[0],
						Setter.ArgumentDict(
								__ItemTuple[1],
								self.ViewDeriveControllerVariable
							)
					),
					SYS.SetList(
						self.SettingValueVariable
					)
				)

			#debug
			'''
			self.debug(
					[
						'We axe here',
						'ArgumentTuplesList is ',
						SYS._str(ArgumentTuplesList)
					]
				)
			'''

			#map
			map(
					lambda __ArgumentTuple:
					getattr(
						self.FiguredAxesVariable,
						__ArgumentTuple[0]
					)(
						*__ArgumentTuple[1]['LiargVariablesList'],
						**__ArgumentTuple[1]['KwargVariablesDict']
					) 
					if __ArgumentTuple[1]['KwargVariablesDict']!=None
					else
					getattr(
						self.FiguredAxesVariable,
						__ArgumentTuple[0]
					)(
						*__ArgumentTuple[1]['LiargVariablesList']
					),
					ArgumentTuplesList
				)

			#return 
			return {'HookingIsBool':False}

		elif type(self.SettingKeyVariable)==str and self.SettingKeyVariable.startswith(
			FigureMpld3KeyStr):

			#deprefix
			ToolTipKeyStr=SYS.deprefix(
					self.SettingKeyVariable,
					FigureMpld3KeyStr
				)

			#debug
			'''
			self.debug(
					[
						'before plugins',
						('self.',self,['ViewDeriveControllerVariable'])
					]
				)
			'''

			#init
			FigurePluginArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.ViewDeriveControllerVariable
				)

			#debug
			'''
			self.debug(
					[
						'We plugin here',
						'FigurePluginArgumentDict is ',
						SYS._str(FigurePluginArgumentDict)
					]
				)
			'''

			#plugin
			from mpld3 import plugins
			self.FigureTooltipVariable=getattr(
					plugins,
					ToolTipKeyStr
				)(
					*[
						self.FigureCartoonVariable[0]
					]+FigurePluginArgumentDict['LiargVariablesList'],
					**FigurePluginArgumentDict['KwargVariablesDict']
				)

			#debug
			'''
			self.debug(
					[
						('self.',self,['FigureTooltipVariable'])
					]
				)
			'''
			
			#connect
			plugins.connect(
				self.FigurePyplotVariable,
				self.FigureTooltipVariable
			)

			#return 
			return {'HookingIsBool':False}

		#call the base method
		BaseClass.set(self)

#</DefineClass>

#</DefinePrint>
FigurerClass.PrintingClassSkipKeyStrsList.extend(
	[
		#'FigurePyplotVariable',
		'FigureCartoonVariable',
		'FigureTooltipVariable',
		'FiguringGridIntsTuple',
		'FiguringSubGridIntsTuple',
		'FiguringAnchorIntsTuple',
		'FiguringShapeIntsTuple',
		'FiguringDrawVariable',
		'FiguredTeamTagStr',
		'FiguredDeriveTeamerVariablesList',
		'FiguredPanelDeriveTeamerVariable',
		'FiguredAxesVariable'
	]
)
#<DefinePrint>
