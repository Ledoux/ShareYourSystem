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
from ShareYourSystem.Standards.Interfacers import Printer
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
def getFiguresList():

	#import 
	import matplotlib._pylab_helpers

	#return
	return [
		Manager.canvas.figure for Manager in matplotlib._pylab_helpers.Gcf.get_all_fig_managers()
	]
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['pyplot'],
	'ClassingStructureVariable':[
		('Panel','Panels'),
		('Chart','Charts'),
		('Draw','Draws')
	]
})
class PyploterClass(BaseClass):
	
	def default_init(self,
						_PyplotTooltipVariablesList=None,
						_PyplotingGridIntsTuple=(22,20),
						_PyplotingShapeVariable=None,
						_PyplotingFigureVariable=None,
						_PyplotingDrawVariable=None,
						_PyplotingChartVariable=None,
						_PyplotingShiftIntsTuple=(1,0),
						_PyplotingPrintBool=True,
						_PyplotedTeamTagStr="",
						_PyplotedParentFigureDerivePyploterVariable=None,
						_PyplotedParentPanelDerivePyploterVariable=None,
						_PyplotedParentChartDerivePyploterVariable=None,						
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
						_PyplotedChartTuplesList=None,
						_PyplotedDrawTuplesList=None,
						_PyplotedParentSingularStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_pyplot(self):	
		
		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We pyplot here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(self.ParentedTotalSingularListDict)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.PyplotedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['PyplotedParentSingularStr'])
			]
		)
		'''

		#/###############/#
		# Cases depending on the level
		#

		#Check
		if (self.ParentDeriveTeamerVariable==None or 'Panels' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Panels',
			'Charts',
			'Draws'
		]):

			#/########################/#
			# pyplotFigure
			#

			#call
			self.pyplotFigure()

			#/########################/#
			# structure pyplot
			# 

			#debug
			'''
			self.debug(
				[
					'We structure pyplot all the children...',
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)
			'''

			#structure
			self.structure(
				[
					'Panels',
					'Charts',
					'Draws'
				],
				'#all',
				_ManagerCommandSetList=['pyplot']
			)

			#debug
			'''
			self.debug(
				[
					'Ok we have structure Panels, Charts, Draws',
					'getFiguresList is ',
					str(getFiguresList())
				]
			)
			'''

		else:

			#/########################/#
			# Inside structure
			#

			#debug
			'''
			self.debug(
				[
					'Ok we check if this parentsingular has a special method ',
					('self.',self,[
						'PyplotedParentSingularStr'
					])
				]
			)
			'''

			#Check
			if self.ParentDeriveTeamerVariable.TeamTagStr=='Panels':

				#debug
				'''
				self.debug(
						[
							'Panel level.'
						]
					)
				'''

				#/#################/#
				# Determine the parent
				#

				#set
				self.PyplotedParentFigureDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

				#pyplotPanel
				self.pyplotPanel()

			elif self.ParentDeriveTeamerVariable.TeamTagStr=='Charts':

				#debug
				'''
				self.debug(
						[
							'Chart level.',
							'determine the parent
						]
					)
				'''

				#/#################/#
				# Determine the parent
				#

				#Check
				if self.ParentDeriveTeamerVariable!=None:

					#Check
					if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable!=None:

						#Check
						if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.PyplotedParentSingularStr=='Panel':

							#debug
							'''
							self.debug(
								[
									'Ok there is a parent Panel for this Chart',
									'Check now for a parent figure'
								]
							)	
							'''


							#alias
							self.PyplotedParentPanelDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

							#alias
							self.PyplotedParentFigureDerivePyploterVariable=self.PyplotedParentPanelDerivePyploterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable
				
						else:

							#alias
							self.PyplotedParentPanelDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

							#alias
							self.PyplotedParentFigureDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable
								
							#debug
							'''
							self.debug(
									[
										'There is no Panel parent',
										'We set bigger PyplotingShapeVariable',
										('self.',self,[
												'PyplotingShapeVariable'
											])
									]
								)
							'''

							#set
							if self.PyplotingShapeVariable==None:

								#debug
								'''
								self.debug(
									[
										('self.',self,[
											'PyplotingShiftIntsTuple',
											'PyplotedCursorIntsList'
										]),
										'self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList is ',
										str(self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList)
									]
								)
								'''
								
								#set	
								self.PyplotingShapeVariable=list(
									self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple
								)

								#Check
								if self.PyplotingShiftIntsTuple[0]>0:

									self.PyplotingShapeVariable[0]/=len(
											self.PyplotedParentFigureDerivePyploterVariable.TeamDict['Charts'].ManagementDict
										)
									self.PyplotingShapeVariable[1]-=2
									
								else:

									self.PyplotingShapeVariable[1]/=len(
											self.PyplotedParentFigureDerivePyploterVariable.TeamDict['Charts'].ManagementDict
										)
									

				#debug
				'''
				self.debug(
					[
						'Ok for this Chart, we have determined the panel and figure parent',
						#('self.',self,[
						#	'PyplotedParentFigureDerivePyploterVariable'
						#])
					]
				)
				'''

				#/#################/#
				# Build the Axes
				#

				#debug
				'''
				self.debug(
					[
						'we set a Chart'
					]
				)
				'''

				#set Chart
				self.pyplotChart()

				#debug
				'''
				self.debug(
					[
						'we have setted the Chart here',
						('self.',self,[
							'PyplotedAxesVariable'
						])
					]
				)
				'''

			elif self.ParentDeriveTeamerVariable.TeamTagStr=='Draws':

				#debug
				'''
				self.debug(
						[
							'Draws level.'
						]
					)
				'''

				#/#################/#
				# Determine the parent
				#

				#set
				self.PyplotedParentChartDerivePyploterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

				#debug
				'''
				self.debug(
						[
							'self.PyplotedParentChartDerivePyploterVariable.PyplotedParentSingularStr is ',
							self.PyplotedParentChartDerivePyploterVariable.PyplotedParentSingularStr
						]
					)
				'''

				#Check
				if self.PyplotedParentChartDerivePyploterVariable.PyplotedParentSingularStr=='Panel':

					#set
					self.PyplotedParentPanelDerivePyploterVariable=self.PyplotedParentChartDerivePyploterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable
			
					#set
					self.PyplotedParentFigureDerivePyploterVariable=self.PyplotedParentPanelDerivePyploterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

				else:

					#debug
					'''
					self.debug(
							[
								'It is not a parent chart inside a panel ',
								'Look if the parent parent is actually the top
							]
						)
					'''

					#Check
					if self.PyplotedParentChartDerivePyploterVariable.ParentDeriveTeamerVariable!=None:
						
						#alias
						PyplotedParentFigurePanelDerivePyploterVariable=self.PyplotedParentChartDerivePyploterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable
						
						#Check
						if PyplotedParentFigurePanelDerivePyploterVariable!=None:

							#debug
							'''
							self.debug(
								[
									'Yes the parent parent is the top'
								]
							)
							'''

							#set
							self.PyplotedParentPanelDerivePyploterVariable=PyplotedParentFigurePanelDerivePyploterVariable
					
							#set
							self.PyplotedParentFigureDerivePyploterVariable=PyplotedParentFigurePanelDerivePyploterVariable

					else:

						#debug
						'''
						self.debug(
							[
								'Nope the parent parent not exist so direct set figure panel with chart parent'
							]
						)
						'''

						#set
						self.PyplotedParentPanelDerivePyploterVariable=self.PyplotedParentChartDerivePyploterVariable
					
						#set
						self.PyplotedParentFigureDerivePyploterVariable=self.PyplotedParentChartDerivePyploterVariable


				#debug
				'''
				self.debug(
					[
						'Ok for this Draw, we have determined the chart panel and figure parent',
						('self.',self,[
							'PyplotedParentFigureDerivePyploterVariable'
						])
					]
				)
				'''

				#pyplotDraw
				self.pyplotDraw()

		#debug
		'''
		self.debug(
			[
				'In the end',
				'getFiguresList is ',
				str(getFiguresList())
			]
		)
		'''

	def pyplotFigure(self):

		#/###############/#
		# Close the old ones
		#

		#get
		PyplotedOldFiguresList=getFiguresList()

		#debug
		'''
		self.debug(
			[
				'The old figures was',
				str(PyplotedOldFiguresList)
			]
		)
		'''

		#import
		from matplotlib import pyplot

		#map
		map(
			lambda __Figure:
			pyplot.close(__Figure),
			getFiguresList()
		)
		
		#/###############/#
		# If it is the top then init the pyplot
		#

		#debug
		'''
		self.debug(
				[
					'Figure Level'
				]
			)
		'''
		
		#import pyplot
		from matplotlib import pyplot

		#init
		if self.PyplotingFigureVariable!=None:

			#init
			self.PyplotedFigureVariable = pyplot.figure(
				**self.PyplotingFigureVariable
			)

		else:

			#init
			self.PyplotedFigureVariable = pyplot.figure()

		#/###############/#
		# Case of a Figure Panel Axes Draws 
		#

		#Check
		if all(
			map(
				lambda __KeyStr:
				__KeyStr not in self.TeamDict,
				['Charts','Panels']
			)
		):

			#/###############/#
			# Set parent 
			#

			#
			self.PyplotedParentFigureDerivePyploterVariable=self
			self.PyplotedParentPanelDerivePyploterVariable=self
			self.PyplotedParentChartDerivePyploterVariable=self

			#/###############/#
			# pyplotChart 
			#

			#debug
			'''
			self.debug(
				[
					'We are in the case of a Figure Panel Axes draw'
				]
			)
			'''

			#init
			self.PyplotedAxesVariable = pyplot.axes()

			#link
			self.PyplotedAxesVariable._figure=self.PyplotedFigureVariable

			#/#################/#
			# Look for view argument
			#

			#debug
			'''
			self.debug(
				[
					'First look for view arguments'
				]
			)
			'''

			#map
			map(
				lambda __AxeStr:
				self.pyplotAxe(__AxeStr),
				[
					'X',
					'Y'
				]
			)

			#debug
			'''
			self.debug(
				[
					'Ok we have maybe setted the PyplotingChartVariable',
					('self.',self,[
							'PyplotingChartVariable'
						]),
					'getFiguresList is ',
					str(getFiguresList())
				]
			)
			'''

			#/###############/#
			# pyplotDraw
			#

			#pyplotDraw
			self.pyplotDraw()

			#debug
			'''
			self.debug(
				[
					'after pyplotDraw',
					'getFiguresList is ',
					str(getFiguresList())
				]
			)
			'''

	def pyplotPanel(self):


		#debug
		'''
		self.debug(
			[
				'We pyplot Panel here',
				('self.',self,[
						'PyplotedCursorIntsList'
					]
				),
				'We reinit the cursor'
			]
		)
		'''

		#set
		self.PyplotedCursorIntsList=[0,0]

	def pyplotAxe(self,_AxeStr):

		#debug
		'''
		self.debug(
			[
				'We pyplotAxe here',
				('self.',self,[
					'PyplotingChartVariable',
					'PyplotedChartTuplesList',
				])
			]
		)
		'''

		#set
		LowAxeStr=_AxeStr.lower()

		#/###############/#
		# Look for a label
		#

		#get
		ViewingLabelStr=getattr(
			self,
			'Viewing'+_AxeStr+'LabelStr'
		)

		#Check
		if ViewingLabelStr!="":

			#Init
			ViewedLabelPlot=False

			#Check
			if (
					_AxeStr=='X' and self.PyplotingShiftIntsTuple[0]>0
				) or (
					_AxeStr=='Y' and self.PyplotingShiftIntsTuple[1]>0
				):

				#Check
				if self.ParentDeriveTeamerVariable!=None and self.ManagementIndexInt<len(self.ParentDeriveTeamerVariable.ManagementDict)-1:

					#append
					self.PyplotedChartTuplesList.append(
						(
							'set_'+LowAxeStr+'label',{
								'#liarg':[""]
							}
						)
					)

					#set
					ViewedLabelPlot=True

			#Check
			if ViewedLabelPlot==False:

				#debug
				'''
				self.debug(
					[
						'We set axis label',
						'ViewingLabelStr is ',
						str(ViewingLabelStr)
					]
				)
				'''

				#append
				#self.PyplotedChartTuplesList.append(
				#	(
				#		'set_'+LowAxeStr+'label',ViewingLabelStr
				#	)
				#)

				#append
				self.PyplotedChartTuplesList.append(
					(
						'set_'+LowAxeStr+'label',{
								'#liarg':[ViewingLabelStr],
								'#kwarg':{
									'fontsize':20
								}
							}
					)
				)
				

		#/###############/#
		# Look for a lim
		#

		#get
		ViewedLimLiargStr=getattr(
			self,
			'Viewed'+_AxeStr+'limLiargStr'
		)

		#Check
		if ViewedLimLiargStr!="":

			#append
			self.PyplotedChartTuplesList.append(
				(
					'set_'+LowAxeStr+'lim',{
						'#liarg:#map@get':[ViewedLimLiargStr]
					}
				)
			)

		#/###############/#
		# Look for ticks
		#

		#get
		ViewedTickLiargStr=getattr(
			self,
			'Viewed'+_AxeStr+'tickLiargStr'
		)

		#Check
		if ViewedTickLiargStr!="":

			#append
			self.PyplotedChartTuplesList.append(
				(
					'set_'+LowAxeStr+'ticks',{
						'#liarg:#map@get':[ViewedTickLiargStr]
					}
				)
			)

		#/###############/#
		# Look for tick labels
		#

		#get
		ViewedTickLabelLiargStr=getattr(
			self,
			'Viewed'+_AxeStr+'tickLabelLiargStr'
		)

		#Check
		if ViewedTickLabelLiargStr!="":

			#Init
			ViewedTickLabelPlot=False

			#Check
			if (
					_AxeStr=='X' and self.PyplotingShiftIntsTuple[0]>0
				) or (
					_AxeStr=='Y' and self.PyplotingShiftIntsTuple[1]>0
				):

				#Check
				if self.ManagementIndexInt<len(self.ParentDeriveTeamerVariable.ManagementDict)-1:

					#append
					self.PyplotedChartTuplesList.append(
						(
							'set_'+LowAxeStr+'ticklabels',{
								'#liarg':[[]]
							}
						)
					)

					#set
					ViewedTickLabelPlot=True

			#Check
			if ViewedTickLabelPlot==False:

				#append
				self.PyplotedChartTuplesList.append(
					(
						'set_'+LowAxeStr+'ticklabels',{
							'#liarg:#map@get':[ViewedTickLabelLiargStr],
							'#kwarg':{
								'fontsize':15
							}
						}
					)
				)


	def pyplotChart(self):

		#/#################/#
		# Check
		#

		#debug
		'''
		self.debug(
			[
				'We pyplot Chart here',
				('self.',self,[
					'PyplotingChartVariable'
				])
			]
		)
		'''

		#Check
		if self.PyplotingChartVariable!=None:

			#copy
			self.PyplotedChartTuplesList+=copy.copy(
				self.PyplotingChartVariable.items()
				if hasattr(self.PyplotingChartVariable,'items')
				else self.PyplotingChartVariable
			)

		#/#################/#
		# Look for view argument
		#

		#debug
		'''
		self.debug(
			[
				'First look for view arguments'
			]
		)
		'''
		
		#map
		map(
			lambda __AxeStr:
			self.pyplotAxe(__AxeStr),
			['X','Y']
		)

		#debug
		'''
		self.debug(
			[
				'Ok we have maybe setted the PyplotedChartTuplesList',
				('self.',self,[
						'PyplotedChartTuplesList'
					])
			]
		)
		'''
		
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
						'self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList is ',
						str(self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList),
						('self.',self,['PyplotingShapeVariable','PyplotingShiftIntsTuple'])
					]
				)
			'''

			#get
			PreviousChartPyploter=self.ParentDeriveTeamerVariable.ManagementDict.getValue(
				self.ManagementIndexInt-1
			)

			#debug
			'''
			self.debug(
				[
					'We have getted the PreviousChartPyploter',
					'PreviousChartPyploter is ',
					SYS._str(PreviousChartPyploter)
				]
			)
			'''
			
			#shift
			if self.PyplotingShiftIntsTuple[0]>0:
				self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList[0
				]+=self.PyplotingShiftIntsTuple[0]+PreviousChartPyploter.PyplotingShapeVariable[0]
			if self.PyplotingShiftIntsTuple[1]>0:
				self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList[1
				]+=self.PyplotingShiftIntsTuple[1]+PreviousChartPyploter.PyplotingShapeVariable[1]

			#debug
			'''
			self.debug(
					[
						'Ok we have shifted',
						'now we link with the fig',
						('self.PyplotedParentPanelDerivePyploterVariable.',self.PyplotedParentPanelDerivePyploterVariable,
							['PyplotedCursorIntsList']),
					]
				)
			'''

		#set
		if self.PyplotedParentPanelDerivePyploterVariable!=None:
			self.PyplotedAnchorIntsList=copy.copy(
				self.PyplotedParentPanelDerivePyploterVariable.PyplotedCursorIntsList
			)

		#/#################/#
		# Check if the size is going to be correct
		#

		#init
		from matplotlib import pyplot

		#debug
		'''
		self.debug(
				[
					'Ok we set an axes here',
					'self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple is ',
					str(self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple),
					('self.',self,[
							'PyplotedAnchorIntsList',
							'PyplotingShapeVariable'
						])
				]
			)
		'''
		
		#Check
		if self.PyplotingShapeVariable==None:
			self.PyplotingShapeVariable=(5,5)

		#init
		PyplotedResetBool=False

		#Check
		if self.PyplotedAnchorIntsList[0] > self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple[0]:

			#tuple
			self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple=(
				self.PyplotedAnchorIntsList[0]+self.PyplotingShapeVariable[0],
				self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple[1]
			)

			#set
			PyplotedResetBool=True

		elif self.PyplotedAnchorIntsList[1] > self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple[1]:

			#tuple
			self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple=(
				self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple[0],
				self.PyplotedAnchorIntsList[1]+self.PyplotingShapeVariable[1],
			)

			#set
			PyplotedResetBool=True 
		
		#Check
		if PyplotedResetBool:

			#debug
			'''
			self.debug(
				[
					'We reset the figure here because the size of the axes is too big'
				]
			)
			'''

		'''
			#list
			PyplotedOldAxesList=self.PyplotedParentFigureDerivePyploterVariable.PyplotedFigureVariable._axstack.as_list()

			#temp
			PyplotedOldFigure=self.PyplotedParentFigureDerivePyploterVariable.PyplotedFigureVariable

			#reinit figure
			self.PyplotedParentFigureDerivePyploterVariable.PyplotedFigureVariable=pyplot.figure()

			#reinit axes with the new grids
			PyplotedNewAxesList=map(
				lambda __PyplotedOldAxes:
				pyplot.subplot2grid(
					self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple, 
					__PyplotedOldAxes.ParentPyploter.PyplotedAnchorIntsList, 
					rowspan=__PyplotedOldAxes.ParentPyploter.PyplotingShapeVariable[0],
					colspan=__PyplotedOldAxes.ParentPyploter.PyplotingShapeVariable[1]
				),
				PyplotedOldAxesList
			)

			#map set_figure
			map(
				lambda __PyplotedNewAxes:
				setattr(
					__PyplotedNewAxes,
					'_figure',
					self.PyplotedParentFigureDerivePyploterVariable.PyplotedFigureVariable
				),
				PyplotedNewAxesList
			)
			
			#map set_axes
			"""
			map(
				lambda __PyplotedNewAxes,__PyplotedOldAxes:
				__PyplotedNewAxes.set_axes(
					__PyplotedOldAxes
				),
				PyplotedNewAxesList,
				PyplotedOldAxesList
			)
			"""

			#map
			map(
				lambda __PyplotedNewAxes,__PyplotedOldAxes:
				setattr(
					__PyplotedNewAxes,
					'ParentPyploter',
					__PyplotedOldAxes.ParentPyploter
				),
				PyplotedNewAxesList,
				PyplotedOldAxesList
			)

			#map
			map(
				lambda __PyplotedNewAxes,__PyplotedOldAxes:
				setattr(
					__PyplotedNewAxes,
					'ParentPyploter',
					__PyplotedOldAxes.ParentPyploter
				),
				PyplotedNewAxesList,
				PyplotedOldAxesList
			)

			#close the old one
			pyplot.close(PyplotedOldFigure)

			#setDoing
			self.setDoing([SYS.PyploterClass])
			map(
				lambda __PyplotedNewAxes:
				__PyplotedNewAxes.ParentPyploter.setDoing(
					[SYS.PyploterClass]
				),
				PyplotedNewAxesList
			)

			#review and re pyplot 
			self.PyplotedParentFigureDerivePyploterVariable.view(
				).pyplot(
				)

			#return
			return self
		'''

		#/#################/#
		# init
		#

		#subplot2grid
		self.PyplotedAxesVariable=pyplot.subplot2grid(
				self.PyplotedParentFigureDerivePyploterVariable.PyplotingGridIntsTuple, 
				self.PyplotedAnchorIntsList, 
				rowspan=self.PyplotingShapeVariable[0],
				colspan=self.PyplotingShapeVariable[1]
			)

		#give a pointer back
		self.PyplotedAxesVariable.ParentPyploter=self

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
		self.PyplotedAxesVariable._figure=self.PyplotedParentFigureDerivePyploterVariable.PyplotedFigureVariable
		

		#debug
		'''
		self.debug(
				[
					'Ok we have setted the axe'
				]
			)
		'''

	def pyplotDraw(self):

		#/#################/#
		# Check
		#

		#Check
		if self.PyplotingDrawVariable!=None:

			#copy
			self.PyplotedDrawTuplesList+=copy.copy(
				self.PyplotingDrawVariable.items()
				if hasattr(self.PyplotingDrawVariable,'items')
				else self.PyplotingDrawVariable
			)

		#/#################/#
		# We mapArgument draw in the parent axes
		#

		#debug
		'''
		self.debug(
			[
				'We map argument draw in the parent axe',
				('self.',self,[
					'PyplotingDrawVariable',
					#'PyplotedParentFigureDerivePyploterVariable'
				]),
				#'self.PyplotedParentChartDerivePyploterVariable.PyplotedAxesVariable is ',
				#str(self.PyplotedParentChartDerivePyploterVariable.PyplotedAxesVariable)
			]
		)
		'''
		
		#map argument
		self.PyplotedLinesList.extend(
			self.PyplotedParentFigureDerivePyploterVariable.mapArgument(
				self.PyplotedParentChartDerivePyploterVariable.PyplotedAxesVariable,
				self.PyplotedDrawTuplesList
			)
		)

		#debug
		'''
		self.debug(
			[
				'Ok now look if we have to set the axes',
				'self.ManagementIndexInt==(len(self.ParentDeriveTeamerVariable.ManagementDict)-1) is ',
				str(self.ManagementIndexInt==(len(self.ParentDeriveTeamerVariable.ManagementDict)-1))
			]
		)
		'''
		
		#/###################/#
		# If it is the last then trigger the axes to set also
		#

		#debug
		'''
		self.debug(
			[
				'Check if we have to make trigger the parent Chart',
				'self.ParentDeriveTeamerVariable!=None is ',
				str(self.ParentDeriveTeamerVariable!=None)
			]
		)
		'''

		#Check
		if self.ParentDeriveTeamerVariable!=None:

			#Check
			if self.ManagementIndexInt==(
				len(self.ParentDeriveTeamerVariable.ManagementDict)-1
			):

				#debug
				'''
				self.debug(
					[
						'I am the last draw of this axes !',
						'Lets the axes setting itself now',
						('self.PyplotedParentChartDerivePyploterVariable.',
							self.PyplotedParentChartDerivePyploterVariable,
							[
								'PyplotingDrawVariable',
								'PyplotedChartTuplesList'
							])
					]
				)	
				'''
				
				#Check
				if len(
					self.PyplotedParentChartDerivePyploterVariable.PyplotedChartTuplesList
					)>0:

					#/#################/#
					# We map argument in the axes
					#

					#debug
					'''
					self.debug(
						[
							'We chart in the parent axe',
							#('self.',self,[
							#	'PyplotedParentChartDerivePyploterVariable'
							#]),
							'self.PyplotedParentChartDerivePyploterVariable.PyplotedChartTuplesList is ',
							SYS._str(self.PyplotedParentChartDerivePyploterVariable.PyplotedChartTuplesList)
						]
					)
					'''

					#map argument
					self.PyplotedParentFigureDerivePyploterVariable.mapArgument(
						self.PyplotedParentChartDerivePyploterVariable.PyplotedAxesVariable,
						self.PyplotedParentChartDerivePyploterVariable.PyplotedChartTuplesList
					)
					
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
							#'PyplotedParentFigureDerivePyploterVariable',
							'SettingValueVariable'
						])
					]
				)
			'''

			#init
			PyplotPlotArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.PyplotedParentFigureDerivePyploterVariable
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
							#'PyplotedParentFigureDerivePyploterVariable',
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
								self.PyplotedParentFigureDerivePyploterVariable
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
						('self.',self,['PyplotedParentFigureDerivePyploterVariable'])
					]
				)
			'''

			#init
			PyplotPluginArgumentDict=Setter.ArgumentDict(
					self.SettingValueVariable,
					self.PyplotedParentFigureDerivePyploterVariable
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
				#we set a Chart

		#call the base method
		BaseClass.set(self)

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


	def show(self):

		#import
		from matplotlib import pyplot

		#show
		pyplot.show()

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Remove the brian objects that are non setted
			#

			#map
			map(
					lambda __KeyStr:
					self.forcePrint(
						[__KeyStr],
						'PyploterClass'
					)
					if getattr(self.PrintingCopyVariable,__KeyStr)!=None
					else None,
					[
						'PyplotedFigureVariable',
						'PyplotedAxesVariable'
					]
				)


			#Debug
			'''
			print('self.__class__ is ')
			print(self.__class__)
			print('self.PyplotingPrintBool')
			print(self.__class__.PyplotingPrintBool)
			print('self.__class__.PyplotingPrintBool')
			print(self.__class__.PyplotingPrintBool)
			print('')
			'''

			#/##################/#
			# Maybe just give a pointer repr of the children
			# pyplot objects

			#Check
			if self.__class__.PyplotingPrintBool==False or self.PyplotingPrintBool==False:

				#Debug
				'''
				print('We remove the pyplot teams')
				print('self.TeamDict.keys() is ')
				print(self.TeamDict.keys())
				print('self.PrintingCopyVariable.TeamDict.keys() is ')
				print(self.PrintingCopyVariable.TeamDict.keys())
				print('')
				'''

				#map
				map(
					lambda __TeamStr:
					self.PrintingCopyVariable.TeamDict.__setitem__(
						__TeamStr,
						Printer.getPointerStr(
							self.TeamDict[
								__TeamStr
							]
						)
					) if __TeamStr in self.TeamDict
					else None,
					['Draws','Charts','Panels']
				)

				#Debug
				'''
				print('We remove the pyplot teams')
				print('self.TeamDict.keys() is ')
				print(self.TeamDict.keys())
				print('')
				'''

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#</DefinePrint>
PyploterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PyplotTooltipVariablesList',
		'PyplotingGridIntsTuple',
		'PyplotingShapeVariable',
		'PyplotingFigureVariable',
		'PyplotingDrawVariable',
		'PyplotingChartVariable',
		'PyplotingShiftIntsTuple',
		'PyplotingPrintBool',
		'PyplotedTeamTagStr',
		'PyplotedParentFigureDerivePyploterVariable',
		'PyplotedParentPanelDerivePyploterVariable',
		'PyplotedParentChartDerivePyploterVariable',
		'PyplotedFigureVariable',
		'PyplotedAxesVariable',
		'PyplotedLinesList',
		'PyplotedAnchorIntsList',
		'PyplotedShiftTuplesList',
		'PyplotedPanelShapeIntsList',
		'PyplotedCursorIntsList',
		'PyplotedChartTuplesList',
		'PyplotedDrawTuplesList',
		'PyplotedParentSingularStr'
	]
)
#<DefinePrint>

