# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Tabularer helps to define names for setting Tables in a hdf5 structure,
given the names of predefined models.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Modeler"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import importlib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['tabular']})
class TabularerClass(
					BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
									'TabularedGroup', 	
									'TabularedFilePointedVariable',									
									'TabularedSuffixStr',																
									'TabularedKeyStrsList', 													
									'TabularedOrderedDict'
								]

	def default_init(self,
					_TabularedGroup=None,
					_TabularedFilePointedVariable=None,
					_TabularedSuffixStr="",
					_TabularedKeyStrsList=None,
					_TabularedOrderedDict=None,
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)


	def do_tabular(self):
		""" """

		#debug
		'''
		self.debug(
				[
					('self.',self,[
							'ModelingSealTuplesList',
							'ModeledClass',
							'WatchModelWithModelerBool',
							'WatchModelWithJoinerBool'
						]),
					'self.model is '+SYS._str(self.model)
				]
			)
		'''
		
		#<NotHook>
		#model first
		self.model()
		#</NotHook>

		#debug
		'''
		self.debug(
					[
						('self.',self,['ModelingSealTuplesList','ModeledClass']),
						('self.DatabasedPointDeriveStorer!=None is '+str(self.DatabasedPointDeriveStorer!=None))
					]
				)
		'''
		
		#Maybe we have to hdformat first
		if self.DatabasedPointDeriveStorerVariable!=None:

			#Check
			if self.DatabasedPointDeriveStorerVariable.HdformatedFileVariable==None:

				#debug
				'''
				self.debug('We have to hdformat first...')
				'''

				#Hdformat
				self.DatabasedPointDeriveStorerVariable.hdformat()
				#self.DatabasedPointDeriveStorerVariable.structure()
			
			#Link
			self.TabularedFilePointedVariable=self.DatabasedPointDeriveStorerVariable.HdformatedFileVariable
			self.GroupedPathStr=self.DatabasedPointDeriveStorerVariable.GroupedPathStr

			#debug
			'''
			self.debug(('self.',self,[
										'HdformatedFileVariable',
										'ModelingSealTuplesList',
										'ModeledClass'
									]))
			'''
			
			#Check
			if self.TabularedFilePointedVariable!=None:

				#debug
				'''
				self.debug(
							[	
								'Looking for names of tables here',
								('self.',self,['GroupedPathStr'])
							]
						)
				'''

				#Definition Tabulared attributes
				self.TabularedGroup=self.TabularedFilePointedVariable.getNode(
					self.GroupedPathStr)

				#debug
				'''
				self.debug(('self.',self,['DatabasedSuffixStr']))
				'''
				
				#set
				self.TabularedSuffixStr='Model'.join(self.DatabasedSuffixStr.split('Model')[:-1])+'Table'

				#debug
				'''
				self.debug(
							[
								('looking for tables with the same suffix Str as : '),
								('self.',self,['TabularedSuffixStr'])
							]
						)
				'''

				#Get and sort
				self.TabularedKeyStrsList=sorted(
					filter(
							lambda __KeyStr:
							__KeyStr.endswith(self.TabularedSuffixStr),
							self.TabularedGroup._v_leaves.keys()
						)
				)
				
				self.TabularedOrderedDict.update(
					map(
							lambda __TabularedKeyStr:
							(
								__TabularedKeyStr,
								self.TabularedGroup._f_getChild(__TabularedKeyStr)
							),
							self.TabularedKeyStrsList
						)
				)

				#debug
				'''
				self.debug(("self.",self,[
											'TabularedSuffixStr',
											'TabularedKeyStrsList'
											]))
				'''

		#<NotHook>
		#Return 
		#return self
		#</NotHook>
		
#</DefineClass>
