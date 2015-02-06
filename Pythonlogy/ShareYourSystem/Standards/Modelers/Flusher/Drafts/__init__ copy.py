#<ImportSpecificModules>

,Attester
from ShareYourSystem.Functers import Hooker,Triggerer
BaseModuleStr="ShareYourSystem.Standards.Objects.Rower"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer")
#</ImportSpecificModules>

#<DefineLocals>
SYS.setSubModule(globals())

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class FlusherClass(
					BaseClass,
				):
	
	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.init}]})
	def init(self,**_KwargVariablesDict):

		#<DefineSpecificDo>
		self.FlushedIsBoolsList=[] 			#<NotRepresented>
		self.FlushedErrorBool=False 		#<NotRepresented>
		#</DefineSpecificDo> 

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':"row"}]})
	def flush(self,**_KwargVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					('self.',self,['DatabasingModelStr','RowedIdentifiedOrderedDict'])
				)

		#<NotHook>
		#row first
		self.row()
		#</NotHook>

		#Unzip
		FlushedIdentifiedColumningStrsList=self.RowedIdentifiedOrderedDict.keys()
		FlushedIdentifiedVariablesList=self.RowedIdentifiedOrderedDict.values()
		
		#Check if it was already rowed
		self.FlushedIsBoolsList=map(
				lambda __Row:
				all(
					map(
							lambda __FlushedIdentifiedColumningStr,__FlushedIdentifiedVariable:
							SYS.getIsEqualBool(
												__Row[__FlushedIdentifiedColumningStr],
												__FlushedIdentifiedVariable
											),
							FlushedIdentifiedColumningStrsList,
							FlushedIdentifiedVariablesList
						)
					),
				self.TabledTable.iterrows()
			) if len(FlushedIdentifiedColumningStrsList)>0 else [False]

		#debug
		self.debug(
					("",vars(),[
								'FlushedIdentifiedColumningStrsList',
								'FlushedIdentifiedVariablesList'
							]
					)
				)

		#Append and Flush if it is new
		if any(self.FlushedIsBoolsList)==False:

			#Get the row
			Row=self.TabledTable.row

			#set the FlushedRowInt
			FlushedRowInt=self.TabledTable.nrows
			
			#Definition the FlushingTuplesList
			FlushingTuplesList=[
									('RowInt',FlushedRowInt)
								]+self.RowedIdentifiedOrderedDict.items(
									)+self.RowedNotIdentifiedOrderedDict.items()
				
			#debug
			self.debug(
						[
							'This is a new row',
							'Colnames are : '+str(self.TabledTable.colnames),
							'FlushingTuplesList is '+str(FlushingTuplesList)
						]
					)

			#set the FlushingTuples in the Row
			try:

				#set
				map(
						lambda __FlushingTuple:
						Row.__setitem__(*__FlushingTuple),
						FlushingTuplesList
					)

				#debug
				self.debug('The Row setting was good, so append flush')

				#Append and Flush
				Row.append()
				self.TabledTable.flush()

			except ValueError:
				
				#debug
				self.debug('ValueError, there should be a shape not corresponding to the one defined in the table')

				#set
				self.FlushedErrorBool=True

		else:

			#debug
			self.debug(
						[
							'This is maybe not an IdentifyingFlusher',
							'Or it is already rowed',
							'self.FlushedIsBoolsList is '+str(self.FlushedIsBoolsList)
						]
					)

		#debug
		self.debug('End of the method')

		#<NotHook>
		#Return self
		return self
		#</NotHook>

#</DefineClass>

#<DefineAttestingFunctions>
import tables
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Standards.Objects import Databaser

def attest_flush():
	MyDatabaser=Databaser.DatabaserClass(
		).update(								
					[
						('MyInt',0),
						('MyStr',"hello"),
						('MyIntsList',[2,4,1]),
						(
							'<Database>MyFlusher',
							FlusherClass().update(
								[
									('DatabasingSealTuplesList',
										[
											('MyInt',tables.Int64Col()),
											('MyStr',tables.StrCol(10)),
											('MyIntsList',(tables.Int64Col(shape=3)))
										]
									),
									('RowedIdentifiedGettingStrsList',
										['MyInt','MyStr']
									)
								]
							)
						)
					]
		).command(
			[('flush',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyFlusher']}		
		).update(
					[
						('MyInt',1),
						('MyStr',"bonjour"),
						('MyIntsList',[2,4,6])
					]
		).command(
			[('flush',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyFlusher']}		
		).update(
					[
						('MyInt',0),
						('MyStr',"hello"),
						('MyIntsList',[0,0,0])
					]
		).command(
			[('flush',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyFlusher']}		
		).hdfclose(
		)
																
	#Return
	return Attester.getAttestedStrWithStrsList(
			[
				MyDatabaser,
				MyDatabaser['<Database>MyFlusher'].hdfview().HdformatedConsoleStr
			]
		)
#</DefineAttestingFunctions>
