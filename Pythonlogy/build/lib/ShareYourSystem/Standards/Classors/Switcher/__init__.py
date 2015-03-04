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
import copy
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
			#DoMethodStrsList=_InstanceVariable.DoMethodStrsList

			#/#################/#
			# Give just the last DoMethodStr
			#

			#Check
			if _InstanceVariable.__class__.DoMethodStr in _InstanceVariable.__class__.SwitchedMethodDict:
			
				#listify
				DoMethodStrsList=[_InstanceVariable.__class__.DoMethodStr]

			else:

				#listify
				DoMethodStrsList=[]

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
		# by default this is all the mro doer that have all the switch do method
		# so do the intersection

		#Check
		if len(DoMethodStrsList)>0:

			#intersection
			DoerClassesList=list(
				set.intersection(*
					map(
						lambda __DoMethodStr:
						set(_InstanceVariable.__class__.SwitchedMethodDict[__DoMethodStr]),
						DoMethodStrsList
					)
				)
			)

		else:

			#init
			DoerClassesList=[]

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
	'''
	print('l 139 Switcher')
	print('DoMethodStrsList is')
	print(DoMethodStrsList)
	print('DoerClassesList is ')
	print(DoerClassesList)
	print('HookStrsList is ')
	print(HookStrsList)
	print('')
	'''
	
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

			#alias
			SwitchedClass=self.DoClass

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
						SwitchedClass,
						self.BindedDecorationMethodStr
					)

			#Now make the amalgam
			setattr(
					SwitchedClass,
					self.SwitchingWrapMethodStr,
					SwitchedDecorationUnboundMethod
				)
			
			#Check
			if hasattr(self.DoClass,'setSwitch')==False:

				#set
				setattr(
						SwitchedClass,
						setSwitch.__name__,
						setSwitch
					)

				#get the unbound
				setSwitchUnboundMethod=getattr(
					SwitchedClass,
					setSwitch.__name__
				)

				#add in the inspect
				SwitchedClass.InspectedMethodDict[setSwitch.__name__]=setSwitchUnboundMethod
				SwitchedClass.InspectedArgumentDict[setSwitch.__name__]=SYS.ArgumentDict(
					setSwitchUnboundMethod
				)

			#Check
			if hasattr(SwitchedClass,'SwitchedMethodDict')==False:

				#init
				SwitchedClass.SwitchedMethodDict={
					self.SwitchingWrapMethodStr:[self.DoClass]
				}

			else:

				#copy
				SwitchedClass.SwitchedMethodDict=copy.copy(
					self.DoClass.__bases__[0].SwitchedMethodDict
				)

				#update
				if setSwitch.__name__ in self.DoClass.SwitchedMethodDict:
					SwitchedClass.SwitchedMethodDict[
						self.SwitchingWrapMethodStr
					].append(SwitchedClass)
				else:
					self.DoClass.SwitchedMethodDict[
						self.SwitchingWrapMethodStr
					]=[SwitchedClass]

			#Add to the KeyStrsList
			SwitchedClass.KeyStrsList+=[
									'SwitchedMethodDict'
								]



#</DefineClass>

