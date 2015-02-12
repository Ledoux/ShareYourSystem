# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Inspecter decorates a class by giving it an InspectedArgumentDict that is 
an inspection of all defined methods.
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Propertiser"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import inspect
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class InspecterClass(BaseClass):

	def default_init(self,**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __call__(self,_Class):

		#Call the parent init method
		BaseClass.__call__(self,_Class)

		#Inspect
		self.inspect()

		#Return _Class
		return _Class

	def do_inspect(self):

		#Alias
		InspectedClass=self.DoClass

		#Debug
		'''
		print('InspectedClass is ',InspectedClass)
		print('')
		'''
		
		#Get the Methods
		InspectedClass.InspectedMethodDict=SYS.MethodDict(InspectedClass)

		#dict
		InspectedClass.InspectedArgumentDict=dict(
			map(	
					lambda __MethodItemTuple:
					(
						__MethodItemTuple[0],
						SYS.ArgumentDict(
							__MethodItemTuple[1]
						)
					),
					InspectedClass.InspectedMethodDict.items()
				)
			)

		#Add to the KeyStrsList
		InspectedClass.KeyStrsList+=[
									'InspectedMethodDict',
									'InspectedArgumentDict'
								]

#</Define_Class>

