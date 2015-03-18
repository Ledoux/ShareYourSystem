# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Networker 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Networker','Network','Networking','Networked')
#</DefineAugmentation>

#<ImportSpecificModules>
Pointer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
NetworkFlatPrefixStr='__Net__'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class NetworkerClass(BaseClass):

	def default_init(
					self,
					_NetworkTagStr='Top',
					_NetworkDeriveNetworkerVariable=None,
					_NetworkTargetStr='Top',
					_NetworkingTeamVariable=None,
					_NetworkingManagementVariable=None,
					_NetworkedTeamStrsList=None,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.NetworkDeriveNetworkerVariable=self

	def do_network(self):

		
		#debug
		self.debug(
				[
					'We network here',
					('self.',self,[
							'NetworkingTeamVariable',
							'NetworkingManagementVariable'
						])
				]
			)

		#/##################/#
		# prepare the Net teams
		#

		#map
		self.NetworkedTeamStrsList=map(
				lambda __NetworkingTeamOrManagementStr:
				NetworkFlatPrefixStr+__NetworkingTeamOrManagementStr,
				(self.NetworkingTeamVariable if self.NetworkingTeamVariable!=None else [])+
				(self.NetworkingManagementVariable if self.NetworkingManagementVariable!=None else [])
			)

		#debug
		self.debug(
				[
					'We are going to make team the NetworkedTeamStrsList',
					('self.',self,['NetworkedTeamStrsList'])
				]
			)

		#map
		map(
				lambda __NetworkedTeamStr:
				self.team(__NetworkedTeamStr),
				self.NetworkedTeamStrsList
			)

		#/##################/#
		# parent Down
		#

		#parentDown
		self.parentDown(
				self.NetworkingTeamVariable,
				self.NetworkingManagementVariable,
				**{'NetworkTargetStr':self.NetworkTagStr}
			)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#/##################/#
		# Set the NetworkTagStr
		#

		#debug
		'''
		self.debug(
				[
					'We have parented',
					'we set the control path str',
					('self.',self,[
							'ParentedTotalPathStr',
							'ManagementTagStr'
						])
				]
			)
		'''
		
		#Check
		if self.ManagementTagStr!='':

			#get
			self.NetworkTagStr=(
					self.ParentedTotalPathStr+'/'+self.ManagementTagStr
				).replace('/','_')

		#remove
		if self.NetworkTagStr[0]=='_':
			self.NetworkTagStr=self.NetworkTagStr[1:]

		#/##################/#
		# Find the first top Networker
		#

		#find
		self.debug(
			[
				'We have parented',
				('self.',self,[
						#'ParentedDeriveTeamersList',
						'NetworkTargetStr'
					]),
				'Now find the NetworkDeriveNetworkerVariable'
			]
		)
		
		#Check
		if len(self.ParentedDeriveTeamersList)>0:

			#index
			try:

				#index
				IndexInt=map(
						lambda __ParentedDeriveTeamer:
						hasattr(
							__ParentedDeriveTeamer,
							'NetworkTargetStr'
						) and __ParentedDeriveTeamer.NetworkTargetStr==self.NetworkTargetStr,
						self.ParentedDeriveTeamersList
					).index(True)

				#set
				self.NetworkDeriveNetworkerVariable=self.ParentedDeriveTeamersList[IndexInt]

			except:

				IndexInt=len(self.ParentedDeriveTeamersList)
			
		#debug
		self.debug(
				[
					'Finally NetworkDeriveNetworkerVariable is ',
					SYS._str(self.NetworkDeriveNetworkerVariable)
				]
			)

		#/##################/#
		# Add to the top Controller
		#

		#debug
		self.debug(
			[
				('self.',self,[
					'TeamTagStr',
					'ManagementTagStr'
				])
			]
		)

		#Check
		if self.TeamTagStr!="":
			
			#debug
			self.debug(
					[
						'we make manage the '+str(
							NetworkFlatPrefixStr+self.ParentDeriveTeamerVariable.ManagementTagStr
						)
					]
				)

			#make manage the team net
			self.NetworkDeriveNetworkerVariable.TeamDict[
				NetworkFlatPrefixStr+self.ParentDeriveTeamerVariable.ManagementTagStr
			].manage(
				self.NetworkTagStr,
				self
			)

		if self.ManagementTagStr!="":
			
			#debug
			self.debug(
					[
						'we make manage the '+str(
							NetworkFlatPrefixStr+self.ParentDeriveTeamerVariable.TeamTagStr
						),
						('self.',self,[
								'NetworkTagStr'
							])
					]
				)

			#make manage the team net
			self.NetworkDeriveNetworkerVariable.TeamDict[
				NetworkFlatPrefixStr+self.ParentDeriveTeamerVariable.TeamTagStr
			].manage(
				self.NetworkTagStr,
				self
			)

#</DefineClass>

#<DefineLocals>

#set
Pointer.PointerClass.ManagingValueClass=NetworkerClass

#</DefineLocals>

#</DefinePrint>
NetworkerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NetworkTagStr',
		'NetworkDeriveNetworkerVariable',
		'NetworkTargetStr',
		'NetworkingTeamVariable',
		'NetworkingManagementVariable',
		'NetworkedTeamStrsList'
	]
)
#<DefinePrint>
