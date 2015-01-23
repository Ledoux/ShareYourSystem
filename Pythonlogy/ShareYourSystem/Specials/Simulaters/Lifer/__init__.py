# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Lifer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Dynamizer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineClass>
@DecorationClass()
class LiferClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'RatingMatrixStr',
								'RatedPreStr'
							]

	def default_init(self,
						_LifingVoltage='J',
						_RatingConstantTimeFloat='tau',
						_RatedPreStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_rate(
				self,
			):	

	
		#debug
		'''
		self.debug(('self.',self,[

					]))
		'''

		#add the connection variable		
		self.RatedPreStr+=self.RatingMatrixStr+self.DynamizingTraceStr

		#add the constant time
		#self.RatedPreStr+=')/('+self.RatingConstantTimeStr+'*'+self.DynamizingTimeDimensionStr+')'
		self.RatedPreStr+=')/('+self.RatingConstantTimeStr+')'
		
	def mimic_dynamize(self):

		#parent method
		BaseClass.dynamize(self)

		#rate first
		self.rate()

		#add in the DynamizedPreStr 
		if self.DynamizedPreStr!='(':
			self.DynamizedPreStr+=' + '
		self.DynamizedPreStr+=self.RatedPreStr 

		#Check
		if self.RatingMatrixStr!="":
			self.DynamizedParamStr+=self.RatingMatrixStr+self.DynamizingTraceStr+' : '+self.DynamizingTraceDimensionStr+'\n'

		#Check
		if self.RatingConstantTimeStr!="":
			self.DynamizedParamStr+=self.RatingConstantTimeStr+' : '+self.DynamizingTimeDimensionStr+'\n'

		#set
		self.DynamizingRateThresholdFunction=lambda _VariableFloat :(_VariableFloat<=0.)
		
#</DefineClass>
