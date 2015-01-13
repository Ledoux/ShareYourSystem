# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Deleter has a __delitem__ method for deleting things in the <InstanceVariable>.__dict__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Setter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DeleterClass(BaseClass):
		
	def default_init(self,
						_DeletingKeyVariable=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass(**{'ArgumentingDoStr':"Delete"})
	def __delitem__(self,_KeyVariable,**_KwargVariablesDict):
		""" """

		#debug
		'''
		self.debug(('self.',self,['DeletingKeyVariable']))
		'''

		#Delete
		self.delete(_KeyVariable)

		#set
		return self

	def do_delete(self):
		""" """

		#Do the minimal delitem
		if type(self.DeletingKeyVariable) in [str,unicode]:

			#Del Safely the Value
			if self.DeletingKeyVariable in self.__dict__:
				del self.__dict__[self.DeletingKeyVariable]

#</DefineClass>


