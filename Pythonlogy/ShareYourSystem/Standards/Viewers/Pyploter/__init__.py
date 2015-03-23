# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pyploter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Viewers.Viewer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo("Pyploter","Pyplot","Pyploting","Pyploted")
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Setter,Manager
from ShareYourSystem.Standards.Controllers import Controller
import copy
#</ImportSpecificModules>

#<DefineLocals>
PyplotPlotKeyStr='#plot'
PyplotBarKeyStr='#bar'
PyplotScatterKeyStr='#scatter'
PyplotAxesKeyStr='#axes'
PyplotMpld3KeyStr='#mpld3.plugins.'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['pyplot']
})
class PyploterClass(BaseClass):
	
	def default_init(self,
						_PyplotTooltipVariablesList=None,
						_PyplotingGridIntsTuple=(20,20),
						_PyplotingShapeIntsTuple=(1,1),
						_PyplotingDrawVariable=None,
						_PyplotingShiftIntsTuple=(1,0),
						_PyplotedTeamTagStr="",
						_PyplotedFigureDerivePyploterVariable=None,
						_PyplotedPanelDerivePyploterVariable=None,
						_PyplotedAxesDerivePyploterVariable=None,						
						_PyplotedFigureVariable=None,
						_PyplotedAxesVariable=None,
						_PyplotedLinesList=None,
						_PyplotedAnchorIntsList=[0,0],
						_PyplotedShiftTuplesList={
							'DefaultValueType':property,
							'PropertyInitVariable':None,
							'PropertyDocStr':'I am reactive when I am a Panel and want to know the space I take !'
						},
						_PyplotedPanelShapeIntsList=None,
						_PyplotedCursorIntsList=[0,0],
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_pyplot(self):	
		
		#debug
		'''
		self.debug(
				[
					'We pyplot here',
					#('self.',self,['ViewFirstDeriveViewerVariable'])
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)
		'''

		#/###############/#
		# If it is the top then init the pyplot
		#

		#Check
		if self.ParentDeriveTeamerVariable==None or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Panels','Axes'
		]:

			#debug
			'''
			self.debug(
					[
						'This is a Pyplot-Panel-Axes-Plot level'
					]
				)
			'''

			#import pyplot
			from matplotlib import pyplot

			#init
			self.PyplotedFigureVariable = pyplot.subplot()

			#init
			self.PyplotedAxesVariable = pyplot.axes()

			#link
			self.PyplotedAxesVariable._figure=self.PyplotedFigureVariable	


		"""

		#/###################/#
		# First we get the children pyplotrs and check what they are
		#

		

		#filter
		PyplotedTeamTagStrsList=SYS._filter(
			lambda __KeyStr:
			__KeyStr in ['Panels','Axes','Plots'],
			self.TeamDict.keys()
		)

		#Check
		if len(PyplotedTeamTagStrsList)==1:

			#filter
			self.PyplotedTeamTagStr=PyplotedTeamTagStrsList[0]

			#get
			self.PyplotedDeriveTeamerVariablesList=self.TeamDict[
				self.PyplotedTeamTagStr
			].ManagementDict.values()
		
		#debug
		'''
		self.debug(
				[
					('self.',self,[
							'PyplotedTeamTagStr',
							#'PyplotedDeriveTeamerVariablesList'
						])
				]
			)
		'''

		#/###################/#
		# do something before descending a pyplot call
		#

		if self.PyplotedTeamTagStr=='Panels':

			#debug
			'''
			self.debug(
					[
						'I am the top pyplotr...'
					]
				)
			'''

		elif self.PyplotedTeamTagStr=='Axes' or self.ParentDeriveTeamerVariable!=None and self.ParentDeriveTeamerVariable.TeamTagStr=='Panels':

			#/###############/#
			# Add an axe for the symbol of the panel
			#

			#debug
			'''
			self.debug(
					[
						'We transform the team dict Axes to add a panel axe',
						'self.TeamDict[\'Axes\'] is ',
						SYS._str(self.TeamDict['Axes'])
					]
				)
			'''

			#team
			self.team('Axes')

			#debug
			'''
			self.debug(
					[
						'before setting',
						'self.TeamedValueVariable.ManagementDict is ',
						SYS._str(self.TeamedValueVariable.ManagementDict),
						'Manager.ManagementDict is ',
						str(Manager.ManagementDict)
					]
				)
			'''

			#map an add
			map(
				lambda __DerivePyploter:
				setattr(
					__DerivePyploter,
					'ManagementIndexInt',
					__DerivePyploter.ManagementIndexInt+1
				),
				self.TeamedValueVariable.ManagementDict.values()
			)

			#update
			self.TeamedValueVariable.ManagementDict=Manager.ManagementDict(
				[
					(
						'Panel',SYS.PyploterClass(
							**{

								'ManagementTagStr':'Panel',
								'ManagementIndexInt':0,
								'ParentDeriveTeamerVariable':self.TeamedValueVariable,
								'ViewFirstDeriveViewerVariable':self.ViewFirstDeriveViewerVariable,
								'PyplotedFigureVariable':self.PyplotedFigureVariable,
								'PyplotingShapeIntsTuple':(1,1),
								'PyplotingDrawVariable':{
									'#axes':
									{
										'set_axis_off':{'#liarg':[]},
										'text':{
											'#liarg':[
												-1,0,'$\\mathbf{'+self.ManagementTagStr+'}$'
											],
											'#kwarg':{
												'fontsize':20
											}
										}
										
									}
								},
								'PyplotedPanelDerivePyploterVariable':self,
							}
						)
					)
				],
				**self.TeamedValueVariable.ManagementDict
			)

			#debug
			'''
			self.debug(
					[
						'after setting',
						'self.TeamedValueVariable.ManagementDict is ',
						SYS._str(self.TeamedValueVariable.ManagementDict)
					]
				)
			'''

			#Add maybe a shift in the next pyplot
			if len(self.TeamedValueVariable.ManagementDict)>1:

				#debug
				'''
				self.debug(
						[
							'We add a shift down and right to the next pyplot',
							'self.TeamedValueVariable.ManagementDict.get(1) is',
							SYS._str(self.TeamedValueVariable.ManagementDict.get(1))
						]
					)
				'''

				#set
				self.TeamedValueVariable.ManagementDict.get(1).PyplotingShiftIntsTuple=(1,1)

			#/##################/#
			# There are some Axes to count
			#

			#map get
			self.PyplotedShiftTuplesList=map(
					lambda __DerivePyploter:
					(
						__DerivePyploter.PyplotingShapeIntsTuple,
						__DerivePyploter.PyplotingShiftIntsTuple
					),
					self.TeamDict['Axes'].ManagementDict.values()
				)

			#debug
			'''
			self.debug(
					[
						'I am a still Panel...',
						('self.',self,[
							'PyplotedShiftTuplesList',
							'ManagementIndexInt'
						])
					]
				)
			'''

			#/###############/#
			# Determine what is the anchor considering the one of the last panel
			#

			#Check
			if self.ManagementIndexInt>0:

				#debug
				'''
				self.debug(
					[
						'We get the previous Panel',
						'self.ParentDeriveTeamerVariable.ManagementDict is ',
						SYS._str(self.ParentDeriveTeamerVariable.ManagementDict)
					]
				)
				'''

				#get the previous
				PyplotedPreviousPanelPyploter=self.ParentDeriveTeamerVariable.ManagementDict.get(
					self.ManagementIndexInt-1
				)

				#debug
				'''
				self.debug(
						[
							'We look for the previous panel...',
							#('PyplotedPreviousPanelPyploter.',PyplotedPreviousPanelPyploter,[
							#		'PyplotedAnchorIntsList',
							#		'PyplotedPanelShapeIntsList'
							#	]
							#)
						]
					)
				'''

				#Check
				if self.PyplotingShiftIntsTuple[0]>0:

					#add
					self.PyplotedAnchorIntsList[0]=PyplotedPreviousPanelPyploter.PyplotedAnchorIntsList[0
							]+self.PyplotingShiftIntsTuple[0]+PyplotedPreviousPanelPyploter.PyplotedPanelShapeIntsList[0]+1

				if self.PyplotingShiftIntsTuple[1]>0:

					#add
					self.PyplotedAnchorIntsList[1]=PyplotedPreviousPanelPyploter.PyplotedAnchorIntsList[1
							]+self.PyplotingShiftIntsTuple[1]+PyplotedPreviousPanelPyploter.PyplotedPanelShapeIntsList[1]+1

				#debug
				self.debug(
						[
							'we have setted the new anchor',
							('self.',self,['PyplotedAnchorIntsList'])
						]
					)

			#/###############/#
			# Init the Cursor for after
			#

			#init
			self.PyplotedCursorIntsList=copy.copy(self.PyplotedAnchorIntsList)


			#/###############/#
			# Look maybe at a Panel without Axes and Plots
			#

			#Check
			if len(self.TeamDict['Axes'].ManagementDict.keys())==1:

				#debug
				'''
				self.debug(
						[
							'I am a Panel without Axes and Plots',
							'So we just set an axe here'
						]
					)
				'''

				#set
				self.setAxes()

				#/###################/#
				# if there axes setted then apply the draw set variable 
				#

				#Check
				if self.PyplotedAxesVariable!=None:

					#debug
					'''
					self.debug(
							[
								'There are axes so command the figuring draw variable',
								('self.',self,[
									'PyplotingDrawVariable'
								])
							]
						)
					'''

					#commad self
					#self.command(self,self.PyplotingDrawVariable)
					#self.command(self,[])
					self['#map@set'](self.PyplotingDrawVariable)

				#return
				return

		elif self.PyplotedTeamTagStr=='Plots':

			#debug
			'''
			self.debug(
					[
						'I am an Axes..',
						('self.',self,['ParentDeriveTeamerVariable'])
					]
				)
			'''

			#get the parent panel
			self.PyplotedPanelDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#debug
			'''
			self.debug(
					[
						'I am still an Axes..',
						('self.',self,[
							'PyplotedPanelDerivePyploterVariable',
							#'ViewFirstDeriveViewerVariable',
							'PyplotedAnchorIntsList',
							'PyplotingShapeIntsTuple'
						])
					]
				)
			'''

			#alias
			self.PyplotingGridIntsTuple=self.ViewFirstDeriveViewerVariable.PyplotingGridIntsTuple
			self.setAxes()

			#debug
			'''
			self.debug(
					[
						'I am still an Axes..',
						('self.',self,['PyplotedAxesVariable'])
					]
				)
			'''

		else:

			#debug
			'''
			self.debug(
					[
						'I dont have such panels axes plots...',
						'So I can be a plot or the top one axe one plot pyplotr'
					]
				)
			'''

			#Check
			if self!=self.ViewFirstDeriveViewerVariable:

				#get
				PyplotedParentParentVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

				#debug
				'''
				self.debug(
					[
						'PyplotedParentParentVariable.ParentDeriveTeamerVariable.TeamTagStr is ',
						PyplotedParentParentVariable.ParentDeriveTeamerVariable.TeamTagStr,
						'PyplotedParentParentVariable is ',
						SYS._str(PyplotedParentParentVariable)
					]
				)
				'''

				#Check
				if PyplotedParentParentVariable.ParentDeriveTeamerVariable.TeamTagStr=='Views':

					#/###################/#
					# build a PyplotedAxesVariables
					#

					#debug
					'''
					self.debug(
							[
								'I am a panel without Axes and Plots so just set an axis here...',
							]
						)
					'''

					#alias
					self.PyplotingGridIntsTuple=self.ViewFirstDeriveViewerVariable.PyplotingGridIntsTuple

					#set
					self.setAxes()

				#Check
				elif PyplotedParentParentVariable.ParentDeriveTeamerVariable.TeamTagStr=='Panels':

					#alias
					self.PyplotedPanelDerivePyploterVariable=PyplotedParentParentVariable

					#/###################/#
					# build a PyplotedAxesVariables
					#

					#debug
					'''
					self.debug(
							[
								'I am an axes without Plots so just set an axis here...',
							]
						)
					'''

					#alias
					self.PyplotingGridIntsTuple=self.ViewFirstDeriveViewerVariable.PyplotingGridIntsTuple
					self.PyplotedAnchorIntsList=self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList

					#set
					self.setAxes()

				else:

					#/###################/#
					# point to the PyplotedAxesVariable
					#

					#debug
					'''
					self.debug(
							[
								'I am Plot..',
								'I set my PyplotedAxesVariables corresponding to my parent one',
								#'PyplotedParentParentVariable is ',
								#SYS._str(PyplotedParentParentVariable),
								'PyplotedParentParentVariable.ManagementTagStr is ',
								PyplotedParentParentVariable.ManagementTagStr,
								'PyplotedParentParentVariable.PyplotedAxesVariable is ',
								PyplotedParentParentVariable.PyplotedAxesVariable,
							]
						)
					'''

					#get the parent panel
					self.PyplotedAxesDerivePyploterVariable=PyplotedParentParentVariable

					#get the one of the parent
					self.PyplotedAxesVariable=self.PyplotedAxesDerivePyploterVariable.PyplotedAxesVariable

				#debug
				'''
				self.debug(
						[
							'I have definitely an axes..',
							('self.',self,['PyplotedAxesVariable'])
						]
					)
				'''

				#/###################/#
				# if there are axes setted then apply the draw set variable 
				#

				#Check
				if self.PyplotedAxesVariable!=None:

					#debug
					'''
					self.debug(
							[
								'There are axes so command the figuring draw variable',
								('self.',self,[
									'PyplotingDrawVariable'
								])
							]
						)
					'''

					#commad self
					#self.command(self,self.PyplotingDrawVariable)
					#self.command(self,[])
					self['#map@set'](self.PyplotingDrawVariable)

				#/###################/#
				# if it is the last then trigger the axes to set also
				#

				#Check
				if self.ManagementIndexInt==(len(self.ParentDeriveTeamerVariable.ManagementDict)-1):

					#debug
					'''
					self.debug(
						[
							'I am the last plot of this axes !',
							'Lets the axes setting itself now',
							('self.PyplotedAxesDerivePyploterVariable.',
								self.PyplotedAxesDerivePyploterVariable,
								['PyplotingDrawVariable'])
						]
					)	
					'''

					#commad self
					if self.PyplotedAxesDerivePyploterVariable!=None:
						if self.PyplotedAxesDerivePyploterVariable.PyplotingDrawVariable!=None:
							self.PyplotedAxesDerivePyploterVariable['#map@set'](
								self.PyplotedAxesDerivePyploterVariable.PyplotingDrawVariable
							)


			else:

				#/###################/#
				# Pyplot-Panel-Axes-Plot level
				#

				#debug
				self.debug(
						[
							'I am the top pyplotr but with just one axes..',
							('self.',self,['PyplotingGridIntsTuple'])
						]
					)

				#Set the size of the grid to this just one plot
				self.PyplotingGridIntsTuple=(1,1)

				#get the parent panel
				self.PyplotedPanelDerivePyploterVariable=self

				#init
				self.setAxes()

				#map set
				if self.PyplotingDrawVariable!=None:

					#mapSet
					self.mapSet(
						self.PyplotingDrawVariable
					)
		"""
	
	def mimic_view(self):

		#import mpld3
		import mpld3

		#fig to html
		self.ViewedHtmlStr=mpld3.fig_to_html(
			self.PyplotedFigureVariable,
			template_type="simple"
		)

		#call the base method
		BaseClass.view(self)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/#################/#
		# Lets go for pyplot
		#

		#debug
		'''
		self.debug(
				'We are going to pyplot'
			)
		'''

		#pyplot
		self.pyplot()

		#/#################/#
		# Call the base method
		#

		#call the parent method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)


	def mimic_set(self):

		#Check
		if self.SettingKeyVariable in [
											PyplotPlotKeyStr,
											PyplotScatterKeyStr,
											PyplotBarKeyStr
										]:

			#/####################/#
			# first maybe pyplot if it was not already
			# 

			#debug
			'''
			self.debug(
					[
						'we maybe pyplot first',
					]
				)
			'''

			#pyplot
			self.pyplot()

			#/####################/#
			# Then add in the plot
			# 

			#debug
			'''
			self.debug(
					[
						'before plot',
						('self.',self,[
							#'PyplotedFigureDerivePyploterVariable',
							'SettingValueVariable'
						])
					]
				)
			'''

			#init
			PyplotPlotArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.PyplotedFigureDerivePyploterVariable
				)

			#debug
			'''
			self.debug(
					[
						'We plot here',
						'PyplotPlotArgumentDict is',
						SYS._str(PyplotPlotArgumentDict)
					]
				)
			'''

			#plot
			self.PyplotedLinesList.append(
				self.PyplotedAxesVariable.plot(
					*PyplotPlotArgumentDict['LiargVariablesList'],
					**PyplotPlotArgumentDict['KwargVariablesDict']
				)[0]
			)

			#debug
			'''
			self.debug(
				[
					('self.',self,['PyplotedLinesList']),
					#str(self.PyplotedLinesList[0][0]),
				]
			)
			'''

			#return 
			return {'HookingIsBool':False}

		elif self.SettingKeyVariable==PyplotAxesKeyStr:

			#debug
			'''
			self.debug(
					[
						'before axes',
						('self.',self,[
							#'PyplotedFigureDerivePyploterVariable',
							'PyplotedAxesVariable'
						])
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
								self.PyplotedFigureDerivePyploterVariable
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
						SYS._str(ArgumentTuplesList),
					]
				)
			'''

			#map
			map(
					lambda __ArgumentTuple:
					SYS.get(
						self.PyplotedAxesVariable,
						__ArgumentTuple[0]
					)()
					if len(__ArgumentTuple[1]['LiargVariablesList']
						)==0 and __ArgumentTuple[1]['KwargVariablesDict']==None
					else(
						SYS.get(
							self.PyplotedAxesVariable,
							__ArgumentTuple[0]
						)(**__ArgumentTuple[1]['KwargVariablesDict'])
						if len(__ArgumentTuple[1]['LiargVariablesList']
						)==0
						else(
							SYS.get(
								self.PyplotedAxesVariable,
								__ArgumentTuple[0]
							)(
								*__ArgumentTuple[1]['LiargVariablesList'],
								**__ArgumentTuple[1]['KwargVariablesDict']
							) 
							if __ArgumentTuple[1]['KwargVariablesDict']!=None
							else
							SYS.get(
								self.PyplotedAxesVariable,
								__ArgumentTuple[0]
							)(
								*__ArgumentTuple[1]['LiargVariablesList']
							)
						)
					),
					ArgumentTuplesList
				)

			#return 
			return {'HookingIsBool':False}

		elif type(self.SettingKeyVariable)==str and self.SettingKeyVariable.startswith(
			PyplotMpld3KeyStr):

			#deprefix
			ToolTipKeyStr=SYS.deprefix(
					self.SettingKeyVariable,
					PyplotMpld3KeyStr
				)

			#debug
			'''
			self.debug(
					[
						'before plugins',
						('self.',self,['PyplotedFigureDerivePyploterVariable'])
					]
				)
			'''

			#init
			PyplotPluginArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.PyplotedFigureDerivePyploterVariable
				)

			#debug
			'''
			self.debug(
					[
						'We plugin here',
						'PyplotPluginArgumentDict is ',
						SYS._str(PyplotPluginArgumentDict)
					]
				)
			'''

			#plugin
			from mpld3 import plugins
			self.PyplotTooltipVariablesList=map(
				lambda __PyplotCartoonVariable:
				getattr(
					plugins,
					ToolTipKeyStr
				)(
					*[
						__PyplotCartoonVariable
					]+PyplotPluginArgumentDict['LiargVariablesList'],
					**PyplotPluginArgumentDict['KwargVariablesDict']
				),
				self.PyplotedLinesList
			)

			#debug
			'''
			self.debug(
					[
						('self.',self,['PyplotTooltipVariablesList'])
					]
				)
			'''
			
			#connect
			map(
				lambda __PyplotTooltipVariable:
				plugins.connect(
					self.PyplotedFigureVariable,
					__PyplotTooltipVariable
				),
				self.PyplotTooltipVariablesList
			)

			#return 
			return {'HookingIsBool':False}

		#call the base method
		BaseClass.set(self)

	def setAxes(self):

		#/#################/#
		# First shift in the grid
		#

		#Check
		if self.ManagementIndexInt>0:

			#debug
			'''
			self.debug(
					[
						'first we shift',
						'self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList is ',
						str(self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList),
						('self.',self,['PyplotingShapeIntsTuple','PyplotingShiftIntsTuple'])
					]
				)
			'''

			#get
			PyplotedPreviousAxesPyploter=self.ParentDeriveTeamerVariable.ManagementDict.get(
				self.ManagementIndexInt-1
			)

			#shift
			if self.PyplotingShiftIntsTuple[0]>0:
				self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList[0
				]+=self.PyplotingShiftIntsTuple[0]+PyplotedPreviousAxesPyploter.PyplotingShapeIntsTuple[0]
			if self.PyplotingShiftIntsTuple[1]>0:
				self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList[1
				]+=self.PyplotingShiftIntsTuple[1]+PyplotedPreviousAxesPyploter.PyplotingShapeIntsTuple[1]

			#debug
			'''
			self.debug(
					[
						'Ok we have shifted',
						'now we link with the fig',
						('self.PyplotedPanelDerivePyploterVariable.',self.PyplotedPanelDerivePyploterVariable,
							['PyplotedCursorIntsList']),
					]
				)
			'''

		#set
		if self.PyplotedPanelDerivePyploterVariable!=None:
			self.PyplotedAnchorIntsList=copy.copy(
				self.PyplotedPanelDerivePyploterVariable.PyplotedCursorIntsList
			)

		#/#################/#
		# init
		#

		#debug
		'''
		self.debug(
				[
					'Ok we set an axes here',
					('self.',self,[
							'PyplotingGridIntsTuple',
							'PyplotedAnchorIntsList',
							'PyplotingShapeIntsTuple'
						]),
					''
				]
			)
		'''

		#init
		from matplotlib import pyplot
		self.PyplotedAxesVariable=pyplot.subplot2grid(
				self.PyplotingGridIntsTuple, 
				self.PyplotedAnchorIntsList, 
				rowspan=self.PyplotingShapeIntsTuple[0],
				colspan=self.PyplotingShapeIntsTuple[1]
			)

		#debug
		'''
		self.debug(
				[
					'Ok we have initiated the axes',
					('self.',self,['PyplotedAxesVariable'])
				]
			)
		'''

		#/#################/#
		# link to the fig
		#

		#link
		self.PyplotedAxesVariable._figure=self.PyplotedFigureVariable	

		#debug
		'''
		self.debug(
				[
					'Ok we have setted the axe'
				]
			)
		'''

	def propertize_setPyplotedShiftTuplesList(self,_SettingValueVariable):

		#set
		self._PyplotedShiftTuplesList=_SettingValueVariable

		#debug
		'''
		self.debug(
				[
					'We bind a set of PyplotedShiftTuplesList here',
					'_SettingValueVariable is',
					str(_SettingValueVariable)
				]
			)
		'''

		#init
		self.PyplotedPanelShapeIntsList=list(_SettingValueVariable[0][0])

		#Check
		if len(_SettingValueVariable)>1:
		
			#shift
			for __PyplotedShiftTuple in _SettingValueVariable[1:]:

				#debug
				'''
				self.debug(
						[	
							'We shift with ',
							'__PyplotedShiftTuple is ',
							str(__PyplotedShiftTuple)
						]
					)
				'''

				#Check
				if __PyplotedShiftTuple[1][0]>0:

					#add
					self.PyplotedPanelShapeIntsList[0]+=__PyplotedShiftTuple[1][0]+__PyplotedShiftTuple[0][0]

				if __PyplotedShiftTuple[1][1]>0:

					#dd
					self.PyplotedPanelShapeIntsList[1]+=__PyplotedShiftTuple[1][1]+__PyplotedShiftTuple[0][1]

		#debug
		'''
		self.debug(
				[
					'in the end of the shift',
					('self.',self,[
						'PyplotedPanelShapeIntsList',
						'PyplotedCursorIntsList'
					])
				]
			)
		'''

#</DefineClass>

#</DefinePrint>
PyploterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PyplotTooltipVariablesList',
		'PyplotingGridIntsTuple',
		'PyplotingShapeIntsTuple',
		'PyplotingDrawVariable',
		'PyplotingShiftIntsTuple',
		'PyplotedTeamTagStr',
		'PyplotedFigureDerivePyploterVariable',
		'PyplotedPanelDerivePyploterVariable',
		'PyplotedAxesDerivePyploterVariable',
		#'PyplotedFigureVariable',
		#'PyplotedAxesVariable',
		'PyplotedLinesList',
		'PyplotedAnchorIntsList',
		'PyplotedShiftTuplesList',
		'PyplotedPanelShapeIntsList',
		'PyplotedCursorIntsList'
	]
)
#<DefinePrint>

#<DefineLocals>
Controller.ViewsClass.ManagingValueClass=PyploterClass
PyploterClass.TeamingClassesDict=dict(
	map(
		lambda __KeyStr:
		(__KeyStr,Controller.ViewsClass),
		['Panels','Axes','Plots']
	)
)
#<DefineLocals>
