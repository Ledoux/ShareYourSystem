# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Propertiser is an augmented Defaultor because it will set defaults attributes
possibly in properties for the new-style decorated classes. This can set objects
with high controlling features thanks to the binding 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Inspecter"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import inspect
import collections
#</ImportSpecificModules>

#<DefineLocals>
PropertyGetStr="_"
PropertyRepresentationStr="p:"
PropertyPrefixStr="propertize_"
#</DefineLocals>

#<DefineFunctions>
def getPropertizedTupleWithItemTupleAndClass(_ItemTuple,_Class):

	#Get the KeyStr, and the ValueVariable that should be a dict
	PropertizedKeyStr=_ItemTuple[0]
	PropertizedValueVariable=_ItemTuple[1]
	PropertizedHideKeyStr=PropertyGetStr+PropertizedKeyStr

	#Check that this is a property yet or not
	if type(PropertizedValueVariable)!=property:

		#Init
		PropertizedValueVariable=property()

		#/###################/#
		# Prepare the get property
		#

		#Definition the get function
		PropertizedGetFunctionStr=PropertyPrefixStr+'get'+PropertizedKeyStr

		#Check
		if hasattr(_Class,PropertizedGetFunctionStr):

			#Check for an already defined method
			PropertizedGetFunction=getattr(_Class,PropertizedGetFunctionStr)

		else:

			#Definition a default one
			def PropertizedGetFunction(self):
				return getattr(self,PropertizedHideKeyStr)
			PropertizedGetFunction.__name__=PropertizedGetFunctionStr

		#/###################/#
		# Prepare the set property
		#

		#Definition the set function
		PropertizedSetFunctionStr=PropertyPrefixStr+'set'+PropertizedKeyStr

		#Check
		if hasattr(_Class,PropertizedSetFunctionStr):
			
			#Check for an already defined method
			PropertizedSetFunction=getattr(_Class,PropertizedSetFunctionStr)
		else:

			#Definition a default one
			def PropertizedSetFunction(self,_SettingValueVariable):
				self.__setattr__(PropertizedHideKeyStr,_SettingValueVariable)
			PropertizedSetFunction.__name__=PropertizedSetFunctionStr

		#/###################/#
		# Prepare the del property
		#

		#Definition the del function
		PropertizedDelFunctionStr=PropertyPrefixStr+'del'+PropertizedKeyStr

		#Check
		if hasattr(_Class,PropertizedDelFunctionStr):

			#Check for an already defined method
			PropertizedDelFunction=getattr(_Class,PropertizedDelFunctionStr)

		else:

			#Definition a default one
			def PropertizedDelFunction(self):
				self.__delattr__(PropertizedHideKeyStr)
			PropertizedDelFunction.__name__=PropertizedDelFunctionStr

		#Define in the class...
		map(
			lambda __PropertizedFunction:
			setattr(
				_Class,
				__PropertizedFunction.__name__,
				__PropertizedFunction
			),
			[
				PropertizedGetFunction,
				PropertizedSetFunction,
				PropertizedDelFunction
			]
		)

		#Define in the special dict...
		map(
			lambda __Function:
			_Class.PropertizeMethodsDict.__setitem__(
				__Function.__name__,
				__Function
			),
			[
				PropertizedGetFunction,
				PropertizedSetFunction,
				PropertizedDelFunction
			]
		)

		#Redefine
		PropertizedValueVariable=property(
							PropertizedGetFunction,
							PropertizedSetFunction,
							PropertizedDelFunction,
							_ItemTuple[1]['PropertizingDocStr'
							]if 'PropertizingDocStr' in _ItemTuple[1]
							else "This is here a property but with no more details..."
						)

	#Definition the property
	return (
				PropertizedKeyStr,
				PropertizedValueVariable
			)

def getPropertizedVariableWithItemTuple(_ItemTuple):

	#Maybe it is already defined
	if 'PropertizingInitVariable' in _ItemTuple[1]:
		return _ItemTuple[1]['PropertizingInitVariable']
	else:

		#Return the default one associated with the type
		return SYS.getTypeClassWithTypeStr(SYS.getWordStrsListWithStr(_ItemTuple[0])[-1])

#</DefineFunctions>

