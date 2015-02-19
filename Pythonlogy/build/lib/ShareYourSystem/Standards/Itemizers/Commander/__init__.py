# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Commander gather Variables to set them with an UpdateList.
The command process can be AllSetsForEach (ie a map of the update succesively for each)
or a EachSetForAll (ie each set is a map of each).

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pather"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
CommandPrefixStr="--"
CommandWalkStr="..."
CommandSelfStr="/"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class CommanderClass(BaseClass):

	#Definition 
	RepresentingKeyStrsList=[
							#'CommandingGetVariable',
							#'CommandingSetVariable',
							'CommandingOrderStr',
							'CommandingBeforeWalkBool',
							'CommandingAfterWalkBool',
							'CommandingBeforeSelfBool',
							'CommandingAfterSelfBool'
						]

	def default_init(
				self,
				_CommandingGetVariable=None,
				_CommandingSetVariable=None,	
				_CommandingOrderStr="AllSetsForEachGet",
				_CommandingBeforeWalkBool=False,	
				_CommandingAfterWalkBool=False,	
				_CommandingBeforeSelfBool=False,
				_CommandingAfterSelfBool=False,		
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_set(self):

		#debug
		'''
		self.debug(
				('self.',self,[
						'SettingKeyVariable',
						'SettingValueVariable'
					])
			)
		'''

		#Check
		if type(self.SettingKeyVariable)==str:

			#Check
			if self.SettingKeyVariable.startswith(
				CommandPrefixStr
			):

				#debug
				'''
				self.debug(
						'We command here'
					)
				'''

				#deprefix
				CommandGetKeyStr=SYS.deprefix(
					self.SettingKeyVariable,
					CommandPrefixStr
				)
				
				#Check
				if CommandGetKeyStr.startswith(CommandWalkStr):

					#debug
					'''
					self.debug(
							'We command-walk here'
						)
					'''

					#command
					self.command(
						SYS.deprefix(
							CommandGetKeyStr,
							CommandWalkStr
						),
						self.SettingValueVariable,
						_AfterWalkBool=True
					)

					#stop the setting
					return {'HookingIsBool':False}

				elif CommandGetKeyStr.startswith(CommandSelfStr+CommandWalkStr):

					#debug
					'''
					self.debug(
							'We command-self-walk here'
						)
					'''

					#command
					self.command(
						SYS.deprefix(
							CommandGetKeyStr,
							CommandSelfStr+CommandWalkStr
						),
						self.SettingValueVariable,
						_AfterWalkBool=True,
						_SelfBool=True
					)

					#stop the setting
					return {'HookingIsBool':False}

				else:

					#command
					self.command(
						CommandGetKeyStr,
						self.SettingValueVariable
					)

					#stop the setting
					return {'HookingIsBool':False}

			#Check
			elif self.SettingKeyVariable.startswith(
				CommandWalkStr
			):

				#debug
				'''
				self.debug(
						'We walk-command here'
					)
				'''

				CommandGetKeyStr=SYS.deprefix(
						self.SettingKeyVariable,
						CommandWalkStr
					)

				#Check
				if CommandGetKeyStr.startswith(CommandPrefixStr):

					#command
					self.command(
						SYS.deprefix(
							CommandGetKeyStr,
							CommandPrefixStr
						),
						self.SettingValueVariable,
						_BeforeWalkBool=True
					)

					#stop the setting
					return {'HookingIsBool':False}

				elif CommandGetKeyStr.startswith(CommandSelfStr):

					#command
					self.command(
						SYS.deprefix(
							CommandGetKeyStr,
							CommandSelfStr+CommandPrefixStr
						),
						self.SettingValueVariable,
						_BeforeWalkBool=True,
						_AfterSelfBool=True
					)

					#stop the setting
					return {'HookingIsBool':False}

			#Check
			elif self.SettingKeyVariable.startswith(
				CommandSelfStr+CommandWalkStr+CommandPrefixStr
			):

				#command
				self.command(
					SYS.deprefix(
						self.SettingKeyVariable,
						CommandSelfStr+CommandWalkStr+CommandPrefixStr
					),
					self.SettingValueVariable,
					_BeforeWalkBool=True,
					_BeforeSelfBool=True
				)

				#stop the setting
				return {'HookingIsBool':False}

			#Call the base method
			BaseClass.set(self)

				



	def do_command(self):
		""" """

		#/####################/#
		# Adapt the type for getting things to command
		#

		#debug
		self.debug(
			[
				'Adapt the type for getting things to command',
				("self.",self,[
								'CommandingGetVariable',
								'CommandingSetVariable'
							])
			]
		)

		#Check
		if type(self.CommandingGetVariable)!=list:
			
			#Check
			if SYS.getIsGetDictBool(self.CommandingGetVariable)==False:
				
				#map a get
				CommandedValueVariablesList=[self[self.CommandingGetVariable]]

			else:

				#debug
				'''
				self.debug(
					[
						'it is a dictated dict, so get it first',
						('self.',self,['CommandingGetVariable'])
					]
				)
				'''
				
				#it is a dictated get
				CommandedValueVariablesList=self[
					self.CommandingGetVariable
				]

		else:

			#map a get
			CommandedValueVariablesList=map(
					lambda __CommandingGetVariable:
					self[__CommandingGetVariable],
					self.CommandingGetVariable
				)

		#filter
		CommandedValueVariablesList=SYS.filterNone(CommandedValueVariablesList)

		#debug
		'''
		self.debug(
				[
					'in the end, CommandedValueVariablesList is ',
					SYS._str(CommandedValueVariablesList)
				]
			)
		'''

		#/###################/#
		# Check if we have to walk before
		#

		#Check
		if self.CommandingBeforeWalkBool:

			#debug
			self.debug(
				[
					'we are going to walk before the command',
					'CommandedValueVariablesList is '+SYS._str(CommandedValueVariablesList),
					'self.getDoing(SYS.CommanderClass).values() is '+SYS._str
					(self.getDoing(
						SYS.CommanderClass).values())
				]
			)

			#Debug
			'''
			for __CommandedValueVariable in CommandedValueVariablesList:

				#debug
				self.debug(
					'__CommandedValueVariable is '+SYS._str( __CommandedValueVariable)
				)

				#set
				__CommandedValueVariable.set(
							'GettingNewBool',False
						).command(
							*self.getDoing().values()	
						).set(
							'GettingNewBool',True
						)
			'''

			#set
			CommandedOrderedDict=self.getDoing(
									SYS.CommanderClass
								)
			CommandedOrderedDict['CommandingBeforeSelfBool']=False
			CommandedLiargVariablesList=CommandedOrderedDict.values()

			#map the recursion but pay watch to not set new things to walk in...it is an infinite walk either !
			map(
					lambda __CommandedValueVariable:
					__CommandedValueVariable.set(
							'GettingNewBool',False
						).command(
							*CommandedLiargVariablesList	
						).set(
							'GettingNewBool',True
						),
					CommandedValueVariablesList
				)

		

		#/####################/#
		# Adapt the type for setting things in the commanded variables
		#

		#debug
		'''
		self.debug(
			[
				'Adapt the type for setting things in the commanded variables',
				("self.",self,['CommandingSetVariable'])
			]
		)
		'''

		#Check
		if type(self.CommandingSetVariable)!=list:
			
			#Check
			if hasattr(self.CommandingSetVariable,'items'):

				#items
				CommandedSetVariablesList=self.CommandingSetVariable.items()

			else:

				#list
				CommandedSetVariablesList=[
					self.CommandingSetVariable
				]

		else:

			#alias
			CommandedSetVariablesList=self.CommandingSetVariable

		#debug
		'''
		self.debug(
				[
					'in the end, CommandedSetVariablesList is ',
					SYS._str(CommandedSetVariablesList)
				]
			)
		'''

		#/###################/#
		# Ok now we command locally
		#

		#Check
		if self.CommandingBeforeSelfBool:

			#debug
			self.debug(
					'We command before self here'
				)

			#add
			self['map*set'](CommandedSetVariablesList)

		#Check for the order
		if self.CommandingOrderStr=="AllSetsForEachGet":

			#map
			map(
					lambda __CommandedValueVariable:
					map(
						lambda __CommandedSetVariable:
						__CommandedValueVariable.set(
							*__CommandedSetVariable
						),
						CommandedSetVariablesList
					),
					CommandedValueVariablesList
				)

		elif self.CommandingOrderStr=="EachSetForAllGets":

			#map
			map(
					lambda __CommandedSetVariable:
					map(
						lambda __CommandedValueVariables:
						__CommandedValueVariables.set(
							*__CommandedSetVariable
						),
						CommandedValueVariablesList
					),
					CommandedSetVariablesList
				)

		#Check
		if self.CommandingAfterSelfBool:

			#debug
			self.debug(
					'We command after self here'
				)

			#add
			self['map*set'](CommandedSetVariablesList)

		#/###################/#
		# And we check for a walk after
		#

		#Check
		if self.CommandingAfterWalkBool:

			#debug
			self.debug(
				[
					'we are going to walk the command',
					'CommandedValueVariablesList is '+SYS._str(CommandedValueVariablesList)
				]
			)

			#Debug
			'''
			for __CommandedValueVariable in CommandedValueVariablesList:

				#debug
				self.debug(
					'__CommandedValueVariable is '+SYS._str( __CommandedValueVariable)
				)

				#set
				__CommandedValueVariable.set(
							'GettingNewBool',False
						).command(
							*self.getDoing().values()	
						).set(
							'GettingNewBool',True
						)
			'''

			#set
			CommandedOrderedDict=self.getDoing(
									SYS.CommanderClass
								)
			CommandedOrderedDict['CommandingBeforeSelfBool']=False
			CommandedLiargVariablesList=CommandedOrderedDict.values()

			#map the recursion but pay watch to not set new things to walk in...it is an infinite walk either !
			map(
					lambda __CommandedValueVariable:
					__CommandedValueVariable.set(
							'GettingNewBool',False
						).command(
							*CommandedLiargVariablesList	
						).set(
							'GettingNewBool',True
						),
					CommandedValueVariablesList
				)

#</DefineClass>