# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Argumenter decorates the DoMethod in the decorated classes by a Doer instance.
It helps for setting again automatically in the instance Doing and DoneAttributes thanks to their
shortcutted calls in the named outputs of the DoMethod, or their full name in the _KwargVariablesDict.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Functer=BaseModule

from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineLocals>
OutputingStr="_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class OutputerClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
									'OutputingFunction',
									'OutputingNodeStr',
									'OutputedInitBool',
									'OutputedFunctionsList',
									'OutputedMiddleFunctionStr',
									'OutputedStartFunctionStrsList',
									'OutputedFunctionStrsList'
								]

	def __init__(self,
						_OutputingFunction=None,
						_OutputingNodeStr='Output',
						_OutputedInitBool=False,
						_OutputedFunctionsList=None,
						_OutputedMiddleFunctionStr="",
						_OutputedStartFunctionStrsList=None,
						_OutputedFunctionStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Function):

		#output first
		self.output(_Function)

		#Link
		self.FunctedFunction=self.OutputedFunction

		#Return by calling the Functer method
		return BaseClass.__call__(self,self.OutputingFunction)

	def do_output(self):

		#Definition the OutputedFunction
		def OutputedFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

			#Debug
			'''
			print('We are in the outputed function')
			print('')
			'''

			#Check
			if Noder.NoderClass in _InstanceVariable.__class__.__mro__:

				#Get the children nodes
				NodedOutputVariablesList=_InstanceVariable[
					Noder.NodingPrefixGetStr+self.OutputingNodeStr+Noder.NodingSuffixGetStr
				]

				#debug
				'''
				print('NodedOutputVariablesList is '+str(NodedOutputVariablesList))
				print('')
				'''

				#set maybe for the first time the names of the child output methods
				if self.OutputedInitBool==False:

					#Definition
					self.OutputedMiddleFunctionStr=self.__class__.NameStr+Functer.FunctingDecorationStr

					#debug
					'''
					print('self.OutputedMiddleFunctionStr is '+str(self.OutputedMiddleFunctionStr))
					print('')
					'''

					#set
					self.OutputedFunctionsList=map(
						lambda __ListedVariable:
						__ListedVariable[0] if len(__ListedVariable)>0 else None,
						map(
								lambda __NodedOutputVariable:
								SYS._filter(
									lambda __ListedVariable:
									type(__ListedVariable).__name__=="function"
									and self.OutputedMiddleFunctionStr in __ListedVariable.__name__,
									__NodedOutputVariable.__class__.__dict__.values()
								),
								NodedOutputVariablesList
							)
						)

					#set
					self.OutputedInitBool=True

				#debug
				'''
				print('l. 120 Outputer')
				print('_InstanceVariable.__class__.__name__ is '+_InstanceVariable.__class__.__name__)
				print('self.OutputedFunctionsList is '+str(self.OutputedFunctionsList))
				print('')
				'''

				#Call all the children output methods
				map(
						lambda __OutputedFunction,__NodedOutputVariable:
						__OutputedFunction(__NodedOutputVariable
							) if __OutputedFunction!=None else None,
						self.OutputedFunctionsList,
						NodedOutputVariablesList
					)

			#Then call the one
			try:
				self.OutputingFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict)
			except:
				self.OutputingFunction(_InstanceVariable,*_LiargVariablesList)

			#Return _InstanceVariable
			return _InstanceVariable

		#set
		self.OutputedFunction=OutputedFunction

		#Return self
		#return self

#</DefineClass>

