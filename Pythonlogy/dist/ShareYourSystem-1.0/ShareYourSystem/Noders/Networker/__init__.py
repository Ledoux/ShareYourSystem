# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Networker recruits a bunch of concluded noded variables and makes them
parent and connect. Note also that each networked derive Noders has some
tag attributes such the NetworkKeyStr wich by default is the parented path str 
plus the NodeKeyStr.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Connecter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':["network"]})
class NetworkerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'NetworkingSuffixStr',
								'NetworkingCatchStr',
								'NetworkingAttentionStr',
								'NetworkedDeriveConnectersList',
								'NetworkedDerivePointersList',
							]

	def default_init(self,
						_NetworkingSuffixStr="Connecters",
						_NetworkingCatchStr="Post",
						_NetworkingAttentionStr="Pre",
						_NetworkedDeriveConnectersList=None,
						_NetworkedDerivePointersList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#map
		map(
				lambda __KeyStr:
				self.__setattr__(
						__KeyStr,
						""
					),
				map(
						lambda __TagStr:
						'Newtork'+__TagStr+'Str',
						['Collection','Catch','Attention']
					)
			)

	def do_network(self):	
		
		#recruit first
		if self.VisitingCollectionStrsList==None:
			self.VisitingCollectionStrsList=[self.CollectingCollectionStr]

		#debug
		'''
		self.debug(('self.',self,['VisitingCollectionStrsList']))
		'''

		#recruit
		self.recruit()
		self.NetworkedDeriveConnectersList=self.RecruitedFlatCumulateVariablesList

		#debug
		'''
		self.debug(('self.',self,['NetworkedDeriveConnectersList']))
		'''

		#map a connect
		self.NetworkedDerivePointersList=SYS.flat(
			map(
				lambda __NetworkedDeriveConnecter,__IndexInt:
				__NetworkedDeriveConnecter.parent(
					).connect(
						_ConnectingCatchCollectionStr=self.NetworkingCatchStr+self.NetworkingSuffixStr,
						_ConnectingAttentionCollectionStr=self.NetworkingAttentionStr+self.NetworkingSuffixStr
					).update(
						[
							('NetworkCollectionStr',self.NetworkingSuffixStr),
							('NetworkCatchStr',self.NetworkingCatchStr),
							('NetworkAttentionStr',self.NetworkingAttentionStr),
							('NetworkIndexInt',__IndexInt),
							(
								'NetworkKeyStr',
								__NetworkedDeriveConnecter.ParentedPathStr+'/'+__NetworkedDeriveConnecter.NodeKeyStr
							),
							('point',{
									'LiargVariablesList':
									[
										self,
										'NetworkPointDeriveNetworker'
									]
								}
							)
						]
					).ConnectedCatchDerivePointersList,
				self.NetworkedDeriveConnectersList,
				xrange(len(self.NetworkedDeriveConnectersList))
			)
		)	
#</DefineClass>
