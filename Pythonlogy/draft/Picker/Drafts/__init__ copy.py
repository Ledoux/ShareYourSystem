# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Picker maps a __getitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Mapper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'DoingGetBool':True})
class PickerClass(BaseClass):
	
	def default_init(self,
				_PickingKeyVariablesList=None,
				_PickedValueVariablesList=None,
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_pick(self):
		"""Map the __getitem__ to the <_GettingVariablesList>"""

		#debug
		'''
		self.debug(('self.',self,['PickingKeyVariablesList']))
		'''

		#Apply __getitem__
		self.map('__getitem__',map(
									lambda __PickingKeyVariable:
									{'LiargVariablesList':[__PickingKeyVariable]},
									self.PickingKeyVariablesList
								)
					)

		#link with AppliedMappedVariablesList
		self.PickedValueVariablesList=self.MappedVariablesList

		#debug
		'''
		self.debug(('self.',self,['PickedValueVariablesList']))
		'''
		
		#Return AppliedVariablesList
		return self.PickedValueVariablesList
#</DefineClass>
