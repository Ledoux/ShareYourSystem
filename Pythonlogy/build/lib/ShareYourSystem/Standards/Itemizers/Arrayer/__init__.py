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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Conditioner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import itertools
#</ImportSpecificModules>

#<DefineLocals>
def getLiargVariablesList(_ValueVariable):
	return _ValueVariable
#</DefineLocals>

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
			# Is it going to be a set with several layers
			#

			#debug
			self.debug(
					[
						'Is it going to be a set with several layers ?',
						('self.',self,['ArrayingKeyVariablesList'])
					]
				)

			#Check
			if SYS.getIsListsListBool(self.ArrayingKeyVariablesList):

				#debug
				self.debug('set with several layers')

				#/####################/#
				# Adapt the shape of the ValueVariable
				#

				#list default
				ArrayedLocalValueVariablesList=[]
				ArrayedDeepValueVariablesList=[]

				#Check
				if self.ArrayingValueVariable!=None and len(self.ArrayingValueVariable)>0:

					#Check
					if SYS.getIsTuplesListBool(self.ArrayingValueVariable[0]) or hasattr(
						self.ArrayingValueVariable[0],'items'):

					 	#debug
					 	self.debug('This is an identical layered array setting')

					 	#list
					 	ArrayedLocalValueVariablesList=[self.ArrayingValueVariable[0]]*len(
					 		self.ArrayingKeyVariablesList
					 	)
					 	ArrayedDeepValueVariablesList=self.ArrayingValueVariable[1:]

					elif self.ArrayingValueVariable!=None and len(self.ArrayingValueVariable)>0:

						#debug
					 	self.debug('This is an original layered setting')

					 	#split
						ArrayedLocalValueVariablesList=self.ArrayingValueVariable[0]
						ArrayedDeepValueVariablesList=self.ArrayingValueVariable[1:]
				 	

				#debug
				self.debug(
					[
						'ArrayedLocalValueVariablesList is '+str(
							ArrayedLocalValueVariablesList),
						'ArrayedDeepValueVariablesList is '+str(
							ArrayedDeepValueVariablesList)
					]
				)


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
								)[__ArrayingKeyVariable].array(
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

			#/####################/#
			# It is just one layer
			#

			else:

				#/####################/#
				# Adapt the shape of the ValueVariable
				#

				#list default
				ArrayedLocalValueVariablesList=[]

				#Check
				if self.ArrayingValueVariable==None:

					
					#just a map get
					self['map*get'](*self.ArrayingKeyVariablesList)
				
				#Check
				elif type(self.ArrayingValueVariable)==list:

					#debug
					self.debug('This is an identical non layered setting')

					#map set
					self['map*set'](
							zip(
								self.ArrayingKeyVariablesList,
								self.ArrayingValueVariable
							)
						)

				else:
	
					#map set
					self['map*set'](
							zip(
								self.ArrayingKeyVariablesList,
								[self.ArrayingValueVariable]*len(self.ArrayingKeyVariablesList)
							)
						)

					#debug
					self.debug('This is an original non layered setting')

		

#</DefineClass>

