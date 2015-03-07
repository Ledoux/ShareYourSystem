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
#</ImportSpecificModules>

#<DefineDoStrsList>
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class FigurerClass(BaseClass):
	
	def default_init(self,
						_FigurePyplotVariable=None,
						_FiguredTeamTagStr="",
						_FiguredDeriveTeamerVariablesList=None,
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
		self.debug(
				[
					'We figure here',
					('self.',self,['ViewFirstDeriveViewerVariable'])
				]
			)

		#filter
		FiguredTeamTagStrsList=SYS._filter(
			lambda __KeyStr:
			__KeyStr in ['Panels','Axes'],
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
			self.debug(
					[
						('self.',self,[
								'FiguredTeamTagStr',
								#'FiguredDeriveTeamerVariablesList'
							])
					]
				)

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
		# now do somethiing here depending on the Tag
		#

		if self.FiguredTeamTagStr=='Axes':

			#debug
			self.debug(
					[
						'I am a Panel...'
					]
				)

		else:

			#debug
			self.debug(
					[
						'I am an Axes..'
					]
				)


		"""

		#/################/#
		# If it is the top then recruit all the axis and plots
		#

		#Check
		if self.ViewFirstDeriveViewerVariable==self:

			#debug
			self.debug(
					'We are the first viewer so command other deeper'
				)

			#map
			FiguredCommandGetVariable=SYS.flat(
					SYS.filterNone(
					map(
							lambda __TeamKeyStr:
							self.TeamDict[__TeamKeyStr].ManagementDict.values()
							if __TeamKeyStr in self.TeamDict
							else None,
							['Panels','Axes']
					)
				)
			)

			#debug
			self.debug(
				[
					'FiguredCommandGetVariable is ',
					str(FiguredCommandGetVariable)
				]
			)

			#command
			self.command(
				FiguredCommandGetVariable,
				'#call:figure',
				_AfterWalkBool=True,
				_BeforeSelfBool=False,
				_AfterSelfBool=False,	
			)

		else:

			#debug
			self.debug(
				[
					'I am in a figure !',
				]
			)
		"""

	def mimic_team(self):

		#call the base method
		BaseClass.team(self)

		#Check
		if self.TeamingKeyStr in ['Panels','Axes']:

			#set
			self.TeamedValueVariable.ManagingValueClass=SYS.FigurerClass


	def mimic_view(self):

		#import mpld3
		import mpld3

		#fig to html
		self.ViewedHtmlStr=mpld3.fig_to_html(
			self.FigurePyplotVariable,
			template_type="simple"
		)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the parent method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/###############/#
		# If it is the top then init the figure
		#

		#Check
		if self.ViewFirstDeriveViewerVariable==self:

			#debug
			self.debug(
					[
						'We init a figure'
					]
				)

			#import pyplot
			from matplotlib import pyplot

			#subplots
			self.FigurePyplotVariable = pyplot.figure()

		else:

			#debug
			self.debug(
					[
						'We just do an alias'
					]
				)

			#alias
			self.FigurePyplotVariable=self.ViewFirstDeriveViewerVariable.FigurePyplotVariable

#</DefineClass>

#</DefinePrint>
FigurerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'FigurePyplotVariable',
		'FiguredTeamTagStr',
		'FiguredDeriveTeamerVariablesList'
	]
)
#<DefinePrint>
