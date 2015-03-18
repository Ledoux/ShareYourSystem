# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pointer 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Pointer','Point','Pointing','Pointed')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Interfacers import Printer
from ShareYourSystem.Standards.Itemizers import Pather,Teamer,Manager,Parenter
#</ImportSpecificModules>

#<DefineLocals>
PointPrefixStr="*"
PointPrefixStr="<->"
PointInTeamKeyStr="Inlets"
PointOutTeamKeyStr="Outlets"
PointConnectKeyStr='?>'
def getLiargVariablesList(_ValueVariable):
	return _ValueVariable
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PointerClass(BaseClass):

	def default_init(
					self,
					_PointFromVariable=None,	
					_PointToVariable=None,
					_PointKeyVariablesList=None,
					_PointingKeyVariable=None,
					_PointingOutSetVariable=None,
					_PointingInSetVariable=None,
					_PointingOutTeamStr="Outlets",
					_PointingInTeamStr="Inlets",
					_PointingGetBool=True,
					_PointingValueClass=BaseClass,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_point(self):

		#/####################/#
		# Get the pointed variable
		#

		#debug
		'''
		self.debug(
			[
				'Adapt the type for getting things to point',
				'(if we need to get)',
				("self.",self,[
								'PointingKeyVariable',
								'PointingGetBool'
							])
			]
		)
		'''

		#Check
		if self.PointingGetBool:
		
			#init
			PointedValueVariable=self[self.PointingKeyVariable]

		else:

			#alias
			PointedValueVariable=self.PointingKeyVariable


		#debug
		'''
		self.debug(
				[
					'in the end, PointedValueVariable is ',
					SYS._str(PointedValueVariable)
				]
			)
		'''

		#/####################/#
		# Make it parent if it was not yet the case
		#

		#debug
		'''
		self.debug(
			[
				'We make the PointedValueVariable parentUp',
				'PointedValueVariable is ',
				SYS._str(PointedValueVariable),
				('PointedValueVariable.',PointedValueVariable,[
						'ParentedTotalPathStr'
					])
			]
		)
		'''

		#parentUp
		PointedValueVariable.parentUp()

		#debug
		'''
		self.debug(
			[
				'Ok it has pointed',
				('PointedValueVariable.',PointedValueVariable,[
						'ParentedTotalPathStr'
					])
			]
		)
		'''

		#/####################/#
		# Adapt the type for setting things in the commanded variables
		#

		#debug
		'''
		self.debug(
			[
				'Adapt the type for setting things in the outlet managed pointed variable',
				("self.",self,[
					'PointingOutSetVariable'
					])
			]
		)
		'''

		#inits
		PointingOutSetVariablesList=SYS.SetList(self.PointingOutSetVariable)

		#debug
		'''
		self.debug(
				[
					'in the end, PointingOutSetVariablesList is ',
					SYS._str(PointingSetVariablesList),
					'Now adapt the type for setting things in the outlet managed pointed variable',
					("self.",self,[
						'PointingOutSetVariable'
						])
				]
			)
		'''

		#inits
		PointingInSetVariablesList=SYS.SetList(self.PointingInSetVariable)

		#debug
		'''
		self.debug(
				[
					'in the end, PointingInSetVariablesList is ',
					SYS._str(PointingSetVariablesList)
				]
			)
		'''

		#/####################/#
		# Now put this getted variable in a 
		# encapsulating managed outlets variable

		#debug
		'''
		self.debug(
				[
					'Now we out team '
				]
			)
		'''

		#Check
		if self.PointingOutTeamStr not in self.TeamDict:
			PointedOutDeriveTeamer=self.team(
				self.PointingOutTeamStr
			).TeamedValueVariable
		else:
			PointedOutDeriveTeamer=self.TeamDict[
				self.PointingOutTeamStr
			]

		#team
		PointedOutDeriveTeamer.manage(
				PointedValueVariable.ParentedTotalPathStr.replace(
					'/','_'
				)+'_'+PointedValueVariable.ManagementTagStr,
				SYS.update(
					[
						('PointToVariable',PointedValueVariable),
						('PointFromVariable',self)
					],
					PointingOutSetVariablesList,
				),
				_ValueClass=self.PointingValueClass
			)

		#/####################/#
		# And put also the inverse in a 
		# encapsulating managed inlets in the getted variable

		#debug
		'''
		self.debug(
				[
					'Now we in team ',
					'IMPORTANT the PointingInTeamStr is from the original pointing',
					'not the pointed object',
					('self.',self,['PointingInTeamStr'])
				]
			)
		'''

		#Check
		if self.PointingInTeamStr not in PointedValueVariable.TeamDict:
			PointedInDeriveTeamer=PointedValueVariable.team(
				self.PointingInTeamStr
			).TeamedValueVariable
		else:
			PointedInDeriveTeamer=PointedValueVariable.TeamDict[
			self.PointingInTeamStr
		]

		#team
		PointedInDeriveTeamer.manage(
				self.ParentedTotalPathStr.replace(
					'/','_'
				)+'_'+self.ManagementTagStr,
				SYS.update(
					[
						('PointToVariable',self),
						('PointFromVariable',PointedValueVariable)
					],
					PointingInSetVariablesList,
				),
				_ValueClass=self.PointingValueClass
			)

	def mimic_get(self):

		#Check
		if type(self.GettingKeyVariable)==str:

			#Check
			if self.GettingKeyVariable.startswith(PointPrefixStr):

				#debug
				'''
				self.debug(
						[
							'We get point here',
							('self.',self,['GettingKeyVariable'])
						]
					)
				'''

				#point
				self.point(
						SYS.deprefix(
							self.GettingKeyVariable,
							PointPrefixStr
						),
						None
					)

				#return
				return {'HookingIsBool':False}

		#set
		BaseClass.get(self)

	def mimic_set(self):

		#Check
		if type(self.SettingKeyVariable)==str:

			#Check
			if self.SettingKeyVariable.startswith(PointPrefixStr):

				if type(
					self.SettingValueVariable
				)==list and SYS.getIsTuplesListBool(self.SettingValueVariable
				)==False and len(self.SettingValueVariable)==2:

					#debug
					'''
					self.debug(
							[
								'We set point here',
								('self.',self,['SettingKeyVariable'])
							]
						)
					'''

					#point
					self.point(
							SYS.deprefix(
								self.SettingKeyVariable,
								PointPrefixStr
							),
							self.SettingValueVariable[0],
							self.SettingValueVariable[1]
						)

					#return
					return {'HookingIsBool':False}

				else:

					#debug
					'''
					self.debug(
							[
								'We set point back here',
								('self.',self,['SettingKeyVariable'])
							]
						)
					'''

					#point
					self.point(
							SYS.deprefix(
								self.SettingKeyVariable,
								PointPrefixStr
							),
							self.SettingValueVariable
						) 

					#return
					return {'HookingIsBool':False}

		#set
		BaseClass.set(self)

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#Check
			if self.PrintingCopyVariable.PointToVariable!=None:

				self.PrintingCopyVariable.PointToVariable=Printer.getPointerStr(
					self.PrintingCopyVariable.PointToVariable
				)
			else:

				#append
				self.PrintingCopyVariable.PrintingInstanceSkipKeyStrsList.append('PointToVariable')

				#debug
				'''
				print('Pointer l 325')
				print('Remove PointToVariable')
				print('self.PrintingCopyVariable.PrintingInstanceSkipKeyStrsList is ')
				print(self.PrintingCopyVariable.PrintingInstanceSkipKeyStrsList)
				print('')
				'''
				
		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/##################/#
		# Call the base method
		#

		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/##################/#
		# point the KeyStrsList
		#

		#debug
		'''
		self.debug(
				[
					'We make point the PointKeyVariablesList',
					('self.',self,['PointKeyVariablesList'])
				]
			)
		'''

		#Check
		if self.PointKeyVariablesList!=None:

			#map
			map(
					lambda __PointKeyStr:
					self.point(
						__PointKeyStr,
						None
					),
					self.PointKeyVariablesList
				)


#</DefineClass>

#<DefineLocals>

#set
Parenter.ParenterClass.ManagingValueClass=PointerClass
PointerClass.PointingValueClass=PointerClass

#</DefineLocals>

#</DefinePrint>
PointerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PointFromVariable',
		#'PointToVariable',
		'PointVariablesList',
		'PointKeyVariablesList',
		'PointingKeyVariable',
		'PointingOutSetVariable',
		'PointingInSetVariable',
		'PointingOutTeamStr',
		'PointingInTeamStr',
		'PointingGetBool',
		'PointingValueClass'
	]
)
#<DefinePrint>
