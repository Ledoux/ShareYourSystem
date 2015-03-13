# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Printer is an object that can directly print 
Strs in the Printer context.

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Interfacer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Doer"
SYS.setSubModule(globals())
SYS.addDo('Printer','_Print','Printing','Printed')
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
#</ImportSpecificModules>

#<DefineLocals>
PrintDictIndentStr="  "
PrintListIndentStr="  "
PrintIndentStr="   /"
PrintEofStr="\n"
PrintIdBool=True
PrintCircularStr="{...}"
PrintAlineaStr=""
PrintAlreadyIdIntsList=[]

def getNumpyArrayStr(_NumpyArray):

	#Definition the ShapeList
	ShapeList=list(numpy.shape(_NumpyArray))

	#debug
	'''
	print('Printer l.25 : getNumpyArrayStr')
	print('ShapeList is',ShapeList)
	print('')
	'''

	#Return the array directly if it is small or either a short represented version of it
	if (len(ShapeList)==1 and ShapeList[0]<3) or (len(ShapeList)>1 and ShapeList[1]<3):
		return str(_NumpyArray)
	return "<numpy.ndarray shape "+str(ShapeList)+">" 
											
def getPointerStr(_Variable,**_KwargVariablesDict):

	#debug
	'''
	print('Printer l.39 : getPointerStr')
	print('')
	'''

	#set in the _KwargVariablesDict
	if 'PrintDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['PrintDeepInt']=0

	#Definition the Local alinea
	PrintedLocalAlineaStr=PrintAlineaStr if _KwargVariablesDict['PrintDeepInt']==0 else ""

	#Define
	if type(_Variable).__name__=='Database':
		PrintedVariableStr=_Variable._Database__name
	elif type(_Variable).__name__=='Collection':
		PrintedVariableStr=_Variable._Collection__name
	else:
		PrintedVariableStr=_Variable.__name__ if hasattr(_Variable,__name__) else ""

	#Debug
	'''
	print('l 85 Printer')
	print('type(_Variable).__name__ is ')
	print(type(_Variable).__name__)
	print('PrintedVariableStr is ')
	print(PrintedVariableStr)
	print('')
	'''

	#Check
	if PrintIdBool:
		return PrintedLocalAlineaStr+"<"+PrintedVariableStr+" ("+_Variable.__class__.__name__+"), "+str(id(_Variable))+">"
	else:
		return PrintedLocalAlineaStr+"<"+PrintedVariableStr+" ("+_Variable.__class__.__name__+")"+" >"

