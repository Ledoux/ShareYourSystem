# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Cumulater pick and 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Walkers.Walker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CumulaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CumulatedVariablesList'
							]

	def default_init(self,
				_CumulatedVariablesList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_cumulate(self):
			
		#debug
		'''
		self.debug(('self.',self,[
									'WalkingSocketDict',
									'WalkedTopOrderedDict'
								]))
		'''	

		#Init
		if 'CumulateVariablesList' not in self.WalkedTopOrderedDict:
			self.WalkedTopOrderedDict['CumulateVariablesList']=[]


		#debug
		'''
		self.debug(
					('self.',self,[
							'ConcludingConditionTuplesList',
							])
				)
		'''
		
		#Check
		self.WalkedTopOrderedDict['CumulateVariablesList'].append(
			self.filter('/').FilteredVariablesList
		)
	
		#debug
		'''
		self.debug(('self.',self,['FilteredVariablesList']))
		'''

		#set
		if self.WalkingSocketDict['TopVariable']==self:
			self.CumulatedVariablesList=self.WalkedTopOrderedDict['CumulateVariablesList']
			#self.CumulatedVariablesList=copy.copy(self.WalkedTopOrderedDict['CumulateVariablesList'])
		

#</DefineClass>
