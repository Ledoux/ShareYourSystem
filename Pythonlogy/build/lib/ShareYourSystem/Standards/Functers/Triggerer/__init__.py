# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


While the fset methods defined in properties attributes are good members for assuring
the binding role between values in an instance, the Triggerer makes available
the way of calling an other method (given its name <TriggeringHookStr>) 
before or after the decorated one, and depending on a certain 
TriggeringConditionTuplesList to be realized.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Functers.Functer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import inspect
from ShareYourSystem.Functers import Hooker
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class TriggererClass(BaseClass):
	
	def default_init(self,
					_TriggeringFunction=None,
					_TriggeringConditionTuplesList=None, 	
					_TriggeringHookFunctionStr='set', 			
					_TriggeringHookStr='After', 
					_TriggeringGetStr='',				
					_TriggeredFunction=None,  					
					_TriggeredIsBool=False, 					
					_TriggeredIfFunction=None,  				
					_TriggeredIfFunctionStr="",    			
					**_KwargVariablesDict
				):

		#Call the init parent method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#trigger
		self.trigger()

		#Return
		return _Class

	def __call__(self,_Function):

		#trigger
		self.trigger(_Function)

		#Link
		self.FunctedFunction=self.TriggeredFunction

		#debug
		'''
		self.debug(('self.',self,['FunctedFunction']))
		'''

		#Return the TriggeredFunction
		return BaseClass.__call__(self,_Function)

	def do_trigger(self):

		#Get the name
		self.TriggeredMethodStr=self.TriggeringFunction.__name__
		
		#Definition the big triggering wrapped method
		def TriggeredFunction(*_LiargVariablesList,**_KwargVariablesDict):

			#debug
			'''
			self.debug(('self.',self,['TriggeredIsBool']))
			'''

			#Alias
			InstanceVariable=_LiargVariablesList[0]

			#Hook at the level of the class if it was not already
			if self.TriggeredIsBool==False:

				#Definition the triggering methods
				def triggerIfBool(*_TriggeringLiargVariablesList,**_TriggeringKwargVariablesDict):

					#debug
					'''
					self.debug('We are in the triggerIfBool')
					'''

					#Alias
					TriggeredInstanceVariable=_TriggeringLiargVariablesList[0]

					#Definition the TriggeredGetMethod
					if self.TriggeringGetStr=='':
						TriggeredGetMethod=lambda __KeyStr:getattr(TriggeredInstanceVariable,__KeyStr)
					else:
						TriggeredGetMethod=getattr(TriggeredInstanceVariable,self.TriggeringGetStr)

					#debug
					'''
					self.debug(
								[
									('self.TriggeringConditionTuplesList is '+str(self.TriggeringConditionTuplesList)),
									('picked values are '+str(map(
											lambda __TriggeringTuple:
											TriggeredGetMethod(__TriggeringTuple[0]),
											self.TriggeringConditionTuplesList
											)
										)
									)
								]
							)
					'''

					#Check if we have to trigger
					TriggeredAllBoolsList=map(
											lambda __TriggeringTuple:
											__TriggeringTuple[1][0](
												TriggeredGetMethod(__TriggeringTuple[0]),
												__TriggeringTuple[1][1]
											),
											self.TriggeringConditionTuplesList
										)
									

					#debug
					'''
					self.debug('TriggeredAllBoolsList is '+str(TriggeredAllBoolsList))
					'''

					#Check
					if all(TriggeredAllBoolsList) or len(TriggeredAllBoolsList)==0:

						#debug
						'''
						self.debug(
									[
										('Call the triggering method'),
									]
								)
						'''

						#Get the TriggeredFunction (by the name, because the method can be after augmented by other decorations)
						if self.TriggeredMethodStr!="<lambda>":
							TriggeredFunction=getattr(TriggeredInstanceVariable,self.TriggeredMethodStr)

							#Call the TriggeringFunction
							try:
								TriggeredFunction(
									*_TriggeringLiargVariablesList[1:],
									**_TriggeringKwargVariablesDict
								)
							except:
								TriggeredFunction(
									*_TriggeringLiargVariablesList[1:]
								)

						else:

							#Call directly the lambda function
							self.TriggeringFunction(*_TriggeringLiargVariablesList)

						

						#debug
						'''
						self.debug('Ok it was called')
						'''

				#debug
				'''
				self.debug("Hook at the level of the class")
				'''

				#set the TriggeredClass
				TriggeredClass=InstanceVariable.__class__

				#debug
				'''
				self.debug('TriggeredClass is '+str(TriggeredClass))
				'''

				#set the triggered function in the class
				self.TriggeredIfFunction=triggerIfBool
				self.TriggeredIfFunctionStr='trigger'+str(self.TriggeringConditionTuplesList)
				setattr(
							TriggeredClass,
							self.TriggeredIfFunctionStr,
							self.TriggeredIfFunction
						)

				#Get the triggered hook function
				self.TriggeredHookFunction=getattr(TriggeredClass,self.TriggeringHookFunctionStr).im_func

				#Definition the new triggered hook function
				HookingVariablesListKeyStr='Hooking'+(
								'After' if self.TriggeringHookStr=='Before' else (
									'Before' if self.TriggeringHookStr=='After' else ''
									) ) +'VariablesList'
				@Hooker.HookerClass(**{
										HookingVariablesListKeyStr:[
										{'CallingVariable':self.TriggeredIfFunction}
										]
				})
				def triggeredHookFunction(*_TriggeringHookLiargVariablesList,**_TriggeringHookKwargVariablesDict):

					#Call the TriggeredHookFunction
					self.TriggeredHookFunction(
						*_TriggeringHookLiargVariablesList,
						**_TriggeringHookKwargVariablesDict
					)

				#set in the class
				setattr(
							TriggeredClass,
							self.TriggeringHookFunctionStr,
							triggeredHookFunction
						)
				
				#Say True now
				self.TriggeredIsBool=True

			#debug
			'''
			self.debug(('self',self,['TriggeringFunction']))
			'''

			#Call the TriggeringFunction
			self.TriggeringFunction(*_LiargVariablesList,**_KwargVariablesDict)

			#Return self for the wrapped method call
			return InstanceVariable

		#set 
		self.TriggeredFunction=TriggeredFunction

		#Return self
		#return self

#</DefineClass>

