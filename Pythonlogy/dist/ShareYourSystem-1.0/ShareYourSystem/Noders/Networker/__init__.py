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
									'NetworkedDeriveConnectersList',
									'NetworkedGraphTuplesList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_NetworkingSuffixStr="Connectome",
						_NetworkingCatchStr="Post",
						_NetworkingAttentionStr="Pre",
						_NetworkedDeriveConnectersList=None,
						_NetworkedGraphTuplesList=None,
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
		self.NetworkedGraphTuplesList=map(
				lambda __NodedDeriveConnecter:
				(
					__NodedDeriveConnecter,
					__NodedDeriveConnecter.connect(
						**{
							'CatchingCollectionStr':self.NetworkingCatchStr+self.NetworkingSuffixStr,
							'AttentioningCollectionStr':self.NetworkingAttentionStr+self.NetworkingSuffixStr
						}
					).update(
						[
							('NetworkCollectionStr',self.NetworkingSuffixStr),
							('NetworkCatchStr',self.NetworkingCatchStr),
							('NetworkAttentionStr',self.NetworkingAttentionStr)
						]
					).ConnectedDerivePointersList
				),
				self.NetworkedDeriveConnectersList
		)
#</DefineClass>
