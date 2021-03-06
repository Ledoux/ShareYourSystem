
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
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
BaseModuleStr="ShareYourSystem.Standards.Walkers.Recruiter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Deriver
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineFunctions>
def getMobilizedIsBoolWithParentClassAndDeriveClassesList(
	_ParentClass,_DeriveClassesList):

	#Debug
	'''
	print('Mobilizer l.37')
	print('_ParentClass is ',_ParentClass)
	print('_DeriveClassesList is ',_DeriveClassesList)
	print('')
	'''

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
				_MobilizingCollectionSuffixStr="Figurome",
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
		self.RecruitingConcludeConditionVariable.append(
				(
					'__class__',
					getMobilizedIsBoolWithParentClassAndDeriveClassesList,
					self.MobilizedAttestClassesList
				)
			)

		#debug
		'''
		self.debug(('self.',self,['RecruitingConcludeConditionVariable']))
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

```

<small>
View the Mobilizer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Walkers/Mobilizer" target="_blank">Github</a>
</small>