def getDictStr(
	_DictatedVariable,**_KwargVariablesDict
	):
	
	#set in the _KwargVariablesDict
	if 'PrintDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['PrintDeepInt']=0

	#debug
	'''
	print('Printer l.59 : getDictStr')
	print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	print('')
	'''

	#Global
	global PrintAlineaStr

	#Definition the LocalPrintAlineaStr
	LocalPrintAlineaStr=PrintAlineaStr+"".join(
		[PrintIndentStr]*(_KwargVariablesDict['PrintDeepInt']))

	#Init the PrintedDictStr
	PrintedDictStr="\n"+LocalPrintAlineaStr+"{ "

	#Scan the Items (integrativ loop)
	if type(_DictatedVariable)!=dict and hasattr(
		_DictatedVariable,"items"
	):
		
		#debug
		'''
		print('l 135 Printer')
		print('_DictatedVariable is ')
		print(_DictatedVariable)
		print('type(_DictatedVariable) is ')
		print(type(_DictatedVariable))
		print('')
		'''
		
		#items
		PrintedTuplesList=_DictatedVariable.items()

	else:

		#sort
		PrintedTuplesList=sorted(
			_DictatedVariable.iteritems(), key=lambda key_value: key_value[0]
		)

	#Integrativ loop for seriaizing the items
	for __PrintedKeyStr,__PrintedValueVariable in PrintedTuplesList:
	
		#debug
		'''
		print('Printer l.127')
		print('__PrintedKeyStr is',__PrintedKeyStr)
		print('')
		'''

		#set the begin of the line
		PrintedDictStr+="\n"+LocalPrintAlineaStr+PrintDictIndentStr

		#Force the cast into Str
		if type(__PrintedKeyStr) not in [unicode,str]:
			__PrintedKeyStr=str(__PrintedKeyStr)

		#Get the WordStrsList
		WordStrsList=SYS.getWordStrsListWithStr(__PrintedKeyStr)

		#Init the PrintedValueVariableStr
		PrintedValueVariableStr="None"

		#Split the case if it is a pointing variable or not
		if len(WordStrsList)>0:

			#Value is displayed
			"""
			if SYS.getWordStrsListWithStr(__PrintedKeyStr)[-1]=="Pointer":
			
				#Pointer Case
				PrintedValueVariableStr=getPointerStr(
												__PrintedValueVariable,
												**_KwargVariablesDict
											)
			"""
			"""						
			elif ''.join(SYS.getWordStrsListWithStr(__PrintedKeyStr)[-2:])=="PointersList":
			
				#debug
				'''
				print('__PrintedValueVariable is ',__PrintedValueVariable)
				print('')
				'''

				#Pointer Case
				PrintedValueVariableStr=str(
						map(
								lambda List:
								getPointerStr(
									List,
									**_KwargVariablesDict),
								__PrintedValueVariable
							)
						)  if type(__PrintedValueVariable)==list else "None"
			"""
			
		#Special Suffix Cases
		if PrintedValueVariableStr=="None":
				
			#debug
			'''
			print('go to represent')
			print('__PrintedKeyStr is ',__PrintedKeyStr)
			print('id(__PrintedValueVariable) is ',id(__PrintedValueVariable))
			print('')
			'''

			#Other Cases
			PrintedValueVariableStr=getPrintStr(
				__PrintedValueVariable,
				**_KwargVariablesDict
				)

		#Key and Value Case
		PrintedDictStr+="'"+__PrintedKeyStr+"' : "+PrintedValueVariableStr

	#Add a last line
	PrintedDictStr+="\n"+LocalPrintAlineaStr+"}"

	#debug
	'''
	print('PrintedDictStr is ',PrintedDictStr)
	print('')
	'''

	#return the DictStr
	return PrintedDictStr

def getListStr(_List,**_KwargVariablesDict):	

	#Global
	global PrintAlineaStr

	#set in the _KwargVariablesDict
	if 'PrintDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['PrintDeepInt']=0

	#debug
	'''
	print('Printer l.166 : getListStr')
	print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	print('_List is '+str(_List))
	print('')
	'''

	#Init the PrintedDictStr
	if type(_List)==list:
		BeginBracketStr='['
		EndBracketStr=']'
	else:
		BeginBracketStr='('
		EndBracketStr=')'

	#Definition the LocalPrintAlineaStr
	LocalPrintAlineaStr=PrintAlineaStr+"".join(
		[PrintIndentStr]*(_KwargVariablesDict['PrintDeepInt']))

	#Do the first Jump
	PrintedListStr="\n"+LocalPrintAlineaStr+BeginBracketStr
	
	#Scan the Items (integrativ loop)
	for ListInt,List in enumerate(_List):
	
		#set the begin of the line
		PrintedListStr+="\n"+LocalPrintAlineaStr+PrintListIndentStr

		#Get the represented version
		PrintedValueVariableStr=getPrintStr(
				List,**dict(
					_KwargVariablesDict,
					**{'PrintingAlineaIsBool':False}
				)
			)
			
		#Key and Value Case
		PrintedListStr+=str(ListInt)+" : "+PrintedValueVariableStr

	#Add a last line
	PrintedListStr+="\n"+LocalPrintAlineaStr+EndBracketStr

	#return the DictStr
	return PrintedListStr

