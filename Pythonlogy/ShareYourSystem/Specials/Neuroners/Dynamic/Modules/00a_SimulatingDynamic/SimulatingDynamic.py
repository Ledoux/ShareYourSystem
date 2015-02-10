#<ImportSpecificModules>
import ShareYourSystem as SYS
import matplotlib
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
class SimulatingDynamicClass(
						SYS.DynamicClass
					):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>

		#<DefineFeatures>
		self.StepTimeFloat=0.05*0.001 #(ms)
		self.RunTimeFloat=1000.*0.001 #(ms)
		self.InitialMeanRateFloat=0.
		self.InitialDeviationRateFloat=0.01
		#</DefineFeatures>

		#<DefineUtilities>
		self.ScaleTimeFloat=self.RunTimeFloat/self.StepTimeFloat
		self.SelectedIntsList=range(0,10)
		#</DefineUtilities>

		#<DefineOutputs>
		self.InititalRateFloatsList=np.zeros(self.UnitsInt,dtype=float)
		self.RateFloatsArray=np.zeros((self.UnitsInt,(int)(self.ScaleTimeFloat)),dtype=float)
		#</DefineOutputs>

		#</DefineSpecificDo>

		#<DefineGroupedDict>
		#self['App_Group_Config'] = SYS.ConfigClass()
		#</DefineGroupedDict>


		#Display just what we want
		self.RepresentingKeyVariablesList = [
												#'GroupedOrderedDict'
											]

		#Definition the features
		self.FeaturingTuplesList += [
										#ColumnStr 		#GettingVariable 	#Col 			#VariablesList
										('StepTimeFloat', 	'StepTimeFloat',	Float32Col(),	[0.1]),
										('RunTimeFloat',	'RunTimeFloat',		Float32Col(),	[1.,10.])
									]

		#Definition the outputs
		self.OutputingTuplesList += [
									#ColumnStr 		#GettingVariable 	#Col 
									('RateFloatsArray', 'RateFloatsArray',	(Float64Col,('UnitsInt'))),
								]
			

	def outputAfter(self,**_LocalOutputingVariablesDict):

		print('Do a simulation...')
		print('')

		#Definition the DelayTimeInt			
		DelayTimeInt=(int)(self.DelayTimeFloat/self.StepTimeFloat)

		#set the ScaleTimeFloat
		self.ScaleTimeFloat=self.RunTimeFloat/self.StepTimeFloat

		#Reinit the self.RateFloatsArray
		self.RateFloatsArray=np.zeros((self.UnitsInt,self.ScaleTimeFloat),dtype=float)

		#set the initial conditions
		self.RateFloatsArray[:,0]=self.InitialDeviationRateFloat*scipy.stats.norm.rvs(self.InitialMeanRateFloat,size=self.UnitsInt)

		#Compute the first order differential equation (integrativ loop)
		for TimeIndexInt in xrange(1,(int)(self.ScaleTimeFloat)):

			#Write the differential discretized version of the vectorized quation
			PreviousTimeIndexInt=TimeIndexInt-1

			#Compute the next time
			self.RateFloatsArray[:,TimeIndexInt] = self.RateFloatsArray[:,PreviousTimeIndexInt] + (

			#Leak Term										#Interaction Term
			-self.RateFloatsArray[:,PreviousTimeIndexInt] + self.StaticTransferFunction(
				np.dot(self.ConnectionsArray,self.RateFloatsArray[:,PreviousTimeIndexInt-DelayTimeInt])
				)
				
																					
			) * (self.StepTimeFloat/self.RateTimeFloat)

			'''
			print(self.RateFloatsArray[:,TimeIndexInt])
			print(self.RateFloatsArray[:,PreviousTimeIndexInt])
			print(self.RateFloatsArray[:,TimeIndexInt-1-DelayTimeInt])
			print('')
			'''

		print('Simulation done...')
		print('')

	#</DefineHookMethods>

	def plotAfter(self,**_LocalPlotingVariablesDict):

		#set the Figure and the Axe
		Axe=self.PlotedFigure.add_subplot(self.PlotingRowsInt,self.PlotingColsInt,self.PlotedInt)
		self.PlotedInt+=1

		#do the figure
		Axe.plot(
					np.array(range((int)(self.ScaleTimeFloat)))*self.StepTimeFloat,
					self.RateFloatsArray.T[:,filter(
													lambda __Int:
													__Int<self.UnitsInt,
													self.SelectedIntsList
													)
					],
					lw=2
				)
		Axe.set_xlabel("$t\ (s)$")
		Axe.set_ylabel("$r_{i}(t)\ (1)$")
		Axe.set_title("")

#</DefineClass>

#<DefineAttestingFunctions>
def attest_default():
	return SYS.SimulatingDynamicClass()

def attest_output():

	#Append a default output
	SYS.Config.seed(5)

	#Return the object __repr__
	TestedVariable=SYS.SimulatingDynamicClass().output()
	print(TestedVariable)
	return TestedVariable

def attest_store():

	#Insert the default output
	SYS.Config.seed(5)
	Dynamic=SYS.SimulatingDynamicClass().organize().output().collect().output().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Dynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

def attest_scan():

	#Insert with all the scanning featuring values
	SimulatingDynamic=SYS.SimulatingDynamicClass().organize().scan().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+SimulatingDynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

#</DefineAttestingFunctions>
