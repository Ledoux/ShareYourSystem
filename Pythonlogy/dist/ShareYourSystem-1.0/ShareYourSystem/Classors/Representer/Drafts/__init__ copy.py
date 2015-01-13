#<ImportSpecificModules>
import collections
import copy
import inspect
import numpy

from ShareYourSystem.Objects import Initiator
,Inspecter
import importlib
BaseModule=Inspecter
DecorationModule=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
SYS.setSubModule(globals())

RepresentingDictIndentStr="  "
RepresentingListIndentStr="  "
RepresentingIndentStr="   /"
RepresentingEofStr="\n"
RepresentingIdBool=True
RepresentedAlineaStr=""
#</DefineLocals>

#<DefineFunctions>
def getRepresentedNumpyArray(_NumpyArray):

	#Definition the ShapeList
	ShapeList=list(numpy.shape(_NumpyArray))

	#debug
	'''
	print('Representer l.25 : getRepresentedNumpyArray')
	print('ShapeList is',ShapeList)
	print('')
	'''

	#Return the array directly if it is small or either a short represented version of it
	if (len(ShapeList)==1 and ShapeList[0]<3) or (len(ShapeList)>1 and ShapeList[1]<3):
		return str(_NumpyArray)
	return "<numpy.ndarray shape "+str(ShapeList)+">" 
											
def getRepresentedPointerStrWithVariable(_Variable,**_KwargVariablesDict):

	#debug
	'''
	print('Representer l.39 : getRepresentedPointerStrWithVariable')
	print('')
	'''

	#set in the _KwargVariablesDict
	if 'RepresentedDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['RepresentedDeepInt']=0

	#Definition the Local alinea
	RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

	if RepresentingIdBool:
		return RepresentedLocalAlineaStr+"<"+(
			_Variable.__name__ if hasattr(_Variable,__name__) else ""
			)+" ("+_Variable.__class__.__name__+"), "+str(id(_Variable))+">"
	else:
		return RepresentedLocalAlineaStr+"<"+(
			_Variable.__name__ if hasattr(_Variable,__name__) else ""
			)+" ("+_Variable.__class__.__name__+")"+" >"

def getRepresentedStrWithDictatedVariable(
	_DictatedVariable,**_KwargVariablesDict
	):
	
	#set in the _KwargVariablesDict
	if 'RepresentedDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['RepresentedDeepInt']=0

	#debug
	'''
	print('Representer l.59 : getRepresentedStrWithDictatedVariable')
	print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	print('')
	'''

	#Global
	global RepresentedAlineaStr

	#Definition the LocalRepresentedAlineaStr
	LocalRepresentedAlineaStr=RepresentedAlineaStr+"".join(
		[RepresentingIndentStr]*(_KwargVariablesDict['RepresentedDeepInt']))

	#Init the RepresentedDictStr
	RepresentedDictStr="\n"+LocalRepresentedAlineaStr+"{ "

	#Scan the Items (integrativ loop)
	if type(_DictatedVariable)==collections.OrderedDict:
		TuplesList=_DictatedVariable.items()
	else:
		TuplesList=sorted(_DictatedVariable.iteritems(), key=lambda key_value: key_value[0])

	#Integrativ loop for seriaizing the items
	for KeyStr,ValueVariable in TuplesList:
	
		#set the begin of the line
		RepresentedDictStr+="\n"+LocalRepresentedAlineaStr+RepresentingDictIndentStr

		#Force the cast into Str
		if type(KeyStr) not in [unicode,str]:
			KeyStr=str(KeyStr)

		#Get the WordStrsList
		WordStrsList=SYS.getWordStrsListWithStr(KeyStr)

		#Init the RepresentedValueVariableStr
		RepresentedValueVariableStr="None"

		#Split the case if it is a pointing variable or not
		if len(WordStrsList)>0:

			#Value is displayed
			if SYS.getWordStrsListWithStr(KeyStr)[-1]=="Pointer":
			
				#Pointer Case
				RepresentedValueVariableStr=getRepresentedPointerStrWithVariable(
												ValueVariable,
												**_KwargVariablesDict
											)
											
			elif ''.join(SYS.getWordStrsListWithStr(KeyStr)[-2:])=="PointersList":
			
				#Pointer Case
				RepresentedValueVariableStr=str(
						map(
								lambda ListedVariable:
								getRepresentedPointerStrWithVariable(
									ListedVariable,
									**_KwargVariablesDict),
								ValueVariable
							)
						)
				
		#Special Suffix Cases
		if RepresentedValueVariableStr=="None":
				
			#Other Cases
			RepresentedValueVariableStr=represent(
				ValueVariable,**_KwargVariablesDict
				)

		#Key and Value Case
		RepresentedDictStr+="'"+KeyStr+"' : "+RepresentedValueVariableStr

	#Add a last line
	RepresentedDictStr+="\n"+LocalRepresentedAlineaStr+"}"

	#return the DictStr
	return RepresentedDictStr

