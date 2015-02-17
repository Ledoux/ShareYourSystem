# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Conditioner

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Debugger"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Representer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Representer=DecorationModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConditionerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'ConditioningTestVariable',
									'ConditioningGetBoolFunction',
									'ConditioningAttestVariable',
									'ConditioningInstanceVariable',
									'ConditioningTypesList',
									'ConditionedIsBool',
								]
	
	def default_init(self,
						_ConditioningTestVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestVariable=None,
						_ConditioningInstanceVariable=None,
						_ConditioningTypesList=[type(len),type(type)],
						_ConditionedIsBool=True,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_condition(self):

		#debug
		self.debug(
				('self.',self,[
					'ConditioningInstanceVariable',
					'ConditioningTestVariable'
				])
			)

		#Check
		if self.ConditioningInstanceVariable!=None:

			#Check
			if self.ConditioningTestVariable in self.ConditioningTypesList:

				#call
				self.ConditioningTestVariable=self.ConditioningTestVariable(
						self.ConditioningInstanceVariable
					)

			else:
				
				#try
				try:

					#get
					self.ConditioningTestVariable=self.ConditioningInstanceVariable[
						self.ConditioningTestVariable
					]

				except:

					#pass
					pass

		#debug
		'''
		self.debug(('self.',self,[
									'ConditioningTestVariable',
									'ConditioningAttestVariable'
								]))
		'''
		
		#call
		self.ConditionedIsBool=self.ConditioningGetBoolFunction(
			self.ConditioningTestVariable,
			self.ConditioningAttestVariable
		)

		#debug
		'''
		self.debug(('self.',self,['ConditionedIsBool']))
		'''
		
#</DefineClass>

