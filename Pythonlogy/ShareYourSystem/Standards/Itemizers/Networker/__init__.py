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
NetworkOutPrefixStr='_Net_'
NetworkInTeamKeyStr='Networks'
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
					_NetworkingDoStr="",
					_NetworkedTeamKeyStrsList=None,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.NetworkDeriveNetworkerVariable=self

	def do_network(self):

		#debug
		'''
		self.debug(
				[
					'We network here',
					('self.',self,[
							'NetworkingTeamVariable',
							'NetworkingManagementVariable'
						])
				]
			)
		'''
		
		#/##################/#
		# prepare the Net teams
		#

		#map
		self.NetworkedTeamKeyStrsList=map(
				lambda __NetworkingTeamOrManagementStr:
				NetworkOutPrefixStr+self.NetworkingDoStr+'_'+__NetworkingTeamOrManagementStr,
				(self.NetworkingTeamVariable if self.NetworkingTeamVariable!=None else [])+
				(self.NetworkingManagementVariable if self.NetworkingManagementVariable!=None else [])
			)

		#debug
		'''
		self.debug(
				[
					'We are going to make team the NetworkedTeamKeyStrsList',
					('self.',self,['NetworkedTeamKeyStrsList'])
				]
			)
		'''

		#map
		map(
				lambda __NetworkedTeamKeyStr:
				self.team(__NetworkedTeamKeyStr),
				self.NetworkedTeamKeyStrsList
			)

		#/##################/#
		# parent Down
		#

		#parentDown
		self.parentDown(
				self.NetworkingTeamVariable,
				self.NetworkingManagementVariable,
				**{
					'NetworkTargetStr':self.NetworkTagStr,
					'NetworkingDoStr':self.NetworkingDoStr
				}
			)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/##################/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'First we call the base method',
				('self.',self,[
							'NetworkingTeamVariable',
							'NetworkingManagementVariable'
						])
			]
		)
		'''

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)

		#debug
		'''
		self.debug(
			[
				'We have called the base method',
				('self.',self,[
							'NetworkingTeamVariable',
							'NetworkingManagementVariable'
						])
			]
		)
		'''

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
		# Find the NetworkDeriveNetworkerVariable in the grand parents
		#

		#find
		'''
		self.debug(
			[
				'We have parented',
				('self.',self,[
						#'ParentedDeriveTeamersList',
						'NetworkTargetStr'
					]),
				'Now find the NetworkDeriveNetworkerVariable that has the NetworkTagStr',
				'equal to the self.NetworkTargetStr'
			]
		)
		'''

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
						) and __ParentedDeriveTeamer.NetworkTagStr==self.NetworkTargetStr,
						self.ParentedDeriveTeamersList
					).index(True)

				#set
				self.NetworkDeriveNetworkerVariable=self.ParentedDeriveTeamersList[IndexInt]

			except:

				IndexInt=len(self.ParentedDeriveTeamersList)
			
		#debug
		'''
		self.debug(
				[
					'Finally NetworkDeriveNetworkerVariable is ',
					SYS._str(self.NetworkDeriveNetworkerVariable)
				]
			)
		'''

		#/##################/#
		# Add to the NetworkDeriveNetworkerVariable
		#

		#debug
		'''
		self.debug(
			[
				('self.',self,[
					'TeamTagStr',
					'ManagementTagStr'
				])
			]
		)
		'''

		#Check
		if self.TeamTagStr!="":
			
			#debug
			'''
			self.debug(
					[
						'Check if we have to make manage the '+str(
							NetworkOutPrefixStr+self.ParentDeriveTeamerVariable.ManagementTagStr
						),
						'self.NetworkDeriveNetworkerVariable.NetworkingManagementVariable is ',
						str(self.NetworkDeriveNetworkerVariable.NetworkingManagementVariable)
					]
				)
			'''

			#Check
			if self.NetworkDeriveNetworkerVariable.NetworkingManagementVariable!=None:

				#Check
				if self.ParentDeriveTeamerVariable.ManagementTagStr in self.NetworkDeriveNetworkerVariable.NetworkingManagementVariable:

					#debug
					self.debug(
						[
							'Yes we make team point here',
							('self.',self,['PointingInManagementKeyStr']),
							'self.ParentDeriveTeamerVariable.ManagementTagStr is ',
							str(self.ParentDeriveTeamerVariable.ManagementTagStr)
						]
					)

					#point
					self.NetworkDeriveNetworkerVariable.point(
							self,
							_OutTeamKeyStr=NetworkOutPrefixStr+self.NetworkingDoStr+'_'+self.ParentDeriveTeamerVariable.ManagementTagStr,
							_InTeamKeyStr=NetworkInTeamKeyStr
					)

		if self.ManagementTagStr!="":
			
			#debug
			'''
			self.debug(
					[
						'we make point the top networker on the team'+str(
							NetworkOutPrefixStr+self.ParentDeriveTeamerVariable.TeamTagStr
						),
						('self.',self,[
								'NetworkTagStr'
							])
					]
				)
			'''

			#Check
			if self.NetworkDeriveNetworkerVariable.NetworkingTeamVariable!=None:

				#Check
				if self.ParentDeriveTeamerVariable.TeamTagStr in self.NetworkDeriveNetworkerVariable.NetworkingTeamVariable:

					#debug
					'''
					self.debug(
						[
							'Yes we make team point here',
							('self.NetworkDeriveNetworkerVariable.',
								self.NetworkDeriveNetworkerVariable,
								['PointingInManagementKeyStr'])
						]
					)
					'''

					#point
					self.NetworkDeriveNetworkerVariable.point(
						self,
						_OutTeamKeyStr=NetworkOutPrefixStr+self.NetworkingDoStr+'_'+self.ParentDeriveTeamerVariable.TeamTagStr,
						_InTeamKeyStr=NetworkInTeamKeyStr
					)

		#debug
		'''
		self.debug(
			[
				'In the end',
				('self.',self,[
							'NetworkingTeamVariable',
							'NetworkingManagementVariable'
						])
			]
		)
		'''

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Simplify the repr of the flatted teams
			#

			#Check
			if type(self.NetworkedTeamKeyStrsList)==list:

				#map
				map(
					lambda __NetworkedTeamKeyStr:
					self.PrintingCopyVariable.TeamDict.__setitem__(
						__NetworkedTeamKeyStr,
						"Pointer with "+str(
							len(
								self.PrintingCopyVariable.TeamDict[__NetworkedTeamKeyStr].ManagementDict
							)
						)+" managed encapsulations"
					),
					self.NetworkedTeamKeyStrsList
				)
			
			#/##################/#
			# Simplify also the repr of the networks team
			#

			#Check
			if NetworkInTeamKeyStr in self.TeamDict:

				#set
				self.PrintingCopyVariable.TeamDict[
					NetworkInTeamKeyStr
				]="Pointer with "+str(
							len(
								self.PrintingCopyVariable.TeamDict[
									NetworkInTeamKeyStr
								].ManagementDict
							)
						)+" managed encapsulations"


		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#<DefineLocals>

#set
Pointer.PointerClass.ManagingValueClass=NetworkerClass
SYS.ParenterClass.ManagingValueClass=NetworkerClass

#</DefineLocals>

#</DefinePrint>
NetworkerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NetworkTagStr',
		'NetworkDeriveNetworkerVariable',
		'NetworkTargetStr',
		'NetworkingTeamVariable',
		'NetworkingManagementVariable',
		'NetworkingDoStr',
		'NetworkedTeamKeyStrsList'
	]
)
#<DefinePrint>
