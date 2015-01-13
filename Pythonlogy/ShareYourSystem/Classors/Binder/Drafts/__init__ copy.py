# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Binder...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Observer"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Observer=BaseModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class BinderClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
							'BindingMethodStr',
							'BindingHookStr',
							'BindedUnboundMethod'
						]

	def default_init(self,
					_BindingMethodStr="",	
					_BindingHookStr="After",
					_BindedUnboundMethod=None,						   			
					**_KwargVariablesDict
				):

		#Call the init parent method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent method
		Observer.ObserverClass.__bases__[0].__call__(self,_Class)

		#bind
		self.bind()

		#Return
		return _Class

	def do_bind(self):

		#observe without linking
		self.observe(_IsBool=False)

		#Get
		self.BindedUnboundMethod=getattr(
			self.DoClass,
			self.BindingMethodStr
		)

		#Debug
		'''
		print('Binder l.77')
		print('self.BindedUnboundMethod is')
		print(self.BindedUnboundMethod)
		print('')
		'''

		#Definition
		if self.BindingHookStr=='After':

			#Definition
			def BindedNewFunction(*_LiargVariablesList,**_KwargVariablesDict):
				
				#Debug
				'''
				print('We are in the BindedNewFunction')
				print('self.ObservedOldUnboundMethod is ')
				print(self.ObservedOldUnboundMethod)
				print('_LiargVariablesList is ')
				print(_LiargVariablesList)
				print('_KwargVariablesDict is ')
				print(_KwargVariablesDict)
				print('')
				'''

				#call
				self.BindedUnboundMethod(*_LiargVariablesList,**_KwargVariablesDict)

				#return
				return self.ObservedOldUnboundMethod(*_LiargVariablesList,**_KwargVariablesDict)

		else:

			#Definition
			def BindedNewFunction(*_LiargVariablesList,**_KwargVariablesDict):
				
				#Debug
				'''
				print('We are in the BindedNewFunction')
				print('self.ObservedOldUnboundMethod is ')
				print(self.ObservedOldUnboundMethod)
				'''
				
				#Debug
				'''
				print('_LiargVariablesList is ')
				print(_LiargVariablesList)
				print('_KwargVariablesDict is ')
				print(_KwargVariablesDict)
				print('')
				'''

				#call the ObservedOldUnboundMethod 
				OutputVariable=self.ObservedOldUnboundMethod(*_LiargVariablesList,**_KwargVariablesDict)
				
				#call then the binded
				self.BindedUnboundMethod(*_LiargVariablesList,**_KwargVariablesDict)

				#return
				return OutputVariable

		#link
		self.ObservedNewFunction=BindedNewFunction

		#observe
		self.observe(_IsBool=True)

		#Return self
		#return self

#</DefineClass>

