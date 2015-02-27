# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Recruiter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Walkers.Visiter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RecruiterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'RecruitingConcludeConditionVariable',
								'RecruitedFlatCumulateVariablesList'
							]

	def default_init(self,
				_RecruitingConcludeConditionVariable=None,
				_RecruitedFlatCumulateVariablesList=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_recruit(self):
		
		#Check
		if type(self.VisitingBeforeUpdateList)!=list:
			self.VisitingBeforeUpdateList=[]

		#add
		self.VisitingBeforeUpdateList+=[
			(
				'PickingKeyVariablesList',['/']
			),
			(
				'ConcludingConditionVariable',
				self.RecruitingConcludeConditionVariable
			),
			(
				'cumulate',
				SYS.ApplyDictClass()
			)
		]

		#visit
		self.visit()

		#debug
		'''
		self.debug(('self.',self,['CumulatedVariablesList']))
		'''
		
		#flat
		self.RecruitedFlatCumulateVariablesList=SYS.filterNone(
			SYS.flat(
				self.CumulatedVariablesList
			)
		)
#</DefineClass>
