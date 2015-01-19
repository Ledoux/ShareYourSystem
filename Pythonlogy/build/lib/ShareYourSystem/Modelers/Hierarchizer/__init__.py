# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Hierarchizer is a Joiner that taking care of the 
order of the joining connections between derived Joiners,
whatever is the level of their setting in the hierarchy of 
their parent derived Storers.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Joiner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import tables
from ShareYourSystem.Noders import Noder
Joiner=BaseModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':[
		'model',
		'tabular',
		'join',
		'flush'
	]
})
class HierarchizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
							]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_flush(self):

		#debug
		'''
		self.debug(	
					[
						'we setSwitch first and flush',
						('self.',self,[
										'JoiningAttentionStr',
										'JoiningCollectionStr'
									])
					]
				)
		'''
		
		#<NotHook>
		#flush then
		BaseClass.flush(self)
		#</NotHook>

		#debug
		'''
		self.debug('we hierarchize now, self.hierarchize is '+str(self.hierarchize))
		'''

		#call
		self.hierarchize()

		#switch first
		self.transmit(
			[
				('setSwitch',{
								'LiargVariablesList':[],
								'KwargVariablesDict':
								{
									'_ClassVariable':'Hierarchizer',
									'_DoStrsList':['Flush']
								}
							})
			],
			[self.JoiningAttentionStr+self.JoiningCollectionStr],
			#Self is not switched (if not it is circular !)
			#False
		)

	def do_hierarchize(self):

		#debug
		'''
		self.debug(
					[
						'flush then in the joined attention databasers',
						('self.',self,['JoinedAttentionCollectionOrderedDict'])
					]
				)
		'''

		#map
		map(
				lambda __JoinedAttentionCollectionDeriveJoinerPointer:
				__JoinedAttentionCollectionDeriveJoinerPointer.PointVariable.flush(),
				self.JoinedAttentionCollectionOrderedDict.values()
			)
		

#</DefineClass>

