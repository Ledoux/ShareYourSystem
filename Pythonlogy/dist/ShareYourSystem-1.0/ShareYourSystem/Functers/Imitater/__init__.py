# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Imitater 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import six
import inspect

from ShareYourSystem.Classors import Doer,Representer
from ShareYourSystem.Functers import Functer,Triggerer,Hooker
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ImitaterClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
									'ImitatingFunction',
									'ImitatedFunction'
								]

	def __init__(self,	
						_ImitatingFunction=None,
						_ImitatedFunction=None,
						**_KwargVariablesDict
				):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Function):

		#imitate
		self.imitate(_Function)

		#Link
		self.FunctedFunction=self.ImitatedFunction

		#Call the call of the parent class
		return BaseClass.__call__(self,_Function)

	def do_imitate(self):

		#Debug
		'''
		print('l. 63 Imitater')
		print('self.ImitatingFunction is ',self.ImitatingFunction)
		print('')
		'''

		#Definitions
		ImitatedDoMethodStr=self.ImitatingFunction.__name__
		ImitatedDoStr=ImitatedDoMethodStr[0].upper()+ImitatedDoMethodStr[1:]
		ImitatedDoerStr=Doer.getDoerStrWithDoStr(ImitatedDoStr)

		#Debug
		'''
		print('ImitatedDoMethodStr is ',ImitatedDoMethodStr)
		print('ImitatedDoStr is ',ImitatedDoStr)
		print('ImitatedDoerStr is ',ImitatedDoerStr)
		print('')
		'''

		#Definitions
		ImitatedModule=getattr(SYS,ImitatedDoerStr)
		ImitatedClass=getattr(ImitatedModule,SYS.getClassStrWithNameStr(ImitatedDoerStr))
		ImitatedDoneExecStr=getattr(
			ImitatedClass,
			ImitatedClass.NameStr+'DoneExecStr'
		).replace('def DoerFunction','def ImitaterFunction')

		#Define
		def imitateDo(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):
			
			#Debug
			'''
			print('Imitater l.93 inside of the function imitateDo')
			print('_InstanceVariable is ',_InstanceVariable)
			print('_LiargVariablesList is ',_LiargVariablesList)
			print('_KwargVariablesDict is ',_KwargVariablesDict)
			print('')
			'''

			if len(_KwargVariablesDict)>0:

				#group by
				[ImitatedItemTuplesList,ImitatedNotItemTuplesList]=SYS.groupby(
					lambda __ItemTuple:hasattr(_InstanceVariable,__ItemTuple[0]),
					_KwargVariablesDict.items()
				)

				#Debug
				'''
				print('ImitatedItemTuplesList is ',ImitatedItemTuplesList)
				print('ImitatedNotItemTuplesList is ',ImitatedNotItemTuplesList)
				print('')
				'''

				#set in the instance the corresponding kwarged arguments
				map(	
						lambda __ItemTuple:
						#set direct explicit attributes
						_InstanceVariable.__setattr__(*__ItemTuple),
						ImitatedItemTuplesList
					)

				#Define
				ImitatedKwargDict=dict(ImitatedNotItemTuplesList)

			else:

				#Define
				ImitatedKwargDict={}

			#Init
			ImitatedOutputVariable=None

			#Debug
			'''
			print('l.141 Imitater')
			print('self.ImitatingFunction is ',self.ImitatingFunction)
			print('ImitatedKwargDict is ',ImitatedKwargDict)
			print('')
			'''
			
			#call the imitated function
			if len(ImitatedKwargDict)>0:
				ImitatedOutputVariable=self.ImitatingFunction(
									_InstanceVariable,
									*_LiargVariablesList,
									**ImitatedKwargDict
								)
			else:
				ImitatedOutputVariable=self.ImitatingFunction(
						_InstanceVariable,
						*_LiargVariablesList
						)

			#Check
			if ImitatedClass.DoingGetBool==False:

				#Return 
				return _InstanceVariable
			
			else:

				#Return the 
				return ImitatedOutputVariable

		#Link
		ImitatedFunctionKeyStr='imitate'+ImitatedDoStr+'With'+inspect.getmodule(
			self.ImitatingFunction
					).__name__.split('.')[-1]
		if hasattr(ImitatedClass,ImitatedFunctionKeyStr)==False:
			setattr(ImitatedClass,ImitatedFunctionKeyStr,imitateDo)
		else:

			ImitatedLastInt=sorted(
				map(
					lambda __MethodKeyStr:
					(int)(__MethodKeyStr.split('_')[-1]),
					SYS._filter(
						lambda __KeyStr:
						__KeyStr.startswith(ImitatedFunctionKeyStr),
						ImitatedClass.__dict__.keys()
						)
				)
			)[-1]
			setattr(ImitatedClass,ImitatedFunctionKeyStr+'_'+str(ImitatedLastInt),imitateDo)

		#Add to the ImitatedDoneExecStr
		ImitatedDoneExecStr+='\n\treturn _InstanceVariable.'+ImitatedFunctionKeyStr+'(*_LiargVariablesList,**_KwargVariablesDict)'

		#Debug
		'''
		print('ImitatedDoneExecStr is ')
		print(ImitatedDoneExecStr)
		print('')
		'''
		
		#exec
		six.exec_(ImitatedDoneExecStr)

		#set the name
		locals()['ImitaterFunction'].__name__=self.__class__.NameStr+Doer.DoingDecorationStr+ImitatedDoMethodStr

		#Link
		self.ImitatedFunction=locals()['ImitaterFunction']

#</DefineClass>

