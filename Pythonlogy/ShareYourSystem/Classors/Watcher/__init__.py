# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Watcher 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Binder"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
import copy
from ShareYourSystem.Classors import Doer,Observer,Representer
Binder=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
WatchingPrefixKeyStr="Watch"
#</DefineLocals>

#<SetRepresent>
def getIsBoolWithItemTupleAndPrefixStr(_ItemTuple,_PrefixStr):

	#Debug
	'''
	print('Watcher l 35')
	print('_ItemTuple is ',_ItemTuple)
	print('_PrefixStr is ',_PrefixStr)
	print('')
	'''
	
	#Return
	return _ItemTuple[0].split('>')[-1].startswith(_PrefixStr)
OldRepresentFunction=copy.copy(Representer.represent)
def represent(_Variable,**_KwargVariablesDict):
	return OldRepresentFunction(
		_Variable,
		**dict(
			_KwargVariablesDict,
			**{
				'RepresentingNotConcludeTuplesList':
				[
					(getIsBoolWithItemTupleAndPrefixStr,'_Watch'),
					(getIsBoolWithItemTupleAndPrefixStr,'Watch')
				]
			}
		)
	)
represent.__name__="Watcher@represent"
Representer.represent=represent
#</SetRepresent>

#<DefineFunctions>
def watch(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

	#Debug
	'''
	print('l 67')
	print('In the watch function ')
	print('_KwargVariablesDict is ')
	print(_KwargVariablesDict)
	print('')
	'''

	"""
	#alias
	FuncDict=_InstanceVariable.__class__.watch.__dict__

	#Debug
	'''
	print('l 79')
	print('In the watch function ')
	print('FuncDict is ')
	print(FuncDict)
	print('')
	'''
	"""
	
	#Set in the _InstanceVariable
	_InstanceVariable.__setattr__(
			_KwargVariablesDict['WatchDoBoolKeyStr'],
			True
		)

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
			['BindObserveWrapMethodStr','BindDoClassStr','WatchDoBoolKeyStr']
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
class WatcherClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[	
		'WatchingIsBool',	
		'WatchedDoBoolKeyStr',
		'WatchedDecorationMethodStr'
	]

	def default_init(self,		
						_WatchingIsBool=False,
						_WatchedDoBoolKeyStr="",
						_WatchedDecorationMethodStr="",
						**_KwargVariablesDict
				):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent method
		Observer.ObserverClass.__bases__[0].__call__(self,_Class)

		#Watch
		self.watch()

		#Return
		return _Class

	def do_watch(self):

		#Check
		if self.WatchingIsBool:

			#Debug
			'''
			print('l 133 Watcher')
			print('self.ObservingWrapMethodStr is '+self.ObservingWrapMethodStr)
			print('')
			'''

			#Keep the old value
			self.WatchedWrapMethodStr=self.ObservingWrapMethodStr

			#observe first
			self.observe(
							True
						)

			#Debug
			'''
			print('l 171 Watcher')
			print('self.ObservedWrapMethodStr is ',self.ObservedWrapMethodStr)
			'''
			
			#Check
			if self.ObservedWrapMethodStr.startswith(
				watch.__name__+Binder.BindingDecorationSuffixStr
			)==False:

				#Debug
				'''
				print('l 173 this is a new watch method')
				print('')
				'''

				#Define
				WatchedDoMethodStr=self.WatchedWrapMethodStr
				WatchedDoStr=WatchedDoMethodStr[0].upper()+WatchedDoMethodStr[1:]
				self.WatchedDoBoolKeyStr=WatchingPrefixKeyStr+WatchedDoStr
				self.WatchedDoBoolKeyStr+='With'+self.DoClass.NameStr
				self.WatchedDoBoolKeyStr+='Bool'

				WatchedIsInitBool=True
				if hasattr(self.DoClass,'ResetDoBoolKeyStr'):
					if self.WatchedDoBoolKeyStr!=self.DoClass.ResetDoBoolKeyStr:
						WatchedIsInitBool=False
				if WatchedIsInitBool:
					#WARNING this cancels the reset property binding before
					#Set already in the class
					setattr(
							self.DoClass,
							self.WatchedDoBoolKeyStr,
							False
						)

				#Debug
				'''
				print('l 145 Watcher')
				print('WatchedDoMethodStr is ',WatchedDoMethodStr)
				print('WatchedDoStr is ',WatchedDoStr)
				print('self.WatchedDoBoolKeyStr is ',self.WatchedDoBoolKeyStr)
				print('')
				'''

				#first bind
				self.bind(
							True,
							watch,
							"",
							watch.__name__,
							[('WatchDoBoolKeyStr',self.WatchedDoBoolKeyStr)],
							**{'ObservingWrapMethodStr':self.ObservedWrapMethodStr}
						)

				#set
				self.WatchedDecorationMethodStr=self.BindedDecorationMethodStr

				#Now make the amalgam
				setattr(
						self.DoClass,
						WatchedDoMethodStr,
						self.BindedDecorationUnboundMethod
					)

			else:

				#set
				self.WatchedDecorationMethodStr=self.ObservedWrapMethodStr

#</DefineClass>
