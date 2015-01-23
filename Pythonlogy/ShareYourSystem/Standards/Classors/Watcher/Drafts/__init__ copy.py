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
								['Objects.Initiator','Classors.Classor']
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

