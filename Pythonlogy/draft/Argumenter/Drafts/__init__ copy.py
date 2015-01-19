# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Argumenter decorates the DoMethod in the decorated classes by a Doer instance.
It helps for setting again automatically in the instance Doing and DoneAttributes thanks to their
shortcutted calls in the named arguments of the DoMethod, or their full name in the _KwargVariablesDict.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import inspect

from ShareYourSystem.Classors import Doer,Inspecter
Functer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
ArgumentingStr="_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ArgumenterClass(BaseClass):

	def __init__(self,
						_ArgumentingFunction=None,
						_ArgumentingDoStr="",
						_ArgumentedFunction=None,
						_ArgumentedInspectOrderedDict=None,
						_ArgumentedDoingStr="",
						_ArgumentedDoneFunctionStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Variable):

		#argument first
		self.argument(_Variable)

		#Link
		self.FunctedFunction=self.ArgumentedFunction

		#Return by calling the Functer method
		return BaseClass.__call__(self,self.ArgumentingFunction)

	def argument(self,_Variable):

		#debug
		'''
		self.debug(('locals ',locals(),['_Variable']))
		'''

		#set
		if self.ArgumentingFunction==None or _Variable!=None:
			self.ArgumentingFunction=_Variable

		#set the ArgumentingDoStr if not already
		if self.ArgumentingDoStr=="":

			#debug
			'''
			self.debug(('self.',self,['ArgumentingFunction']))
			'''

			#Keep only the last part of the name to avoid the FunctingDecorationStrs
			NameStr=self.ArgumentingFunction.__name__.split(Functer.FunctingDecorationStr)[-1]

			#Then transform into an object VariableStr
			self.ArgumentingDoStr=NameStr[0].upper()+NameStr[1:]
			
		#debug
		'''
		self.debug(('self.',self,['ArgumentingDoStr']))
		'''

		#set the ArgumentedDoingStr
		self.ArgumentedDoingStr=Doer.getDoingStrWithDoneStr(
			Doer.getDoneStrWithDoStr(self.ArgumentingDoStr)
			)

		#Find the Arguments Types
		self.ArgumentedInspectOrderedDict=SYS.getArgumentDictWithFunction(self.ArgumentingFunction)

		#Definition the ArgumentedFunction
		def ArgumentedFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

			
			#debug
			'''
			self.debug(
						[
							('',locals(),[
											'_LiargVariablesList'
								]),
							('self.',self,[
											'ArgumentingDoStr',
											'ArgumentedDoingStr',
											'ArgumentedInspectOrderedDict'
											])
						]
					)
			'''
			
			#set in the instance the corresponding listed arguments if they are not None
			map(	
					lambda __KeyStr,__Variable:
					_InstanceVariable.__setattr__(__KeyStr,__Variable) 
					if __Variable!=None and hasattr(_InstanceVariable,__KeyStr)
					else None,
					map(
							lambda __InputKeyStr:
							self.ArgumentedDoingStr+ArgumentingStr.join(
								__InputKeyStr.split(ArgumentingStr)[1:]
								),
							self.ArgumentedInspectOrderedDict['InputKeyStrsList'][1:]
					),
					_LiargVariablesList
				)


			#Definition the ArgumentedSetTuplesList
			ArgumentedKwargTuplesList=map(
											lambda __ItemTuple:
											(
												self.ArgumentedDoingStr+ArgumentingStr.join(
												__ItemTuple[0].split(ArgumentingStr)[1:]),
												__ItemTuple[1]
											) if __ItemTuple[0].startswith(ArgumentingStr)
											else __ItemTuple,
											_KwargVariablesDict.items()
										)

			#set in the instance the corresponding kwarged arguments
			map(	
					lambda __ItemTuple:
					#set direct explicit attributes
					_InstanceVariable.__setattr__(*__ItemTuple) 
					if hasattr(_InstanceVariable,__ItemTuple[0])
					else None,
					ArgumentedKwargTuplesList
				)

			#Call the argumenting self.ArgumentingFunction
			return self.ArgumentingFunction(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict)

		#set
		self.ArgumentedFunction=ArgumentedFunction

		#Return self
		return self

#</DefineClass>

