# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Storer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineDoStrsList>
DoStrsList=["Storer","Store","Storing","Stored"]
#<DefineDoStrsList>

#<ImportSpecificModules>

from ShareYourSystem.Standards.Modelers import Hierarchizer
import itertools
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StorerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
									'StoredRetrieveListsList',
									'StoredScansList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		self.AnalyzingDeriveFeaturerClass=Hierarchizer.HierarchizerClass

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Joiner.JoinerClass.model}]})
	#@Argumenter.ArgumenterClass()
	def do_store(self):

		#define
		StoredDatabaseKeyStr='Parameters'+self.AnalyzingDeriveFeaturerClass.NameStr
		StoredDatabaseGetKeyStr='<Database>'+StoredDatabaseKeyStr

		#table
		self[StoredDatabaseGetKeyStr].table()

		#scan first in the children ParametersFeaturer
		self.StoredRetrieveListsList=map(
				lambda __NodedOutputVariable:
				__NodedOutputVariable[StoredDatabaseGetKeyStr
				].scan().ScannedRetrieveListsList,
				getattr(self,'Noded'+self[StoredDatabaseGetKeyStr].HierarchizingNodeStr+'OrderedDict').values()
			)

		"""
		#Scan the values of this model
		self.StoredScansList=list(
									itertools.product(*self.StoredRetrieveListsList)
								)

		#debug
		self.debug(('self.',self,[
									'StoredRetrieveListsList',
									'StoredScansList'
								]))


		zip(self.HierarchizedKeyStrsList,self.StoredRetrieveListsList)

		#scan in the ParametersFeaturer
		self['<Database>ParametersFeaturer'].scan(_DatabaseKeyStr="ResultsHierarchizer")
		"""

		#Set the done variables and insert
		self.setDoneVariables()['<Database>ParametersHierarchizer'].scan()

		#Return self
		#return self

#</DefineClass>

