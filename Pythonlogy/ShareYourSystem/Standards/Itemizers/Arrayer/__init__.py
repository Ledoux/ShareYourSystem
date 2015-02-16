# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Arrayer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Setter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import itertools
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ArrayerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
								'ArrayingKeyVariablesList',
								'ArrayingValueVariable',
							]

	def default_init(self,
						_ArrayingKeyVariablesList=None,
						_ArrayingValueVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_array(self):
		
		#Check
		if len(self.ArrayingKeyVariablesList)>0:

			#/####################/#
			# Adapt the shape of the ValueVariable
			#

			#Check
			if SYS.getIsTuplesListBool(self.ArrayingValueVariable[0]) or hasattr(
				self.ArrayingValueVariable[0],'items'):

			 	#debug
			 	self.debug('This is an identical array setting')

			 	#list
			 	ArrayedLocalValueVariablesList=[self.ArrayingValueVariable[0]]*len(
			 		self.ArrayingKeyVariablesList
			 	)
			 	ArrayedDeepValueVariablesList=self.ArrayingValueVariable[1:]

			elif self.ArrayingValueVariable!=None and len(self.ArrayingValueVariable)>0:

				#debug
			 	self.debug('This is an original setting')

			 	#split
				ArrayedLocalValueVariablesList=self.ArrayingValueVariable[0]
				ArrayedDeepValueVariablesList=self.ArrayingValueVariable[1:]

			else:

				#debug
			 	self.debug('There is no identical or original setting')

			 	#list default
				ArrayedLocalValueVariablesList=[]
				ArrayedDeepValueVariablesList=[]

			#/####################/#
			# Case where we have to set and then array deeper
			#

			#Check
			if len(self.ArrayingKeyVariablesList)>1:

				

				#map
				map(
						lambda __ArrayingKeyVariable,__ArrayingLocalValueVariable:
						self.set(
								__ArrayingKeyVariable,
								__ArrayingLocalValueVariable
								if __ArrayingLocalValueVariable!=None
								else {}
							).SettingValueVariable.array(
								self.ArrayingKeyVariablesList[1:],
								ArrayedDeepValueVariablesList
							),
						self.ArrayingKeyVariablesList[0],
						ArrayedLocalValueVariablesList
					)

			#/####################/#
			# Case where we have just to set
			#

			else:

				#map
				map(
						lambda __ArrayingKeyVariable,__ArrayingLocalValueVariable:
						self.set(
								__ArrayingKeyVariable,
								__ArrayingLocalValueVariable
								if __ArrayingLocalValueVariable!=None
								else {}
							),
						self.ArrayingKeyVariablesList[0],
						ArrayedLocalValueVariablesList
					)

		

#</DefineClass>

