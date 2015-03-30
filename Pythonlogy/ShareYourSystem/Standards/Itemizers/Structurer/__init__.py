# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Structurer 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Connecter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Structurer','Structure','Structuring','Structured')
#</DefineAugmentation>

#<ImportSpecificModules>
Connecter=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
StructureOutPrefixStr='_Struc_'
StructureInTeamKeyStr='Structures'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class StructurerClass(BaseClass):

	def default_init(
					self,
					_StructureTagStr='Top',
					_StructureTopDeriveStructurerVariable=None,
					_StructureTargetStr='Top',
					_StructureConnectPrefixStrsList=None,
					_StructuringTeamVariable=None,
					_StructuringManagementVariable=None,
					_StructuringSingPluralVariable=None,
					_StructuringDoStr="",
					_StructuringClassBool=True,
					_StructuringCircularBool=False,
					_StructuredTeamKeyStrsList=None,
					_StructuredOnceBool=False,
					**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.StructureTopDeriveStructurerVariable=self

	def do_structure(self):

		#/###################/#
		# Check the level
		#

		#debug
		self.debug(
			[
				'We structure here',
				'self.StructureTopDeriveStructurerVariable==self is ',
				str(self.StructureTopDeriveStructurerVariable==self)
			]
		)

		#Check
		if self.StructureTopDeriveStructurerVariable==self:

			#debug
			self.debug(
				[
					'Watch at the circular condition',
					('self.',self,['StructuringCircularBool'])
				]
			)

			#Check
			if self.StructuringCircularBool==False:

				#debug
				'''
				self.debug(
						[
							'We structure top here',
							('self.',self,[
									'StructuringTeamVariable',
									'StructuringManagementVariable'
								])
						]
					)
				'''
				
				#/###################/#
				# Set the structure of singular team if not already
				#

				#Check
				if self.StructuredOnceBool==False:

					#Check
					if self.StructuringSingPluralVariable!=None:

						#debug
						self.debug(
							[
								'we structure for the first time here',
								('self.',self,['StructuringSingPluralVariable'])
							]
						)
						
						#map add the sing plurals
						map(
							lambda __ItemTuple:
							SYS.addSingPlural(
								*__ItemTuple
							),
							SYS.SetList(self.StructuringSingPluralVariable)
						)

						#Define a class
						class StructureClass(StructurerClass):pass
						StructureClass.__name__=self.NameStr+'s'
						StructureClass.ManagingValueClass=self.__class__

						#set
						setattr(
							self.Module,
							StructureClass.__name__,
							StructureClass
						)

						#dict
						ClassesDict=dict(
								map(
									lambda __ItemTuple:
									(__ItemTuple[1],StructureClass),
									_SingPluralVariable
								)
							)

						#Check
						if self.StructuringClassBool:

							#map
							if _Class.TeamingClassesDict==None:
								_Class.TeamingClassesDict=ClassesDict
							else:
								_Class.TeamingClassesDict.update(
									ClassesDict
								)

							#set 
							self.__class__.StructuringOnceBool=True

						else:

							#map
							if self.TeamingClassesDict==None:
								self.TeamingClassesDict=ClassesDict
							else:
								self.TeamingClassesDict.update(
									ClassesDict
								)


						#set
						self.StructuredOnceBool=True

				#/##################/#
				# prepare the struc teams
				#

				#map
				self.StructuredTeamKeyStrsList=map(
						lambda __StructuringTeamOrManagementStr:
						StructureOutPrefixStr+self.StructuringDoStr+'_'+__StructuringTeamOrManagementStr,
						(self.StructuringTeamVariable if self.StructuringTeamVariable!=None else [])+
						(self.StructuringManagementVariable if self.StructuringManagementVariable!=None else [])
					)

				#debug
				'''
				self.debug(
						[
							'We are going to make team the StructuredTeamKeyStrsList',
							('self.',self,['StructuredTeamKeyStrsList'])
						]
					)
				'''

				#map
				map(
						lambda __StructuredTeamKeyStr:
						self.team(__StructuredTeamKeyStr),
						self.StructuredTeamKeyStrsList
					)

				#/##################/#
				# parent Down
				#

				#parentDown
				self.parentDown(
						self.StructuringTeamVariable,
						self.StructuringManagementVariable,
						'structure',
						**{
							'StructureTargetStr':self.StructureTagStr,
							'StructureTopDeriveStructurerVariable':self,
							'StructuringDoStr':self.StructuringDoStr,
							'StructuringCircularBool':True	
						}
					)
			else:

				#reset
				self.StructuringCircularBool=True


		else:

			#debug
			self.debug(
				[
					'We structure in a level here'
				]
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
							'StructuringTeamVariable',
							'StructuringManagementVariable'
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
							'StructuringTeamVariable',
							'StructuringManagementVariable'
						])
			]
		)
		'''

		#/##################/#
		# Set the StructureTagStr
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
			self.StructureTagStr=(
					self.ParentedTotalPathStr+'/'+self.ManagementTagStr
				).replace('/','_')

		#remove
		if self.StructureTagStr[0]=='_':
			self.StructureTagStr=self.StructureTagStr[1:]

		#/##################/#
		# Find the StructureTopDeriveStructurerVariable in the grand parents
		#

		#find
		'''
		self.debug(
			[
				'We have parented',
				('self.',self,[
						#'ParentedTotalDeriveTeamersList',
						'StructureTargetStr'
					]),
				'Now find the StructureTopDeriveStructurerVariable that has the StructureTagStr',
				'equal to the self.StructureTargetStr'
			]
		)
		'''

		#Check
		if len(self.ParentedTotalDeriveTeamersList)>0:

			#index
			try:

				#index
				IndexInt=map(
						lambda __ParentedDeriveTeamer:
						hasattr(
							__ParentedDeriveTeamer,
							'StructureTargetStr'
						) and __ParentedDeriveTeamer.StructureTagStr==self.StructureTargetStr,
						self.ParentedTotalDeriveTeamersList
					).index(True)

				#set
				self.StructureTopDeriveStructurerVariable=self.ParentedTotalDeriveTeamersList[IndexInt]

			except:

				IndexInt=len(self.ParentedTotalDeriveTeamersList)
			
		#debug
		'''
		self.debug(
				[
					'Finally StructureTopDeriveStructurerVariable is ',
					SYS._str(self.StructureTopDeriveStructurerVariable)
				]
			)
		'''

		#/##################/#
		# Add to the StructureTopDeriveStructurerVariable
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
							StructureOutPrefixStr+self.ParentDeriveTeamerVariable.ManagementTagStr
						),
						'self.StructureTopDeriveStructurerVariable.StructuringManagementVariable is ',
						str(self.StructureTopDeriveStructurerVariable.StructuringManagementVariable)
					]
				)
			'''

			#Check
			if self.StructureTopDeriveStructurerVariable.StructuringManagementVariable!=None:

				#Check
				if self.ParentDeriveTeamerVariable.ManagementTagStr in self.StructureTopDeriveStructurerVariable.StructuringManagementVariable:

					#debug
					self.debug(
						[
							'Yes we make team connect here',
							('self.',self,['PointingInManagementKeyStr']),
							'self.ParentDeriveTeamerVariable.ManagementTagStr is ',
							str(self.ParentDeriveTeamerVariable.ManagementTagStr),

						]
					)

					#connect
					#self.StructureTopDeriveStructurerVariable.connect(
					#		self,
					#		_OutTeamKeyStr=StructureOutPrefixStr+self.StructuringDoStr+'_'+self.ParentDeriveTeamerVariable.ManagementTagStr,
					#		_InTeamKeyStr=StructureInTeamKeyStr
					#)

					#connect out like in the StructureTopDeriveStructurerVariable
					self.StructureTopDeriveStructurerVariable.TeamDict[
						StructureOutPrefixStr+self.StructuringDoStr+'_'+self.ParentDeriveTeamerVariable.ManagementTagStr
					].manage(
						self.StructureTagStr,
						{
							'ConnectedToVariable':self
						}
					)

					#connect in like in the self
					#self.TeamDict[
					#	StructureInTeamKeyStr
					#].manage(
					#	{
					#		'ConnectedToVariable':self.StructureTopDeriveStructurerVariable
					#	}
					#)

		if self.ManagementTagStr!="":
			
			#debug
			'''
			self.debug(
					[
						'we make connect the top structureer on the team'+str(
							StructureOutPrefixStr+self.ParentDeriveTeamerVariable.TeamTagStr
						),
						('self.',self,[
								'StructureTagStr'
							])
					]
				)
			'''

			#Check
			if self.StructureTopDeriveStructurerVariable.StructuringTeamVariable!=None:

				#Check
				if self.ParentDeriveTeamerVariable.TeamTagStr in self.StructureTopDeriveStructurerVariable.StructuringTeamVariable:

					#debug
					'''
					self.debug(
						[
							'Yes we make team connect here',
							#'self.StructureTopDeriveStructurerVariable.TeamDict.keys() is',
							#str(self.StructureTopDeriveStructurerVariable.TeamDict.keys()),
							#('self.',self,['StructureTopDeriveStructurerVariable']),
							'self.StructureTopDeriveStructurerVariable.StructuredTeamKeyStrsList is',
							str(self.StructureTopDeriveStructurerVariable.StructuredTeamKeyStrsList),
							('self.',self,['StructuringDoStr'])
						]
					)
					'''
					
					#connect out like in the StructureTopDeriveStructurerVariable
					self.StructureTopDeriveStructurerVariable.TeamDict[
						StructureOutPrefixStr+self.StructureTopDeriveStructurerVariable.StructuringDoStr+'_'+self.ParentDeriveTeamerVariable.TeamTagStr
					].manage(
						self.StructureTagStr,
						{
							'ConnectedToVariable':self
						}
					)

		#debug
		'''
		self.debug(
			[
				'In the end',
				('self.',self,[
							'StructuringTeamVariable',
							'StructuringManagementVariable'
						])
			]
		)
		'''

		#/##################/#
		# Maybe do some connections
		#

		#debug
		'''
		self.debug(
			[
				'We do here maybe some connections',
				('self.',self,['StructureConnectPrefixStrsList'])
			]
		)
		'''

		#Check
		if self.StructureConnectPrefixStrsList!=None:

			#debug
			self.debug(
				[
					'We do here some connections',
					('self.',self,['StructureConnectPrefixStrsList'])
				]
			)

			#map
			map(
				lambda __StructureConnectPrefixStr:
				self.mapConnect(__StructureConnectPrefixStr),
				self.StructureConnectPrefixStrsList
			)

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
			if type(self.StructuredTeamKeyStrsList)==list:

				#map
				map(
					lambda __StructuredTeamKeyStr:
					self.PrintingCopyVariable.TeamDict.__setitem__(
						__StructuredTeamKeyStr,
						"Pointer with "+str(
							len(
								self.PrintingCopyVariable.TeamDict[
									__StructuredTeamKeyStr
								].ManagementDict
							)
						)+" managed encapsulations"
					),
					self.StructuredTeamKeyStrsList
				)
			
			#/##################/#
			# Simplify also the repr of the structures team
			#

			#Check
			if StructureInTeamKeyStr in self.TeamDict:

				#set
				self.PrintingCopyVariable.TeamDict[
					StructureInTeamKeyStr
				]="Pointer with "+str(
							len(
								self.PrintingCopyVariable.TeamDict[
									StructureInTeamKeyStr
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
Connecter.ConnecterClass.ManagingValueClass=StructurerClass
SYS.ParenterClass.ManagingValueClass=StructurerClass

#</DefineLocals>

#</DefinePrint>
StructurerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'StructureTagStr',
		'StructureTopDeriveStructurerVariable',
		'StructureTargetStr',
		'StructureConnectPrefixStrsList',
		'StructuringTeamVariable',
		'StructuringManagementVariable',
		'StructuringSingPluralVariable',
		'StructuringDoStr',
		'StructuringClassBool',
		'StructuringCircularBool',
		'StructuredTeamKeyStrsList',
		'StructuredOnceBool'
	]
)
#<DefinePrint>
