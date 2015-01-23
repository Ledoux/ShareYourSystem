# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Mobilizer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Recruiter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Classors import Deriver
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineFunctions>
def getMobilizedIsBoolWithParentClassAndDeriveClassesList(
	_ParentClass,_DeriveClassesList):

	#Debug
	print('Mobilizer l.37')
	print('_ParentClass is ',_ParentClass)
	print('_DeriveClassesList is ',_DeriveClassesList)
	print('')

	#Return
	return any(
				map(
					lambda __DeriveClass:
					Deriver.getIsDerivedBoolWithParentClassAndDeriveClass(
						_ParentClass,
						__DeriveClass
					),
					_DeriveClassesList
				)
			)


#<DefineFunctions>

#<DefineClass>
@DecorationClass()
class MobilizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'MobilizingNameStrsList'
								]

	def default_init(self,
				_MobilizingNameStrsList=None,
				_MobilizingCollectionSuffixStr="",
				_MobilizedAttestClassesList=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_mobilize(self):
		
		#Check
		if self.VisitingCollectionStrsList==None:
			self.VisitingCollectionStrsList=[
				self.CollectingCollectionStr
			]
			
		#map
		self.MobilizedAttestClassesList=map(
			SYS.getClassWithNameStr,
			self.MobilizingNameStrsList
		)

		#debug
		'''
		self.debug(('self.',self,['MobilizedAttestClassesList']))
		'''
		
		#append
		self.RecruitingConcludeConditionTuplesList.append(
				(
					'SelfClass',
					getMobilizedIsBoolWithParentClassAndDeriveClassesList,
					self.MobilizedAttestClassesList
				)
			)

		#debug
		'''
		self.debug(('self.',self,['RecruitingConcludeConditionTuplesList']))
		'''

		#recruit
		self.recruit()

		#debug
		'''
		self.debug(('self.',self,['RecruitedFlatCumulateVariablesList']))
		'''

		#Split the different names into different collections
		map(
				lambda __RecruitedFlatCollectVariable:
				self.grasp(
						__RecruitedFlatCollectVariable
					).catch(
						__RecruitedFlatCollectVariable.__class__.NameStr+self.MobilizingCollectionSuffixStr,
					),
				self.RecruitedFlatCumulateVariablesList
			)
#</DefineClass>
