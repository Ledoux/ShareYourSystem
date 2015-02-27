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
class InserterClass(
					BaseClass,
				):
	
	def init(self,**_KwargVariablesDict):

		#<DefineSpecificDo>
		self.InsertedIsBoolsList=[] 			#<NotRepresented>
		self.InsertedErrorBool=False 		#<NotRepresented>
		#</DefineSpecificDo> 

	def insert(self,**_KwargVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""

		#debug
		self.debug('Start of the method')

		#debug
		self.debug(
					('self.',self,['ModelingModelStr','RowedIdentifiedOrderedDict'])
				)

		#<NotHook>
		#row first
		self.row()
		#</NotHook>

		#Unzip
		InsertedIdentifiedColumningStrsList=self.RowedIdentifiedOrderedDict.keys()
		InsertedIdentifiedVariablesList=self.RowedIdentifiedOrderedDict.values()
		
		#Check if it was already rowed
		self.InsertedIsBoolsList=map(
				lambda __Row:
				all(
					map(
							lambda __InsertedIdentifiedColumningStr,__InsertedIdentifiedVariable:
							SYS.getIsEqualBool(
												__Row[__InsertedIdentifiedColumningStr],
												__InsertedIdentifiedVariable
											),
							InsertedIdentifiedColumningStrsList,
							InsertedIdentifiedVariablesList
						)
					),
				self.TabledTable.iterrows()
			) if len(InsertedIdentifiedColumningStrsList)>0 else [False]

		#debug
		self.debug(
					("",vars(),[
								'InsertedIdentifiedColumningStrsList',
								'InsertedIdentifiedVariablesList'
							]
					)
				)

		#Append and Insert if it is new
		if any(self.InsertedIsBoolsList)==False:

			#Get the row
			Row=self.TabledTable.row

			#set the InsertedRowInt
			InsertedRowInt=self.TabledTable.nrows
			
			#Definition the InsertingTuplesList
			InsertingTuplesList=[
									('RowInt',InsertedRowInt)
								]+self.RowedIdentifiedOrderedDict.items(
									)+self.RowedNotIdentifiedOrderedDict.items()
				
			#debug
			self.debug(
						[
							'This is a new row',
							'Colnames are : '+str(self.TabledTable.colnames),
							'InsertingTuplesList is '+str(InsertingTuplesList)
						]
					)

			#set the InsertingTuples in the Row
			try:

				#set
				map(
						lambda __InsertingTuple:
						Row.__setitem__(*__InsertingTuple),
						InsertingTuplesList
					)

				#debug
				self.debug('The Row setting was good, so append insert')

				#Append and Insert
				Row.append()
				self.TabledTable.insert()

			except ValueError:
				
				#debug
				self.debug('ValueError, there should be a shape not corresponding to the one defined in the table')

				#set
				self.InsertedErrorBool=True

		else:

			#debug
			self.debug(
						[
							'This is maybe not an IdentifyingInserter',
							'Or it is already rowed',
							'self.InsertedIsBoolsList is '+str(self.InsertedIsBoolsList)
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

def attest_insert():
	MyDatabaser=Databaser.DatabaserClass(
		).update(								
					[
						('MyInt',0),
						('MyStr',"hello"),
						('MyIntsList',[2,4,1]),
						(
							'<Database>MyInserter',
							InserterClass().update(
								[
									('ModelingDescriptionTuplesList',
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
			[('insert',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyInserter']}		
		).update(
					[
						('MyInt',1),
						('MyStr',"bonjour"),
						('MyIntsList',[2,4,6])
					]
		).command(
			[('insert',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyInserter']}		
		).update(
					[
						('MyInt',0),
						('MyStr',"hello"),
						('MyIntsList',[0,0,0])
					]
		).command(
			[('insert',{'LiargVariablesList':[]})],
			**{'GatherVariablesList':['<Database>MyInserter']}		
		).hdfclose(
		)
																
	#Return
	return Attester.getAttestedStrWithStrsList(
			[
				MyDatabaser,
				MyDatabaser['<Database>MyInserter'].hdfview().HdformatedConsoleStr
			]
		)
#</DefineAttestingFunctions>
