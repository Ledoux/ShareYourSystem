# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Getter helps for getting attributes safely in 
an instance. Through the __getitem__ method, It looks first in the \_\_dict\_\_ to 
check if there is the corresponding GettingKeyStr.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Itemizer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Itemizer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
def getMapList(_LiargVariablesList):
	return SYS.listify(_LiargVariablesList)
def getLiargVariablesList(_ValueVariable):
	return [_ValueVariable]
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class GetterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'GettingKeyVariable',
									'GettingItemBool',
									'GettingNewBool',
									'GettedValueVariable'
								]

	def default_init(self,
						_GettingKeyVariable=None,
						_GettingItemBool=True,
						_GettingNewBool=True,
						_GettedValueVariable=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def __getitem__(self,_KeyVariable):
		""" """

		#Debug
		'''
		print('l.53 __getitem__ Getter')
		print('self.get is ',self.get.im_func)
		print('_KeyVariables is ',_KeyVariable)
		print('')
		'''

		#get
		self.get(_KeyVariable)
		
		#Debug
		'''
		self.debug(('self.',self,['GettedValueVariable']))
		'''
		
		#return
		return self.GettedValueVariable
		
	def do_get(self):
		""" """

		#debug
		'''
		self.debug(
			[
				("self.",self,[
						'GettingKeyVariable',
						'NameStr'
					]
				)
			]
		)
		'''

		#itemize first
		if self.GettingItemBool:

			#debug
			'''
			self.debug('first we itemize')
			'''

			#Check
			if self.GettingKeyVariable==Itemizer.ItemMapPrefixStr+'get':

				#set
				self.ItemizingMapGetVariable='GettedValueVariable'

			#itemize
			self.itemize(
					self.GettingKeyVariable
				)

			#Check
			if self.GettingKeyVariable==Itemizer.ItemMapPrefixStr+'get':

				#set
				self.GettingItemBool=False

		else:

			#set
			self.ItemizedValueMethod=None

			#set
			self.GettingItemBool=True

		#/############################
		# Case of a method get 
		#

		#debug
		'''
		self.debug(
				('self.',self,['ItemizedValueMethod'])
			)
		'''

		#Check 
		if self.ItemizedValueMethod!=None:

			#debug
			'''
			self.debug(
				[
					'This is a method get',
					('self.',self,[
						'ItemizedValueMethod',
						'ItemizingMapGetVariable'
						]
					)
				]
			)
			'''

			#alias
			self.GettedValueVariable=self.ItemizedValueMethod

			#Stop the getting
			return {"HookingIsBool":False}

		#/############################
		# Case of a non method get 
		#

		elif type(self.GettingKeyVariable) in [str,unicode]:

			#debug
			'''
			self.debug(
					'This is a non method get'
				)
			'''

			#Get safely the Value
			if self.GettingKeyVariable in self.__dict__:

				#__getitem__ in the __dict__
				self.GettedValueVariable=self.__dict__[
					self.GettingKeyVariable
				]

				#debug
				'''
				self.debug(
							[
								'This is a Spe in Instance',
								('self.',self,['GettedValueVariable'])
							]
						)
				'''

				#Stop the getting
				return {"HookingIsBool":False}
				
			elif self.GettingKeyVariable in self.__class__.__dict__:

				#__getitem__ in the __class__
				self.GettedValueVariable=self.__class__.__dict__[
					self.GettingKeyVariable
				]

				#debug
				'''
				self.debug(
							[
								'This is in the __class__',
								('self.',self,['GettedValueVariable'])
							]
						)
				'''

				#Stop the getting
				return {"HookingIsBool":False}

			elif self.GettingNewBool:

				#debug
				self.debug(
						[
							'we are going to set a default value here',
							('self.',self,['GettingKeyVariable'])
						]
					)

				#get
				GettedValueType=SYS.getTypeClassWithTypeStr(
					SYS.getTypeStrWithKeyStr(
						self.GettingKeyVariable)
				)

				#debug
				self.debug('GettedValueType is '+str(GettedValueType))

				#Check
				if callable(GettedValueType):

					#alias
					self.GettedValueVariable=GettedValueType()

					#set a default value
					self.__setattr__(
						self.GettingKeyVariable,
						self.GettedValueVariable
					)

				#Stop the getting
				return {"HookingIsBool":False}

				
		#set
		self.GettedValueVariable=None

		#debug
		'''
		self.debug(
					[
						'Not found here so set it to None',
						('self.',self,['GettedValueVariable'])
					]
				)
		'''
		#Return an output dict
		return {"HookingIsBool":True}

#</DefineClass>


