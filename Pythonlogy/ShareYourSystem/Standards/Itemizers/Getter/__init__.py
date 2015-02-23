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
class GetClass(object):

	def __init__(self,_Function):

		#Call the base method
		object.__init__(self)

		#init
		self.Function=_Function
		self.SelfVariable=None

	def __call__(self):

		#Debug
		'''
		print('__call__ GetClass')
		print(
				'_LiargVariablesList is '+str(_LiargVariablesList)
			)
		print('')
		'''

		#return
		return self.Function(
			self.SelfVariable
		)


SYS.GetClass=GetClass
GetDeletePrefixStr="#delete:"
GetDirectPrefixStr="#direct:"
GetShortKeyStr="#get"
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

	def getMapValueVariable(self):

		#return
		return self.GettedValueVariable

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
	
	#def __delitem__(self,_KeyVariable):


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
		# Case of a GetClass get
		#

		#Check
		if type(self.GettingKeyVariable)==GetClass:

			#Check
			if self.GettingKeyVariable.SelfVariable==None:
				self.GettingKeyVariable.SelfVariable=self

			#call
			self.GettedValueVariable=self.GettingKeyVariable()

			#Stop the getting
			return {"HookingIsBool":False}


		#/############################
		# Cases of a key str get 
		#

		#Check
		if type(self.GettingKeyVariable) in [str,unicode]:

			#debug
			'''
			self.debug(
					'This is a non method get'
				)
			'''

			'''
			#/############################
			# Case of a delete in the instance __dict__ 
			#

			if self.GettingKeyVariable.startswith(GetDeletePrefixStr)

				#delete
				del self.__dict__[
					SYS.deprefix(
						self.GettingKeyVariable,
						GetDeletePrefixStr
					)
				]

				#Stop the getting
				return {"HookingIsBool":False}
			'''

			#/############################
			# Case of a direct str get 
			#

			if self.GettingKeyVariable.startswith(GetDirectPrefixStr):

				#debug
				'''
				self.debug('This is a direct get of a str variable')
				'''

				#set
				self.GettedValueVariable=SYS.deprefix(
					self.GettingKeyVariable,
					GetDirectPrefixStr
				)

				#Stop the getting
				return {"HookingIsBool":False}

			#/############################
			# Case of a get in the instance __dict__ 
			#

			#Get safely the Value
			elif self.GettingKeyVariable in self.__dict__:

				#debug
				'''
				self.debug(
					[
						'self.GettingKeyVariable exists in the __dict__',
						self.GettingKeyVariable
					]
				)
				'''
				
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
			
			#/############################
			# Case of the __class__ get
			#

			#Check
			elif self.GettingKeyVariable=='__class__':

				#set
				self.GettedValueVariable=self.__class__

				#Stop the getting
				return {"HookingIsBool":False}

			#/############################
			# Case of a get in the instance __dict__ 
			#

			#Check
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
				'''
				self.debug(
						[
							'we are going to set a default value here',
							('self.',self,['GettingKeyVariable'])
						]
					)
				'''

				#get
				GettedValueType=SYS.getTypeClassWithTypeStr(
					SYS.getTypeStrWithKeyStr(
						self.GettingKeyVariable)
				)

				#debug
				'''
				self.debug('GettedValueType is '+str(GettedValueType))
				'''

				#Check
				if callable(GettedValueType):

					#alias
					self.GettedValueVariable=GettedValueType()

					#set a default value
					self.__setattr__(
						self.GettingKeyVariable,
						self.GettedValueVariable
					)

					#add in the SettingValue
					try:
						self.GettedValueVariable.DictKeyStr=self.GettingKeyVariable
					except:
						pass

				#Stop the getting
				return {"HookingIsBool":False}


		#/############################
		# Cases of a dict GetVariable get 
		#

		elif hasattr(self.GettingKeyVariable,'items') and type(self.GettingKeyVariable)!=type:

			#debug
			'''
			self.debug(
				[
					'we get or set with an itemizable instance',
					('self.',self,['GettingKeyVariable'])
				]
			)
			'''

			#try
			try:

				#debug
				'''
				self.debug(
					[
						'we get with the GetVariable'
					]	
				)
				'''
				
				#get
				self.GettedValueVariable=self[
					self.GettingKeyVariable['GetVariable']
				]

				#del
				del self.GettingKeyVariable['GetVariable']

			except:

				try:

					#debug
					'''
					self.debug(
						[
							'we get with the GetShortKeyStr'
						]	
					)
					'''
					
					#get
					self.GettedValueVariable=self[
						self.GettingKeyVariable[GetShortKeyStr]
					]

					#del
					del self.GettingKeyVariable[GetShortKeyStr]

				except:

					#pass
					pass


			#Stop the getting
			return {"HookingIsBool":False}

		#/############################
		# Cases of a direct get 
		#

		#elif hasattr(self.GettingKeyVariable,'MroClassesList'):
		if type(self.GettingKeyVariable)!=str:

			#debug
			'''
			self.debug('This is a direct get of a non str variable')
			'''

			#set
			self.GettedValueVariable=self.GettingKeyVariable

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


