# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Hooker can be a powerful tool if it is good used. it would like to 
imitate the logic of establishing a modulared and personalized protocol 
like a wordpress procedure with their hooked php functions like add_action.
Here methods can be augmented by a decorating Hooker calling before or after 
a list of defined functions, and paying attention to the cases where non redundant
calls in circular processes are avoided.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>


#<ImportSpecificModules>
import collections
import copy
import inspect
import os
import sys
from ShareYourSystem.Objects import Caller
#</ImportSpecificModules>

#<DefineLocals>
ArgumentingStr="_"
HookingBeforeStr='Before'
HookingAfterStr='After'
#</DefineLocals>

#<DefineFunctions>
def setHookerWithHookingInstanceVariable(_Hooker,_InstanceVariable):

	#set to the HookerPointer the corresponding class
	_Hooker.HookedClass=_InstanceVariable.__class__

	#debug
	'''
	print('We have to first set in the class the hooking classes and corresponding functions')
	print(str([self.HookingBeforeVariablesList,self.HookingAfterVariablesList]))
	print('')
	'''

	#Definition a HookedCaller
	HookedCaller=Caller.CallerClass()
	CallingDefaultDict=dict(
		Caller.CallerClass.DoingAttributeVariablesOrderedDict,**{
		'CallingInstanceVariable':_InstanceVariable}
	)

	#Debug
	'''
	print('_Hooker.HookingBeforeVariablesList is ',_Hooker.HookingBeforeVariablesList)
	print('_Hooker.HookingAfterVariablesList is ',_Hooker.HookingAfterVariablesList)
	print('')
	'''

	#set the Hooked functions
	[_Hooker.HookedBeforeFunctionsList,_Hooker.HookedAfterFunctionsList]=map(
		lambda __HookingDictsList:
		map(
				lambda __HookingDict:
				HookedCaller.call(**dict(CallingDefaultDict,**__HookingDict)).CallingVariable,
				__HookingDictsList
		),
		[_Hooker.HookingBeforeVariablesList,_Hooker.HookingAfterVariablesList]
	)

	#set the hooking functions
	[_Hooker.HookedBeforeStrsList,_Hooker.HookedAfterStrsList]=map(
		lambda __HookedBeforeFunctionsList:
		map(
				lambda __HookedBeforeFunction:
				__HookedBeforeFunction.im_func.__repr__() 
				if hasattr(__HookedBeforeFunction,'im_func')
				else __HookedBeforeFunction.__repr__()
				,__HookedBeforeFunctionsList
			),
			[_Hooker.HookedBeforeFunctionsList,_Hooker.HookedAfterFunctionsList]
		)

	#debug
	'''
	print('Hooker l.158 : hooked functions are setted and they are : ')
	print(str([_Hooker.HookedBeforeStrsList,_Hooker.HookedAfterStrsList]))
	print('')
	'''

	#Say ok for the setting
	_Hooker.HookedIsBool=True

#<DefineFunctions>

