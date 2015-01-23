# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


While the fset methods defined in properties attributes are good members for assuring
the binding role between values in an instance, the Observer makes available
the way of calling an other method (given its name <ObservingHookWhenStr>) 
before or after the decorated one, and depending on a certain 
ObservingConcludeTuplesList to be realized.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Tester"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import inspect
from ShareYourSystem.Functers import Hooker
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Observer","Observe","Observing","Observed"]
#<DefineDoStrsList>

#<DefineLocals>
ObservingPrefixStr="Observe_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ObserverClass(BaseClass):
	
	def default_init(self,
					_ObservingTriggerMethodStr="",
					_ObservingHookMethodStr="set", 	
					_ObservingHookWhenStr='After', 				
					_ObservedTriggerMethodFunction=None,  	
					_ObservedHookMethodFunction=None, 									   			
					**_KwargVariablesDict
				):

		#Call the init parent method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#observe
		self.observe()

		#Return
		return _Class

	def do_observe(self):

		#Get
		self.ObservedTriggerMethodFunction=getattr(
			self.DoClass,
			self.ObservingTriggerMethodStr
		)

		#Get
		self.ObservedHookMethodFunction=getattr(
			self.DoClass,
			self.ObservingHookMethodStr
		)

		#Get the name
		self.ObservedMethodStr=self.ObservedTriggerMethodFunction.__name__
		

		ObservedConcludeConditionTuplesList=copy.deepcopy(
			self.ConcludingConditionTuplesList
		)

		#set
		self.ObservedConcludeConditionTuplesListKeyStr=ObservingPrefixStr+self.ObservingTriggerMethodStr+"ConcludeConditionTuplesList"

		#Definition
		def observe(*_ObservingLiargVariablesList,**_ObservingKwargVariablesDict):

			#debug
			'''
			self.debug('We are in the triggerIfBool')
			'''

			#Alias
			ObservedInstanceVariable=_ObservingLiargVariablesList[0]

			#Check
			if self.conclude(**).ConcludedIsBool:

				#debug
				'''
				self.debug(
							[
								('Call the Observing method'),
							]
						)
				'''

				#Get the ObservedFunction (by the name, because the method can be after augmented by other decorations)
				if self.ObservedMethodStr!="<lambda>":
					ObservedFunction=getattr(ObservedInstanceVariable,self.ObservedMethodStr)

					#Call the ObservingFunction
					try:
						ObservedFunction(
							*_ObservingLiargVariablesList[1:],
							**_ObservingKwargVariablesDict
						)
					except:
						ObservedFunction(
							*_ObservingLiargVariablesList[1:]
						)

				else:

					#Call directly the lambda function
					self.ObservingFunction(*_ObservingLiargVariablesList)

				

				#debug
				'''
				self.debug('Ok it was called')
				'''

				#debug
				'''
				self.debug("Hook at the level of the class")
				'''

				#set the ObservedClass
				ObservedClass=InstanceVariable.__class__

				#debug
				'''
				self.debug('ObservedClass is '+str(ObservedClass))
				'''

				#set the Observed function in the class
				self.ObservedIfFunction=triggerIfBool
				self.ObservedIfFunctionStr='trigger'+str(self.ObservingConcludeTuplesList)
				setattr(
							ObservedClass,
							self.ObservedIfFunctionStr,
							self.ObservedIfFunction
						)

				#Get the Observed hook function
				self.ObservedHookFunction=getattr(ObservedClass,self.ObservingHookMethodStr).im_func

				#Definition the new Observed hook function
				HookingVariablesListKeyStr='Hooking'+(
								'After' if self.ObservingHookWhenStr=='Before' else (
									'Before' if self.ObservingHookWhenStr=='After' else ''
									) ) +'VariablesList'
				@Hooker.HookerClass(**{
										HookingVariablesListKeyStr:[
										{'CallingVariable':self.ObservedIfFunction}
										]
				})
				def ObservedHookFunction(*_ObservingHookLiargVariablesList,**_ObservingHookKwargVariablesDict):

					#Call the ObservedHookFunction
					self.ObservedHookFunction(
						*_ObservingHookLiargVariablesList,
						**_ObservingHookKwargVariablesDict
					)

		#set in the class
		setattr(
					self.DoClass,
					self.ObservingHookMethodStr,
					ObservedHookFunction
				)

		#Return self
		#return self

#</DefineClass>

