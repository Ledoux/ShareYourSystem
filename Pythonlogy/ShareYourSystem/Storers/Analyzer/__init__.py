# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Analyzer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Storers.Saver"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import tables

from ShareYourSystem.Classors import Doer
#from ShareYourSystem.Databasers import Modeler,Joiner,Hierarchizer
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
							'Int',
							'Float',
							'Str'
	]
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class AnalyzerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'AnalyzingNodeSuffixStr',
									'AnalyzingParametersKeyStrsList',
									'AnalyzingResultsKeyStrsList',
									'AnalyzingFlushBool',
									'AnalyzedDoStr'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_AnalyzingNodeSuffixStr="",
						_AnalyzingParametersKeyStrsList=None,
						_AnalyzingResultsKeyStrsList=None,
						_AnalyzingFlushBool=False,
						_AnalyzedDoStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
		'''
		#set
		self.AnalyzingResultsKeyStrsList=self.__class__.DoneAttributeVariablesOrderedDict.keys()
		self.collect(
				"Data"+self.AnalyzingNodeSuffixStr,
				"Results",
				Joiner.JoinerClass().update(
					[
						(
							'Attr_ModelingSealTuplesList',
							map(
								Modeler.getModelingColumnTupleWithGetKeyStr,
								self.AnalyzingResultsKeyStrsList
							)
						),
						('Attr_RowingGetStrsList',self.AnalyzingResultsKeyStrsList),
						(
							'JoiningDownTuplesList',
							[
								(
									self.__class__.NameStr,
									'/NodePointDeriveNoder/<Data>ParametersHierarchizer'
								)
							]
						)
					]
				)
			)

		self.AnalyzingParametersKeyStrsList=self.__class__.DoingAttributeVariablesOrderedDict.keys()
		self.collect(
				"Data"+self.AnalyzingNodeSuffixStr,
				"Parameters",
				Hierarchizer.HierarchizerClass().update(
					[
						(
							'Attr_ModelingSealTuplesList',
							map(
								Modeler.getModelingColumnTupleWithGetKeyStr,
								self.AnalyzingParametersKeyStrsList
							)
						),
						('Attr_RowingGetStrsList',self.AnalyzingParametersKeyStrsList),
						(
							'JoiningDownTuplesList',
							map(
									lambda __NodedComponentKeyStr:
									(
										__NodedComponentKeyStr,
										'/NodePointDeriveNoder/<Component>'+__NodedComponentKeyStr+'/<Data>ParametersHierarchizer'
									),
									self.NodedComponentOrderedDict.keys()
								) if hasattr(self,'NodedComponentOrderedDict') else []
						)
					]
				)
			)

		#join
		map(
				lambda __NodedDataKeyStr:
				self.NodedDataOrderedDict[__NodedDataKeyStr].join(),
				[
					'ParametersHierarchizer',
					'ResultsJoiner'
				]
			)
		'''

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Joiner.JoinerClass.model}]})
	def do_analyze(self):
		
		from ShareYourSystem.Databasers import Modeler,Joiner,Hierarchizer

		#set done variables and flush in the parameters (that will also make flush in the results because of the join)
		self.setDoneVariables()[
			'<Data>ParametersHierarchizer'
		].flush()

		#Return self
		#return self
#</DefineClass>

