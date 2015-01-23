#<ImportSpecificModules>
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Initiator
import sys
#</ImportSpecificModules>

#<DefineFunctions>
def getClassStrWithNameStr(_Str):
	return _Str+"Class"
def getNameStrWithClassStr(_ClassStr):
	return 'Class'.join(_ClassStr.split('Class')[:-1])
def getNameStrWithModuleStr(__ModuleStr):
	return __ModuleStr.split('.')[-1]
#</DefineFunctions>

#<DefineLocals>
ClassingDecorationStr="Class@"
BaseModule=Initiator
BaseNameStr=getNameStrWithModuleStr(BaseModule.__name__)
BaseClass=getattr(BaseModule,getClassStrWithNameStr(BaseNameStr))
#</DefineLocals>

#<DefineClass>
class ClassorClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#<DefineSpecificDo>
		self.ClassingClass=None
		self.NameStr=""
		#</DefineSpecificDo>

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Do
		self._class(_Class)

		#Return 
		return self.ClassingClass

	def _class(self,_Class):

		#set
		if self.ClassingClass==None:
			self.ClassingClass=_Class

		#set the classed Str of the derived or not classor
		self.NameStr=getNameStrWithClassStr(self.__class__.__name__)

		#set in the class the classed Strs
		self.ClassingClass.NameStr=getNameStrWithClassStr(_Class.__name__)

		#Give a Pointer to the Hooker
		setattr(self.ClassingClass,self.NameStr+'Pointer',self)

		#debug 
		print('Classor l.56 : Give to the SYS')
		print("self.NameStr is ",self.NameStr)
		print('')

		#Give to the SYS
		setattr(SYS,self.NameStr,sys.modules[self.__module__])
		setattr(SYS,self.ClassingClass.__name__,self.ClassingClass)

#</DefineClass>

#<DefineSYS>
#debug
'''
print('Classor l.66 :  set to the SYS')
print('')
'''

#set to the SYS
ImportedModuleStrsList=map(
								lambda __Str:
								'ShareYourSystem.'+__Str,
								['Objectss.Initiator','Classors.Classor']
							)
ImportedClassedNameStrsList=map(
										lambda __ModuleStr:
										__ModuleStr.split('.')[-1],
										ImportedModuleStrsList
							)
ImportedClassStrsList=map(
								lambda __ImportedClassedNameStr:
								getClassStrWithNameStr(__ImportedClassedNameStr),
								ImportedClassedNameStrsList
							)
#print(sys.modules.keys())
ImportedModulesList=map(sys.modules.__getitem__,ImportedModuleStrsList)
ImportedClassesList=map(
							lambda __ImportedModule,__ImportedClassStr:
							getattr(__ImportedModule,__ImportedClassStr),
							ImportedModulesList,
							ImportedClassStrsList
						)
map(
		lambda __ImportedClassedNameStr,__ImportedModule:
		setattr(SYS,__ImportedClassedNameStr,__ImportedModule),
		ImportedClassedNameStrsList,
		ImportedModulesList
	)
map(
		lambda __ImportedClassedNameStr,__ImportedClass:
		setattr(SYS,__ImportedClassedNameStr,__ImportedClass),
		ImportedClassStrsList,
		ImportedClassesList
	)
#</DefineSYS>

# -*- coding: utf-8 -*-
"""
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
The Watcher
"""
#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Tester"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>
#<DefineDoStrsList>
DoStrsList=["Watcher","Watch","Watching","Watched"]
#<DefineDoStrsList>
#<ImportSpecificModules>
import collections
import inspect

