# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Classor Module defines the ClassorClass 
class, which is the deepest parent class in the framework for decorating another class. For each decorated class, 
it just sets up the NameStr in it and also a KeyStrsList for accumulating the new KeyStrs from 
other attributes that can be provided by other decorating Classes.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Initiator"
DecorationModuleStr=""
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineLocals>
ClassDecorationStr="Cls@"
LocalModuleFolderPathStrAndModuleStrTuplesList=[]
#</DefineLocals>

#<DefineFunctions>
def getClass(_InstanceVariable,_ClassVariable=None):

	#Check
	if type(_ClassVariable) in SYS.StrTypesList:
		if _ClassVariable=="":
			return _InstanceVariable.__class__
		else:
			return getattr(SYS,SYS.getClassStrWithNameStr(_ClassVariable))
	elif _ClassVariable==None:
		return _InstanceVariable.__class__
	else:
		return _ClassVariable

def callAllMro(_InstanceVariable,_MethodStr,*_LiargVariablesList,**_KwargVariablesDict):

	#map
	map(
			lambda __MroClass:
			getattr(
				_InstanceVariable,
				_MethodStr
			)(__MroClass,*_LiargVariablesList,**_KwargVariablesDict)
			if hasattr(__MroClass,_MethodStr)
			else None,
			_InstanceVariable.__class__.__mro__
		)

	#Debug
	'''
	print('Classor l 50 ')
	print('_InstanceVariable is ',_InstanceVariable)
	print('')
	'''
	
	#return 
	return _InstanceVariable
#</DefineFunctions>

#<DefineClass>
#@DecorationClass
class ClassorClass(BaseClass):

	#set the Local NameStr
	NameStr="Classor"

	def default_init(self,**_KwargVariablesDict):

		#set the NameStr
		self.NameStr=SYS.getNameStrWithClassStr(self.__class__.__name__)

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Classor l.53 __call__ method')
		print('_Class is ',_Class)
		print('')
		'''

		#set in the class the classed Strs
		_Class.NameStr=SYS.getNameStrWithClassStr(_Class.__name__)

		#Give a Pointer to the Hooker
		setattr(_Class,'DeriveClassor',self)

		#set the KeyStrsList
		_Class.KeyStrsList=SYS.getKeyStrsListWithClass(_Class)

		#set to the SYS the module
		if len(SYS.NameStrsList)==0:
			setattr(SYS,self.NameStr,sys.modules[self.__class__.__module__])
			setattr(SYS,self.__class__.__name__,self.__class__)
			SYS.NameStrsList.append(self.NameStr)
		setattr(SYS,_Class.NameStr,sys.modules[_Class.__module__])
		setattr(SYS,_Class.__name__,_Class)
		SYS.NameStrsList.append(_Class.NameStr)

		#get the module
		Module=sys.modules[_Class.__module__]
		_Class.Module=Module
		_Class.Module.LocalFolderPathStr=SYS.PythonlogyLocalFolderPathStr+Module.__name__.replace(
			'.','/')+'/'
		
		#Check
		if hasattr(_Class,'callAllMro')==False:
			setattr(
					_Class,
					callAllMro.__name__,
					callAllMro
				)
			setattr(
					_Class,
					getClass.__name__,
					getClass
				)
			
		#add in LocalModuleFolderPathStrAndModuleStrTuplesList
		global LocalModuleFolderPathStrAndModuleStrTuplesList
		LocalModuleFolderPathStrAndModuleStrTuplesList.append(
			(
				_Class.Module.LocalFolderPathStr,
				_Class.Module.__name__
			)
		)

		#append
		ConceptModuleStr='.'.join(_Class.Module.__name__.split('.')[:-1])
		if hasattr(_Class,"ConceptModuleStr")==False or _Class.ConceptModuleStr!=ConceptModuleStr:

			#set
			_Class.ConceptModuleStr=ConceptModuleStr

			#append
			LocalModuleFolderPathStrAndModuleStrTuplesList.append(
					(
						SYS.PythonlogyLocalFolderPathStr+ConceptModuleStr.replace('.','/')+'/',
						ConceptModuleStr
					)
				)
			
		#Return 
		return _Class
		
#</DefineClass>

#give to SYS
SYS.LocalModuleFolderPathStrAndModuleStrTuplesList=LocalModuleFolderPathStrAndModuleStrTuplesList
SYS.ClassorClass=ClassorClass
SYS.Classor=sys.modules[ClassorClass.__module__]