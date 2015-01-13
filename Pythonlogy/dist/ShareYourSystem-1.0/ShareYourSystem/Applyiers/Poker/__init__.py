# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Poker instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Grabber"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PokerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
									'PokingNodeStr',
									'PokingGetStrsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PokingNodeStr="",
						_PokingGetStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Joiner.JoinerClass.model}]})
	#@Argumenter.ArgumenterClass()
	def do_poke(self):
		
		#debug
		'''
		self.debug(('self.',self,['PokingNodeStr','PokingGetStrsList']))
		'''
		
		#Apply __getitem__
		self.map('couple',map(
									lambda __PokingGetStr:
									{
										'LiargVariablesList':
										[
											self.PokingNodeStr,
											__PokingGetStr
										]
									},
									self.PokingGetStrsList
								)
					)

		#Return self
		#return self

#</DefineClass>