def getRepresentedStrWithListedVariable(_ListedVariable,**_KwargVariablesDict):	

	#Global
	global RepresentedAlineaStr

	#set in the _KwargVariablesDict
	if 'RepresentedDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['RepresentedDeepInt']=0

	#debug
	'''
	print('Representer l.166 : getRepresentedStrWithListedVariable')
	print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	print('_ListedVariable is '+str(_ListedVariable))
	print('')
	'''

	#Init the RepresentedDictStr
	if type(_ListedVariable)==list:
		BeginBracketStr='['
		EndBracketStr=']'
	else:
		BeginBracketStr='('
		EndBracketStr=')'

	#Definition the LocalRepresentedAlineaStr
	LocalRepresentedAlineaStr=RepresentedAlineaStr+"".join(
		[RepresentingIndentStr]*(_KwargVariablesDict['RepresentedDeepInt']))

	#Do the first Jump
	RepresentedListStr="\n"+LocalRepresentedAlineaStr+BeginBracketStr
	
	#Scan the Items (integrativ loop)
	for ListedVariableInt,ListedVariable in enumerate(_ListedVariable):
	
		#set the begin of the line
		RepresentedListStr+="\n"+LocalRepresentedAlineaStr+RepresentingListIndentStr

		#Get the represented version
		RepresentedValueVariableStr=represent(
				ListedVariable,**dict(_KwargVariablesDict,**{'RepresentingAlineaIsBool':False}))
			
		#Key and Value Case
		RepresentedListStr+=str(ListedVariableInt)+" : "+RepresentedValueVariableStr

	#Add a last line
	RepresentedListStr+="\n"+LocalRepresentedAlineaStr+EndBracketStr

	#return the DictStr
	return RepresentedListStr

