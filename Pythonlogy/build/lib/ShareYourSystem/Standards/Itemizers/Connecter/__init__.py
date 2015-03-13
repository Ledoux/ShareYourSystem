# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Connecter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
ConnectOutTeamStr="Outlets"
ConnectInTeamStr="Inlets"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ConnecterClass(BaseClass):

	def default_init(
				self,
				_ConnectedOutDeriveConnectersList=None,
				_ConnectedOutPointDeriveConnectersList=None,
				**_KwargVariablesDict
			):	

		#Call the manage init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#team
		self.team(ConnectOutTeamStr)
		self.team(ConnectInTeamStr)
		
	def do_connect(self):

		#debug
		self.debug(
				[
					'We connect here',
					'first we get the outs ',
					'self.TeamDict[ConnectOutTeamStr].ManagementDict.keys() is',
					str(self.TeamDict[ConnectOutTeamStr].ManagementDict.keys()),
				]
			)

		#/################/#
		# Get the post derive pointing parenters and make them point
		#	

		#set
		self.ConnectedOutDeriveConnectersList=self.TeamDict[
			ConnectOutTeamStr
		].ManagementDict.values()

		#debug
		self.debug(
				[
					'We have getted the post derive connecters',
					('self.',self,['ConnectedOutDeriveConnectersList'])
				]
			)

		#set
		self.ConnectedOutPointDeriveConnectersList=map(
				lambda __ConnectedOutDeriveConnecter:
				__ConnectedOutDeriveConnecter.point(
					_BackBool=True
				).PointedToVariable,
				self.ConnectedOutDeriveConnectersList
			)

		#debug
		self.debug(
				[
					'We have getted the post point connecters',
					('self.',self,['ConnectedOutPointDeriveConnectersList'])
				]
			)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/######################/#
		# Call the base method
		#

		#set
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/#####################/#
		# Call the connect method
		#

		#debug
		self.debug(
				'Now we are going to connect'
			)

		#connect
		self.connect()

#</DefineClass>

#<DefineLocals>

#Set
SYS.ManagerClass.ManagingValueClass=ConnecterClass

#</DefineLocals>

#</DefinePrint>
ConnecterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ConnectedOutDeriveConnectersList',
		'ConnectedOutPointDeriveConnectersList'
	]
)
#<DefinePrint>
