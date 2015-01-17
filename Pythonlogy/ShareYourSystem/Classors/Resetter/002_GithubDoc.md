
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Resetter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Watcher"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
from ShareYourSystem.Classors import Doer,Observer
#</ImportSpecificModules>

#<DefineFunctions>
def getResetBool(_InstanceVariable,**_KwargVariablesDict):

	#get and return
	return getattr(_InstanceVariable,'_'+_KwargVariablesDict['ResetDoBoolKeyStr'])

def setResetBool(_InstanceVariable,_ValueVariable,**_KwargVariablesDict):

	#Debug
	'''
	print('l 37 Resetter')
	print('We are in the setResetBool')
	print('_KwargVariablesDict is ')
	print(_KwargVariablesDict)
	print('')
	'''
	
	#Alias
	HideResetDoBoolKeyStr='_'+_KwargVariablesDict['ResetDoBoolKeyStr']

	#Check
	if hasattr(
			_InstanceVariable,
			HideResetDoBoolKeyStr
			)==False:
		_InstanceVariable.__setattr__(HideResetDoBoolKeyStr,False)

	#get
	ResetDoBool=getattr(
			_InstanceVariable,
			_KwargVariablesDict['ResetDoBoolKeyStr']
			)

	#Debug
	'''
	print('l 58 Resetter')
	print("_KwargVariablesDict['ResetDoBoolKeyStr'] is ",_KwargVariablesDict['ResetDoBoolKeyStr'])
	print('ResetDoBool is ',ResetDoBool)
	print('')
	'''

	#check
	if ResetDoBool==True and _ValueVariable==False:

		#Debug
		'''
		print('l 69 Resetter')
		print('Yes we reset')
		print('')
		'''

		#map
		map(
				lambda __DefaultSetTuple:
				_InstanceVariable.__setattr__(
						__DefaultSetTuple[0],
						__DefaultSetTuple[1]
				),
				#self.DoClass.DefaultAttributeItemTuplesList
				getattr(
					SYS,
					_KwargVariablesDict['BindDoClassStr']
				).DoneAttributeVariablesOrderedDict.items()
			)

	#set
	_InstanceVariable.__setattr__(
		HideResetDoBoolKeyStr,
		_ValueVariable
		)

def delResetBool(_InstanceVariable,**_KwargVariablesDict):

	#delete
	_InstanceVariable.__delattr__('_'+_KwargVariablesDict['ResetDoBoolKeyStr'])
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class ResetterClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[ 				
	]

	def default_init(self,					
						**_KwargVariablesDict
				):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent method
		Observer.ObserverClass.__bases__[0].__call__(self,_Class)

		#reset
		self.reset()

		#Return
		return _Class

	def do_reset(self):

		#watch first
		self.watch(True,**{'ObservingWrapMethodStr':self.DoClass.DoMethodStr})

		#set to the class
		"""
		self.DoClass.ResetDoBoolKeyStr='Reset'+'Watch'.join(
			self.WatchedDoBoolKeyStr.split('Watch')[1:])
		"""
		self.DoClass.ResetDoBoolKeyStr=self.WatchedDoBoolKeyStr

		#Debug
		'''
		print('Resetter l 125')
		print('self.WatchedDoBoolKeyStr is ',self.WatchedDoBoolKeyStr)
		print('self.DoClass.ResetDoBoolKeyStr is ',self.DoClass.ResetDoBoolKeyStr)
		print('Now we bind')
		'''
		
		#map binds
		ResettedBindDecorationUnboundMethodsList=map(
				lambda __Function:
				self.bind(
							True,
							__Function,
							"",
							__Function.__name__+'With'+self.DoClass.NameStr,
							[('ResetDoBoolKeyStr',self.DoClass.ResetDoBoolKeyStr)],
							**{'ObservingWrapMethodStr':""}
					).BindedDecorationUnboundMethod,
				[getResetBool,setResetBool,delResetBool]
			)

		#Set
		setattr(
					self.DoClass,
					self.DoClass.ResetDoBoolKeyStr,
					property(
						*ResettedBindDecorationUnboundMethodsList
					)
				)

		#Add to the KeyStrsList
		self.DoClass.KeyStrsList+=[
									self.DoClass.ResetDoBoolKeyStr,
									'ResetDoBoolKeyStr'
								]
#</DefineClass>


```

<small>
View the Resetter sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Classors/Resetter" target="_blank">Github</a>
</small>

