#<ImportSpecificModules>
import ShareYourSystem as SYS
import numpy as np
import scipy.stats
from tables import *
import time
import operator
import os
#</ImportSpecificModules>

#<DefineLocals>
HookStr="Mul"
#</DefineLocals>

#<DefineClass>
class MulClass(SYS.JoinerClass):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>
		self.FirstInt=1
		self.SecondInt=1
		self.MulInt=1
		#</DefineSpecificDo>

		#Definition the features
		self['App_Model_ParameterizingOrderedDict']={

										'ColumningTuplesList':
										[
											#ColumnStr 	#Col 	
											('FirstInt',	Int64Col())
											('SecondInt',	Int64Col())
										]
									}

		#Definition the outputs
		self.OutputingTuplesList=[
										#ColumnStr 	#GettingVariable 	#Col 
										('MulInt',		'MulInt',			Int64Col()),	
										('MulIntsList',	'MulIntsList',		Int64Col(shape=2)),
										('SeedMulInt',	'SeedMulInt',		Int64Col())	
									]

		#Definition the stores
		self.StoringTuplesList=[
									('MulIntsListArrayStr',	'MulIntsList',	StrCol(100))
								]
						
	def outputAfter(self,**_LocalOutputingVariablesDict):
		
		#set 
		self.SeedMulInt=self['App_Group_Config'].SeedInt

		#Definition the RandomFloatsList
		RandomFloatsList=scipy.stats.uniform.rvs(size=2)

		#Bind with MulIntsList setting
		self['MulIntsList']=map(
									int,
									scipy.floor(
										self.MinFloat+(self.MaxFloat-self.MinFloat)*RandomFloatsList
										)
								)

	#</DefineHookMethods>
	
	#<DefineTriggeringHookMethods>
	def bindMulIntsListAfter(self):

		#Bind with MulInt setting
		self['MulInt']=reduce(operator.__mul__,self.MulIntsList)
	#</DefineTriggeringHookMethods>	
#</DefineClass>

#<DefineAttestingFunctions>
def attest_default():
	return SYS.MulClass()

def attest_output():

	#Append a default output
	SYS.Config.seed(5)

	#Return the object __repr__
	TestedVariable=SYS.MulClass().output()
	print(TestedVariable)
	return TestedVariable

def attest_store():

	#Insert the default output
	SYS.Config.seed(5)
	Mul=SYS.MulClass().organize().output().collect().output().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Mul.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

def attest_scan():

	#Insert with all the scanning featuring values
	Mul=SYS.MulClass().organize().scan().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Mul.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

#</DefineAttestingFunctions>
