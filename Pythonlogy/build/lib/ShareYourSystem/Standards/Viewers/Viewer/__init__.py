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
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Numscipyer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo("Viewer","View","Viewing","Viewed")
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Controllers import Controller
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	def default_init(self, 
						_ViewDeriveControllerVariable=None,
						_ViewFirstDeriveViewerVariable=None,
						_ViewingXVariable=None,
						_ViewingYVariable=None,
						_ViewingIdStr="",
						_ViewingXScaleFloat=1.,
						_ViewingYScaleFloat=1.,
						_ViewingXLabelStr="",
						_ViewingYLabelStr="",
						_ViewedTagStr="",
						_ViewedXTagStr="",
						_ViewedYTagStr="",
						_ViewedHtmlStr="",
						_ViewedLegendLabelStr="",
						_ViewedXLabelStr="",
						_ViewedYLabelStr="",
						_ViewedXlimMinStrsList=None,
						_ViewedXlimMaxStrsList=None,
						_ViewedYlimMinStrsList=None,
						_ViewedYlimMaxStrsList=None,
						_ViewedXlimLiargStr="",
						_ViewedYlimLiargStr="",
						_ViewedXtickLiargStr="",
						_ViewedYtickLiargStr="",
						_ViewedXtickLabelLiargStr="",
						_ViewedYtickLabelLiargStr="",
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.ViewDeriveControllerVariable=self

	def do_view(self):

		#debug
		'''
		self.debug(
				[
					'We view here',
					('self.',self,[
						'ViewingQtBool'
					])
				]
			)
		'''

		#Check
		if self.ViewingIdStr=="":
			self.ViewingIdStr=str(self.PrintIdInt)

		#debug
		'''
		self.debug(
			[
				"id(self) is ",
				str(id(self)),
				('self.',self,['ViewingIdStr']),
				'SYS.IdDict["+self.ViewingIdStr+"]',
				SYS._str(SYS.IdDict[int(self.ViewingIdStr)]),
				#SYS._str(SYS.IdDict[id(self)]),
				('self.',self,[
					'ViewingXVariable',
					'ViewingYVariable'
				])
			]
		)
		'''

		#set
		self.ViewedTagStr=self.StructureTagStr.replace('*','')

		#/####################/#
		# Now we view each Axe
		#

		#map
		map(
			lambda __AxeStr:
			self.viewAxe(__AxeStr),
			[
				'X',
				'Y'
			]
		)

	def viewAxe(self,_AxeStr):

		#/##################/#
		# Set a certain axis
		#

		#set
		ViewedTagStr=self.ViewedTagStr+_AxeStr

		#set
		setattr(
			self,
			'Viewed'+_AxeStr+'TagStr',
			ViewedTagStr
		)

		#get
		LimMinStrsList=getattr(
			self,
			'Viewed'+_AxeStr+'limMinStrsList'
		)
		if LimMinStrsList==None:
			LimMinStrsList=[]

		LimMinStrsList.append(
			"SYS.IdDict["+self.ViewingIdStr+"].Viewing"+_AxeStr+"Variable.min()"
		)

		#get 
		LimMaxStrsList=getattr(
			self,
			'Viewed'+_AxeStr+'limMaxStrsList'
		)
		if LimMaxStrsList==None:
			LimMaxStrsList=[]
		LimMaxStrsList.append(
			"SYS.IdDict["+self.ViewingIdStr+"].Viewing"+_AxeStr+"Variable.max()"
		)

		#set
		setattr(
			self,
			'Viewed'+_AxeStr+'limLiargStr',
			"".join([
				">>SYS.set(SYS,'"+ViewedTagStr+"LimFloatsArray',",
				"[",
				#"SYS.IdDict["+self.ViewingIdStr+"].Viewing"+_AxeStr+"Variable.min()",
				"min("+",".join(LimMinStrsList)+")"
				if len(LimMinStrsList)>1
				else LimMinStrsList[0],
				",",
				#"SYS.IdDict["+self.ViewingIdStr+"].Viewing"+_AxeStr+"Variable.max()]",
				"max("+",".join(LimMaxStrsList)+")"
				if len(LimMaxStrsList)>1
				else LimMaxStrsList[0],
				']).'+ViewedTagStr+"LimFloatsArray"
			])
		)

		#join
		setattr(
			self,
			'Viewed'+_AxeStr+'tickLiargStr',
			"".join([
						">>SYS.set(SYS,'"+ViewedTagStr+"TickFloatsArray',",
						"map(lambda __Float:float(SYS.getFloatStr(__Float)),",
						"SYS.getTickFloatsArray(",
						'SYS.'+ViewedTagStr+"LimFloatsArray,3",
						")))."+ViewedTagStr+"TickFloatsArray"
						])
		)

		#debug
		self.debug(
			[
				'Scale the tick labels',
				('self.',self,[
						"Viewing"+_AxeStr+"ScaleFloat"
					])
			]
		)

		#set
		setattr(
			self,
			'Viewed'+_AxeStr+'tickLabelLiargStr',
			"".join([
						">>SYS.set(SYS,'"+ViewedTagStr+"TickStrsArray',",
						"map(lambda __Float:'$'+SYS.getFloatStr(SYS.IdDict["+self.ViewingIdStr+"].Viewing"+_AxeStr+"ScaleFloat*__Float)+'$',",
						#"map(lambda __Float:'$'+str(self.Viewing"+_AxeStr+"ScaleFloat*__Float)+'$',",
						"SYS."+ViewedTagStr+"TickFloatsArray))."+ViewedTagStr+"TickStrsArray"
						])
		)

		#debug
		'''
		self.debug(
			[
				'In the end of the set of the x axis',
				(
					'self.',self,[
						'ViewedLegendLabelStr',
						'Viewed'+_AxeStr+'LabelStr',
						'Viewed'+_AxeStr+'limLiargTagStr',
						'Viewed'+_AxeStr+'tickLiargStr',
						'Viewed'+_AxeStr+'tickLabelLiargStr'
					]
				)
			]
		)
		'''

	def getLabelStr(self,_VariableStr):

		#Check
		if '_' in _VariableStr:
			ViewedWordStrsList=_VariableStr.split('_')
			return ViewedWordStrsList[0]+'_{'+",".join(ViewedWordStrsList[1:])+'}'
		else:
			return _VariableStr

#</DefineClass>

#<DefineLocals>
Controller.ViewsClass.ManagingValueClass=ViewerClass
#<DefineLocals>

#</DefinePrint>
ViewerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ViewDeriveControllerVariable',
		'ViewFirstDeriveViewerVariable',
		'ViewingXVariable',
		'ViewingYVariable',
		'ViewingIdStr',
		'ViewingXScaleFloat',
		'ViewingYScaleFloat',
		'ViewingXLabelStr',
		'ViewingYLabelStr',
		'ViewedTagStr',
		'ViewedXTagStr',
		'ViewedYTagStr',
		'ViewedHtmlStr',
		'ViewedLegendLabelStr',
		'ViewedXLabelStr',
		'ViewedYLabelStr',
		'ViewedXlimMinStrsList',
		'ViewedXlimMaxStrsList',
		'ViewedYlimMinStrsList',
		'ViewedYlimMaxStrsList',
		'ViewedXlimLiargStr',
		'ViewedYlimLiargStr',
		'ViewedXtickLiargStr',
		'ViewedYtickLiargStr',
		'ViewedXtickLabelLiargStr',
		'ViewedYtickLabelLiargStr'
	]
)
#<DefinePrint>