#<Define_Class>
@DecorationClass()
class PropertiserClass(BaseClass):

	def default_init(self,
						**_KwargVariablesDict
					):

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

		#Debug
		'''
		print('l.146 : We are going to propertize')
		print('')
		'''
		
		#propertize
		self.propertize()

		#Debug
		'''
		print('l.153 : propertize is done')
		print('')
		'''

		#Return 
		return _Class

	def do_propertize(self):

		#Alias
		PropertizedClass=self.DoClass

		#Debug
		'''
		print('PropertizedClass is ',PropertizedClass)
		print('')
		'''
		
		#init
		PropertizedClass.PropertizeMethodsDict={}

		#debug
		'''
		print('Propertiser l.47 default method')
		print('Class is ',Class)
		print('')
		'''

		#/###################/#
		# Check for new properties in the default dict
		#

		#Check
		if hasattr(PropertizedClass,"DefaultAttributeVariablesOrderedDict"):

			#debug
			'''
			print('PropertizedClass.DefaultAttributeVariablesOrderedDict is',PropertizedClass.DefaultAttributeVariablesOrderedDict)
			print('')
			'''

			#set the PropertizedDefaultTuplesList
			PropertizedClass.PropertizedDefaultTuplesList=SYS._filter(
				lambda __DefaultSetTuple:
				type(__DefaultSetTuple[1]
					)==property or (
					hasattr(__DefaultSetTuple[1],'items'
						) and 'DefaultingSetType' in __DefaultSetTuple[1
					] and __DefaultSetTuple[1
					]['DefaultingSetType']==property),
				PropertizedClass.DefaultAttributeVariablesOrderedDict.items()
			)

			#debug
			'''
			print('Before set PropertizedClass.PropertizedDefaultTuplesList is ',PropertizedClass.PropertizedDefaultTuplesList)
			print('')
			'''

			#set at the level of the class the PropertyGetStr+KeyStr
			map(	
					lambda __PropertizedDefaultTuple:
					setattr(
								PropertizedClass,
								PropertyGetStr+__PropertizedDefaultTuple[0],
								getPropertizedVariableWithItemTuple(__PropertizedDefaultTuple)
							),
					PropertizedClass.PropertizedDefaultTuplesList
				)

			#set the PropertizedTuple for each at the level of the class
			PropertizedClass.PropertizedDefaultTuplesList=map(
					lambda __PropertizedDefaultTuple:
					getPropertizedTupleWithItemTupleAndClass(
						__PropertizedDefaultTuple,
						PropertizedClass
					),
					PropertizedClass.PropertizedDefaultTuplesList
				)

			#debug
			'''
			print('After set PropertizedClass.PropertizedDefaultTuplesList is ',PropertizedClass.PropertizedDefaultTuplesList)
			print('')
			'''
			
			#Reset at the level of the class the properties
			map(	
					lambda __PropertizedDefaultTuple:
					setattr(
								PropertizedClass,
								*__PropertizedDefaultTuple
							),
					PropertizedClass.PropertizedDefaultTuplesList
				)

			#Add to the KeyStrsList
			PropertizedClass.KeyStrsList+=[
										"PropertizedDefaultTuplesList"
									]


		#/###################/#
		# Check for overriden propertize_ methods 
		#

		#filter
		PropertizedNewMethodDict=dict(
			SYS._filter(
				lambda __MethodItemTuple:
				__MethodItemTuple[0].startswith(PropertyPrefixStr
					) and (
					getattr(
						PropertizedClass.__bases__[0],
						__MethodItemTuple[0]
					)!=__MethodItemTuple[1]
					if hasattr(PropertizedClass.__bases__[0],
						__MethodItemTuple[0]
					) else True
				),
				PropertizedClass.InspectedMethodDict.items()
			)
		)

		#Debug
		print('Propertizer l 369')
		print('PropertizedClass is ')
		print(PropertizedClass)
		print('PropertizedMethodDict is')
		print(SYS.indent(PropertizedNewMethodDict))
		print('')

		#map
		PropertizedKeyStrsList=map(
				lambda __PropertizedKeyStr:
				SYS.deprefix(
					__PropertizedKeyStr,
					PropertyPrefixStr
				)[3:],
				PropertizedNewMethodDict.keys()
			)

		#map reset the properties
		map(
				lambda __PropertizedKeyStr:
				setattr(
						PropertizedClass,
						__PropertizedKeyStr,
						property(
								getattr(
									PropertizedClass,
									PropertyPrefixStr+'get'+__PropertizedKeyStr
								),
								getattr(
									PropertizedClass,
									PropertyPrefixStr+'set'+__PropertizedKeyStr
								),
								getattr(
									PropertizedClass,
									PropertyPrefixStr+'del'+__PropertizedKeyStr
								)
							)
					),
				PropertizedKeyStrsList
			)

#</Define_Class>



