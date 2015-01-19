# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Organizer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Modelers import Modeler
from ShareYourSystem.Noders import Noder
import operator
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['organize']
})
class OrganizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'OrganizingDataCollectionStr',
								'OrganizingComponentCollectionStr',
								'OrganizingOutKeyStrsList',
								'OrganizingInKeyStrsList',
								'OrganizingOutStr',
								'OrganizingInStr',
								'OrganizedTopDeriveDatabaserVariable',
								'OrganizedInstallIsBool',
								'OrganizedDataGetStr',
								'OrganizedComponentGetStr',
								'OrganizedDataGetStr',
								'OrganizedComponentGetStr',
								'OrganizedInConnectAttentionGetStrsList',
								'OrganizedOutConnectAttentionGetStrsList'
							]

	def default_init(self,
						_OrganizingDataCollectionStr="Data",
						_OrganizingComponentCollectionStr="Component",
						_OrganizingOutKeyStrsList=None,
						_OrganizingInKeyStrsList=None,
						_OrganizingOutStr="Results",
						_OrganizingInStr="Parameters",
						_OrganizedTopDeriveDatabaserVariable=None,
						_OrganizedInstallIsBool=False,
						_OrganizedDataGetStr="",
						_OrganizedComponentGetStr="",
						_OrganizedInConnectAttentionGetStrsList=None,
						_OrganizedOutConnectAttentionGetStrsList=None,
						_OrganizedComponentCollectionOrderedDict=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_organize(self):

		#Check
		if len(self.OrganizingInKeyStrsList)==0:
			self.OrganizingInKeyStrsList=self.__class__.DoingAttributeVariablesOrderedDict.keys()
		if len(self.OrganizingOutKeyStrsList)==0:
			self.OrganizingOutKeyStrsList=self.__class__.DoneAttributeVariablesOrderedDict.keys()

		#set
		self.OrganizedDataGetStr=Noder.NodingPrefixGetStr+self.OrganizingDataCollectionStr+Noder.NodingSuffixGetStr
		self.OrganizedComponentGetStr=Noder.NodingPrefixGetStr+self.OrganizingComponentCollectionStr+Noder.NodingSuffixGetStr

		#Make the hierarchical joins for the ins 
		self.OrganizedInConnectAttentionGetStrsList=map(
				lambda __DeriveNoder:
				'/NodePointDeriveNoder/'+self.OrganizedComponentGetStr+__DeriveNoder.NodeKeyStr+'/'+self.OrganizedDataGetStr+self.OrganizingInStr+'Hierarchizer',
				self[self.OrganizedComponentGetStr]
			)

		#Set
		self.OrganizedComponentCollectionOrderedDict=getattr(
			self,
			self.OrganizingComponentCollectionStr+'CollectionOrderedDict'
		)

		#map
		self.OrganizedOutConnectAttentionGetStrsList=[
				'/NodePointDeriveNoder/'+self.OrganizedDataGetStr+self.OrganizingInStr+'Hierarchizer'
		]

		#debug
		'''
		self.debug(
					('self.',self,[
									'OrganizedInConnectAttentionGetStrsList',
									'OrganizedOutConnectAttentionGetStrsList'
								])
			)
		'''

		#import
		from ShareYourSystem.Modelers import Hierarchizer

		#Set a parameters and a results database
		self.push(
				[
					(
						self.OrganizingInStr,
						Hierarchizer.HierarchizerClass().update(
							[
								(
									'Attr_DatabasingSealTuplesList',
									map(
										Modeler.getDatabasingColumnTupleWithGetKeyStr,
										self.OrganizingInKeyStrsList
									)
								),
								(
									'Attr_RowingGetStrsList',
									self.__class__.DoingAttributeVariablesOrderedDict.keys()
								),
								(
									'ConnectingGraspClueVariablesList',
									self.OrganizedInConnectAttentionGetStrsList
								)
							]
						)
					),
					(
						self.OrganizingOutStr,
						Hierarchizer.HierarchizerClass().update(
							[
								(
									'Attr_DatabasingSealTuplesList',
									map(
										Modeler.getDatabasingColumnTupleWithGetKeyStr,
										self.OrganizingOutKeyStrsList
									)
								),
								(
									'ConnectingGraspClueVariablesList',
									self.OrganizedOutConnectAttentionGetStrsList
								),
								('TagStr','Networked')
							]
						)
					)
				],
			**{'CollectingCollectionStr':self.OrganizingDataCollectionStr}
		)

		#set
		self.OrganizedTopDeriveDatabaserVariable=getattr(
				self,
				self.OrganizingDataCollectionStr+'CollectionOrderedDict'
			).values()[-1]
#</DefineClass>

