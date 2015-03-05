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
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineLocals>
ClassDecorationStr="Cls@"
LocalModuleFolderPathStrAndModuleStrTuplesList=[]
#</DefineLocals>

#<DefineLocals>
def getClass(_InstanceVariable,_ClassVariable=None):

	#Debug
	'''
	print('Classor l 35')
	print('_ClassVariable is ')
	print(_ClassVariable)
	print('')
	'''
	
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
#</DefineLocals>

#<DefineClass>
class ClassorClass(object):

	#set the Local NameStr
	NameStr="Classor"

	def default_init(self,**_KwargVariablesDict):

		#set the NameStr
		self.NameStr=SYS.getNameStrWithClassStr(self.__class__.__name__)

		#Map the update
		map(
				lambda __ItemTuple:
				self.__setattr__(__ItemTuple[0],__ItemTuple[1]) 
				#If we want to not set the items setted during hooks and that are not specified...
				if hasattr(self,__ItemTuple[0]) else None
				,_KwargVariablesDict.iteritems()
			)

		#call the base method
		object.__init__(self)

	def __call__(self,_Class):


		#/###################/#
		# Set the NameStr, Module, SelfClass...
		#

		#get
		self.Module=sys.modules[_Class.__module__]

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

		#set to the SYS the module
		if len(SYS.NameStrsList)==0:
			setattr(SYS,self.NameStr,sys.modules[self.__class__.__module__])
			setattr(SYS,self.__class__.__name__,self.__class__)
			SYS.NameStrsList.append(self.NameStr)
		setattr(SYS,_Class.NameStr,self.Module)
		setattr(SYS,_Class.__name__,_Class)
		SYS.NameStrsList.append(_Class.NameStr)

		#get the module and set it to the class
		_Class.Module=self.Module
		_Class.Module.LocalFolderPathStr=SYS.PythonlogyLocalFolderPathStr+self.Module.__name__.replace(
			'.','/')+'/'

		#set a pointer to itself
		_Class.SelfClass=_Class
		_Class.MroClassesList=_Class.__mro__
		
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

		#/###################/#
		# Give ref to the concept module
		#

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
			
		#/###################/#
		# Alert the base method that a derive object exists
		#

		#set
		if len(_Class.__bases__)>0:

			#set the DerivedBaseClas
			FirstBaseClass=_Class.__bases__[0]

			#Debug
			'''
			print('l. 183 Classor')
			print('We can set derived bases for the base')
			print('FirstBaseClass is ',FirstBaseClass)
			print('')
			'''
			
			#Append to the parent class 
			if hasattr(FirstBaseClass,'DeriveClassesList'):
				FirstBaseClass.DeriveClassesList.append(_Class)
			elif FirstBaseClass!=object:
				FirstBaseClass.DeriveClassesList=[_Class]

		#/###################/#
		# Inspect the methods
		#

		#Get the Methods
		_Class.InspectMethodDict=SYS.MethodDict(_Class)

		#dict
		_Class.InspectArgumentDict=dict(
			map(	
					lambda __MethodItemTuple:
					(
						__MethodItemTuple[0],
						SYS.ArgumentDict(
							__MethodItemTuple[1]
						)
					),
					_Class.InspectMethodDict.items()
				)
			)

		#/###################/#
		# set the KeyStrsList
		#

		#set the KeyStrsList
		_Class.KeyStrsList=SYS.getKeyStrsListWithClass(_Class)+['KeyStrsList']

		#Return 
		return _Class
		
#</DefineClass>

#give to SYS
SYS.LocalModuleFolderPathStrAndModuleStrTuplesList=LocalModuleFolderPathStrAndModuleStrTuplesList
SYS.ClassorClass=ClassorClass
SYS.Classor=sys.modules[ClassorClass.__module__]