#<DefineClass>
@DecorationClass()
class HookerClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
									'HookingFunction'
									'HookingBeforeVariablesList'
									'HookingAfterVariablesList'
									'HookingUniqueBool'
									'HookedFunction'
									'HookedBeforeVariablesList'
									'HookedAfterVariablesList'
									'HookedBeforeFunctionsList'
									'HookedAfterFunctionsList'
									'HookedIsBool'
								]

	def default_init(self,
						_HookingFunction=None,
						_HookingBeforeVariablesList=None,
						_HookingAfterVariablesList=None,
						_HookingUniqueBool=True,
						_HookedFunction=None,
						_HookedBeforeVariablesList=None,
						_HookedAfterVariablesList=None,
						_HookedBeforeFunctionsList=None,
						_HookedAfterFunctionsList=None,
						_HookedIsBool=False,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Function):
		
		#debug
		'''
		print('Hooker l.127')
		print("_Function is "+str(_Function))
		print('')
		'''

		#Hook
		self.hook(_Function)

		#Call the __call__ parent method
		self.FunctedFunction=self.HookedFunction
		BaseClass.__call__(self,_Function)

		#Return the FunctedFunction
		return self.FunctedFunction

	def do_hook(self):

		#Debug
		'''
		print('self.HookingFunction is ',self.HookingFunction)
		print('')
		'''
		
		#Definition the FunctedFunction
		def HookedFunction(*_LiargVariablesList,**_KwargVariablesDict):

			#debug
			'''
			print('Hooker l.173 : we are in the hooked function')
			print('')
			'''

			#Definition an alias of the instance
			InstanceVariable=_LiargVariablesList[0]

			#Init maybe the _KwargVariablesDict
			if 'HookingIsBool' not in _KwargVariablesDict:
				_KwargVariablesDict['HookingIsBool']=True
				_KwargVariablesDict['HookedFunctionsList']=[]
				_KwargVariablesDict['HookingUniqueBool']=self.HookingUniqueBool	

			#Init maybe the hooking classes and functions for the first call
			if self.HookedIsBool==False:

				#set the HookedFunction
				setHookerWithHookingInstanceVariable(self,InstanceVariable)

			#debug
			'''
			print('self.HookedAfterFunctionsList is '+str(self.HookedAfterFunctionsList))
			print('')
			'''

			#After hooks (integrativ loop)
			for __HookedAfterFunction in self.HookedAfterFunctionsList:

				#Check
				if _KwargVariablesDict['HookingIsBool']:
	
					#Check
					if callable(__HookedAfterFunction):
					
						#Check if it is a unique call or not
						HookedIsBool=True
						if _KwargVariablesDict['HookingUniqueBool']:
							if __HookedAfterFunction in _KwargVariablesDict['HookedFunctionsList']:
								HookedIsBool=False

						#Append 
						_KwargVariablesDict['HookedFunctionsList'].append(__HookedAfterFunction)

						#Check for calling
						if HookedIsBool:

							#debug
							'''
							print('__HookedAfterFunction is called '+str(
												__HookedAfterFunction))
							print('From Module '+str(inspect.getmodule(__HookedAfterFunction)))
							print('')
							'''

							#Call and try with or without _KwargVariablesDict
							try:
								OutputVariable=__HookedAfterFunction(*_LiargVariablesList,**_KwargVariablesDict)
							except:
								OutputVariable=__HookedAfterFunction(*_LiargVariablesList)

							#Update maybe the _KwargVariablesDict
							if type(OutputVariable)==dict:
								_KwargVariablesDict.update(OutputVariable)

				else:

					#Return the instance
					return InstanceVariable

			#Check if it is a unique call or not
			HookedIsBool=True
			if _KwargVariablesDict['HookingUniqueBool']:
				if self.HookingFunction in _KwargVariablesDict['HookedFunctionsList']:
					HookedIsBool=False

			#Append 
			_KwargVariablesDict['HookedFunctionsList'].append(self.HookingFunction)

			if _KwargVariablesDict['HookingIsBool']:

				#debug
				'''
				print('_Function is called '+str(_Function))
				print('From Module '+str(inspect.getmodule(_Function)))
				print('')
				'''

				#Call and try with or without _KwargVariablesDict
				try:
					OutputVariable=self.HookingFunction(*_LiargVariablesList,**_KwargVariablesDict)
				except:
					OutputVariable=self.HookingFunction(*_LiargVariablesList)

				#Update maybe the _KwargVariablesDict
				if type(OutputVariable)==dict:
					_KwargVariablesDict.update(OutputVariable)

			else:

				#Return the instance
				return InstanceVariable

			#Before hooks (integrativ loop)
			for __HookedBeforeFunction in self.HookedBeforeFunctionsList:

				#Check
				if _KwargVariablesDict['HookingIsBool']:
					
					#Check
					if callable(__HookedBeforeFunction):

						#Check if it is a unique call or not
						HookedIsBool=True
						if _KwargVariablesDict['HookingUniqueBool']:
							if __HookedBeforeFunction in _KwargVariablesDict['HookedFunctionsList']:
								HookedIsBool=False

						#Append 
						_KwargVariablesDict['HookedFunctionsList'].append(__HookedBeforeFunction)

						#Check for calling
						if HookedIsBool:

							#debug
							'''
							print('__HookedBeforeFunction is called '+str(__HookedBeforeFunction))
							print('From Module '+str(inspect.getmodule(__HookedBeforeFunction)))
							print('')
							'''

							#Call and try with or without _KwargVariablesDict
							try:
								OutputVariable=__HookedBeforeFunction(*_LiargVariablesList,**_KwargVariablesDict)
							except:
								OutputVariable=__HookedBeforeFunction(*_LiargVariablesList)

							#Update maybe the _KwargVariablesDict
							if type(OutputVariable)==dict:
								_KwargVariablesDict.update(OutputVariable)

				else:

					#Return the Instance
					return InstanceVariable

			#Return self for the wrapped method call
			return InstanceVariable

		#debug
		'''
		print('HookedFunction is '+str(HookedFunction))
		print('')
		'''

		#set
		self.HookedFunction=HookedFunction

		#Return self
		#return self

#</DefineClass>

