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
	('Applyier','Applyiers'),
	('Walker','Walkers'),
	('Noder','Noders'),
	('Storer','Storers'),
	('Databaser','Databasers'),
	('Ploter','Ploters'),
	('Tutorials','Tutorials'),
	('Simulater','Simulaters'),
	('Muziker','Muzikers')
]

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
	print('SYS  getIsNoneBool l.168 ')
	print('_Variable is ',_Variable)
	print('type(_Variable) is ',type(_Variable))
	print('')
	'''

	#Define 
	Type=type(_Variable)

	#Check
	import numpy
	if Type!=numpy.ndarray:

		#return
		return type(_Variable)==None.__class__

	else:

		#return 
		return False

def getLocalFolderPathStr(_ModuleVariable):
	return ShareYourSystemLocalFolderPathStr+_ModuleVariable

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

def flat(_VariablesList):
	if len(_VariablesList)>0:
		if type(_VariablesList[0])!=list:
			_VariablesList[0]=[_VariablesList[0]]
		return functools.reduce(
									lambda __FlattedList,__AddedVariable:
									__FlattedList+flat(list(__AddedVariable)) 
									if type(__AddedVariable) in [list,tuple] 
									else __FlattedList+[__AddedVariable],
									_VariablesList
								)
	else:
		return _VariablesList

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

def map_(_Function,_List):
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

def chunk(_LimitStrsList,_TextStr,**_KwargVariablesDict):
	if 'ChunksInt' in _KwargVariablesDict:
		ChunksInt=_KwargVariablesDict['ChunksInt']
	else:
		ChunksInt=1
	return getStrsListWithBeginStrAndEndStrAndStrsIntAndStr(
		_LimitStrsList[0],_LimitStrsList[1],ChunksInt,_TextStr,**_KwargVariablesDict)

def groupby(_FunctionPointer,_List):
	return getSplitListsListWithSplittedListAndFunctionPointer(_List,_FunctionPointer)

def getIsTuplesListBool(_TuplesList):

	#Check for list of tuples
	if type(_TuplesList)==list:
		return all(
					map(
							lambda _Tuple:
							type(_Tuple)==tuple,
							_TuplesList
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
		return _VariableA==_VariableB
	elif len(_VariableA)!=len(_VariableB):
			return False
	else:
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

def getArgumentDictWithFunction(_Function):

	#Unpack
	InputKeyStrList,ArgVariablesListKeyStr,KwargsVariablesDictKeyStr,DefaultVariablesList=inspect.getargspec(_Function)

	#Init the Dict
	ArgumentDict={}

	#debug
	'''
	print('InputKeyStrList is',InputKeyStrList)
	print('DefaultVariablesList is',DefaultVariablesList)
	print('')
	'''

	#set
	DefaultVariablesList=DefaultVariablesList if DefaultVariablesList!=None else []
	
	#Definition the DefaultIndexInt
	ArgumentDict['DefaultIndexInt']=len(InputKeyStrList)-len(DefaultVariablesList)

	#set the ArgumentOrderedDict
	ArgumentDict.update([
							('InputKeyStrsList',InputKeyStrList),
							('LiargVariablesListKeyStr',ArgVariablesListKeyStr if ArgVariablesListKeyStr!=None else ""),
							('KwargVariablesDictKeyStr',KwargsVariablesDictKeyStr if KwargsVariablesDictKeyStr!=None else ""),
							('DefaultOrderedDict',collections.OrderedDict(
								zip(
									InputKeyStrList[ArgumentDict['DefaultIndexInt']:],
									DefaultVariablesList
									)
								)
							)
						])

	#Return
	return ArgumentDict

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


#</DefineFunctions>

#<DefineLocals>
SingularStrToPluralStrOrderedDict=dictify(ConceptStrsTuplesList,0,1)
PluralStrToSingularStrOrderedDict=dictify(ConceptStrsTuplesList,1,0)
#</DefineLocals>

"""
#<DefineClass>
class ShareYourSystem():

	def __init__(self,_Module):
		self.__dict__['Module']=_Module

	def __setattr__(self,_KeyVariable,_ValueVariable):
		
		#Give it the IdInt
		if hasattr(_ValueVariable,'IdInt'):
			_ValueVariable.IdInt=id(_ValueVariable)
			_ValueVariable.SysStr=_KeyVariable

		#set
		self.__dict__[_KeyVariable]=_ValueVariable


	def __getattr__(self,_KeyVariable):
		return getattr(self.Module,_KeyVariable)

sys.modules[__name__]=ShareYourSystem(sys.modules[__name__])
#sys.modules['__main__'].ShareYourSystem=ShareYourSystem(sys.modules[__name__])
#</DefineClass>
"""