def getRepresentedStrWithVariable(_Variable,**_KwargVariablesDict):

	#set in the _KwargVariablesDict
	if 'RepresentedDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['RepresentedDeepInt']=0

	#debug
	'''
	print('Representer l.213 : getRepresentedStrWithVariable')
	print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	print('_Variable is '+str(_Variable))	
	print("hasattr(_Variable,'__repr__') is "+str(hasattr(_Variable,"__repr__")))
	if hasattr(_Variable,"__repr__"):
		print('hasattr(_Variable.__class__,"InspectedOrderedDict") is '+str(
			hasattr(_Variable.__class__,"InspectedOrderedDict")))
		if hasattr(_Variable.__class__,"InspectedOrderedDict"):
			print("_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesDictKeyStr'] is "+str(
				_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesDictKeyStr']))	
			print(_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesDictKeyStr'])
	print('')
	'''

	#Dict types print
	if type(_Variable) in [dict,collections.OrderedDict]:

		#Increment the deep
		_KwargVariablesDict['RepresentedDeepInt']+=1

		#debug
		'''
		print('This is a dictated type so get a represent like a dict')
		print('')
		'''

		#Return 
		return getRepresentedStrWithDictatedVariable(_Variable,**_KwargVariablesDict)

	#List types print
	elif type(_Variable) in [list,tuple]:

		#debug
		'''
		print('This is a listed type so get a represent like a list')
		print('')
		'''

		#Check if it is a List of Objects or Python Types
		if all(
				map(
					lambda ListedVariable:
					type(ListedVariable) in [float,int,str,unicode,numpy.float64],
					_Variable
					)
			)==False:

			#Increment the deep
			_KwargVariablesDict['RepresentedDeepInt']+=1

			#debug
			'''
			print('Print a represented version of the list')
			print('')
			'''

			#Return 
			return getRepresentedStrWithListedVariable(_Variable,**_KwargVariablesDict)

		else:

			#debug
			'''
			print('Here just print the list directly')
			print('')
			'''

			#Definition the Local alinea
			RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

			#Return 
			return RepresentedLocalAlineaStr+repr(
				_Variable).replace("\n","\n"+RepresentedLocalAlineaStr)

	#Instance print
	elif type(_Variable).__name__ in ["instancemethod"]:

		#Definition the Local alinea
		RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

		#return RepresentedAlineaStr+"instancemethod"
		return RepresentedLocalAlineaStr+_Variable.__repr__().split('of')[0]+">"

	#Str types
	elif type(_Variable) in SYS.StrTypesList:

		#debug
		'''
		print('This is a Str type so get a represent like a Str')
		print('')
		'''

		#Definition the Local alinea
		RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

		#Return
		return RepresentedLocalAlineaStr+_Variable.replace("\n","\n"+RepresentedLocalAlineaStr)

	#Other
	elif hasattr(_Variable,"__repr__") and hasattr(
		_Variable.__class__,"InspectedOrderedDict") and '__repr__' in _Variable.__class__.InspectedOrderedDict and _Variable.__class__.InspectedOrderedDict[
		'__repr__']['KwargVariablesDictKeyStr']!="":

		#debug
		'''
		print('This is a representer so call the repr of it with the _KwargVariablesDict')
		print('')
		'''
		
		#Return the repr of the _Variable but shifted with the RepresentedAlineaStr
		return _Variable.__repr__(**_KwargVariablesDict)

	else:

		#debug
		'''
		print('This is not identified so call the repr of it')
		print('')
		'''

		#Definition the Local alinea
		RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

		#Return a repr of the _Variable but shifted with the RepresentedAlineaStr
		return RepresentedLocalAlineaStr+repr(_Variable).replace("\n","\n"+RepresentedLocalAlineaStr)

def _print(_Variable,**_KwargVariablesDict):
	print(represent(_Variable,**_KwargVariablesDict))
def represent(_Variable,**_KwargVariablesDict):

	#Definition the global
	global RepresentedAlineaStr

	#Represent without shifting the Strs or not
	if 'RepresentingAlineaIsBool' not in _KwargVariablesDict or _KwargVariablesDict['RepresentingAlineaIsBool']:
		return getRepresentedStrWithVariable(_Variable,**_KwargVariablesDict)
	else:
		RepresentedOldAlineaStr=RepresentedAlineaStr
		RepresentedAlineaStr=""
		RepresentedStr=getRepresentedStrWithVariable(_Variable,**_KwargVariablesDict)
		RepresentedAlineaStr=RepresentedOldAlineaStr
		return RepresentedStr

