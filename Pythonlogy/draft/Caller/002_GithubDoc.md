
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


The Caller is an Object that helps to get an make call a function/method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Packager"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CallerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CallingVariable',
								'CallingFunctionStr',
								'CallingMethod',
								'CallingMethodStr',
								'CallingInstanceVariable',
								'CallingClass',
								'CallingClassStr',
							]

	def default_init(self,
						_CallingVariable=None,
						_CallingFunctionStr="",
						_CallingMethod=None,
						_CallingMethodStr="",
						_CallingInstanceVariable=None,
						_CallingClass=None,
						_CallingClassStr="",
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	#<DefineDoMethod>	
	def do_call(self):

		#Module first to know where we are
		self.package()

		#debug
		'''
		print("self.CallingVariable is ",self.CallingVariable)
		print('')
		'''

		#If it was not yet setted or changed
		if self.CallingVariable==None or self.CallingVariable.__name__!=self.CallingFunctionStr:

			#debug
			'''
			print('Get in the module')
			print('self.PackagingModuleVariable is '+str(self.PackagingModuleVariable))
			print('')
			'''

			#Get maybe the one in the module
			if self.CallingFunctionStr!="":

				#debug
				'''
				print('Get in the module with the function Str')
				print('self.CallingFunctionStr is ',self.CallingFunctionStr)
				print('')
				'''

				#Get and return
				self.CallingVariable=getattr(self.PackagedModuleVariable,self.CallingFunctionStr)
				return self

		#Get the function 
		if self.CallingVariable==None or self.CallingVariable.__name__!=self.CallingMethodStr:

			#debug
			'''
			print('Get in a class')
			print('self.PackagingModuleVariable is '+str(self.PackagingModuleVariable))
			print('self.CallingVariable is ',self.CallingVariable)
			print('self.CallingMethodStr is ',self.CallingMethodStr)
			print('self.CallingClass is ',self.CallingClass)
			print('self.CallingClassStr is ',self.CallingClassStr)
			print('self.CallingInstanceVariable is ',self.CallingInstanceVariable)
			print('')
			'''
			
			#Get with the CallingInstanceVariable class maybe
			if self.CallingClass==None and self.CallingInstanceVariable!=None:
				self.CallingClass=self.CallingInstanceVariable.__class__

			#Import the module if not already
			if self.CallingClass==None:
				if self.CallingClassStr!="":
					self.CallingClass=getattr(self.PackagedModuleVariable,self.CallingClassStr)
				else:
					self.CallingClass=getattr(
									self.PackagedModuleVariable,
									SYS.getClassStrWithNameStr(
										SYS.getNameStrWithModuleStr(self.PackagedModuleVariable.__name__)
										)
									)
			

			#debug
			'''
			print('Now get the unbounded method function')
			print('self.CallingClass is '+str(self.CallingClass))
			print('')
			'''

			#Check
			if self.CallingMethodStr!="":
	
				#debug
				'''
				print('self.CallingMethodStr is ',self.CallingMethodStr)
				print('')
				'''

				#Return 
				self.CallingVariable=getattr(self.CallingClass,self.CallingMethodStr)

		#Return
		#return self

#</DefineClass>


```

<small>
View the Caller sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Objects/Caller" target="_blank">Github</a>
</small>

