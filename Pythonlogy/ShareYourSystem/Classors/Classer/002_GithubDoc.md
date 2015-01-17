
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


The Classer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Mimicker"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Mimicker=BaseModule
#</ImportSpecificModules>

#<Define_Class>
@DecorationClass()
class ClasserClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
						'ClassingSwitchMethodStrsList'
					]

	def default_init(self,	
						_ClassingSwitchMethodStrsList=None,	
						**_KwargVariablesDict
				):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent method
		Mimicker.MimickerClass.__bases__[0].__call__(self,_Class)

		#class
		self._class()

		#Return
		return _Class

	def do__class(self):

		#Definition the MethodsList
		ClassedFunctionsList=SYS._filter(
			lambda __ListedVariable:
				type(__ListedVariable).__name__=="function"
				if hasattr(__ListedVariable,'__name__')
				else False,
				self.DoClass.__dict__.values()
		)

		#debug
		'''
		print('l 66 Classer')
		print("ClassedFunctionsList is ",WatchedFunctionsList)
		print('Set all the mimick methods')
		print('')
		'''

		#Get all the hooking methods
		ClassedMimickFunctionsList=SYS._filter(
			lambda __ListedVariable:
			__ListedVariable.__name__.startswith(
					Mimicker.MimickingWrapPrefixStr
			)
			if hasattr(__ListedVariable,'__name__')
			else False,
			ClassedFunctionsList
		)

		#debug
		'''
		print('l 82 Classer')
		print("ClassedMimickFunctionsList is ",ClassedMimickFunctionsList)
		print('')
		'''

		#map
		map(	
				lambda __ClassedMimickFunction:
				self.mimic(
					Mimicker.MimickingWrapPrefixStr.join(
						__ClassedMimickFunction.__name__.split(
							Mimicker.MimickingWrapPrefixStr)[1:]
						)
				),
				ClassedMimickFunctionsList
			)

		#debug
		'''
		print('l 104 Classer')
		print('set the switch functions')
		print('self.ClassingSwitchMethodStrsList is ',self.ClassingSwitchMethodStrsList)
		print('self.DoClass.DoMethodStr is ',self.DoClass.DoMethodStr)
		print('')
		'''
		
		#map
		map(	
				lambda __ClassingSwitchUnboundMethodStr:
				self.switch(
					True,
					__ClassingSwitchUnboundMethodStr
				),
				self.ClassingSwitchMethodStrsList
			)
#</DefineClass>


```

<small>
View the Classer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Classors/Classer" target="_blank">Github</a>
</small>

