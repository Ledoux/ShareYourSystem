#<ImportSpecificModules>
import inspect

BaseModuleStr="ShareYourSystem.Standards.Objects.Debugger"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester")
#</ImportSpecificModules>

#<DefineLocals>
SYS.setSubModule(globals())

FunctingDecorationStr='Functer@'
#</DefineLocals>

#<DefineFunctions>
def getFunctedFunctionWithVariable(_Variable):

	#debug
	print('_Variable is '+str(_Variable))
	print("FunctingDecorationStr in _Variable.__name__ is",str(FunctingDecorationStr in _Variable.__name__))
	print('')

	if FunctingDecorationStr in _Variable.__name__:

		#Definition the FunctedStrsList
		FunctedStrsList=_Variable.__name__.split(FunctingDecorationStr)

		#Definition the FunctedFunction
		FunctingFunction=getattr(_Variable,FunctedStrsList[0]+'Pointer').FunctedFunction

		#debug
		print('FunctedStrsList is ',str(FunctedStrsList))
		print('FunctingFunction is '+str(FunctingFunction))
		print('')

		#Return the functed function inside the first found functed pointer
		return FunctingFunction
	else:

		#Return the Variable directly
		return _Variable

def getFunctedPointerWithVariableAndKeyStr(_Variable,_KeyStr):

	#Check
	if FunctingDecorationStr in _Variable.__name__:

		#Definition the FunctedStrsList
		FunctedStrsList=_Variable.__name__.split(FunctingDecorationStr)
		IndexInt=FunctedStrsList.index(_KeyStr)

		#debug
		'''
		print('FunctedStrsList is '+str(FunctedStrsList))
		print('')
		'''

		#Init the FunctedPointer
		FunctedPointer=getattr(_Variable,FunctedStrsList[0]+'Pointer')

		#Check
		if IndexInt>0:

			#debug
			'''
			print('IndexInt is ',str(IndexInt))
			print('')
			'''

			#Get recursively
			for __ForInt in xrange(1,IndexInt+1):
				FunctedPointer=getattr(
										getattr(FunctedPointer,'FunctingFunction'),
										FunctedStrsList[__ForInt]+'Pointer'
									)

			#debug
			'''
			print('FunctedPointer is '+str(FunctedPointer))
			print('')
			'''

		#Return 	
		return FunctedPointer
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class FuncterClass(BaseClass):
	
	def __init__(self,**_KwargVariablesDict):

		#<DefineSpecificDo>
		self.FunctingFunction=None
		self.FunctedFunctionStr=""
		self.FunctedFunction=None
		self.FunctedClass=None
		self.FunctedIsBool=False
		#<DefineSpecificDo>

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Variable):

		#func
		self.func(_Variable)

		#Return the FunctedFunction
		return self.FunctedFunction

	def func(self,_Variable=None):

		#set the FunctingFunction
		if self.FunctingFunction==None or _Variable!=None:
			#self.FunctingFunction=getFunctedFunctionWithVariable(_Variable)	
			self.FunctingFunction=_Variable

		#set the FunctedFunction
		if self.FunctedFunction==None:
			def FunctedFunction(*_LiargVariablesList,**_KwargVariablesDict):
				return self.FunctingFunction(*_LiargVariablesList,**_KwargVariablesDict)
			self.FunctedFunction=FunctedFunction

		#set the name
		self.FunctedFunction.__name__=self.NameStr+FunctingDecorationStr+self.FunctingFunction.__name__

		#debug
		'''
		self.debug("self.FunctedFunction.__name__ is "+self.FunctedFunction.__name__)
		'''

		#Give a Pointer to the Hooker
		setattr(self.FunctedFunction,self.NameStr+'Pointer',self)

		#Definition a represent function for the decorated function
		def represent():
			RepresentedStr=inspect.getmodule(self.FunctingFunction
					).__name__+'.'+self.NameStr+FunctingDecorationStr+Representer.represent(
					self.FunctingFunction,**{'RepresentingAlineaIsBool':False})
			return RepresentedStr
		self.FunctedFunction.__repr__=represent

		#Return self
		return self
#</DefineClass>

