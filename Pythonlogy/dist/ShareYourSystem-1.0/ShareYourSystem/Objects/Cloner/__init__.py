# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Cloner

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Caller"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy

#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Cloner","Clone","Cloning","Cloned"]
#<DefineDoStrsList>

#<DefineLocals>
CloningIdStringsList=[]
#</DefineLocals>

def getCopiedMutableVariableWithMutableVariable(_MutableVariable,**_KwargVariablesDict):

	if 'CloningIdsDict' not in _KwargVariablesDict:
		_KwargVariablesDict['CloningIdsDict']={}
	if 'CloningNotCopyKeyStringsList' not in _KwargVariablesDict:
		_KwargVariablesDict['CloningNotCopyKeyStringsList']=[]

	#get the type
	Type=type(_MutableVariable)

	#Debug
	print('_MutableVariable is ',_MutableVariable)
	print('')

	#itemized variable case
	if Type in [dict,collections.OrderedDict]:
		return Type(
					map(
						lambda __ItemTuple:
						(
							__ItemTuple[0],
							__ItemTuple[1].clone(
								_KwargVariablesDict['CloningIdsDict'],
								_KwargVariablesDict['CloningNotCopyKeyStringsList']
							)
							if hasattr(__ItemTuple[1],'clone')
							else getCopiedMutableVariableWithMutableVariable(
								__ItemTuple[1],
								**_KwargVariablesDict
							)
							if type(__ItemTuple[1]) in [list,tuple,set,dict,collections.OrderedDict]
							else __ItemTuple[1]
						),
						_MutableVariable.items()
					)
				)

	#listed variable case
	elif Type in [list,tuple,set]:

		return Type(
			map(
				lambda __ListedVariable:
				__ListedVariable.clone(
								_KwargVariablesDict['CloningIdsDict'],
								_KwargVariablesDict['CloningNotCopyKeyStringsList']
							)
				if hasattr(__ListedVariable,'clone')
				else getCopiedMutableVariableWithMutableVariable(
					__ListedVariable,
					**_KwargVariablesDict
				)
				if type(__ListedVariable) in [list,tuple,set,dict,collections.OrderedDict]
				else __ListedVariable,
				_MutableVariable
			)
		)

	#other
	else:

		return _MutableVariable
		
#<DefineClass>
@DecorationClass(**{'DoingGetBool':True})
class ClonerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'CloningIdsDict',
								'CloningNotCopyKeyStringsList',
								'CloningResetBool',
								'ClonedItemTuplesList',
								'ClonedCopyVariable'
							]


	def default_init(self,
						_CloningIdsDict=None,
						_CloningNotCopyKeyStringsList=None,
						_CloningResetBool=False,
						_ClonedItemTuplesList=None,
						_ClonedCopyVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass()
	def do_clone(self):

		#filter
		self.ClonedItemTuplesList=SYS._filter(
				lambda __ItemTuple:
				__ItemTuple[0] not in self.CloningNotCopyKeyStringsList,
				self.__dict__.items()
			)

		"""
		#global
		global CloningIdStringsList

		#check
		if self.CloningResetBool:
			CloningIdStringsList=[]
			self.CloningIdsDict={}

		#if self.IdString in CloningIdStringsList:

		#return 

		#append
		#CloningIdStringsList.append(id(self))

		
		
		#debug
		'''
		self.debug(
			('self.',self,['ClonedItemTuplesList'])
		)
		'''

		#debug
		self.ClonedValueTuplesList=[]
		for __ClonedItemTuple in self.ClonedItemTuplesList:

			print('__ClonedItemTuple[0] is ',__ClonedItemTuple[0])
			print('__ClonedItemTuple[1] is ',__ClonedItemTuple[1])
			print('')

			ClonedIdString=id(__ClonedItemTuple[1])
			if hasattr(
						__ClonedItemTuple[1],
						'clone'
					):

				print('IdString in CloningIdStringsList is ',ClonedIdString in CloningIdStringsList)
				print('')

				#Check
				if ClonedIdString in CloningIdStringsList:
	
					#
					self.ClonedValueTuplesList.append(self.CloningIdsDict[ClonedIdString])

				else:

					#append
					CloningIdStringsList.append(ClonedIdString)

					#set
					self.CloningIdsDict[ClonedIdString]=__ClonedItemTuple[1]

					#append
					self.ClonedValueTuplesList.append(
						__ClonedItemTuple[1].clone(
							self.CloningIdsDict,
							self.CloningNotCopyKeyStringsList
						)
					)

			else:

				self.ClonedValueTuplesList.append(
					getCopiedMutableVariableWithMutableVariable(__ClonedItemTuple[1],
						**{
							'CloningIdsDict':self.CloningIdsDict,
							'CloningNotCopyKeyStringsList':self.CloningNotCopyKeyStringsList
						})
				)

		'''
		#copy or clone
		self.ClonedValueTuplesList=map(
			lambda __ClonedValueTuple:
			__ClonedValueTuple.clone() if hasattr(
					__ClonedValueTuple,
					'clone'
				)
			else getCopiedMutableVariableWithMutableVariable(__ClonedValueTuple),
			SYS.unzip(self.ClonedItemTuplesList,[1])
		)
		'''
			
		#update
		self.CloningIdsDict[self.IdString]=self.ClonedCopyVariable
		

		#instance
		self.ClonedCopyVariable=self.__class__(
				**dict(	
				copy.deepcopy(
						self.ClonedItemTuplesList
						#zip(
						#	SYS.unzip(self.ClonedItemTuplesList,[0]),
						#	self.ClonedValueTuplesList
						#	)
				)
			)
		)
		"""	
		
		for __ClonedItemTuple in self.ClonedItemTuplesList:
			print(__ClonedItemTuple)
			copy.deepcopy(__ClonedItemTuple)

		#copy
		self.ClonedCopyVariable=copy.deepcopy(self)


		#return
		return self.ClonedCopyVariable

		#Return self
		#return self
	
#</DefineClass>

