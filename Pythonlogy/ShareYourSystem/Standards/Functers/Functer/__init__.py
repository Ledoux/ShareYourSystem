# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Functer is the first Module for beginnning to decorate methods 
inside of the classes of the framework. So here, FuncterClass instances
decorate methods, but just for setting the essential attributes 
of this augmentation at the level of the decorating class, and also
give to the new decorated method a __repr__ and attributes to
keep having access to the nested method attributes.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Debugger"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import inspect
from ShareYourSystem.Standards.Classors import Representer
#</ImportSpecificModules>

#<DefineLocals>
FunctingDecorationStr='Func@'
FunctingAttributeStr='.'
#</DefineLocals>

#<DefineFunctions>
def getFunctingFunctionWithFuncFunction(_FuncFunction):

	#debug
	'''
	print('_FuncFunction is '+str(_FuncFunction))
	print("FunctingDecorationStr in _FuncFunction.__name__ is",str(FunctingDecorationStr in _FuncFunction.__name__))
	print('')
	'''

	if FunctingDecorationStr in _FuncFunction.__name__:

		#Definition the FunctedDecorationStrsList
		FunctedDecorationStrsList=_FuncFunction.__name__.split(FunctingDecorationStr)

		#Definition the FunctedFunction
		FunctingFunction=getattr(_FuncFunction,FunctedDecorationStrsList[0]+'Pointer').FunctingFunction

		#debug
		'''
		print('FunctedDecorationStrsList is ',str(FunctedDecorationStrsList))
		print('FunctingFunction is '+str(FunctingFunction))
		print('')
		'''

		#Return the functed function inside the first found functed pointer
		return FunctingFunction
	else:

		#Return the Variable directly
		return _FuncFunction

def getFunctedPointerWithFuncFunctionAndNameStr(_FuncFunction,_NameStr):

	#Check
	if FunctingDecorationStr in _FuncFunction.__name__:

		#Definition the FunctedDecorationStrsList
		FunctedDecorationStrsList=_FuncFunction.__name__.split(FunctingDecorationStr)
		
		#debug
		'''
		print('FunctedDecorationStrsList is '+str(FunctedDecorationStrsList))
		print('')
		'''

		#Definition the FunctedNameStrsList
		FunctedNameStrsList=map(
										lambda __FunctedDecorationStr:
										__FunctedDecorationStr.split(FunctingAttributeStr)[0],
										FunctedDecorationStrsList
									)

		#debug
		'''
		print('FunctedNameStrsList is '+str(FunctedNameStrsList))
		print('')
		'''

		#Find the index
		IndexInt=FunctedNameStrsList.index(_NameStr)

		#Init the FunctedPointer
		FunctedPointer=getattr(_FuncFunction,FunctedDecorationStrsList[0]+'Pointer')

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
										FunctedNameStrsList[__ForInt]+'Pointer'
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
	
	#Definition
	RepresentingKeyStrsList=[
									'FunctingFunction',
									'FunctedModuleStr',
									'FunctedFunction',
									'FunctedClass',
									'FunctedIsBool'
								]

	def default_init(self,
				_FunctingFunction=None,
				_FunctedModuleStr="",
				_FunctedFunction=None,
				_FunctedClass=None,
				_FunctedIsBool=False,
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Variable):

		#func
		self.funct(_Variable)

		#Return the FunctedFunction
		return self.FunctedFunction

	def do_funct(self):
		
		#set the FunctedFunction
		if self.FunctedFunction==None:
			def FunctedFunction(*_LiargVariablesList,**_KwargVariablesDict):
				return self.FunctingFunction(*_LiargVariablesList,**_KwargVariablesDict)
			self.FunctedFunction=FunctedFunction

		#set the name
		self.FunctedModuleStr=inspect.getmodule(self.FunctingFunction
					).__name__
		self.FunctedNameStr=self.NameStr+FunctingDecorationStr+self.FunctedModuleStr.split('.')[-1]+'.'+self.FunctingFunction.__name__
		self.FunctedFunction.__name__=self.FunctedNameStr

		#debug
		'''
		self.debug("self.FunctedFunction.__name__ is "+self.FunctedFunction.__name__)
		'''

		#Give a Pointer to the Hooker
		setattr(self.FunctedFunction,self.NameStr+'Pointer',self)

		#Definition a represent function for the decorated function
		def represent():
			return Representer.represent(self.FunctingFunction,**{'RepresentingAlineaIsBool':False})
		self.FunctedFunction.__repr__=represent

		#Return self
		return self
#</DefineClass>

