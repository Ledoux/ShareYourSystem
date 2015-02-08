
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


Featurer instances helps for defining Databaser where all 
the rowed variables are identifying items. 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Hierarchizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Modelers import Rower
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class FeaturerClass(
					BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
									'FeaturingAllBool',
									'FeaturedJoinDatabasersList'
								]

	def default_init(self,
						_FeaturingAllBool=False,
						_FeaturingJoinFlushBool=True,	
						_FeaturedJoinDatabasersList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_model(self):

		#<NotHook>
		#feature first
		self.feature()
		#</NotHook>

		#<NotHook>
		#model then
		BaseClass.model(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>


	def mimic_row(self):

		#debug
		'''
		self.debug(('self.',self,self.__class__.DoingAttributeVariablesOrderedDict.keys()))
		'''

		#Put all the GettingStrsList in the identifying container
		if self.FeaturingAllBool:

			#debug
			'''
			self.debug('Set the RowingGetStrsList with all the DatabasingGetStrs')
			'''
			
			#set 
			self['Attr_RowingGetStrsList']=SYS.unzip(
													self.DatabasingSealTuplesList,
													[0]
												)

			#debug
			'''
			self.debug(('self.',self,['RowingGetStrsList','DatabasingSealTuplesList']))
			'''
			
		#<NotHook>
		#row then
		BaseClass.row(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	def mimic_insert(self):

		#<NotHook>
		#feature first
		self.feature()
		#</NotHook>

		#debug
		'''
		self.debug(('self.',self,['FeaturingJoinFlushBool']))
		'''

		#Check
		if len(self.FeaturedJoinDatabasersList)>0 and self.FeaturingJoinFlushBool:

			#debug
			'''
			self.debug('insert in the joined featured databasers')
			'''

			#set
			self.FeaturingJoinFlushBool=False

			#map
			map(
					lambda __FeaturedDatabaser:
					__FeaturedDatabaser.insert(),
					self.FeaturedJoinDatabasersList
				)

			#set
			self.FeaturingJoinFlushBool=True

			#Return
			return

		else:

			#debug
			self.debug('insert now here')

			#insert directly
			BaseClass.insert(self)

	def do_feature(self):

		#Check
		if self.NodePointDeriveNoder!=None:

			#map
			self.FeaturedJoinDatabasersList=SYS.filterNone(
				map(
					lambda __NodedDatabaser:
					__NodedDatabaser if hasattr(
						__NodedDatabaser,'JoiningDownGetKeyStrsList')
					and __NodedDatabaser.JoiningDownGetKeyStrsList !=None and 
					self.NodedDatabaseKeyStr in __NodedDatabaser.JoiningDownGetKeyStrsList
					else None,
					self.DatabasedDeriveDatabasersOrderedDict.values()
				)
			)
		
		#debug
		'''
		self.debug(('self.',self,['FeaturedJoinDatabasersList']))
		'''

#</DefineClass>

```

<small>
View the Featurer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Databasers/Featurer" target="_blank">Github</a>
</small>