def getPrintStr(_Variable,**_KwargVariablesDict):

	#Define global
	global PrintAlreadyIdIntsList

	#set in the _KwargVariablesDict
	if 'PrintDeepInt' not in _KwargVariablesDict:
		_KwargVariablesDict['PrintDeepInt']=0

	#debug
	'''
	print('Printer l.213 : getPrintStr')
	#print('_KwargVariablesDict is ',str(_KwargVariablesDict))
	#print('_Variable is '+str(_Variable))	
	print('type(_Variable) is '+str(type(_Variable)))
	#print("hasattr(_Variable,'__repr__') is "+str(hasattr(_Variable,"__repr__")))
	##if hasattr(_Variable,"__repr__"):
	#	print('hasattr(_Variable.__class__,"InspectedOrderedDict") is '+str(
	#		hasattr(_Variable.__class__,"InspectedOrderedDict")))
	#	if hasattr(_Variable.__class__,"InspectedOrderedDict"):
	#		print("_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesListKeyStr'] is "+str(
	#			_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesListKeyStr']))	
	#		print(_Variable.__class__.InspectedOrderedDict['__repr__']['KwargVariablesListKeyStr'])
	print('')
	'''

	#None type
	if type(_Variable)==None.__class__:
		return "None"

	#Special mongo database case
	elif type(_Variable).__name__ in ["Database","Series","Collection"]:

		#get
		PrinterStr=getPointerStr(_Variable)

		#return
		return PrinterStr

	#Dict types print
	#if type(_Variable) in [dict,collections.OrderedDict]:
	elif hasattr(_Variable,'items') and type(_Variable)!=type:

		#Increment the deep
		_KwargVariablesDict['PrintDeepInt']+=1

		#debug
		'''
		print('This is a dictated type so get a represent like a dict')
		print('')
		'''

		#id
		PrintedIdInt=id(_Variable)

		#debug
		'''
		print('PrintedIdInt is ',PrintedIdInt)
		print('PrintAlreadyIdIntsList is ',PrintAlreadyIdIntsList)
		print('')
		'''

		#Check if it was already represented
		if PrintedIdInt not in PrintAlreadyIdIntsList:

			#Debug
			'''
			print('PrintAlreadyIdIntsList is ',PrintAlreadyIdIntsList)
			print('')
			'''

			#append
			PrintAlreadyIdIntsList.append(PrintedIdInt)

			#Return the repr of the _Variable but shifted with the PrintAlineaStr
			PrintedStr=getDictStr(
						_Variable,
						**_KwargVariablesDict
			)

		else:

			#Return the circular Str
			PrintedStr=PrintCircularStr+getPointerStr(_Variable)

		#Debug
		'''
		print('PrintedIdInt is ',PrintedIdInt)
		print('PrintedStr is ',PrintedStr)
		print('')
		'''
		
		#return 
		return PrintedStr

	#List types print
	elif type(_Variable) in [list,tuple]:

		#id
		PrintedIdInt=id(_Variable)

		#Check if it was already represented
		if PrintedIdInt not in PrintAlreadyIdIntsList:

			#debug
			'''
			print('Printer l 389')
			print('This is a listed type so get a represent like a list')
			print('_Variable is ')
			print(_Variable)
			print('map(type,_Variable) is ')
			print(map(type,_Variable))
			print('')
			'''
			
			#append
			PrintAlreadyIdIntsList.append(PrintedIdInt)

			#import numpy
			import numpy
			from pandas.core import series

			#Check if it is a List of Objects or Python Types
			if all(
					map(
						lambda __ElementVariable:
						type(__ElementVariable) in [
							float,int,str,unicode,numpy.float64,
						] or type(__ElementVariable)==None.__class__,
						_Variable
						)
				)==False:

				#Increment the deep
				_KwargVariablesDict['PrintDeepInt']+=1

				#debug
				'''
				print('Print a represented version of the list')
				print('')
				'''

				#Return 
				PrintedStr=getListStr(_Variable,**_KwargVariablesDict)

			else:

				#debug
				'''
				print('Here just print the list directly')
				print('')
				'''

				#Definition the Local alinea
				PrintedLocalAlineaStr=PrintAlineaStr if _KwargVariablesDict['PrintDeepInt']==0 else ""

				#Return 
				PrintedStr=PrintedLocalAlineaStr+repr(
					_Variable).replace("\n","\n"+PrintedLocalAlineaStr)


			#return 
			return PrintedStr

		else:

			#Return the circular Str
			return PrintCircularStr+getPointerStr(_Variable)

	#Instance print
	elif type(_Variable).__name__ in ["instancemethod"]:

		#Debug
		'''
		print('Printer l 421')
		print('This is a method ')
		print('_Variable.__name__ is ',_Variable.__name__)
		print('')
		'''

		#Definition the Local alinea
		PrintedLocalAlineaStr=PrintAlineaStr if _KwargVariablesDict['PrintDeepInt']==0 else ""
		
		#append
		PrintAlreadyIdIntsList.append(_Variable.im_self)

		#return PrintAlineaStr+"instancemethod"
		PrintedStr=PrintedLocalAlineaStr
		PrintedStr+="< bound method "+_Variable.__name__
		PrintedStr+=" of "+str(_Variable.im_self.__class__)
		PrintedStr+=" "+str(id(_Variable.im_self))+" >"
		#PrintedStr='inst'

		#return
		return PrintedStr

	#Str types
	elif type(_Variable) in SYS.StrTypesList:

		#debug
		'''
		print('This is a Str type so get a represent like a Str')
		print('')
		'''

		#Definition the Local alinea
		PrintedLocalAlineaStr=PrintAlineaStr if _KwargVariablesDict['PrintDeepInt']==0 else ""

		#Return
		return PrintedLocalAlineaStr+_Variable.replace("\n","\n"+PrintedLocalAlineaStr)

	#Other
	#elif hasattr(_Variable,"__repr__") and hasattr(
	#	_Variable.__class__,"InspectInspectDict"
	#	) and '__repr__' in _Variable.__class__.InspectInspectDict and _Variable.__class__.InspectInspectDict[
	#	'__repr__']['KwargVariablesListKeyStr']!="":
	elif hasattr(_Variable.__class__,'__mro__'
		) and SYS.PrinterClass in _Variable.__class__.__mro__:

		#debug
		'''
		print('This is a representer so call the repr of it with the _KwargVariablesDict')
		print('type(_Variable) is ',type(_Variable))
		print('id(_Variable) is ',id(_Variable))
		print('')
		'''
		
		#id
		PrintedIdInt=id(_Variable)

		#Check if it was already represented
		if PrintedIdInt not in PrintAlreadyIdIntsList:

			#append
			PrintAlreadyIdIntsList.append(PrintedIdInt)

			#Return the repr of the _Variable but shifted with the PrintAlineaStr
			PrintedStr=_Variable.__repr__(**_KwargVariablesDict)

			#return 
			return PrintedStr

		else:

			#Return the circular Str
			return PrintCircularStr+getPointerStr(_Variable)

	else:

		#Debug
		'''
		print('This is not identified so call the repr of it')
		print('')
		'''

		#Definition the Local alinea
		PrintedLocalAlineaStr=PrintAlineaStr if _KwargVariablesDict[
			'PrintDeepInt']==0 else ""

		#Define 
		PrintedIdInt=id(_Variable)

		#Debug
		'''
		print('PrintedIdInt is ',PrintedIdInt)
		print('PrintAlreadyIdIntsList is ',PrintAlreadyIdIntsList)
		print('')
		'''

		#Check if it was already represented
		if PrintedIdInt not in PrintAlreadyIdIntsList:

			#debug
			'''
			print('type(_Variable) is ',type(_Variable))
			print('')
			'''

			#Append but only for mutables variable
			if type(_Variable) not in [bool,str,int,float]:
				PrintAlreadyIdIntsList.append(PrintedIdInt)

			else:

				#debug
				'''
				print('_Variable is ',_Variable)
				print('')
				'''
				pass

			#Return a repr of the _Variable but shifted with the PrintAlineaStr
			PrintedStr=PrintedLocalAlineaStr+repr(_Variable).replace(
										"\n",
										"\n"+PrintedLocalAlineaStr
									)

			#return 
			return PrintedStr


		else:

			#Return the circular Str
			return PrintedLocalAlineaStr+PrintCircularStr+getPointerStr(
				_Variable)

