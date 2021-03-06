# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Representer is an important module for beginning to visualize 
the structures of the instanced variables in the environnment.
The idea is to use the indenting representation like in the json.dump
function but with a more suitable (but maybe dirty) access to the 
AlineaStr of each lines of the output, depending on the state 
of the variables. Instances that are created from the decorated class have
a __repr__ method, helping for mentionning for the represented attributes where
do they come from : <Spe> (resp. <Base>) is they were defined at the level of the \_\_class\_\_ 
and <Instance> (resp. <Class>) if they are getted from the <InstanceVariable>.__dict__ 
(resp. <InstanceVariable>.__class__.__dict__)

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Inspecter"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import inspect
import numpy
import sys
from ShareYourSystem.Standards.Objects import Initiator
#</ImportSpecificModules>

#<DefineLocals>
RepresentingDictIndentStr="  "
RepresentingListIndentStr="  "
RepresentingIndentStr="   /"
RepresentingEofStr="\n"
RepresentingIdBool=True
RepresentingCircularStr="{...}"
RepresentedAlineaStr=""
RepresentedAlreadyIdIntsList=[]
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

	#Define
	if type(_Variable).__name__=='Database':
		RepresentedVariableStr=_Variable._Database__name
	else:
		RepresentedVariableStr=_Variable.__name__ if hasattr(_Variable,__name__) else ""

	#Debug
	'''
	print('l 85 Representer')
	print('type(_Variable).__name__ is ')
	print(type(_Variable).__name__)
	print('RepresentedVariableStr is ')
	print(RepresentedVariableStr)
	print('')
	'''

	#Check
	if RepresentingIdBool:
		return RepresentedLocalAlineaStr+"<"+RepresentedVariableStr+" ("+_Variable.__class__.__name__+"), "+str(id(_Variable))+">"
	else:
		return RepresentedLocalAlineaStr+"<"+RepresentedVariableStr+" ("+_Variable.__class__.__name__+")"+" >"

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
	if type(_DictatedVariable)!=dict and hasattr(_DictatedVariable,"items"):
		
		#debug
		'''
		print('l 135 Representer')
		print('_DictatedVariable is ')
		print(_DictatedVariable)
		print('')
		'''
		
		#items
		RepresentedTuplesList=_DictatedVariable.items()
	else:

		#sort
		RepresentedTuplesList=sorted(
			_DictatedVariable.iteritems(), key=lambda key_value: key_value[0]
		)

	#Integrativ loop for seriaizing the items
	for __RepresentedKeyStr,__RepresentedValueVariable in RepresentedTuplesList:
	
		#debug
		'''
		print('Representer l.127')
		print('__RepresentedKeyStr is',__RepresentedKeyStr)
		print('')
		'''

		#set the begin of the line
		RepresentedDictStr+="\n"+LocalRepresentedAlineaStr+RepresentingDictIndentStr

		#Force the cast into Str
		if type(__RepresentedKeyStr) not in [unicode,str]:
			__RepresentedKeyStr=str(__RepresentedKeyStr)

		#Get the WordStrsList
		WordStrsList=SYS.getWordStrsListWithStr(__RepresentedKeyStr)

		#Init the RepresentedValueVariableStr
		RepresentedValueVariableStr="None"

		#Split the case if it is a pointing variable or not
		if len(WordStrsList)>0:

			#Value is displayed
			"""
			if SYS.getWordStrsListWithStr(__RepresentedKeyStr)[-1]=="Pointer":
			
				#Pointer Case
				RepresentedValueVariableStr=getRepresentedPointerStrWithVariable(
												__RepresentedValueVariable,
												**_KwargVariablesDict
											)
			"""
			"""						
			elif ''.join(SYS.getWordStrsListWithStr(__RepresentedKeyStr)[-2:])=="PointersList":
			
				#debug
				'''
				print('__RepresentedValueVariable is ',__RepresentedValueVariable)
				print('')
				'''

				#Pointer Case
				RepresentedValueVariableStr=str(
						map(
								lambda ListedVariable:
								getRepresentedPointerStrWithVariable(
									ListedVariable,
									**_KwargVariablesDict),
								__RepresentedValueVariable
							)
						)  if type(__RepresentedValueVariable)==list else "None"
			"""
			
		#Special Suffix Cases
		if RepresentedValueVariableStr=="None":
				
			#debug
			'''
			print('go to represent')
			print('__RepresentedKeyStr is ',__RepresentedKeyStr)
			print('id(__RepresentedValueVariable) is ',id(__RepresentedValueVariable))
			print('')
			'''

			#Other Cases
			RepresentedValueVariableStr=getRepresentedStrWithVariable(
				__RepresentedValueVariable,
				**_KwargVariablesDict
				)

		#Key and Value Case
		RepresentedDictStr+="'"+__RepresentedKeyStr+"' : "+RepresentedValueVariableStr

	#Add a last line
	RepresentedDictStr+="\n"+LocalRepresentedAlineaStr+"}"

	#debug
	'''
	print('RepresentedDictStr is ',RepresentedDictStr)
	print('')
	'''

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
		RepresentedValueVariableStr=getRepresentedStrWithVariable(
				ListedVariable,**dict(_KwargVariablesDict,**{'RepresentingAlineaIsBool':False})
				)
			
		#Key and Value Case
		RepresentedListStr+=str(ListedVariableInt)+" : "+RepresentedValueVariableStr

	#Add a last line
	RepresentedListStr+="\n"+LocalRepresentedAlineaStr+EndBracketStr

	#return the DictStr
	return RepresentedListStr

