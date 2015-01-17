
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


Findoer (sorry Finder is already an important module in python standards, so just to be sure to not override...)
instances helps to find in a hdf5 table RowedVariablesList corresponding to the FindingConditionTuplesList.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Findoer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Functers import Argumenter,Hooker
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RecovererClass(
						BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
									'RecoveredDict'
								]

	def default_init(self,
						_RecoveredDict=None,
						**_KwargVariablesDict
					):
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'MethodCallingStr':"find"}]})
	#@Argumenter.ArgumenterClass()
	def do_recover(self):

		#debug
		'''
		self.debug(
					[
						'Is the self.RecoveredDict already setted ?',
						'len(self.RecoveredDict) is '+str(len(self.RecoveredDict))
					]
			)
		'''

		#<NotHook>
		#find first
		self.find()
		#</NotHook>

		#Check
		if len(self.RecoveredDict)==0:

			#debug
			'''
			self.debug(
						[
							'The RecoveredDict is not yet setted',
							'Look if we have found only one FilteredRowedDict',
							'len(self.FoundFilterRowDictsList) is '+str(len(self.FoundFilterRowDictsList))
						]
					)
			'''

			#Check
			if len(self.FoundFilterRowDictsList)==1:

				#debug
				'''
				self.debug('It is good, there is one solution !')
				'''

				#set the RecoveredDict
				self.RecoveredDict.update(self.FoundFilterRowDictsList[0])

		#debug
		'''
		self.debug(
					[
						'Now we update with the self.RecoveredDict',
						'self.RecoveredDict is '+str(self.RecoveredDict)
					]
				)
		'''

		#set the RetrievingIndexesList and retrieve
		self.RetrievingIndexesList=(
										0,
										self.RecoveredDict['ModeledInt']
									)
	
		#Now we can retrieve
		self.retrieve()

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

#</DefineClass>

```

<small>
View the Recoverer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Databasers/Recoverer" target="_blank">Github</a>
</small>

