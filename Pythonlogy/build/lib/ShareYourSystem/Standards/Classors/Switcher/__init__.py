# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Switcher

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Watcher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
from ShareYourSystem.Standards.Classors import Doer,Observer
#</ImportSpecificModules>

#<DefineFunctions>
def setSwitch(
			_InstanceVariable,
			_DoerVariable=None,
			_DoVariable=None,
			_HookVariable=None
		):

	#Debug
	'''
	print('l 31 setSwitch')
	print('_DoerVariable is ',_DoerVariable)
	print('_DoVariable is ',_DoVariable)
	print('_HookVariable is ',_HookVariable)
	#print('_InstanceVariable.__class__.NameStr is ',_InstanceVariable.__class__.NameStr)
	print('')
	'''
	
	#Adapt the shape
	if type(_DoerVariable)!=list:
		if _DoerVariable==None:
			_DoerVariable=_InstanceVariable.__class__
		DoerClassVariablesList=[_DoerVariable]
	else:
		DoerClassVariablesList=_DoerVariable
	if type(_DoVariable)!=list:
		if _DoVariable==None:
			_DoVariable=_InstanceVariable.DoStr
		DoStrsList=[_DoVariable]
	else:
		DoStrsList=_DoVariable
	if type(_HookVariable)!=list:
		if _HookVariable==None:
			HookStrsList=['Before','After']
		else:
			HookStrsList=[_HookVariable]
	else:
		HookStrsList=_HookVariable

	#get
	SwitchClassesList=map(
		lambda __DoerVariable:
		_InstanceVariable.getClass(__DoerVariable),
		DoerClassVariablesList
	)

	#Debug
	'''
	print('l 51 Switcher')
	print('SwitchClassesList is ')
	print(SwitchClassesList)
	print('')
	'''

	#map
	map(
		lambda __HookStr:
		map(
			lambda __SwitchClass:
			map(
					lambda __MethodStr:
					_InstanceVariable.__setattr__(
						'Watch'+__HookStr+__MethodStr[0].upper()+__MethodStr[1:]+'With'+__SwitchClass.NameStr+'Bool',
						False
					),
					DoStrsList,
				),
			SwitchClassesList
			),
		HookStrsList
		)

	#return 
	return _InstanceVariable
	
def switch(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

	#Debug
	'''
	print('l 51')
	print('In the switch function ')
	print('_KwargVariablesDict is ')
	print(_KwargVariablesDict)
	print('')
	'''
	
	"""
	#alias
	FuncDict=switch.__dict__

	#Debug
	'''
	print('l 52')
	print('In the switch function ')
	print('FuncDict is ')
	print(FuncDict)
	print('')
	'''
	"""

	#Check
	if hasattr(_InstanceVariable,_KwargVariablesDict['WatchBeforeDoBoolKeyStr']):

		#get
		WatchDoBool=getattr(
				_InstanceVariable,
				_KwargVariablesDict['WatchBeforeDoBoolKeyStr']
				)

		#Switch
		if WatchDoBool:
			return _InstanceVariable
	
	#get the wrapped method
	WrapUnboundMethod=getattr(
		getattr(
			SYS,
			_KwargVariablesDict['BindDoClassStr']
		),
		_KwargVariablesDict['BindObserveWrapMethodStr']
	)

	#del
	map(
			lambda __KeyStr:
			_KwargVariablesDict.__delitem__(__KeyStr),
			[
				'BindObserveWrapMethodStr',
				'BindDoClassStr',
				'WatchBeforeDoBoolKeyStr'
			]
		)

	#Call
	return WrapUnboundMethod(
		_InstanceVariable,
		*_LiargVariablesList,
		**_KwargVariablesDict
	)
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class SwitcherClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[ 
		'SwitchingIsBool',
		'SwitchingWrapMethodStr'				
	]

	def default_init(self,
						_SwitchingIsBool=False,
						_SwitchingWrapMethodStr="",					
						**_KwargVariablesDict
				):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent method
		Observer.ObserverClass.__bases__[0].__call__(self,_Class)

		#reset
		self.switch()

		#Return
		return _Class

	def do_switch(self):

		#Check
		if self.SwitchingIsBool:

			#Debug
			'''
			print('l 195 Switcher')
			print('self.SwitchingWrapMethodStr is '+self.SwitchingWrapMethodStr)
			print('')
			'''

			#watch first
			self.watch(
						True,
						**{'ObservingWrapMethodStr':self.SwitchingWrapMethodStr}
					)

			#Debug
			'''
			print('l 204 Switcher')
			print('self.WatchedDecorationMethodStr is ',self.WatchedDecorationMethodStr)
			print('')
			'''
			
			#first bind
			self.bind(
						True,
						switch,
						"",
						switch.__name__,
						[('WatchBeforeDoBoolKeyStr',self.WatchedBeforeDoBoolKeyStr)],
						**{'ObservingWrapMethodStr':self.WatchedDecorationMethodStr}
					)

			#Define
			SwitchedDecorationUnboundMethod=getattr(
						self.DoClass,
						self.BindedDecorationMethodStr
					)

			#Now make the amalgam
			setattr(
					self.DoClass,
					self.SwitchingWrapMethodStr,
					SwitchedDecorationUnboundMethod
				)
			
			#Check
			if hasattr(self.DoClass,'setSwitch')==False:

				#set
				setattr(
						self.DoClass,
						setSwitch.__name__,
						setSwitch
					)

				#get the unbound
				setSwitchUnboundMethod=getattr(
					self.DoClass,
					setSwitch.__name__
				)

				#add in the inspect
				self.DoClass.InspectedMethodDict[setSwitch.__name__]=setSwitchUnboundMethod
				self.DoClass.InspectedArgumentDict[setSwitch.__name__]=SYS.ArgumentDict(
							setSwitchUnboundMethod
						)

#</DefineClass>

