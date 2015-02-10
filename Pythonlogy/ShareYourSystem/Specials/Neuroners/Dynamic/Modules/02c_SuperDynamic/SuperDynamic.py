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
#</DefineLocals>

#<DefineClass>
class SuperDynamicClass(
						SYS.PerturbatingDynamicClass,
						SYS.SimulatingDynamicClass
					):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>

		#<DefineFeatures>
		#</DefineFeatures>

		#<DefineUtilities>
		#</DefineUtilities>

		#<DefineOutputs>
		#</DefineOutputs>

		#</DefineSpecificDo>

		#<DefineGroupedDict>
		#</DefineGroupedDict>


		#Display just what we want
		self.RepresentingKeyVariablesList = [
												#'GroupedOrderedDict'
											]

		#Definition the features
		self.FeaturingTuplesList = [
										#ColumnStr 	#GettingVariable 	#Col 			#VariablesList

									]

		#Definition the outputs
		self.OutputingTuplesList = [
									#ColumnStr 		#GettingVariable 		#Col 
								]
						

	def outputAfter(self,**_LocalOutputingVariablesDict):
		pass

	#</DefineHookMethods>
	
	#<DefineTriggeringHookMethods>
	#</DefineTriggeringHookMethods>	

#</DefineClass>

#<DefineAttestingFunctions>
def attest_default():
	return SYS.SuperDynamicClass()

def attest_output():

	#Append a default output
	SYS.Config.seed(5)

	#Return the object __repr__
	TestedVariable=SYS.SuperDynamicClass().output()
	print(TestedVariable)
	return TestedVariable

def attest_store():

	#Insert the default output
	SYS.Config.seed(5)
	SuperDynamic=SYS.SuperDynamicClass().organize().output().collect().output().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+SuperDynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

def attest_scan():

	#Insert with all the scanning featuring values
	Dynamic=SYS.MulClass().organize().scan().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Mul.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

#</DefineAttestingFunctions>