#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class RepresenterClass(BaseClass):
	
	def default_init(self,**_KwargVariablesDict):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Representer l.341 : _Class is ',_Class)
		print('')
		'''

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#Represent
		self.represent(self.ClassingClass)

		#Return
		return self.ClassingClass

	def represent(self,_Class):

		#debug
		'''
		print('Representer l.352 : _Class is ',_Class)
		print('')
		'''

		#set in the class the represented key Strs if not already
		RepresentedBoolKeyStr='Represented'+self.ClassingClass.NameStr+'Bool'

		#debug
		'''
		print('RepresentedBoolKeyStr is ',RepresentedBoolKeyStr)
		print('hasattr(_Class,"RepresentedBoolKeyStr") is ',hasattr(_Class,RepresentedBoolKeyStr
			))
		print('')
		'''

		#Check
		if hasattr(_Class,RepresentedBoolKeyStr
			)==False or getattr(_Class,RepresentedBoolKeyStr)==False:

			#Look for specific Dict
			_Class.RepresentedSpecificKeyStrsList=[]

			#Definition the RepresentedSourceStr
			RepresentedSourceStr=_Class.SourceStr
				
			#debug
			'''
			print('Representer l.367 : RepresentedSourceStr is ',RepresentedSourceStr)
			print('')
			'''

			#Check that there is a '<DefineSpecificDo>' part
			_Class.RepresentedSpecificKeyStrsList=_Class.DoSpecificKeyStrsList
			if len(_Class.RepresentedSpecificKeyStrsList)>0:
				_Class.RepresentedNotGettingStrsList=map(
						lambda _KeyStr:
						_KeyStr.split('=')[0],
						SYS._filter(
								lambda __ExpressionStr:
									"<NotRepresented>" in __ExpressionStr and "=" in __ExpressionStr and __ExpressionStr[0] not in ['\n'],
									_Class.SpecificDoStr.split('self.')
								)
						)
			else:
				_Class.RepresentedNotGettingStrsList=[]
					
			'''
			elif self.NameStr=='Representer':
				_Class.RepresentedSpecificKeyStrsList=[
															'RepresentedNotGettingVariablesList',
															'RepresentingKeyVariablesList',
															'RepresentedTuplesList'
														]
				_Class.RepresentedNotGettingStrsList=[
															'RepresentedNotGettingVariablesList',
															'RepresentingKeyVariablesList',
															'RepresentedTuplesList'
														]
			'''

			#Get the BasedKeyStrsList
			_Class.RepresentedBasedKeyStrsList=list(SYS.collect(
											_Class,
											'__bases__',
											'RepresentedSpecificKeyStrsList'
											))

			#debug
			'''
			print(
					_Class.__name__,
					#Class.__mro__,
					#Class.RepresentedNotGettingStrsList,
					list(_Class.RepresentedBasedKeyStrsList)
					)
			'''


			#set in the class
			setattr(_Class,RepresentedBoolKeyStr,True)

			#Definition the representing methods
			def represent(_InstanceVariable,**_KwargVariablesDict):
		
				#Refresh the attributes
				RepresentedTuplesList=_InstanceVariable.__dict__.items()

				#Remove the class NotRepresented attributes
				RepresentedTuplesList=filter(
												lambda _RepresentedTuple:
												_RepresentedTuple[0] not in _Class.RepresentedNotGettingStrsList,
												RepresentedTuplesList
										)

				#Remove the instance NotRepresented attributes
				#RepresentedTuplesList=filter(
				#								lambda _RepresentedTuple:
				#								_RepresentedTuple[0] not in _InstanceVariable.RepresentedNotGettingVariablesList,
				#								RepresentedTuplesList
				#						)

				#First keeps only the Specific and New attributes
				RepresentedTuplesList=map(
											lambda _RepresentedTuple:
											("<Spe>"+_RepresentedTuple[0],_RepresentedTuple[1]),
											filter(
													lambda _Tuple:
													_Tuple[0] in _Class.RepresentedSpecificKeyStrsList,
													RepresentedTuplesList
												)
										)+map(
											lambda _NewTuple:
											("<New>"+_NewTuple[0],_NewTuple[1]),
											filter(
													lambda _Tuple:
													_Tuple[0] not in _Class.RepresentedBasedKeyStrsList
														+_Class.RepresentedSpecificKeyStrsList,
													RepresentedTuplesList
												)
										)

				#Add some forced Values with the instance RepresentingKeyVariables
				#RepresentedTuplesList+=map(
				#									lambda _KeyVariable:
				#									("<NotSpe>"+str(_KeyVariable),_InstanceVariable[_KeyVariable]),
				#									_InstanceVariable.RepresentingKeyVariablesList
				#								)

				#Simplify the numpy variables repr
				'''
				RepresentedTuplesList=map(
												lambda _RepresentedTuple:
												_RepresentedTuple
												if type(_RepresentedTuple[1]) not in [numpy.ndarray] 
												else (
														_RepresentedTuple[0],
														getRepresentedNumpyArray(_RepresentedTuple[1])
													),
												RepresentedTuplesList
											)
				'''
				#return the representedVariable
				return 	getRepresentedPointerStrWithVariable(_InstanceVariable
						)+getRepresentedStrWithVariable(
									dict(RepresentedTuplesList),**_KwargVariablesDict)

			#Bound and set in the InspectedOrderedDict
			_Class.__repr__=represent
			_Class.InspectedOrderedDict['__repr__']=Inspecter.getInspectedOrderedDictWithFunction(
				_Class.__repr__)
#</DefineClass>

#set in the InitiatorClass
Initiator.InitiatorClass.RepresentedNotGettingStrsList=['InitiatingUpdateBool']
Initiator.InitiatorClass.RepresentedSpecificKeyStrsList=['InitiatingUpdateBool']
