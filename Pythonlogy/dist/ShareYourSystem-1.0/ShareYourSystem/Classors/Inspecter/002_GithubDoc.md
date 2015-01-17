
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


An Inspecter decorates a class by giving it an InspectedArgumentDict that is 
an inspection of all defined methods.
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Propertiser"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import inspect
#</ImportSpecificModules>

#<DefineFunction>
def getInspectedUnboundMethodsListWithClass(_Class):
	return SYS._filter(
			lambda __AttributeVariable:
			type(__AttributeVariable).__name__=="function",
			_Class.__dict__.values()
			)
#<DefineFunction>

#<DefineClass>
@DecorationClass()
class InspecterClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#Inspect
		self.inspect()

		#Return _Class
		return _Class

	def do_inspect(self):

		#Alias
		InspectedClass=self.DoClass

		#Debug
		'''
		print('InspectedClass is ',InspectedClass)
		print('')
		'''
		
		#Get the Args
		InspectedClass.InspectedArgumentDict=dict(
								map(	
									lambda __Function:
									(
										__Function.__name__,
										SYS.getArgumentDictWithFunction(__Function)
									),
									getInspectedUnboundMethodsListWithClass(InspectedClass)
								)
							)

		#Add to the KeyStrsList
		InspectedClass.KeyStrsList+=[
									'InspectedArgumentDict',
								]

#</Define_Class>


```

<small>
View the Inspecter sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Classors/Inspecter" target="_blank">Github</a>
</small>