def getRepresentedStrWithVariable(_Variable,**_KwargVariablesDict):

	#Define global
	global RepresentedAlreadyIdIntsList

	#set in the _KwargVariablesDict
	if 'RepresentedDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['RepresentedDeepInt']=0

	#debug
	'''
	print('Representer l.213 : getRepresentedStrWithVariable')
	#print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	#print('_Variable is '+str(_Variable))	
	print('type(_Variable) is '+str(type(_Variable)))
	#print("hasattr(_Variable,'__repr__') is "+str(hasattr(_Variable,"__repr__")))
	##if hasattr(_Variable,"__repr__"):
	#	print('hasattr(_Variable.__class__,"InspectedOrderedDict") is '+str(
	#		hasattr(_Variable.__class__,"InspectedOrderedDict")))
	#	if hasattr(_Variable.__class__,"InspectedOrderedDict"):
	#		print("_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesSetKeyStr'] is "+str(
	#			_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesSetKeyStr']))	
	#		print(_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesSetKeyStr'])
	print('')
	'''

	#None type
	if type(_Variable)==None.__class__:
		return "None"

	#Dict types print
	#if type(_Variable) in [dict,collections.OrderedDict]:
	if hasattr(_Variable,'items') and type(_Variable)!=type:

		#Increment the deep
		_KwargVariablesDict['RepresentedDeepInt']+=1

		#debug
		'''
		print('This is a dictated type so get a represent like a dict')
		print('')
		'''

		#id
		RepresentedIdInt=id(_Variable)

		#debug
		'''
		print('RepresentedIdInt is ',RepresentedIdInt)
		print('RepresentedAlreadyIdIntsList is ',RepresentedAlreadyIdIntsList)
		print('')
		'''

		#Check if it was already represented
		if RepresentedIdInt not in RepresentedAlreadyIdIntsList:

			#Debug
			'''
			print('RepresentedAlreadyIdIntsList is ',RepresentedAlreadyIdIntsList)
			print('')
			'''

			#append
			RepresentedAlreadyIdIntsList.append(RepresentedIdInt)

			#Return the repr of the _Variable but shifted with the RepresentedAlineaStr
			RepresentedStr=getRepresentedStrWithDictatedVariable(
						_Variable,
						**_KwargVariablesDict
			)

			
			
		else:

			#Return the circular Str
			RepresentedStr=RepresentingCircularStr+getRepresentedPointerStrWithVariable(_Variable)

		#Debug
		'''
		print('RepresentedIdInt is ',RepresentedIdInt)
		print('RepresentedStr is ',RepresentedStr)
		print('')
		'''
		
		#return 
		return RepresentedStr

	#List types print
	elif type(_Variable) in [list,tuple]:

		#id
		RepresentedIdInt=id(_Variable)

		#Check if it was already represented
		if RepresentedIdInt not in RepresentedAlreadyIdIntsList:

			#debug
			'''
			print('This is a listed type so get a represent like a list')
			print('')
			'''

			#append
			RepresentedAlreadyIdIntsList.append(RepresentedIdInt)

			#Check if it is a List of Objects or Python Types
			if all(
					map(
						lambda ListedVariable:
						type(ListedVariable) in [float,int,str,unicode,numpy.float64] or ListedVariable==None,
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
				RepresentedStr=getRepresentedStrWithListedVariable(_Variable,**_KwargVariablesDict)

			else:

				#debug
				'''
				print('Here just print the list directly')
				print('')
				'''

				#Definition the Local alinea
				RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""

				#Return 
				RepresentedStr=RepresentedLocalAlineaStr+repr(
					_Variable).replace("\n","\n"+RepresentedLocalAlineaStr)


			#return 
			return RepresentedStr

		else:

			#Return the circular Str
			return RepresentingCircularStr+getRepresentedPointerStrWithVariable(_Variable)

	#Instance print
	elif type(_Variable).__name__ in ["instancemethod"]:

		#Debug
		'''
		print('Representer l 421')
		print('This is a method ')
		print('_Variable.__name__ is ',_Variable.__name__)
		print('')
		'''

		#Definition the Local alinea
		RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict['RepresentedDeepInt']==0 else ""
		
		#append
		RepresentedAlreadyIdIntsList.append(_Variable.im_self)

		#return RepresentedAlineaStr+"instancemethod"
		RepresentedStr=RepresentedLocalAlineaStr
		RepresentedStr+="< bound method "+_Variable.__name__
		RepresentedStr+=" of "+str(_Variable.im_self.__class__)
		RepresentedStr+=" "+str(id(_Variable.im_self))+" >"
		#RepresentedStr='inst'

		

		#return
		return RepresentedStr

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
		_Variable.__class__,"InspectedArgumentDict"
		) and '__repr__' in _Variable.__class__.InspectedArgumentDict and _Variable.__class__.InspectedArgumentDict[
		'__repr__']['KwargVariablesSetKeyStr']!="":

		#debug
		'''
		print('This is a representer so call the repr of it with the _KwargVariablesDict')
		print('type(_Variable) is ',type(_Variable))
		print('id(_Variable) is ',id(_Variable))
		print('')
		'''
		
		#id
		RepresentedIdInt=id(_Variable)

		#Check if it was already represented
		if RepresentedIdInt not in RepresentedAlreadyIdIntsList:

			#append
			RepresentedAlreadyIdIntsList.append(RepresentedIdInt)

			#Return the repr of the _Variable but shifted with the RepresentedAlineaStr
			RepresentedStr=_Variable.__repr__(**_KwargVariablesDict)

			#return 
			return RepresentedStr

		else:

			#Return the circular Str
			return RepresentingCircularStr+getRepresentedPointerStrWithVariable(_Variable)

	else:

		#Debug
		'''
		print('This is not identified so call the repr of it')
		print('')
		'''

		#Definition the Local alinea
		RepresentedLocalAlineaStr=RepresentedAlineaStr if _KwargVariablesDict[
			'RepresentedDeepInt']==0 else ""

		#Define 
		RepresentedIdInt=id(_Variable)

		#Debug
		'''
		print('RepresentedIdInt is ',RepresentedIdInt)
		print('RepresentedAlreadyIdIntsList is ',RepresentedAlreadyIdIntsList)
		print('')
		'''

		#Check if it was already represented
		if RepresentedIdInt not in RepresentedAlreadyIdIntsList:

			#debug
			'''
			print('type(_Variable) is ',type(_Variable))
			print('')
			'''

			#Append but only for mutables variable
			if type(_Variable) not in [bool,str,int,float]:
				RepresentedAlreadyIdIntsList.append(RepresentedIdInt)

			else:

				#debug
				'''
				print('_Variable is ',_Variable)
				print('')
				'''
				pass

			#Return a repr of the _Variable but shifted with the RepresentedAlineaStr
			RepresentedStr=RepresentedLocalAlineaStr+repr(_Variable).replace(
										"\n",
										"\n"+RepresentedLocalAlineaStr
									)

			#return 
			return RepresentedStr


		else:

			#Return the circular Str
			return RepresentedLocalAlineaStr+RepresentingCircularStr+getRepresentedPointerStrWithVariable(
				_Variable)

def _print(_Variable,**_KwargVariablesDict):
	print(represent(_Variable,**_KwargVariablesDict))

def represent(_Variable,**_KwargVariablesDict):

	#Definition the global
	global RepresentedAlineaStr,RepresentedAlreadyIdIntsList

	#Debug
	'''
	print('Representer l.545')
	print('Reinit the RepresentedAlreadyIdIntsList')
	print('')
	'''

	#Reinit
	RepresentedAlreadyIdIntsList=[]

	#Debug
	'''
	print('Representer l.554')
	print('_KwargVariablesDict is ',_KwargVariablesDict)
	print('')
	'''
	
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

#Link
def __main__represent(_RepresentingStr,**_KwargVariablesDict):
	return represent(
		_RepresentingStr,
		**dict(_KwargVariablesDict,**{'RepresentingAlineaIsBool':False})
	)
def __main__print(_RepresentingStr,**_KwargVariablesDict):
	return _print(
		_RepresentingStr,
		**dict(_KwargVariablesDict,**{'RepresentingAlineaIsBool':False})
	)
SYS._str = __main__represent
SYS._print = __main__print

#<DefineClass>
@DecorationClass()
class RepresenterClass(BaseClass):
	
	def default_init(self,**_KwargVariablesDict):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#debug
		'''
		print('Representer l.478 : _Class is ',_Class)
		print('')
		'''

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#debug
		'''
		print('Representer l.485 : self.DoClass is ',self.DoClass)
		print('')
		'''

		#Represent
		self.represent()

		#Return
		return _Class

	def do_represent(self):

		#alias
		RepresentedClass=self.DoClass

		#debug
		'''
		print('Representer l.352 : RepresentedClass is ',RepresentedClass)
		print('')
		'''

		#Check
		'''
		if hasattr(RepresentedClass,'RepresentingKeyStrsList')==False or (
			len(RepresentedClass.__bases__)>0 and hasattr(RepresentedClass.__bases__[0
			],'RepresentingKeyStrsList') and RepresentedClass.__bases__[0
			].RepresentingKeyStrsList==RepresentedClass.RepresentingKeyStrsList):
			
			#init
			RepresentedClass.RepresentingKeyStrsList=[]
		'''

		RepresentedClass.RepresentingKeyStrsList=RepresentedClass.DefaultSetKeyStrsList

		#init
		#RepresentedClass.RepresentingSkipKeyStrsList=None

		#init
		#RepresentedClass.RepresentingForceKeyStrsList=None

		#set the BaseKeyStrsList
		KeyStrsSet=set(
			SYS.collect(
					RepresentedClass,
					'__bases__',
					'RepresentingKeyStrsList'
					)
			)
		#KeyStrsSet.difference_update(set(RepresentedClass.RepresentingKeyStrsList))
		RepresentedClass.RepresentedBaseKeyStrsList=list(KeyStrsSet)

		#Split between the one from the class or not
		[
			RepresentedClass.RepresentedSpecificKeyStrsList,
			RepresentedClass.RepresentedNotSpecificKeyStrsList
		]=SYS.groupby(
			lambda __KeyStr:
			__KeyStr not in RepresentedClass.RepresentedBaseKeyStrsList,
			RepresentedClass.RepresentingKeyStrsList
		)

		#debug
		'''
		print(
				RepresentedClass.__name__,
				#Class.__mro__,
				#Class.RepresentedNotGettingStrsList,
				list(RepresentedClass.RepresentedBasedKeyStrsList)
				)
		'''	

		#Add to the KeyStrsList
		RepresentedClass.KeyStrsList+=[
									'RepresentingKeyStrsList',
									'RepresentingSkipKeyStrsList',
									'RepresentingForceKeyStrsList',
									'RepresentedBaseKeyStrsList',
									'RepresentedSpecificKeyStrsList',
									'RepresentedNotSpecificKeyStrsList',
								]

		"""
		#Definition the representing methods
		def represent(_InstanceVariable,**_KwargVariablesDict):
	
			#debug
			'''
			_InstanceVariable.debug(('RepresentedClass',RepresentedClass,[
											'RepresentingKeyStrsList',
											'RepresentedBaseKeyStrsList',
											'RepresentedSpecificKeyStrsList',
											'RepresentedNotSpecificKeyStrsList'
											]))
			'''

			#Represent the Specific KeyStrs
			RepresentedTuplesList=map(
										lambda __RepresentingSpecificKeyStr:
										(
											"<Spe>"+("<Instance>"
											if __RepresentingSpecificKeyStr in _InstanceVariable.__dict__
											else "<Class>"
											)+__RepresentingSpecificKeyStr
											,
											getattr(_InstanceVariable,__RepresentingSpecificKeyStr)
										),
										RepresentedClass.RepresentedSpecificKeyStrsList
									)

			#Represent the BaseKeyStrs
			if 'RepresentingBaseKeyStrsListBool' in _KwargVariablesDict and _KwargVariablesDict['RepresentingBaseKeyStrsListBool']:
				
				RepresentedTuplesList+=map(
										lambda __NotSpecificKeyStrsList:
										(
											"<Base>"+("<Instance>"
											if __NotSpecificKeyStrsList in _InstanceVariable.__dict__
											else "<Class>"
											)+__NotSpecificKeyStrsList
											,
											getattr(_InstanceVariable,__NotSpecificKeyStrsList)
										),
										RepresentedClass.RepresentedNotSpecificKeyStrsList
									)
					
				RepresentedTuplesList+=map(
										lambda __RepresentedBaseKeyStr:
										(
											"<Base>"+("<Instance>"
											if __RepresentedBaseKeyStr in _InstanceVariable.__dict__
											else "<Class>"
											)+__RepresentedBaseKeyStr
											,
											getattr(_InstanceVariable,__RepresentedBaseKeyStr)
										),
										RepresentedClass.RepresentedBaseKeyStrsList
									)

			#Represent the NewInstanceKeyStrs in the __dict__
			if 'RepresentingNewInstanceKeyStrsListBool' not in _KwargVariablesDict or _KwargVariablesDict[
			'RepresentingNewInstanceKeyStrsListBool']:
				
				#filter
				RepresentedNewInstanceTuplesList=SYS._filter(
											lambda __NewItemTuple:
											__NewItemTuple[0] not in RepresentedClass.DefaultSetKeyStrsList+RepresentedClass.DefaultBaseSetKeyStrsList,
											_InstanceVariable.__dict__.items()
										)

				
				#Debug
				'''
				print('RepresentedNewInstanceTuplesList is ')
				print(RepresentedNewInstanceTuplesList)
				print('RepresentedClass.RepresentingSkipKeyStrsList is ')
				print(RepresentedClass.RepresentingSkipKeyStrsList)
				print('')
				'''

				#Check
				if _InstanceVariable.RepresentingSkipKeyStrsList==None:
					_InstanceVariable.RepresentingSkipKeyStrsList=[]

				#filter
				RepresentedNewInstanceTuplesList=SYS._filter(
						lambda __RepresentedNewInstanceTuple:
						__RepresentedNewInstanceTuple[0] not in _InstanceVariable.RepresentingSkipKeyStrsList,
						RepresentedNewInstanceTuplesList
					)

				#Debug
				'''
				print('RepresentedNewInstanceTuplesList is ')
				print(RepresentedNewInstanceTuplesList)
				print('')
				'''

				#map
				RepresentedTuplesList+=map(
											lambda __NewItemTuple:
											(
												"<New><Instance>"+__NewItemTuple[0],
												__NewItemTuple[1]
											),
											RepresentedNewInstanceTuplesList
										)

			#Represent the NewClassKeyStrs in the _RepresentedClass__.__dict__
			if 'RepresentingNewClassKeyStrsListBool' not in _KwargVariablesDict or _KwargVariablesDict[
			'RepresentingNewClassKeyStrsListBool']:

				RepresentedTuplesList+=map(
											lambda __NewKeyStr:
											(
												"<New><Class>"+__NewKeyStr,
												_InstanceVariable.__class__.__dict__[__NewKeyStr]
											),
											SYS._filter(
															lambda __KeyStr:
															__KeyStr not in RepresentedClass.KeyStrsList and __KeyStr not in _InstanceVariable.__dict__,
															SYS.getKeyStrsListWithClass(
																_InstanceVariable.__class__
															)
														)
										)

			if 'RepresentingNotConcludeTuplesList' in _KwargVariablesDict:

				#Debug
				'''
				print('l 792 Representer')
				print('RepresentedTuplesList is ')
				print(RepresentedTuplesList)
				print('')
				'''

				#filter
				RepresentedTuplesList=SYS._filter(
					lambda __RepresentedTuple:
					any(
						map(
							lambda __RepresentingNotConcludeTuple:
							__RepresentingNotConcludeTuple[0](
								__RepresentedTuple,
								__RepresentingNotConcludeTuple[1]
							),
						_KwargVariablesDict['RepresentingNotConcludeTuplesList']
						)
					)==False,
					RepresentedTuplesList
				)

				#Debug
				'''
				print('l 815 Representer')
				print('RepresentedTuplesList is ')
				print(RepresentedTuplesList)
				print('')
				'''
			
			if 'RepresentingKeyStrsList' in _KwargVariablesDict:

				RepresentedTuplesList+=map(
						lambda __RepresentingKeyStr:
						(
							"<Spe><Instance>"+__RepresentingKeyStr,
							_InstanceVariable.__dict__[__RepresentingKeyStr]
						) 
						if __RepresentingKeyStr in _InstanceVariable.__dict__ and __RepresentingKeyStr not in RepresentedClass.DefaultSetKeyStrsList
						else(
								(
									"<Base><Instance>"+__RepresentingKeyStr,
									_InstanceVariable.__dict__[__RepresentingKeyStr]
								) 
								if __RepresentingKeyStr in _InstanceVariable.__dict__ and __RepresentingKeyStr in RepresentedClass.DefaultBaseSetKeyStrsList
								else
								(
									(
										"<Base><Class>"+__RepresentingKeyStr,
										getattr(_InstanceVariable,__RepresentingKeyStr)
									)
									if __RepresentingKeyStr not in _InstanceVariable.__dict__
									else
									(
										"<New><Instance>"+__RepresentingKeyStr,
										_InstanceVariable.__dict__[__RepresentingKeyStr]
									)
								)
						),
						_KwargVariablesDict['RepresentingKeyStrsList'
						]+_InstanceVariable.RepresentingForceKeyStrsList
					)
						


			#Append
			global RepresentedAlreadyIdIntsList

			#debug
			'''
			print('Represener l.629')
			print('id(_InstanceVariable) is ',id(_InstanceVariable))
			print('_InstanceVariable not in RepresentedAlreadyIdIntsList is ',str(
				_InstanceVariable not in RepresentedAlreadyIdIntsList))
			print('')
			'''

			#define the RepresentedStr
			return getRepresentedPointerStrWithVariable(
				_InstanceVariable
					)+getRepresentedStrWithVariable(
							dict(RepresentedTuplesList),
							**_KwargVariablesDict
						)
		"""

		#Bound and set in the InspectedOrderedDict
		#RepresentedClass.__repr__=represent
		#RepresentedClass.InspectedArgumentDict['__repr__']=SYS.ArgumentDict(
		#	RepresentedClass.__repr__)

#</DefineClass>

#set in the InitiatorClass
Initiator.InitiatorClass.RepresentedNotGettingStrsList=['InitiatingUpdateBool']
Initiator.InitiatorClass.RepresentedSpecificKeyStrsList=['InitiatingUpdateBool']
