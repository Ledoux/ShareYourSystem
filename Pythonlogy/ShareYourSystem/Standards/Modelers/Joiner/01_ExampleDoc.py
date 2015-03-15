
#ImportModules
import ShareYourSystem as SYS

#Define a Sumer class
@SYS.ClasserClass()
class SumerClass(SYS.ControllerClass):
								
	def default_init(self,
						_SumingFirstInt=0,
						_SumingSecondInt=0,
						_SumedTotalInt=0,
						**_KwargVariablesDict
					):

		#Call the parent init method
		SYS.ControllerClass.__init__(self,**_KwargVariablesDict)
						
	def do_sum(self):
		
		#debug
		'''
		self.debug(('self.',self,['SumingFirstInt','SumingSecondInt']))
		'''

		#set the SumedTotalInt
		self.SumedTotalInt=self.SumingFirstInt+self.SumingSecondInt

#Definition of a Storer instance with a noded data
MySumer=SumerClass(
	**{
			'HdformatingFileKeyStr':'Sums_1.hdf5',
			'FolderingPathStr':SYS.Joiner.LocalFolderPathStr
		}
	)['#map@set'](
		{
			'-Models':[
				('|Parameter',[
					(
						'ModelingDescriptionTuplesList',
						[
							#GetStr #ColumnStr #Col
							('SumingFirstInt','SumingFirstInt',SYS.tables.Int64Col()),
							('SumingSecondInt','SumingSecondInt',SYS.tables.Int64Col())
						]
					)
				]),
				('|Result',[
					(
						'ModelingDescriptionTuplesList',
						[
							#GetStr #ColumnStr #Col
							('SumedTotalInt','SumedTotalInt',SYS.tables.Int64Col())
						]
					),
					(
						'ParentingTriggerVariable',
						[
							'<->/^/|Parameter'
						]
					)
				])
			]
		}
	).get('?v')


#print
print('MySumer is ')
SYS._print(MySumer)