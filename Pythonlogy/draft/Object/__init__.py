# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Object defines the first class for augmenting new-style object classes

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr=""
DecorationModuleStr=""
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineClass>
#@DecorationClass
class ObjectClass(object):

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

		#call the base method
		object.__init__(self)

#</DefineClass>

#set
ObjectClass.NameStr="Object"
object=ObjectClass
SYS.Object=sys.modules[ObjectClass.__module__]
