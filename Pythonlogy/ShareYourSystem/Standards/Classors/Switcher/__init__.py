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
			_DoMethodVariable=None,
			_DoerClassVariable=None,
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
	
	#/#################/#
	# Adapt the shape of the do method str to switch
	#

	#Check
	if type(_DoMethodVariable)!=list:

		#Check
		if _DoMethodVariable==None:

			#/#################/#
			# Give all the do method str
			#

			#alias
			DoStrsList=_InstanceVariable.DoMethodStrsList

		else:
		
			#listify
			DoMethodStrsList=[_DoMethodVariable]


	else:

		#just alias
		DoMethodStrsList=_DoMethodVariable

	#/#################/#
	# Adapt the shape of the mro doer to switch
	#

	#Check
	DoerClassesList=SYS.GetList(_DoerClassVariable)
	if _DoerClassVariable==None:

		#/#################/#
		# by default this is all the mro doer that have all the do method
		#

		DoerClassesList=SYS._filter(
			lambda __MroDoerClass:
			all(
				map(
					lambda __DoMethodStr:
					hasattr(__MroDoerClass,__DoMethodStr),
					DoMethodStrsList
				)
			),
			_InstanceVariable.__class__.MroDoerClassesList
		)

	#/#################/#
	# Adapt the shape of the hook strs
	#

	#Check
	if type(_HookVariable)!=list:
		if _HookVariable==None:
			HookStrsList=['Before','After']
		else:
			HookStrsList=[_HookVariable]
	else:
		HookStrsList=_HookVariable


	#/#################/#
	# Now map the switch
	#

	#Debug
	print('l 92 Switcher')
	print('DoMethodStrsList is')
	print(DoMethodStrsList)
	print('DoerClassesList is ')
	print(DoerClassesList)
	print('HookStrsList is ')
	print(HookStrsList)
	print('')

	#map
	map(
		lambda __HookStr:
		map(
			lambda __DoerClass:
			map(
					lambda __DoMethodStr:
					_InstanceVariable.__setattr__(
						'Watch'+__HookStr+__DoMethodStr[0].upper(
							)+__DoMethodStr[1:]+'With'+__DoerClass.NameStr+'Bool',
						False
					),
					DoMethodStrsList,
				),
			DoerClassesList
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