from ShareYourSystem.Functers import Functer,Hooker
#</ImportSpecificModules>
#<Define_Class>
@DecorationClass()
class WatcherClass(BaseClass):
def default_init(self,
_WatchedFuncFunctionsList=None,
_WatchedHookFunctionsList=None,
_WatchedBindFunctionsList=None,
**_KwargVariablesDict
):
#Call the parent init method
BaseClass.__init__(self,**_KwargVariablesDict)
def __call__(self,_Class):
#Call the parent init method
BaseClass.__call__(self,_Class)
#Watch
self.watch()
#Return _Class
return _Class
#<DefineDoMethod>
def do_watch(self):
pass
"""
#Alias
WatchedClass=self.DoClass
#Definition
WatchedInstanceVariable=None
#Definition the MethodsList
WatchedFunctionsList=SYS._filter(
lambda __ListedVariable:
type(__ListedVariable).__name__=="function"
if hasattr(__ListedVariable,'__name__')
else False,
WatchedClass.__dict__.values()
)
#debug
'''
print("self.ClassingClass is",self.ClassingClass)
print("WatchedFunctionsList is ",WatchedFunctionsList)
print('Define the functed methods')
print('')
'''
#Get all the hooking methods
self.WatchedFuncFunctionsList=SYS._filter(
lambda __ListedVariable:
Functer.FunctingDecorationStr in __ListedVariable.__name__
if hasattr(__ListedVariable,'__name__')
else False,
WatchedFunctionsList
)
#debug
'''
print("self.WatchedFuncFunctionsList is "+str(self.WatchedFuncFunctionsList))
print('')
'''
#debug
'''
print('Set the hooking methods')
print('')
'''
#Get all the hooking methods
self.WatchedHookFunctionsList=SYS._filter(
lambda __WatchedFunctedFunction:
'Hooker'+Functer.FunctingDecorationStr in __WatchedFunctedFunction.__name__,
self.WatchedFuncFunctionsList
)
#If there are some, call them to be binded then
if len(self.WatchedHookFunctionsList)>0:
#Create an instance
WatchedInstanceVariable=WatchedClass()
#debug
'''
print('self.WatchedHookFunctionsList is '+str(self.WatchedHookFunctionsList))
print('')
'''
WatchedHookersList=map(
lambda __WatchedHookFunction:
Functer.getFunctedPointerWithFuncFunctionAndNameStr(__WatchedHookFunction,'Hooker'),
self.WatchedHookFunctionsList
)
#set the corresponding Hookers
setHookerWithHookingInstanceVariable=Hooker.setHookerWithHookingInstanceVariable
map(
lambda __WatchedHooker:
setHookerWithHookingInstanceVariable(
__WatchedHooker,
WatchedInstanceVariable),
WatchedHookersList
)
#debug
'''
print('Set the switching methods')
print('')
'''
#Get all the binding methods
self.WatchedSwitchFunctionsList=SYS._filter(
lambda __WatchedFunctedFunction:
'Switcher'+Functer.FunctingDecorationStr in __WatchedFunctedFunction.__name__,
self.WatchedFuncFunctionsList
)
#If there are some call them to be binded then
if len(self.WatchedSwitchFunctionsList)>0:
#Debug
'''
print('self.WatchedSwitchFunctionsList is '+str(self.WatchedSwitchFunctionsList))
print('')
'''
#Create an instance
if WatchedInstanceVariable==None:
WatchedInstanceVariable=WatchedClass()
#Debug
'''
print('WatchedInstanceVariable is ',WatchedInstanceVariable)
print('WatchedClass.__module__ is ',WatchedClass.__module__)
print('')
'''
#Call the functions
map(
lambda __WatchedSwitchFunction:
__WatchedSwitchFunction(WatchedInstanceVariable),
self.WatchedSwitchFunctionsList
)
#debug
'''
print('Set the binding methods')
print('')
'''
#Get all the binding methods (maybe the switch analysis added some news)
self.WatchedBindFunctionsList=SYS._filter(
lambda __ListedVariable:
'Triggerer'+Functer.FunctingDecorationStr in __ListedVariable.__name__
if hasattr(__ListedVariable,'__name__')
else False,
WatchedClass.__dict__.values()
)
#If there are some call them to be binded then
if len(self.WatchedBindFunctionsList)>0:
#debug
'''
print('self.WatchedBindFunctionsList is '+str(self.WatchedBindFunctionsList))
print('')
'''
#Create an instance
if WatchedInstanceVariable==None:
WatchedInstanceVariable=WatchedClass()
#Call the functions
map(
lambda __WatchedBindFunction:
__WatchedBindFunction(WatchedInstanceVariable),
self.WatchedBindFunctionsList
)
"""	
#</Define_Class>
