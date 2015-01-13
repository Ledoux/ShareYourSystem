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
BaseModuleStr="ShareYourSystem.Databasers.Hierarchizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Functers import Imitater,Switcher
from ShareYourSystem.Databasers import Rower
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Featurer","Feature","Featuring","Featured"]
#<DefineDoStrsList>

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

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_FeaturingAllBool=False,
						_FeaturingJoinFlushBool=True,	
						_FeaturedJoinDatabasersList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingBeforeVariablesList':[{'CallingVariable':Rower.RowerClass.row}]})
	@Imitater.ImitaterClass()
	def model(self):

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

	#@Hooker.HookerClass(**{'HookingBeforeVariablesList':[{'CallingVariable':Rower.RowerClass.row}]})
	@Imitater.ImitaterClass()
	def row(self):

		#debug
		'''
		self.debug(('self.',self,self.__class__.DoingAttributeVariablesOrderedDict.keys()))
		'''

		#Put all the GettingStrsList in the identifying container
		if self.FeaturingAllBool:

			#debug
			'''
			self.debug('Set the RowingGetStrsList with all the ModelingGetStrs')
			'''
			
			#set 
			self['Attr_RowingGetStrsList']=SYS.unzip(
													self.ModelingSealTuplesList,
													[0]
												)

			#debug
			'''
			self.debug(('self.',self,['RowingGetStrsList','ModelingSealTuplesList']))
			'''
			
		#<NotHook>
		#row then
		BaseClass.row(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

	@Imitater.ImitaterClass()
	def flush(self):

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
			self.debug('flush in the joined featured databasers')
			'''

			#set
			self.FeaturingJoinFlushBool=False

			#map
			map(
					lambda __FeaturedDatabaser:
					__FeaturedDatabaser.flush(),
					self.FeaturedJoinDatabasersList
				)

			#set
			self.FeaturingJoinFlushBool=True

			#Return
			return

		else:

			#debug
			self.debug('flush now here')

			#flush directly
			BaseClass.flush(self)


	@Switcher.SwitcherClass()
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
