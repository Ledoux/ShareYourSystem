#<ImportSpecificModules>
import collections
import tables
import os
import ShareYourSystem as SYS
import sys
#</ImportSpecificModules>

#<DefineLocals>
JoiningStr='_'
#</DefineLocals>

#<DefineClass>
class JoinerClass(SYS.TablerClass):
	
	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>
		self.JoinedVariablesList=[]
		#</DefineSpecificDo>

	def tabularAfter(self,**_TabularingVariablesDict):

		#Maybe it is joined
		if 'JoinedOrderedDict' in self.ModeledDict:
			
			self.join(self.ModeledDict['JoiningStr'])

			'''
			self.TabularedRowedTuplesList+=zip( 
												map(
														lambda __JoiningChildObjects:
														'ModeledJoinList'+getattr(
																__JoiningChildObjects,
																DoneJoiningKeyStrKeyStr
															),
														self.ModeledDict['JoinedOrderedDict'].values()
													),
												self.JoinedModeledFeaturedIntsTuplesList
											)+[('ModeledJoinList',self.ModeledJoinList)]
			'''
			
			pass
	#</DefineHookMethods>

	def join(self,_JoiningStr,_GatheringVariablesList,**_LocalJoiningVariablesDict):

		#debug
		print('join method')
		print('_JoiningStr is ',_JoiningStr)

		if _LocalJoiningVariablesDict=={}:
			_LocalJoiningVariablesDict['IsJoiningBool']=False

		#Nodify
		self.nodify(_JoiningStr)
				
		#debug
		print('join',self.NodifiedKeyStr)
		print('For the deeper child by the way it is already joined')
		print('self.JoinedVariablesList',self.JoinedVariablesList)
		print('')
		
		if len(self.NodifiedOrderedDict)==0 or _LocalJoiningVariablesDict['IsJoiningBool']:

			'''
			print('join',self.NodifiedKeyStr)
			print('We have the right to join !')
			print('len(JoiningOrderedDict)',len(JoiningOrderedDict))
			print("_LocalJoiningVariablesDict['IsJoiningBool']",
				_LocalJoiningVariablesDict['IsJoiningBool'])
			print('')
			'''

			ParentPointer=getattr(self,self.NodifiedStr+'ParentPointer')
			if ParentPointer!=None:

				'''
				print('join',self.NodifiedKeyStr)
				print('ParentPointer exists')
				print('')
				'''

				Int=getattr(self,self.NodifiedStr+"Int")
				if Int==0:

					'''
					print('join',self.NodifiedKeyStr)
					print('This is the first child so init 
						the ParentPointer.JoinedVariablesList')
					print('')
					'''

					ParentPointer.JoinedVariablesList=[""]*len(
						getattr(ParentPointer,self.NodifiedStr+"OrderedDict"))	

				
				'''
				#Get the GatheredVariablesList
				GatheredVariablesList=self.gather(_GatheringVariablesList)

				print('join',self.NodifiedKeyStr)
				print('append in the ParentPointer.JoinedVariablesList[Int]')
				print('Int is ',str(Int))
				print('GatheredVariablesList is ',GatheredVariablesList)
				
				#set in the parent pointer
				ParentPointer.JoinedVariablesList[Int]=JoiningStr.join(
					map(
							lambda __JoiningTuple:
							'('+str(__JoiningTuple[0])+','+str(__JoiningTuple[1])+')',
							GatheredVariablesList
						)
				)
				'''

				

			else:

				print('join',self.NodifiedKeyStr)
				print('ParentPointer is None')	
				
		else:

			print('join',self.NodifiedKeyStr)
			print('This either a not last level of child or it is not yet authorized to join')
			print('len(self.NodifiedOrderedDict.values()) is ',len(self.NodifiedOrderedDict.values()))
			print("_LocalJoiningVariablesDict['IsJoiningBool']",_LocalJoiningVariablesDict['IsJoiningBool'])
			print('so join the deeper children groups first')
			print('')

			map(
					lambda __JoiningObjects:
					__JoiningObjects.join(
											_JoiningStr,
											_GatheringVariablesList,
											**_LocalJoiningVariablesDict
										),
					self.NodifiedOrderedDict.values()
				)

			'''
			print('join',self.NodifiedKeyStr)
			print('The deeper children groups are joined now')
			print('So join here !')
			print('')
			'''

			self.join(
						_JoiningStr,
						_GatheringVariablesList,
						**dict(
									_LocalJoiningVariablesDict,**{'IsJoiningBool':True}
								)
						)

		'''
		print("join END for ",self.NodifiedKeyStr)
		print('self.JoinedModeledIntsTuplesList',self.JoinedModeledIntsTuplesList)
		print('')
		'''

