# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


ShareYourSystem helps for defining scientific applications
in a Hierarchical Model-View-Controller framework.
"""

#<ImportSpecificModules>
import collections
import copy
import functools
import importlib
import inspect
import inflect
import operator
import os
import re
import sys
#</ImportSpecificModules>

#<DefineLocals>
OuvatonUrlStr="http://shareyoursystem.ouvaton.org"
ShareYourSystemLocalFolderPathStr='/Users/ledoux/Documents/ShareYourSystem/'
OuvatonLocalFolderPathStr=ShareYourSystemLocalFolderPathStr+"Ouvaton/"
PythonlogyLocalFolderPathStr=ShareYourSystemLocalFolderPathStr+'Pythonlogy/'
GithubMasterUrlStr="https://github.com/Ledoux/ShareYourSystem/tree/master"

h5lsPathStr="/usr/local/bin/h5ls"
#PythonPathStr=os.popen('which python'+str(sys.version[0])).read()[:-2]
PythonPathStr="/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python"
IPythonPathStr=os.popen('which ipython'+str(sys.version[0])).read()[:-2]
if IPythonPathStr=="":
	IPythonPathStr="/usr/local/bin/ipython" if sys.version[0
	]=='2' else "/Library/Frameworks/Python.framework/Versions/3.4/bin/ipython3"

NameStrsList=[]

if sys.version[0]==2:
	StrTypesList=[str,unicode]
else:
	StrTypesList=[str]

InflectEngine=inflect.engine()

MutableStrsList=['List','Tuple','Dict','Set']
NotMutableStrsList=['Bool','Int','Float','Str']

ConceptStrsTuplesList=[
	('Object','Objects'),
	('Classor','Classors'),
	('Interfacer','Interfacers'),
	('Guider','Guiders'),
	('Itemizer','Itemizers'),
	('Walker','Walkers'),
	('Noder','Noders'),
	('Controller','Controllers'),
	('Modeler','Modelers'),
	('Viewer','Viewers'),
	('Ploter','Ploters'),
	('Tutorials','Tutorials'),
	('Brianer','Brianers'),
	('Neuroner','Neuroners'),
	('Simulater','Simulaters'),
	('Muziker','Muzikers')
]

PythonSet=set
#</DefineLocals>

#<DefineFunctions>
def setConceptModule(_ModuleGlobalsDict):

	#Debug
	'''
	print('----------------------')
	print('ShareYourSystem  l 73 ')
	print('Begin of the concept set')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('')
	'''

	#Define
	ModuleFolderPathStr='/'.join(_ModuleGlobalsDict['__file__'].split('/')[:-1])
	__all__ = _filter(
					lambda __DirKeyStr:
					os.path.isdir(__DirKeyStr) and os.path.isfile(__DirKeyStr+'/__init__.py'),
					os.listdir(ModuleFolderPathStr)
			)

	#Get
	VarsDict=vars()

	#map
	VarsItemTuplesList=map(
			lambda __VarsKeyStr:
			(
				__VarsKeyStr,
				VarsDict[__VarsKeyStr]
			),
			#_ModuleGlobalsDict.keys()
			[
				'ModuleFolderPathStr',
				'__all__'
			]
		)

	#map Sys to module
	map(
			lambda __VarsItemTuple:
			_ModuleGlobalsDict.__setitem__(
				__VarsItemTuple[0],
				__VarsItemTuple[1]
			) 
			#if __VarsItemTuple[0] not in _ModuleGlobalsDict
			#else None,
			,VarsItemTuplesList
		)

	#Debug
	'''
	print('l 118 ShareYourSystem')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('End of the concept set')
	print('----------------------')
	print('')
	'''

def setSubModule(_ModuleGlobalsDict):
	
	#Debug
	'''
	print('----------------------')
	print('ShareYourSystem  l 131 ')
	print('Begin of the sub set')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('')
	'''

	#map
	'''
	ModuleGlobalsItemTuplesList=map(
			lambda __ModuleGlobalsKeyStr:
			(__ModuleGlobalsKeyStr,_ModuleGlobalsDict[__ModuleGlobalsKeyStr]),
			#_ModuleGlobalsDict.keys()
			[
			]
		)
	'''

	#Debug
	'''
	print('ShareYourSystem l 150')
	print('ModuleGlobalsItemTuplesList is ')
	#print(ModuleGlobalsItemTuplesList)
	print('')
	'''

	'''
	#get
	SysGlobalsDict=globals()

	#map module to sys
	map(
			lambda __ModuleGlobalsItemTuple:
			SysGlobalsDict.__setitem__(*__ModuleGlobalsItemTuple),
			ModuleGlobalsItemTuplesList
		)
	'''
	
	#Define
	BaseModule=None
	BaseNameStr=""
	BaseClass=None
	DecorationModule=None
	DecorationNameStr=""
	DecorationClass=None

	#Get
	BaseModuleStr=_ModuleGlobalsDict['BaseModuleStr']

	#Debug
	'''
	print('ShareYourSystem l 181')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('BaseModuleStr is '+BaseModuleStr)
	print('')
	'''

	if BaseModuleStr!="":
		BaseModule=importlib.import_module(BaseModuleStr)
		BaseNameStr=getNameStrWithModuleStr(BaseModule.__name__)
		BaseClass=getattr(BaseModule,getClassStrWithNameStr(BaseNameStr))

	#Get
	DecorationModuleStr=_ModuleGlobalsDict['DecorationModuleStr']

	#Debug
	'''
	print('ShareYourSystem l 197')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('DecorationModuleStr is '+DecorationModuleStr)
	print('')
	'''

	if DecorationModuleStr!="":
		DecorationModule=importlib.import_module(DecorationModuleStr)
		DecorationNameStr=getNameStrWithModuleStr(DecorationModule.__name__)
		DecorationClass=getattr(DecorationModule,getClassStrWithNameStr(DecorationNameStr))

	#Get
	VarsDict=vars()

	#map
	VarsItemTuplesList=map(
			lambda __VarsKeyStr:
			(
				__VarsKeyStr,
				VarsDict[__VarsKeyStr]
			),
			#_ModuleGlobalsDict.keys()
			[
				'BaseModule',
				'BaseNameStr',
				'BaseClass',
				'DecorationModule',
				'DecorationNameStr',
				'DecorationClass'
			]
		)

	#Debug
	'''
	print('ShareYourSystem l 231')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('VarsItemTuplesList is ')
	print(VarsItemTuplesList)
	print('')
	'''

	#map Sys to module
	map(
			lambda __VarsItemTuple:
			_ModuleGlobalsDict.__setitem__(
				__VarsItemTuple[0],
				__VarsItemTuple[1]
			) 
			#if __VarsItemTuple[0] not in _ModuleGlobalsDict
			#else None,
			,VarsItemTuplesList
		)

	#Debug
	'''
	print('l 252 ShareYourSystem')
	print("_ModuleGlobalsDict['__name__'] is ",_ModuleGlobalsDict['__name__'])
	print('End of the sub set')
	print('----------------------')
	print('')
	'''
	
def getClassStrWithNameStr(_Str):
	return _Str+"Class"

def getNameStrWithClassStr(_ClassStr):
	return 'Class'.join(_ClassStr.split('Class')[:-1])

def getNameStrWithModuleStr(__ModuleStr):
	return __ModuleStr.split('.')[-1]

def getClassWithNameStr(_NameStr):
	return globals()[getClassStrWithNameStr(_NameStr)]

def getKeyStrsListWithClass(_Class):
	return list(filter(
						lambda __KeyStr:
						#You need to do with getattr to have the __getattr__ look up that renders 'instance method' for unbound methods
						__KeyStr[0]==__KeyStr[0].upper() and type(
							getattr(_Class,__KeyStr)
							).__name__!="instancemethod" and __KeyStr[0:2]!="__",
						_Class.__dict__.keys()
					))

def getWordStrsListWithStr(_Str):
	'''
		<Help>
			Split a Str into its Words
		</Help>

		<Test>
			#Load ShareYourSystem as SYS
			import ShareYourSystem as SYS

			#Print some cells
			print("The Words in the Str SuperMan are :"+str(getWordStrsListWithStr("SuperMan")));
			print("The Words in the Str \"FeelLike-A-RainBow\" are :"+str(getWordStrsListWithStr("FeelLike-A-RainBow")));
			print("The Words in the Str \"MySYSHopeItsWorkingHELLO\" are :"+str(getWordStrsListWithStr("MySYSHopeItsWorkingHELLO")));
		</Test>	
	'''
	
	#Get all the Strs with an upper char at the first index
	if type(_Str) in StrTypesList:
		StrsList=list(filter(None,re.split("([A-Z][^A-Z]*)",_Str)))

		#Join the abreviated Strs
		if len(StrsList)>1:

			WordsInt=0
			PreviousStr=StrsList[WordsInt]
			while WordsInt<len(StrsList)-1:
			
				#Increment the Word
				WordsInt+=1
				
				#Definition the Next Str
				NextStr=StrsList[WordsInt]
			
				#Check for Upper Abreviations
				if len(NextStr)==1:
					if (all(map(lambda Char:Char.upper()==Char,list(PreviousStr)))) and (NextStr.upper()==NextStr):
					
						#Join Previous and NextStr
						StrsList[WordsInt-1]=PreviousStr+NextStr

						#Remove the NextStr
						StrsList.pop(WordsInt)
				
						#Increment
						WordsInt-=1

				#Shift the Previous Str
				if WordsInt<len(StrsList):
					PreviousStr=StrsList[WordsInt]

		#Return StrsList
		return StrsList

	#Return [] by default
	else:
		return [""]

def getDefaultArray():
	import numpy
	return numpy.array([])

def getTypeClassWithTypeStr(_TypeStr):

	#Debug
	'''
	print('SYS getTypeClassWithTypeStr l.121 ')
	print('_TypeStr is '+_TypeStr)
	print('')
	'''

	#Check
	if _TypeStr=='OrderedDict':

		#Special collections case
		return collections.OrderedDict

	elif _TypeStr=='Function':

		#Return None
		return None.__class__

	#elif _TypeStr=='Array':
	#
	#	#return 
	#	return getDefaultArray

	elif _TypeStr in MutableStrsList+NotMutableStrsList :

		#Other standard mutable cases
		return getattr(
				sys.modules['__builtin__'],
				_TypeStr[0].lower()+_TypeStr[1:]
			)

	elif _TypeStr in NameStrsList:

		#Type defined in the SYS system
		return getattr(
				globals()[_TypeStr],
				getClassStrWithNameStr(_TypeStr)
			)

	else:

		#Define
		ClassStr=getClassStrWithNameStr(_TypeStr)

		#debug
		'''
		print('SYS getTypeClassWithTypeStr l.166 ')
		print('ClassStr is '+ClassStr)
		print('')
		'''
		
		#Return an instance of this corresponding class		
		if hasattr(sys.modules['ShareYourSystem'],ClassStr):
			return getattr(sys.modules['ShareYourSystem'],ClassStr)

		#Return None class
		else:
			return None.__class__

def getTypeStrWithKeyStr(_KeyStr):

	#debug
	'''
	print('SYS  getTypeStrWithKeyStr l.168 ')
	print('_KeyStr is '+_KeyStr)
	print('')
	'''

	#Definition
	global NameStrsList

	#filter
	TypeStrsList=list(
		filter(
		lambda __Variable:
		__Variable!=None,
		map(
			lambda __TypeStr:
			__TypeStr if _KeyStr.endswith(__TypeStr)
			else None,
			[
				'OrderedDict'
			]+NameStrsList
		)
	))

	#Check
	if len(TypeStrsList)==1:

		#Return the found type
		return TypeStrsList[0]

	else:

		#Return the last word
		return getWordStrsListWithStr(_KeyStr)[-1]

def getIsNoneBool(_Variable):

	#debug
	'''
	print('SYS  getIsNoneBool l.443 ')
	print('_Variable is ',_Variable)
	print('type(_Variable) is ',type(_Variable))
	print('')
	'''

	#Define 
	Type=type(_Variable)

	#Check
	import numpy
	if Type!=numpy.ndarray:

		#Debug
		'''
		print('SYS  getIsNoneBool l.456 ')
		print('Type is ')
		print(Type)
		print('')
		'''
		
		#return
		return Type==None.__class__

	else:

		#Debug
		'''
		print('SYS  getIsNoneBool l.456 ')
		print('Type is ')
		print(Type)
		print('')
		'''

		#return 
		return False

def getLocalFolderPathStr(_ModuleVariable):
	return ShareYourSystemLocalFolderPathStr+_ModuleVariable

def getNone(_KeyVariable,_ValueVariable):
	return None

def add(_VariableA,_VariableB):

	#Debug
	'''
	print('SYS l 500 ')
	print('add')
	print('type(_VariableA) is '+str(type(_VariableA)))
	print('')
	'''

	#Check
	if hasattr(_VariableA,'__add__'):

		#Debug
		'''
		print('SYS l 502')
		print('_VariableA has __add__')
		print('')
		'''

		#set
		_VariableA=_VariableA.__add__(_VariableB)

		#return 
		return _VariableA

	elif type(_VariableA)==PythonSet:

		#Debug
		'''
		print('SYS l 512')
		print('_VariableA is a set')
		print('_VariableB is ')
		print(_VariableB)
		print('')
		'''

		#set
		_VariableA=_VariableA.union(_VariableB)
		
		#Debug
		'''
		print('_VariableA is after union')
		print(_VariableA)
		print('')
		'''
		
		#return
		return _VariableA


def stdout(_PrintStr):
	sys.stdout.write(_PrintStr+'\n')
	sys.stdout.flush()

def wait(_SecondInt):
	import time
	for __IndexInt in xrange(_SecondInt):
		sys.stdout.write('...'+str(_SecondInt-__IndexInt)+'s')
		sys.stdout.flush()
		time.sleep(1)
	sys.stdout.write('\n')
	sys.stdout.flush()

def indent(_Variable):
	if hasattr(_Variable,'items')==False:
		_Variable=_Variable.__dict__
	import json
	return json.dumps(
			dict(
				zip(
						_Variable.keys(),
						map(str,_Variable.values())
					)
			),
				indent=2
		)

def pick(_Variable,_GetVariablesList,_GetMethodStr='getattr'):

	#Check
	if _GetMethodStr=='getattr':

		#return 
		return map(
				lambda __GetVariable:
				getattr(
					_Variable,
					__GetVariable
				),
				_GetVariablesList
			)
	elif _GetMethodStr=='__getitem__':

		#return 
		return map(
				lambda __GetVariable:
				_Variable[__GetVariable],
				_GetVariablesList
			)




def _filter(_Function,_List):
	if sys.version[0]==2:
		return filter(_Function,_List)
	else:
		return list(filter(_Function,_List))

def filterNone(_List):
	return _filter(
						lambda __ListedVariable:
						__ListedVariable!=None,
						_List
					)

def flip(_Dict):
	return type(_Dict)(
				map(lambda __ItemTuple:(__ItemTuple[1],__ItemTuple[0]),_Dict.items())
			)

def reverse(_List):
	ReversedList=copy.copy(list(_List))
	ReversedList.reverse()
	return ReversedList

def sum(_VariablesList):

	#Check
	if len(_VariablesList)>0:

		#reduce
		return functools.reduce(
								lambda __List,__Variable:
								__List+list(__Variable) 
								if type(__Variable) in [list,tuple] 
								else __List+[__Variable],
								_VariablesList
							)
	else:

		#return
		return []

def flat(_VariablesList):
	if len(_VariablesList)>0:
		if type(_VariablesList[0])!=list:
			_VariablesList[0]=[_VariablesList[0]]
		return functools.reduce(
									lambda __List,__Variable:
									__List+flat(list(__Variable)) 
									if type(__Variable) in [list,tuple] 
									else __List+[__Variable],
									_VariablesList
								)
	else:
		return _VariablesList

def path(_PathStrsList):

	#Reduce
	PathStr=functools.reduce(
			lambda _TotalPathStr,_PathStr:
			_TotalPathStr+_PathStr 
			if (len(_TotalPathStr)>0 and _TotalPathStr[-1]=='/') and (len(_PathStr)>0 and _PathStr[0]!='/'
				) or (len(_TotalPathStr)>0 and _TotalPathStr[-1]!='/') and (len(_PathStr)>0 and _PathStr[0]=='/')
			else 
			_TotalPathStr[:-1]+_PathStr 
			if (len(_TotalPathStr)>0 and _TotalPathStr[-1]=='/') and (len(_PathStr)>0 and _PathStr[0]=='/'
				)
			else _TotalPathStr+'/'+_PathStr 
			if '/' not in [_PathStr,_TotalPathStr]
			else "",
			_PathStrsList
			)

	#Maybe add / at the beginning
	if (len(PathStr)>0 and PathStr[0]!='/') or PathStr=="":
		PathStr='/'+PathStr

	#Return
	return PathStr

def collect(_Variable,_WalkingKeyStr,_GettingKeyStr):

	#Get the collectedListsList
	return flat(map(
					lambda _ListedVariable:
					flat(
							([
								getattr(_ListedVariable,_GettingKeyStr
									)] if hasattr(_ListedVariable,_GettingKeyStr)
								else []
							)+(collect(_ListedVariable,_WalkingKeyStr,_GettingKeyStr
								) if hasattr(_ListedVariable,_WalkingKeyStr)
								else []
							)
						)
					,getattr(_Variable,_WalkingKeyStr)
				))

def map_(_Function,_List,**_KwargVariablesDict):
	
	#Check
	if 'MultiprocessBool' in _KwargVariablesDict and _KwargVariablesDict['MultiprocessBool']:

		from multiprocessing import Pool
		MapPool=Pool(min(len(_List),100))
		return MapPool.map(_Function,_List)

	else:

		#Check version
		if sys.version[0]==2:
			map(_Function,_List)
		else:
			return list(map(_Function,_List))

	
def range_(*ArgsList):
	if sys.version[0]==2:
		return range(*ArgsList).__iter__()
	else:
		return range(*ArgsList)

def unzip(_TuplesList,_IndexesList):
	PickedList=map_(
				lambda __Tuple:
				map(__Tuple.__getitem__,_IndexesList),
				_TuplesList
			)
	if len(_IndexesList)==1 and len(PickedList)>0:
		return list(zip(*PickedList)[0])
	return zip(*PickedList)

def dictify(_TuplesList,_KeyIndexInt,_ValueIndexInt):
	TuplesList=unzip(_TuplesList,[_KeyIndexInt,_ValueIndexInt])
	return collections.OrderedDict(zip(TuplesList[0],TuplesList[1]))

def listify(_List):
	return map(lambda __ElementVariable:[__ElementVariable],_List)

def where(_DictsList,_TuplesList,**_KwargsDict):

	if 'IsInCheckingBool' in _KwargsDict and _KwargsDict['IsInCheckingBool']:

		return map(
						lambda __RowingDict:
						#Say True for the ones that respect all the conditions
						__RowingDict
						if all(
							map(
								lambda __FilteringTuple:
								__FilteringTuple[1][0](__RowingDict[__FilteringTuple[0]],__FilteringTuple[1][1])
								#Check that the Key exists...Can maybe make slower the process....
								if __FilteringTuple[0] in __RowingDict else False
								,_TuplesList
								)
							)
						#set None either
						else None,
						_DictsList
					)

	else:

		return map(
						lambda __RowingDict:
						#Say True for the ones that respect all the conditions
						__RowingDict
						if all(
							map(
								lambda __FilteringTuple:
								__FilteringTuple[1][0](__RowingDict[__FilteringTuple[0]],__FilteringTuple[1][1])
								,_TuplesList
								)
							)
						#set None either
						else None,
						_DictsList
					)



def getStrsListWithBeginStrAndEndStrAndStrsIntAndStr(
		_BeginStr,_EndStr,_StrsInt,_Str,**_KwargVariablesDict):
	
	#set the PickedStrsList
	PickedStrsList=[]
	
	#CountsInt
	if _StrsInt=="All":
		CountsInt=1
	else:
		CountsInt=_StrsInt

	#Scan the Strs
	StrInt=0
	while StrInt<CountsInt:
	
		#Get With the Beginning
		BeginSplittedPickedStr=_Str.split(_BeginStr)
		
		#Check that there is this Flag
		if len(BeginSplittedPickedStr)>1:
		
			#Join the End
			PickedStr=_BeginStr.join(BeginSplittedPickedStr[1:])
			
			#SplittedPickedStr by the EndStr
			EndSplittedPickedStr=PickedStr.split(_EndStr)
			
			#Record if it not the EndStr in the FlagsDict !
			if EndSplittedPickedStr[0]!='",\'EndStr\':"':
			
				#Record the PickedStr
				PickedStrsList.append(EndSplittedPickedStr[0])

			#set the new Str
			_Str=_EndStr.join(EndSplittedPickedStr[1:])

		#Increment
		StrInt+=1

		#Special All Case
		if _StrsInt=="All" and len(BeginSplittedPickedStr)>1:
			StrInt-=1
	
	#Return '' by default
	return PickedStrsList

def sign(_Variable):
	if _Variable<0:
		return -1
	else:
		return 1

def chunk(_LimitStrsList,_TextStr,**_KwargVariablesDict):
	if 'ChunksInt' in _KwargVariablesDict:
		ChunksInt=_KwargVariablesDict['ChunksInt']
	else:
		ChunksInt=1
	return getStrsListWithBeginStrAndEndStrAndStrsIntAndStr(
		_LimitStrsList[0],_LimitStrsList[1],ChunksInt,_TextStr,**_KwargVariablesDict)

def deprefix(_WordStr,_PrefixStr):
	return _PrefixStr.join(_WordStr.split(_PrefixStr)[1:])

def desuffix(_WordStr,_SuffixStr):
	return _SuffixStr.join(_WordStr.split(_SuffixStr)[:-1])

def groupby(_FunctionPointer,_List):
	return getSplitListsListWithSplittedListAndFunctionPointer(_List,_FunctionPointer)

def itemizable(_Variable):
	return hasattr(_Variable,'items') or hasattr(_Variable,'__dict__')

def previous(_PathStr,_SplitStr='/'):

	#split
	WordStrsList=_PathStr.split(_SplitStr)

	#Check
	if len(WordStrsList)>0:
		return _SplitStr.join(WordStrsList[:-1]),WordStrsList[-1]
	else:
		return _SplitStr

def update(_ItemizableVariable,_UpdateVariable):

	#Check
	if hasattr(_ItemizableVariable,'items'):
		_ItemizableVariable.update(_UpdateVariable)
	else:
		_ItemizableVariable['#map@set'](_UpdateVariable)

	#return
	return _ItemizableVariable

def set(_Variable,_KeyStr,_ValueVariable):

	#set
	setattr(
			_Variable,
			_KeyStr,
			_ValueVariable
		)

	#return 
	return getattr(_Variable,_KeyStr)

def getIsTuplesListBool(_TuplesList):

	#Check for list of tuples
	if type(_TuplesList)==list:
		return all(
					map(
							lambda __Tuple:
							type(__Tuple)==tuple,
							_TuplesList
						)
					)

	#Return False either
	return False

def getIsListsListBool(_ListsList):

	#Check for list of list
	if type(_ListsList)==list:
		return all(
					map(
							lambda __List:
							type(__List)==list,
							_ListsList
						)
					)

	#Return False either
	return False

def getSingularStrWithPluralStr(_PluralStr):
	return _PluralStr[:-1]

def getIsEqualBool(_VariableA,_VariableB):
		
	#debug
	'''
	print('getIsEqualBool Avant')
	print('_VariableA is',_VariableA)
	print('_VariableB is ',_VariableB)
	print('')
	'''

	#import
	import numpy

	#Cast maybe into numpy array before
	if type(_VariableA)==numpy.ndarray and type(_VariableB)==list:
		_VariableB=numpy.array(_VariableB)
	elif type(_VariableB)==numpy.ndarray and type(_VariableA)==list:
		_VariableA=numpy.array(_VariableA)

	#debug
	'''
	print('getIsEqualBool Apres')
	print('_VariableA is',_VariableA)
	print('_VariableB is ',_VariableB)
	print('')
	'''

	#Then do the equal process
	if numpy.ndarray not in map(type,[_VariableA,_VariableB]):

		#special unicode case
		if type(_VariableA)==unicode:
			_VariableA=str(_VariableA)
		if type(_VariableB)==unicode:
			_VariableB=str(_VariableB)	

		#return
		return _VariableA==_VariableB

	elif len(_VariableA)!=len(_VariableB):
		
		#return
		return False
		
	else:

		#return
		return all(
					map(
						lambda __ArrayingInt:
						getIsEqualBool(_VariableA[__ArrayingInt],_VariableB[__ArrayingInt]),
						range_(len(_VariableA))
					))

def getIsInListBool(_ContainedVariable,_ContainingList):

	#debug
	'''
	print('getIsInListBool function')
	print('_ContainedVariable is ',_ContainedVariable)
	print('_ContainingList is ',_ContainingList)
	print('')
	'''

	return any(
				map(
					lambda __ListedVariable:
					getIsEqualBool(_ContainedVariable, __ListedVariable),
					_ContainingList
				)
			)

def getSplitListsListWithSplittedListAndFunctionPointer(_SplittedList,_FunctionPointer):

	#Init the SplitListsList
	SplitListsList=[[],[]]

	#do the map with side effect
	map(
			lambda ListedVariable:
			SplitListsList[0].append(ListedVariable) 
			if _FunctionPointer(ListedVariable) 
			else SplitListsList[1].append(ListedVariable),
			_SplittedList
		)

	#Return
	return SplitListsList

def getIndexTuplesList(__SizeTuple):

	#numpy
	import itertools

	#map
	return list(
		itertools.product(*map(xrange,__SizeTuple))
	)

def getUnSerializedTuple(_Variable,_SerializedList):

	#debug
	'''
	print('_SerializedList is ',_SerializedList)
	print('')
	'''
	
	#Return 
	return tuple(
					[
						_SerializedList[0],
						type(_Variable[_SerializedList[0]])(_SerializedList[1])
					]
				)

def getProcessIdStrsListWithProcessNameStr(_ProcessNameStr):

	return map(
				lambda __LineStr:
				__LineStr.split(' ')[3],
				_filter(
					lambda __LineStr:
					'.py' in __LineStr,
					os.popen(
						"ps -ef | grep "+_ProcessNameStr
					).read().split('\n')
				)
			)

def setGUI(*_LiargVariablesList):
	from ShareYourSystem.Standards.Controllers import Systemer

def lib():

	#join
	SetupFilePathStr='/'.join(__file__.split('/')[:-1])+'/lib.py'

	#open
	SetupFile=open(SetupFilePathStr,'r')

	#chunk
	InstalledPackageStr=chunk(
			['packages=[','],'],SetupFile.read()
		)[0]

	#close
	SetupFile.close()
	
	#filter
	InstalledTextStrsList=InstalledPackageStr.split('\n')
	InstalledTextStrListsList=_filter(
		lambda __InstalledChunkList:
		len(__InstalledChunkList)>0,
		map(
				lambda __InstalledTextStr:
				chunk(
					["'ShareYourSystem","',"],
					__InstalledTextStr
				),
				InstalledTextStrsList
		)
	)

	#return
	return map(
		lambda __InstalledTextStrList:
		('ShareYourSystem'+__InstalledTextStrList[0])
		if __InstalledTextStrList[0]!="'"
		else 'ShareYourSystem',
		InstalledTextStrListsList
	)[:-1]
#</DefineFunctions>

#<DefineLocals>
SingularStrToPluralStrOrderedDict=dictify(ConceptStrsTuplesList,0,1)
PluralStrToSingularStrOrderedDict=dictify(ConceptStrsTuplesList,1,0)

class ClassesList(list):

	def __init__(self,_ClassVariable=None):
		
		#call the base 
		list.__init__(self)

		#/#################/#
		# Adapt the shape of the args
		#

		#Check
		if type(_ClassVariable)!=list:

			#Check
			if _ClassVariable==None:

				#/#################/#
				# Give all the mro doer
				#

				#alias
				self.extend(_InstanceVariable.__class__.MroDoerClassesList)

			elif type(_ClassVariable)==str:
				
				#get
				_ClassVariable=getattr(
						sys.modules['ShareYourSystem'],
						getClassStrWithNameStr(_ClassVariable)
				)

				#listify
				self.append(_ClassVariable)

			else:

				#listify
				self.append(_ClassVariable)

		else:

			#map
			_ClassVariable=map(
					lambda __ElementVariable:
					getattr(
						sys.modules['ShareYourSystem'],
						getClassStrWithNameStr(__ElementVariable)
					) if type(__ElementVariable)==str else __ElementVariable,
					_ClassVariable
				)

			#extend
			self.extend(_ClassVariable)


class GetList(list):

	def __init__(self,_ListVariable=None,_GetterVariable=None):
		
		#call the base 
		list.__init__(self)

		#init
		self.ListVariable=_ListVariable
		self.GetterVariable=_GetterVariable

		#Check
		if hasattr(self.GetterVariable,'__getitem__'):
			GetMethod=getattr(
				self.GetterVariable,
				'__getitem__'
			)
		else:
			GetMethod=lambda __KeyVariable:getattr(
				self.GetterVariable,
				__KeyVariable
			) if type(__KeyVariable)==str else __KeyVariable

		#init
		if self.ListVariable==None:
			self.ListVariable=[]

		#Check
		if type(self.ListVariable)!=list:
			
			#debug
			'''
			self.debug(
				[
					'We get nicely',
					('self.',self,['CommandingGetVariable'])
				]
			)
			'''

			#Check
			if self.GetterVariable!=None:

				#get
				ValueVariable=GetMethod(
						self.ListVariable
					)
			else:

				#alias
				ValueVariable=self.ListVariable

			#Check
			if type(ValueVariable)!=list:
				ValueVariable=[ValueVariable]

		else:

			#Check
			if self.GetterVariable!=None:

				#map a get
				ValueVariable=map(
						lambda __ElementVariable:
						GetMethod(__ElementVariable),
						self.ListVariable
					)
			else:

				#alias
				ValueVariable=self.ListVariable

		#Debug
		'''
		print('SYS GetList')
		print('ValueVariable is ')
		print(ValueVariable)
		print('')
		'''

		#flat maybe
		ValueVariable=flat(ValueVariable)

		#filter
		self.extend(filterNone(ValueVariable))

class SetList(list):

	def __init__(self,_ListVariable=None):

		#call the base 
		list.__init__(self)

		#init
		self.ListVariable=_ListVariable

		#init
		if self.ListVariable==None:
			self.ListVariable=[]

		#Check
		if type(self.ListVariable)!=list:
			
			#Check
			if hasattr(self.ListVariable,'items'):

				#items
				self.extend(self.ListVariable.items())

			elif type(self.ListVariable)==tuple and len(self.ListVariable)==2:

				#append the tuple
				self.append(self.ListVariable)

			else:

				#list
				self.append(
					('get',self.ListVariable)
				)

		else:

			#adapt
			self.ListVariable=map(
					lambda __ElementVariable:
					__ElementVariable
					if type(__ElementVariable) in [list,tuple]
					else ('get',__ElementVariable),
					self.ListVariable
				)

			#alias
			self.extend(self.ListVariable.__iter__())

class MethodDict(collections.OrderedDict):

	def __init__(self,_Class=None):

		#set
		self.Class=_Class

		#init
		collections.OrderedDict.__init__(self)

		#init
		self.MethodKeyStrsList=[]
		self.UnboundMethodsList=[]

		#Check
		if _Class!=None:

			"""
			print(
				"\n".join(
					map(
						lambda __KeyStr:
						str((__KeyStr,type(getattr(_Class,__KeyStr)))),
						dir(_Class)
					)
				)
			)
			"""

			#filter
			self.MethodKeyStrsList=_filter(
				lambda __KeyStr:
				type(
					getattr(
						_Class,
						__KeyStr
					)
				).__name__=='instancemethod',
				dir(_Class)
			)

			#map
			self.UnboundMethodsList=map(
					lambda __MethodKeyStr:
					getattr(_Class,__MethodKeyStr),
					self.MethodKeyStrsList
				)

		#update
		self.update(
			zip(
					self.MethodKeyStrsList,
					self.UnboundMethodsList
				)
		)

class ArgumentDict(collections.OrderedDict):

	def __init__(self,_Function=None):

		#set
		self.Function=_Function

		#init
		collections.OrderedDict.__init__(self)

		#Check
		if _Function!=None:

			#Unpack
			InputKeyStrList,ArgVariablesListKeyStr,KwargsVariablesSetTagStr,DefaultVariablesList=inspect.getargspec(
				_Function
			)

			#debug
			'''
			print('InputKeyStrList is',InputKeyStrList)
			print('DefaultVariablesList is',DefaultVariablesList)
			print('')
			'''

			#set
			DefaultVariablesList=DefaultVariablesList if DefaultVariablesList!=None else []
		
			#Definition the DefaultIndexInt
			self['DefaultIndexInt']=len(InputKeyStrList)-len(DefaultVariablesList)

			#set the ArgumentOrderedDict
			self.update(
				[
					('InputKeyStrsList',InputKeyStrList),
					('LiargVariablesListKeyStr',ArgVariablesListKeyStr if ArgVariablesListKeyStr!=None else ""),
					('KwargVariablesSetTagStr',KwargsVariablesSetTagStr if KwargsVariablesSetTagStr!=None else ""),
					('DefaultOrderedDict',collections.OrderedDict(
						zip(
							InputKeyStrList[self['DefaultIndexInt']:],
							DefaultVariablesList
							)
						)
					),
					('FunctionNameStr',_Function.__name__)
				]
			)
#</DefineLocals>

#<DefineClass>
class ShareYourSystem():

	def __init__(self,_WrapModule):

		#Bind the Module
		self.__dict__['WrapModule']=_WrapModule

		#Get the library ref
		_WrapModule.ModuleStrsList=lib()
		_WrapModule.NameStrsList=map(
			lambda __ModuleStr:
			__ModuleStr.split('.')[-1],
			_WrapModule.ModuleStrsList
		)
		_WrapModule.ClassStrsList=map(getClassStrWithNameStr,_WrapModule.NameStrsList)

	def __setattr__(self,_KeyVariable,_ValueVariable):
		
		'''
		#Give it the IdInt
		if hasattr(_ValueVariable,'IdInt'):
			_ValueVariable.IdInt=id(_ValueVariable)
			_ValueVariable.SysStr=_KeyVariable

		#set
		self.__dict__[_KeyVariable]=_ValueVariable
		'''

		#Give it to the Module
		setattr(
					self.__dict__['WrapModule'],
					_KeyVariable,
					_ValueVariable
			)

	def __getattr__(self,_KeyVariable):

		#alias
		WrapModule=self.__dict__['WrapModule']

		#VERY pretentious way of accessing 
		#numpy, matplotlib operator functions as if it was in the SYS library...
		#(but it's then simpler as the pylab module)
		if _KeyVariable=='array':
			import numpy
			return numpy.array
		elif _KeyVariable=='contains':
			return operator.contains
		elif _KeyVariable in ['plot','show']:
			from matplotlib import pyplot
			return getattr(pyplot,_KeyVariable)

		#Check for maybe automatically importing submodules
		if hasattr(WrapModule,_KeyVariable)==False:

			#Debug
			'''
			print('SYS l. 889')
			print('SYS has not this _KeyVariable')
			print('_KeyVariable is ',_KeyVariable)
			print('')
			'''

			#Check for special methods
			if _KeyVariable in ['_print','_str']:
				from ShareYourSystem.Standards.Interfacers import Printer
				return getattr(WrapModule,_KeyVariable)

			#Check
			if _KeyVariable.endswith('Class'):

				#Debug
				'''
				print('SYS l. 898')
				print('it looks like a class')
				print('')
				'''

				#try
				try:

					#get
					ValueModuleStr=WrapModule.ModuleStrsList[
							WrapModule.ClassStrsList.index(_KeyVariable)
						]

					#Debug
					'''
					print('SYS l. 948')
					print('ValueModuleStr is '+ValueModuleStr)
					print('')
					'''
					
					#import
					ValueModule=importlib.import_module(ValueModuleStr)

					#return
					return getattr(ValueModule,_KeyVariable)

				except:
					
					#print
					'''
					print('l 941 SYS')
					print('No _KeyVariable like')
					print(_KeyVariable)
					print('')
					'''

					#raise
					raise AttributeError

			#Check for a SYS module call
			else:

				#try
				try:

					#get
					ValueModuleStr=WrapModule.ModuleStrsList[
							WrapModule.NameStrsList.index(_KeyVariable)
						]

					#import
					ValueModule=importlib.import_module(ValueModuleStr)

					#return
					return ValueModule

				except:

					#Check for a non SYS module call
					try:

						#import
						ValueModule=importlib.import_module(_KeyVariable)

						#return
						return ValueModule

					except:

						#print
						'''
						print('l 1050 SYS')
						print('No _KeyVariable like')
						print(_KeyVariable)
						print('WrapModule.NameStrsList is ')
						print(WrapModule.NameStrsList)
						print('WrapModule.ModuleStrsList is ')
						print(WrapModule.ModuleStrsList)
						'''

						#raise
						raise AttributeError
						
		else:

			#return 
			return getattr(WrapModule,_KeyVariable)

#set
sys.modules[__name__]=ShareYourSystem(sys.modules[__name__])
#</DefineClass>




