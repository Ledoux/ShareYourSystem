# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Initiator is a trivial module... It just helps for defining directly in 
the __dict__ of an instance of the InitiatorClass some attributes given
by the items setted in the _KwargVariablesDict from the __init__ method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Object"
DecorationModuleStr=""
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineClass>
#@DecorationClass
class InitiatorClass(BaseClass):

	def __init__(self,**_KwargVariablesDict):
		
		#debug
		'''
		print('_KwargVariablesDict is ',_KwargVariablesDict)
		print('')
		'''

		#Map the update
		map(
				lambda __ItemTuple:
				self.__setattr__(__ItemTuple[0],__ItemTuple[1]) 
				#If we want to not set the items setted during hooks and that are not specified...
				if hasattr(self,__ItemTuple[0]) else None
				,_KwargVariablesDict.iteritems()
			)

		#set
		self.IdInt=id(self)
			
#</DefineClass>

#set
InitiatorClass.NameStr="Initiator"
SYS.InitiatorClass=InitiatorClass
SYS.Initiator=globals()