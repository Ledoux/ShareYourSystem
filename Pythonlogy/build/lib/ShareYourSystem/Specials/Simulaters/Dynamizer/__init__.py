# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Dynamizer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DynamizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'DynamizingTraceStr',
								'DynamizingExternalCurrentStr',
								'DynamizingTraceDimensionStr',
								'DynamizedParamStr',
								'DynamizedParamStr',
								'DynamizedPreStr',
								'DynamizedPostStr'
							]

	def default_init(self,
						_DynamizingTraceStr="v",
						_DynamizingExternalCurrentStr='mu',
						_DynamizingTraceDimensionStr='mV',
						_DynamizingTimeDimensionStr='ms',
						_DynamizingThresholdFunction=None,
						_DynamizedParamStr="",
						_DynamizedPreStr="",
						_DynamizedPostStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_dynamize(
				self,
			):	

		#debug
		'''
		self.debug(('self.',self,[

					]))
		'''

		#set
		self.DynamizedPostStr='d'+self.DynamizingTraceStr+'/dt='

		#init
		self.DynamizedPreStr='('

		#Check
		if self.DynamizingExternalCurrentStr!="":

			#Add in params declaration
			self.DynamizedParamStr+=self.DynamizingExternalCurrentStr+' : '+self.DynamizingTraceDimensionStr+'\n'

			#Add in DynamizedPostStr
			self.DynamizedPreStr+=self.DynamizingExternalCurrentStr

	def mimic_populate(self):

		#dynamize first
		self.dynamize()

		#set
		self.PopulatingEquationStr='\n'.join(
			[
				self.DynamizedParamStr,
				self.DynamizedPostStr+self.DynamizedPreStr+' : '+self.DynamizingTraceDimensionStr
			]
		)

		#parent
		BaseClass.populate(self)

#</DefineClass>