#</DefineClass>

#<DefineAttestingFunctions>
def attest_join():

	'''
	#Build a grouped structure
	Joiner=SYS.JoinerClass().update(
								[
									(
										'App_Structure_ChildJoiner1',
										SYS.JoinerClass().update(
										[
											(
												'App_Structure_GrandChildJoiner1',
												SYS.JoinerClass()
											)
										])
									),
									(
										'App_Structure_ChildJoiner2',
										SYS.JoinerClass().update(
											[]
										)
									)
								]	
							).walk(
										[
											'StructuredOrderedDict.items()'
										],
										**{
												'BeforeUpdateList':
												[
													('parentize',{'ArgsVariable':"Structure"}),
													('join',{'ArgsVariable':[
																				"Structure",
																				[
																					["StructuredKeyStr"]
																				]
																			]
															}
													)
												]
											}
							).hdfclose()
	'''

	#Build Hdf groups
	Tabler=SYS.TablerClass().hdformat().update(
								[
									(
										'App_Structure_ChildGrouper1',
										SYS.GrouperClass().update(
										[
											(
												'App_Structure_GrandChildTabler1',
												SYS.TablerClass()
											)
										])
									)
								]	
							).walk(
										[
											'StructuredOrderedDict.items()'
										],
										**{
												'BeforeUpdateList':
												[
													('parentize',{'ArgsVariable':"Structure"}),
													('group',{'ArgsVariable':"Structure"})
												]
											}
									).update(
								map(
										lambda __Tuple:
										(
											'/App_Structure_ChildGrouper1/App_Structure_GrandChildTabler1/'+__Tuple[0],
											__Tuple[1]
										),
										[
											('MyInt',0),
											('MyStr',"hello"),
											('UnitsInt',3),
											('MyIntsList',[2,4,1]),
											('MyFloat',0.1),
											('MyFloatsList',[2.3,4.5,1.1]),
											('App_Scan_ChildModeler',SYS.ModelerClass()),
											('App_Model_FeaturingDict',
														{
															'ColumningTuplesList':
															[
																('MyInt',tables.Int64Col()),
																('MyStr',tables.StrCol(10)),
																('MyIntsList',(tables.Int64Col,'UnitsInt'))
															]
														}
											),
											('App_Model_OutputingDict',
												{
													'ColumningTuplesList':
													[
														('MyFloat',tables.Float32Col()),
														('MyFloatsList',(tables.Float32Col,'UnitsInt'))
													]
												}
											),
											('model',{'ArgsVariable':"Feature"}),
											('tabular',{'ArgsVariable':"Feature"}),
											('flush',{}),
											('UnitsInt',2),
											('MyIntsList',[2,4]),
											('MyFloatsList',[2.3,4.5]),
											('tabular',{'ArgsVariable':"Feature"}),
											('flush',{}),
											('model',{
														'ArgsVariable':"Output",
														'KwargsDict':{'JoiningStr':"Scan"}
													}
											),
											('tabular',{
														'ArgsVariable':"Output",
													}
											),
											('flush',{})
										]
									)
							).hdfclose()
																
	#Return the object itself
	print(Joiner)
	return Joiner
#</DefineAttestingFunctions>
