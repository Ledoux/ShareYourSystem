#<ImportSpecificModules>
import collections
import copy
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
class RecovererClass(
						SYS.FindoerClass
				):
	
	#<DefineHookMethods>
	def recoverBefore(self,**_RecoveringVariablesDict):

		#debug
		self.debug('Start of the method')

		#If it was not yet setted
		if self.RecoveredDict=={}:

			#debug
			print('self.RetrievedFilteredRowedDictsList is ')
			SYS._print(self.FoundFilteredRowedDictsList)
			print('')

			if len(self.FoundFilteredRowedDictsList)==1:
				
				#debug
				print('It is good, there is one solution !')
				print('')

				#set the RecoveredDict
				self.RecoveredDict=self.FoundFilteredRowedDictsList[0]

			else:

				#debug
				print('Recoverer There are not multiple retrieved states')
				print('self.FoundFilteredRowedDictsList is ',self.FoundFilteredRowedDictsList)
				print('')

		#Update
		self.update(self.RecoveredDict.items())

	#</DefineHookMethods>

	#<DefineMethods>
	def recover(self,_ModelStr,**_RecoveringVariablesDict):
		"""Call the retrieve<HookStr> methods and return self by default"""

		#debug
		'''
		print('Recoverer recover method')
		print('')
		'''

		#Maybe refresh some modeled attributes
		if _ModelStr!="":
			self.find(_ModelStr)
		else:
			_ModelStr=self.DatabasedDatabasingStr
			
		#Refresh the attributes 
		LocalRecoveringVariablesDict=dict(
			{'RecoveringStr':_ModelStr},**_RecoveringVariablesDict
		)
		LocalOutputedPointer=self
		self.IsRecoveringBool=True
		self.RecoveredDict={}

		#Hook methods
		for OrderStr in ["Before","After"]:
		
			#Definition the HookMethodStr
			HookingMethodStr='recover'+OrderStr

			#Check that there is HookingMethods for it
			if HookingMethodStr in self.__class__.HookingMethodStrToMethodsListDict:

				#Call the specific Appended methods 
				for HookingMethod in self.__class__.HookingMethodStrToMethodsListDict[HookingMethodStr]:

					#Call the HookMethod
					OutputVariable=HookingMethod(self,**LocalRecoveringVariablesDict)

					if type(OutputVariable)==dict:
						if 'LocalRecoveringVariablesDict' in OutputVariable:
							LocalRecoveringVariablesDict=OutputVariable['LocalRecoveringVariablesDict']
						if 'LocalOutputedPointer' in OutputVariable:
							LocalOutputedPointer=OutputVariable['LocalOutputedPointer']

					#Check Bool
					if self.IsRecoveringBool==False:
						return LocalOutputedPointer

		#Return the LocalOutputedPointer
		return LocalOutputedPointer


#</DefineClass>

#<DefineAttestingFunctions>
def attest_recover():

	#Bound an output method
	def outputAfter(_Recoverer):
		_Recoverer.MulInt=_Retriever.FirstInt*_Retriever.SecondInt
	SYS.RecovererClass.HookingMethodStrToMethodsListDict['outputAfter']=[outputAfter]

	#Retrieve
	Recoverer=SYS.RecovererClass(
		).update(
					[
						('FirstInt',0),
						('SecondInt',0),
						('App_Model_ParameterizingDict',{
											'ColumningTuplesList':
											[
												#ColumnStr 	#Col 	
												('FirstInt',	tables.Int64Col()),
												('SecondInt',	tables.Int64Col())
											],
											'IsFeaturingBool':True,
										}),
						('App_Model_ResultingDict',{
											'ColumningTuplesList':
											[
												#ColumnStr 	#Col 	
												('MulInt',	tables.Int64Col())
											],
											'JoiningTuple':("","Parameter")
										})
					]
		).update(
					[
						('FirstInt',1),
						('SecondInt',2)
					]
		).insert('Result'
		).update(
					[
						('FirstInt',1),
						('SecondInt',3)
					]
		).insert(
		).update(
					[
						('FirstInt',2),
						('SecondInt',2)
					]
		).insert(
		).update(
					[
						('FirstInt',2),
						('SecondInt',3)
					]
		).insert(
		).update(
					[
						('FirstInt',3),
						('SecondInt',3)
					]
		).insert(
		).recover(
					'Result'	
		).hdfclose()

	#Return the object and the h5py
	return "\n\n\n\n"+SYS.represent(
			Retriever
		)+'\n\n\n'+SYS.represent(
				os.popen('h5ls -dlr '+Retriever.HdformatingPathStr).read()
			)
#</DefineAttestingFunctions>
