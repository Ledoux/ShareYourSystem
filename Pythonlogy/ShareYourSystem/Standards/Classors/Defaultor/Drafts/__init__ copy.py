#<ImportSpecificModules>
import inspect
import collections

BaseModuleStr="ShareYourSystem.Standards.Classors.Classor")
DecorationModule=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
Classor=BaseModule
SYS.setSubModule(globals())

DefaultingStr="_"
#</DefineLocals>

#<DefineFunctions>
def getDefaultedOrderedDictWithMethodFunction(_MethodFunction):

	#Check
	if _MethodFunction.__func__.func_defaults!=None:

		#Inspect to get the DefaultInputStrList

		InputStrList,ArgVariablesListKeyStr,KwargsVariablesSetKeyStr,DefaultStrsList=inspect.getargspec(
			)

		#debug
		'''
		print("_MethodFunction is "+str(_MethodFunction))
		print("_MethodFunction.__func__.func_defaults is ",_MethodFunction.__func__.func_defaults)
		print("")
		'''

		#Zip with the func_defaults
		return collections.OrderedDict(
							zip(
									map(
											lambda __DefaultInputStr:
											DefaultingStr.join(__DefaultInputStr.split(DefaultingStr)[1:]),
											SYS._filter(
												lambda __InputStr:
												DefaultingStr in __InputStr,
												InputStrList[1:]
											)
										),
									_MethodFunction.__func__.func_defaults
								)
							)
	else:

		#Return an empty ordered dict
		return collections.OrderedDict()
#</DefineFunctions>

#<Define_Class>
@DecorationClass()
class DefaultorClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#Definition attributes
		self.DefaultingSetMethodStr=""
		self.DefaultedSetMethod=None

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#Do
		self.default(self.ClassingClass)

		#Return 
		return self.ClassingClass

	def default(self,_Class):

		#Check
		if hasattr(_Class,'DefaultedIsBool')==False or _Class.DefaultedIsBool==False:

			#set the DefaultOrderedDict
			_Class.InitArgumentOrderedDict=SYS.getArgumentOrderedDictWithFunction(_Class.__init__)

			#Definition DefaultedInitFunction
			DefaultedInitFunction=_Class.__init__.__func__
		
			#Get the DefaultedSetMethod
			if self.DefaultingSetMethodStr!="":
				self.DefaultedSetMethod=getattr(_InstanceVariable,self.DefaultingSetMethodStr)

			#debug
			print("_Class.DefaultOrderedDict is ",_Class.DefaultOrderedDict)
			print("")

			#Definition the new init method
			def init(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

				#debug
				print('_LiargVariablesList is ',dir(_LiargVariablesList))
				print('')

				#set the DefaultOrderedDict in the instance
				if self.DefaultedSetMethod!=None:
					map(
							lambda __DefaultItemTuple:
							self.DefaultedSetMethod(__DefaultItemTuple[0],locals()[__DefaultItemTuple[0]]),
							_Class.DefaultOrderedDict.items()
						)
				else:
					map(
							lambda __DefaultItemTuple:
							_InstanceVariable.__dict__.__setitem__(
								__DefaultItemTuple[0],
								locals()[__DefaultItemTuple[0]]
							),
							_Class.DefaultOrderedDict.items()
						)

				#Call the based __init__ method
				try:
					DefaultedInitFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict)
				except:
					DefaultedInitFunction(_InstanceVariable,*_LiargVariablesList)

			#set to the class
			init.__name__="Defaultor@init"
			_Class.__init__=init

			#set to True
			_Class.DefaultedIsBool=True



		


#</Define_Class>