def _print(_Variable,**_KwargVariablesDict):
	print(represent(_Variable,**_KwargVariablesDict))

def represent(_Variable,**_KwargVariablesDict):

	#Definition the global
	global PrintAlineaStr,PrintAlreadyIdIntsList

	#Debug
	'''
	print('Printer l.545')
	print('Reinit the PrintAlreadyIdIntsList')
	print('')
	'''

	#Reinit
	PrintAlreadyIdIntsList=[]

	#Debug
	'''
	print('Printer l.554')
	print('_KwargVariablesDict is ',_KwargVariablesDict)
	print('')
	'''
	
	#Represent without shifting the Strs or not
	if 'PrintingAlineaIsBool' not in _KwargVariablesDict or _KwargVariablesDict['PrintingAlineaIsBool']:
		return getPrintStr(_Variable,**_KwargVariablesDict)
	else:
		PrintedOldAlineaStr=PrintAlineaStr
		PrintAlineaStr=""
		PrintedStr=getPrintStr(_Variable,**_KwargVariablesDict)
		PrintAlineaStr=PrintedOldAlineaStr
		return PrintedStr

def __main__represent(_PrintStr,**_KwargVariablesDict):
	return represent(
		_PrintStr,
		**dict(_KwargVariablesDict,**{'PrintingAlineaIsBool':False})
	)
