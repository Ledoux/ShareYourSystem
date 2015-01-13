# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Updater maps a __setitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Gatherer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class UpdaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'UpdatingItemTuplesList'
							]

	def default_init(self,
				_UpdatingItemTuplesList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_update(self):
		""" """

		#debug
		'''
		self.debug("self.UpdatingItemTuplesList is "+Representer.represent(
			self.UpdatingItemTuplesList,**{'RepresentingAlineaIsBool':False}))
		'''

		#Apply
		self.map('__setitem__',map(
									lambda __UpdatingItemTuple:
									{'LiargVariablesList':__UpdatingItemTuple},
									self.UpdatingItemTuplesList
								)
		)

		#Return
		#return self
#</DefineClass>
