# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Storer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Controllers.Organizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Modelers import Hierarchizer
from ShareYourSystem.Noders import Noder
import operator
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class StorerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'StoringOrganizeIsBool'
							]

	def default_init(self,
						_StoringOrganizeIsBool=False,
						_StoringFlushIsBool=True,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_store(self):

		#Check
		if self.StoringOrganizeIsBool==False:

			#organize
			self.organize()

			#Walk
			self.walk(
				{
					'AfterUpdateList':[
						('organize',{'LiargVariablesList':[]})
					],
					'GatherVariablesList':[self.OrganizedComponentGetStr]
				}
			)

			#structure
			self.structure(
					[self.OrganizingComponentCollectionStr]
				)

			#network
			self.network(
					**{
						'VisitingCollectionStrsList':[
							self.OrganizingDataCollectionStr,
							self.OrganizingComponentCollectionStr
						],
						'RecruitingConcludeConditionTuplesList':[
							(
								'__class__.__mro__',
								operator.contains,Hierarchizer.HierarchizerClass
							)
						]
					}
				)

			#set
			self.StoringOrganizeIsBool=True

		#Check
		if self.StoringFlushIsBool:

			#Walk
			self.walk(
				{
					'AfterUpdateList':[
						('callDo',{'LiargVariablesList':[]})
					],
					'GatherVariablesList':[self.OrganizedComponentGetStr]
				}
			)

			#debug
			'''
			self.debug(('self.',self,['OrganizedTopDeriveDatabaserVariable']))
			'''

			#flush
			self.OrganizedTopDeriveDatabaserVariable.flush()	
		
#</DefineClass>