def __main__print(_PrintStr,**_KwargVariablesDict):
	return _print(
		_PrintStr,
		**dict(_KwargVariablesDict,**{'PrintingAlineaIsBool':False})
	)
SYS._str = __main__represent
SYS._print = __main__print
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PrinterClass(BaseClass):

	def default_init(self,
						_PrintIdInt=0,
						_PrintingVariable=None,
						_PrintingInstanceSkipKeyStrsList=None,
						_PrintingInstanceForceKeyStrsList=None,
						_PrintingClassSkipKeyStrsList=[],
						_PrintingClassForceKeyStrsList=[],
						_PrintingBaseBool=False,
						_PrintingNewInstanceBool=True,
						_PrintingNewClassBool=True,
						_PrintingOutBool=True,
						_PrintingSelfBool=False,
						_PrintedStr="",
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#id
		self.PrintIdInt=id(self)

		#init
		self.PrintingInstanceSkipKeyStrsList=[]
		self.PrintingInstanceForceKeyStrsList=[]
			
	def do__print(self,**_KwargVariablesDict):

		#Debug
		'''
		print('l 680 _print')
		print('_KwargVariablesDict is ')
		print(_KwargVariablesDict)
		print('')
		'''

		#/###################/#
		# Check if it is a ReprStr
		# or just a PrintStr

		#Check 
		if self.PrintingSelfBool:

			#Debug
			'''
			print('l 693')
			print('we repr str here')
			print('')
			'''
			
			#print
			self.PrintedStr=self.PrintingVariable.getReprStr(
				**_KwargVariablesDict
			)

		else:

			#Debug
			'''
			print('l 705')
			print('we just get print Str here')
			print('')
			'''

			#print
			self.PrintedStr=getPrintStr(
					self.PrintingVariable,
					**_KwargVariablesDict
				)
		
		#Check
		if self.PrintingOutBool:
			print(self.PrintedStr)

	def __repr__(self,**_KwargVariablesDict):

		#Debug
		'''
		print('l 718 __repr__')
		print('_KwargVariablesDict is ')
		print(_KwargVariablesDict)
		print('')
		'''

		#init a new one
		self.PrintingVariable=self.__class__()

		#loop
		for __ItemTuple in self.__dict__.items():

			#Debug
			'''
			print('Try to copy')
			print(__ItemTuple[0])
			print('')
			'''

			#copy
			#self.PrintingVariable.__dict__[__ItemTuple[0]]=copy.copy(
			#	__ItemTuple[1]
			#)

			#try
			try:

				#copy
				self.PrintingVariable.__dict__[__ItemTuple[0]]=copy.copy(
					__ItemTuple[1]
				)
			except:


				#debug
				#print('Try to copy but FAILED')
				#print(__ItemTuple[0])
				#print('')

				#pass
				pass
				

		#Debug
		'''
		print('l 764 OK')
		print('type(self.PrintingVariable) is ')
		print(type(self.PrintingVariable))
		print('')
		'''

		#get
		ReprStr=self._print(
			self.PrintingVariable,
			_OutBool=False,
			_SelfBool=True,
			**_KwargVariablesDict
		).PrintedStr

		#Debug
		'''
		print('l 763 Printer')
		print('ReprStr is ')
		print(ReprStr)
		'''

		#reset
		self.PrintingSelfBool=False
		self.PrintingOutBool=True

		#return 
		return ReprStr

	def getReprStr(self,**_KwargVariablesDict):

		#Debug
		'''
		print('l 741 getReprStr')
		print('_KwargVariablesDict is ')
		print(_KwargVariablesDict)
		print('')
		'''

		#debug
		'''
		_Variable.debug(('_Variable.__class__',self.__class__,[
				'PrintingKeyStrsList',
				'DefaultBaseKeyStrsList',
				'DefaultSpecificKeyStrsList',
				'PrintedNotSpecificKeyStrsList'
				]))
		'''

		#/###################/#
		# Print the Default Key Strs... form the Instance or the still the Class
		#

		#filter the skip key strs
		PrintedDefaultSpecificKeyStrsList=SYS._filter(
				lambda __DefaultSpecificKeyStr:
				__DefaultSpecificKeyStr not in list(
					self.PrintingInstanceSkipKeyStrsList)+list(
					self.PrintingClassSkipKeyStrsList), 
				self.__class__.DefaultSpecificKeyStrsList
			)

		#Represent the Specific KeyStrs
		PrintedTuplesList=map(
									lambda __SpecificKeyStr:
									(
										"<Spe>"+("<Instance>"
										if __SpecificKeyStr in self.__dict__ 
										else (
											"<Instance>_"
											if hasattr(
													self.__class__,__SpecificKeyStr
											) and type(getattr(
												self.__class__,__SpecificKeyStr
											))==property and getattr(
												self.__class__,'_'+__SpecificKeyStr
											)!=getattr(self,'_'+__SpecificKeyStr) and (
											'_'+__SpecificKeyStr not in self.PrintingClassSkipKeyStrsList and __SpecificKeyStr not in self.PrintingInstanceSkipKeyStrsList
											)
											else
											"<Class>"
											)
										)+__SpecificKeyStr,
										getattr(self,__SpecificKeyStr)
									),
									PrintedDefaultSpecificKeyStrsList
							)

		#/###################/#
		# Print the Default Base Key Strs... form the Instance or the still the Class
		#

		#Represent the BaseKeyStrs
		if self.PrintingBaseBool:
			
			#Debug
			'''
			print('Printer l 723')
			print('We print the bases')
			print('self.__class__.DefaultBaseKeyStrsList is ')
			print(self.__class__.DefaultBaseKeyStrsList)
			print('')
			'''

			#filter
			PrintedDefaultBaseKeyStrsList=SYS._filter(
					lambda __DefaultSpecificKeyStr:
					__DefaultSpecificKeyStr not in list(
						self.PrintingInstanceSkipKeyStrsList
					)+list(self.PrintingClassSkipKeyStrsList), 
					self.__class__.DefaultBaseKeyStrsList
				)
				
			PrintedTuplesList+=map(
									lambda __BaseKeyStr:
									(
										"<Base>"+("<Instance>"
										if __BaseKeyStr in self.__dict__
										else "<Class>"
										)+__BaseKeyStr
										,
										getattr(self,__BaseKeyStr)
									),
									PrintedDefaultBaseKeyStrsList
								)

		#/###################/#
		# Print the New key strs in the instance
		#

		#print the NewInstanceKeyStrs in the __dict__
		if self.PrintingNewInstanceBool:
			
			#filter
			PrintedNewInstanceTuplesList=SYS._filter(
				lambda __NewItemTuple:
				__NewItemTuple[0
				] not in self.__class__.DefaultSpecificKeyStrsList+self.__class__.DefaultBaseKeyStrsList,
				self.__dict__.items()
			)

			#filter
			PrintedNewInstanceTuplesList=SYS._filter(
					lambda __PrintedNewInstanceTuple:
					__PrintedNewInstanceTuple[0] not in list(
						self.PrintingInstanceSkipKeyStrsList)+list(
						self.PrintingClassSkipKeyStrsList),
					PrintedNewInstanceTuplesList
				)

			#map
			PrintedTuplesList+=map(
				lambda __NewItemTuple:
				(
					"<New><Instance>"+__NewItemTuple[0],
					__NewItemTuple[1]
				),
				PrintedNewInstanceTuplesList
			)

		#/###################/#
		# Print the New key strs in the class
		#

		#Represent the NewClassKeyStrs in the _self.__class____.__dict__
		if self.PrintingNewClassBool:


			#filter
			PrintedNewClassKeyStrsList=SYS._filter(
					lambda __KeyStr:
					__KeyStr not in self.__class__.KeyStrsList and __KeyStr not in self.__dict__,
					SYS.getKeyStrsListWithClass(
						self.__class__
					)
				)

			#filter
			PrintedNewClassKeyStrsList=SYS._filter(
					lambda __NewClassKeyStr:
					__NewClassKeyStr not in list(
					self.PrintingInstanceSkipKeyStrsList)+list(
					self.PrintingClassSkipKeyStrsList),
					PrintedNewClassKeyStrsList
				)

			#filter
			PrintedTuplesList+=map(
				lambda __NewKeyStr:
				(
					"<New><Class>"+__NewKeyStr,
					self.__class__.__dict__[__NewKeyStr]
				),
				PrintedNewClassKeyStrsList
			)
		
		#/###################/#
		# Print force key strs
		#

		#Debug
		'''
		print('Printer l 811')
		print('We add some forced Key Strs')
		print('')
		'''
		
		#map
		PrintedTuplesList+=map(
				lambda __PrintingKeyStr:
				(
					"<Spe><Instance>"+__PrintingKeyStr,
					self.__dict__[__PrintingKeyStr]
				) 
				if __PrintingKeyStr in self.__dict__ and __PrintingKeyStr not in self.__class__.DefaultSpecificKeyStrsList
				else(
						(
							"<Base><Instance>"+__PrintingKeyStr,
							self.__dict__[__PrintingKeyStr]
						) 
						if __PrintingKeyStr in self.__dict__ and __PrintingKeyStr in self.__class__.DefaultBaseKeyStrsList
						else
						(
							(
								"<Base><Class>"+__PrintingKeyStr,
								getattr(self,__PrintingKeyStr)
							)
							if __PrintingKeyStr not in self.__dict__
							else
							(
								"<New><Instance>"+__PrintingKeyStr,
								self.__dict__[__PrintingKeyStr]
							)
						)
				),
				list(
					self.PrintingInstanceForceKeyStrsList
				)+list(self.PrintingClassForceKeyStrsList)
			)
					
		#Append
		global PrintAlreadyIdIntsList

		#debug
		'''
		print('Printer l.629')
		print('id(self) is ',id(self))
		print('self not in PrintAlreadyIdIntsList is ',str(
			self not in PrintAlreadyIdIntsList))
		print('')
		'''

		#define the PrintedStr
		self.PrintedStr=getPointerStr(
					self
				)+getPrintStr(
					dict(PrintedTuplesList),
					**_KwargVariablesDict
				)

		#return
		return self.PrintedStr

		
#</DefineClass>

#<DefinePrint>
PrinterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PrintIdInt',
		'PrintingVariable',
		'PrintingInstanceSkipKeyStrsList',
		'PrintingInstanceForceKeyStrsList',
		'PrintingClassSkipKeyStrsList',
		'PrintingClassForceKeyStrsList',
		'PrintingBaseBool',
		'PrintingNewInstanceBool',
		'PrintingNewClassBool',
		'PrintingOutBool',
		'PrintedStr'
	]
)
#</DefinePrint>