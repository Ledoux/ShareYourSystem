# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Defaultor is a crucial module for understanding how we
can manage high-computer-performance of many instanciations 
without making the memory crashes. For an Instance that is setted
by default, this latter will find its attributes in the 
class __dict__. Once the instance has setted in its __dict__ a 
special value it will stop to look at the class level. 
There is for now no distinction of get,set for mutable or non mutable 
variable.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Classor"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import six
from ShareYourSystem.Objects import Initiator
Classor=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
DefaultingStr="_"
DefaultDecorationMethodStr="default_init"
DefaultAttributePrefixStr='_'
DefaultWrapMethodStr='default_init'
DefaultDecorationMethodStr="superDefault_init"
#</DefineLocals>

#<DefineFunctions>
def getDefaultedValueVariableWithSetVariable(_SetVariable):

	#Return the instanciation of the type
	if hasattr(_SetVariable,'items'):

		#If it is direct a call of a type without extra argument then instancify
		if 'DefaultingSetType' in _SetVariable and len(_SetVariable)==1:
			DefaultedValueVariable=_SetVariable['DefaultingSetType']()
			return DefaultedValueVariable 
	
	#Return direct the Variable
	return _SetVariable

def setDefaultMutable(
	_InstanceVariable,
	_ClassVariable,
	_AttributeKeyStrsList=None,
	**_KwargVariablesDict
):
	
	#Set
	if 'ForceSetIsBool' in _KwargVariablesDict:
		ForceSetIsBool=_KwargVariablesDict['ForceSetIsBool']
	else:
		ForceSetIsBool=False

	#get
	DefaultClass=_InstanceVariable.getClass(_ClassVariable)

	#Check
	if _AttributeKeyStrsList==None:
		_AttributeKeyStrsList=DefaultClass.DefaultSetKeyStrsList

	#map an init for the mutable variables by detecting them at the level of the class : they are None
	TypeClassesList=map(
			lambda __AttributeKeyStr:
			SYS.getTypeClassWithTypeStr(
				SYS.getTypeStrWithKeyStr(__AttributeKeyStr)
			)
			if (
				SYS.getIsNoneBool(
				getattr(
					_InstanceVariable,
					__AttributeKeyStr
				)
			) if ForceSetIsBool==False else True)
			and getattr(DefaultClass,__AttributeKeyStr)==None
			else None.__class__,
			_AttributeKeyStrsList
	)

	#debug
	'''
	print('l 83 Defaultor')
	print('TypeClassesList is '+str(TypeClassesList))
	print('')
	'''
	
	#set in the instance
	map(
			lambda __AttributeKeyStr,__TypeClass:
			setattr(
					_InstanceVariable,
					__AttributeKeyStr,
					__TypeClass()
			)
			if __TypeClass!=None.__class__ 
			else None,
			_AttributeKeyStrsList,
			TypeClassesList
	)

	#return 
	return _InstanceVariable

def setDefault(
	_InstanceVariable,
	_ClassVariable,
	_AttributeKeyStrsList=None,
	**_KwargVariablesDict
):
	
	#get
	DefaultClass=_InstanceVariable.getClass(_ClassVariable)

	#Check
	if _AttributeKeyStrsList==None:
		_AttributeKeyStrsList=_ClassVariable.DefaultSetKeyStrsList

	#check
	if 'DefaultNotSetKeyStrsList' in _KwargVariablesDict:

		#filter
		_AttributeKeyStrsList=SYS._filter(
				lambda __AttributeKeyStr:
				__AttributeKeyStr not in _KwargVariablesDict['DefaultNotSetKeyStrsList'],
				_AttributeKeyStrsList
			)
		
	#Debug
	'''
	print('Defaultor l 62')
	print('_AttributeKeyStrsList is ')
	print(_AttributeKeyStrsList)
	print('')
	'''

	#map a set for all the class attributes into the instance
	map(
			lambda __AttributeKeyStr:
			_InstanceVariable.__setattr__
			(
				__AttributeKeyStr,
				getattr(
						DefaultClass,
						__AttributeKeyStr
					)
			),
			_AttributeKeyStrsList
		)

	#set
	setDefaultMutable(_InstanceVariable,DefaultClass,_AttributeKeyStrsList)

	#return 
	return _InstanceVariable

#Definition the new init method
def initDefault(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

	#debug
	'''
	print('Defaultor l.134 : ')
	print('_LiargVariablesList is ',_LiargVariablesList)
	print('_KwargVariablesDict is ',_KwargVariablesDict)
	print('')
	'''

	#set at the level of the class
	InitKwargVariablesDict=dict(
		map(
			lambda __SettingItemTuple:
			(
				DefaultingStr.join(__SettingItemTuple[0].split(DefaultingStr)[1:]) 
				if __SettingItemTuple[0].startswith(DefaultingStr)
				else __SettingItemTuple[0],
				__SettingItemTuple[1]
			),
			_KwargVariablesDict.items()
			)
	)

	#debug
	'''
	print('Defaultor l.155 : ')
	print('InitKwargVariablesDict is ',InitKwargVariablesDict)
	print('')
	'''

	#Call the init method of the Initiator
	Initiator.InitiatorClass.__init__(
		_InstanceVariable,**InitKwargVariablesDict)

	#get
	DefaultClass=getattr(SYS,_KwargVariablesDict['DefaultClassStr'])
	DefaultWrapUnboundMethod=getattr(DefaultClass,_KwargVariablesDict['DefaultWrapMethodStr'])

	#debug
	'''
	print('Defaultor l.182 : ')
	print('DefaultClass is ',DefaultClass)
	print('DefaultWrapUnboundMethod is ',DefaultWrapUnboundMethod)
	print('')
	'''

	#Call the InitMethodFunction
	try:
		DefaultWrapUnboundMethod(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict)
	except:
		DefaultWrapUnboundMethod(_InstanceVariable,*_LiargVariablesList)

#<DefineFunctions>

#<Define_Class>
@DecorationClass()
class DefaultorClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Defaultor l.31 __call__ method')
		print('_Class is ',_Class)
		print('')
		'''

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#debug
		'''
		print('Defaultor l.47 look for an __init__ method')
		print('_Class is ',_Class)
		print('')
		'''

		#Check
		if hasattr(_Class,"__init__"):

			#debug
			'''
			print('It has an __init__ method')
			print('')
			'''

			#get
			InitWrapUnboundMethod=getattr(_Class,DefaultWrapMethodStr)

			#set the DefaultDict
			_Class.InitArgumentDict=SYS.getArgumentDictWithFunction(InitWrapUnboundMethod)

			#Definition the DefaultAttributeItemTuplesList
			DefaultAttributeItemTuplesList=map(
					lambda __DefaultSetItemTuple:
					(
						DefaultingStr.join(
						__DefaultSetItemTuple[0].split(DefaultingStr)[1:]
						),
						getDefaultedValueVariableWithSetVariable(
								__DefaultSetItemTuple[1]
							)
					),
					SYS._filter(
								lambda __DefaultItemTuple:
								__DefaultItemTuple[0].startswith(DefaultingStr),
								_Class.InitArgumentDict['DefaultOrderedDict'].items()
							)
			)

			#set
			_Class.DefaultAttributeVariablesOrderedDict=collections.OrderedDict(
					DefaultAttributeItemTuplesList
				)

			#debug
			'''
			print('_Class.DefaultAttributeItemTuplesList is ',_Class.DefaultAttributeItemTuplesList)
			print('')
			'''

			#set at the level of the class
			map(	
					lambda __DefaultSetItemTuple:
					setattr(_Class,*__DefaultSetItemTuple),
					_Class.DefaultAttributeVariablesOrderedDict.items()
				)

			#set the DefaultSetKeyStrsList
			#_Class.DefaultSetKeyStrsList=SYS.unzip(_Class.DefaultAttributeItemTuplesList,[0])
			_Class.DefaultSetKeyStrsList=_Class.DefaultAttributeVariablesOrderedDict.keys()

			#Get the BaseKeyStrsList
			_Class.DefaultBaseSetKeyStrsList=list(
								SYS.collect(
											_Class,
											'__bases__',
											'DefaultSetKeyStrsList'
								)
			)
			
			#Debug
			'''
			print("l 269 Defaultor")
			print("DefaultDecorationMethodStr is ",DefaultDecorationMethodStr)
			print("")
			'''

			#Define the decorated function
			InitExecStr="def "+DefaultDecorationMethodStr+"(_InstanceVariable,"
			InitExecStr+="*_LiargVariablesList,"
			InitExecStr+="**_KwargVariablesDict):\n\t"
			InitExecStr+="initDefault(_InstanceVariable,"
			InitExecStr+="*_LiargVariablesList,"
			InitExecStr+="**dict(_KwargVariablesDict,**{'DefaultWrapMethodStr':'"+DefaultWrapMethodStr+"','DefaultClassStr':'"+_Class.__name__+"'}))\n"
		
			#debug
			'''
			print('Defaultor l 280')
			print('InitExecStr is ')
			print(InitExecStr)
			print('')
			'''
			
			#exec
			six.exec_(InitExecStr)

			#set with the specific name
			setattr(
						_Class,
						DefaultDecorationMethodStr,
						locals()[DefaultDecorationMethodStr]
					)

			#set with the DoMethodStr shortcut
			setattr(
						_Class,
						"__init__",
						locals()[DefaultDecorationMethodStr]
					)

			#set in the class fi not already 
			if hasattr(_Class,'setDefault')==False:

				#set setDefault
				setattr(
							_Class,
							setDefault.__name__,
							setDefault
						)
				
				#set setDefaultMutable
				setattr(
							_Class,
							setDefaultMutable.__name__,
							setDefaultMutable
						)

			#Add to the KeyStrsList
			_Class.KeyStrsList+=[
										#'DefaultAttributeItemTuplesList',
										'DefaultAttributeVariablesOrderedDict',
										'InitArgumentDict'
									]

		#Return 
		return _Class

#</Define_Class>



