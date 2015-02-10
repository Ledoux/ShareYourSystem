#<ImportSpecificModules>
import itertools
import ShareYourSystem as SYS
import matplotlib.pyplot
import numpy as np
import scipy.stats
from tables import *
import time
import operator
import os
import sys
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>


#<DefineClass>
class PerturbatingDynamicClass(
									SYS.DynamicClass
							):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>

		#<DefineFeatures>
		self.HopfSolvingMethodStr='Contour'
		self.StationaryStr='Null'
		#</DefineFeatures>

		#<DefineUtilities>
		self.InverseStaticTransferFunction=None
		self.DerivativeStaticTransferFunction=None
		self.DynamicTransferFunction=None
		self.DifferentialCurrentStepFloat=0.01
		self.RatePerturbationsArray=np.zeros(self.UnitsInt,dtype=float)
		self.ConnectionComplexesArray=np.zeros(self.UnitsInt,dtype=complex)
		self.LimitingFloatsList=[-5.,5.]
		#</DefineUtilities>

		#<DefineOutputs>
		self.EigenConnectionsArray = np.zeros((2,self.UnitsInt),dtype=float)
		self.EigenHopfPerturbationsArray = np.zeros((2,self.UnitsInt),dtype=float)
		self.EigenJacobianPerturbationsArray = np.zeros((2,self.UnitsInt),dtype=float)
		self.IsRateStableBool = True
		self.IsHopfStableBool = True
		self.HopfFrequency = 0.
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
		self.LocalFeaturingTuplesList = [
										#ColumnStr 			#GettingVariable 	#Col 			#VariablesList
										('StationaryStr', 	'StationaryStr',	StrCol(10),	['null'])
									]
		self.FeaturingTuplesList += self.LocalFeaturingTuplesList

		#Definition the outputs
		self.LocalOutputingTuplesList = [
									#ColumnStr 		#GettingVariable 		#Col 
									('EigenFloatsArray',	'EigenFloatsArray',		(Float64Col,(2,'UnitsInt'))),
									('IsHopfStableBool',	'IsHopfStableBool',			Int64Col())
								]
		self.OutputingTuplesList += self.LocalOutputingTuplesList
						
	def outputAfter(self,**_LocalOutputingVariablesDict):
		
		#set the stationary firing rates
		if self.StationaryStr == 'Null':

			#set the trivial zero solutions
			self.StationaryFloatsList = np.zeros(self.UnitsInt,dtype='float')
			
			#Definition the ZeroStaticTransferFunctionFloat
			self.ZeroStaticTransferFunctionFloat = self.DerivativeStaticTransferFunction(0.)

		elif self.StationaryStr == 'Other':
			pass
			#self.ZeroStaticTransferFunctionFloat=map(self.DerivativeStaticTransferFunction,self.StationaryFloatsList)

		#set the DynamicTransferFunction
		if self.StaticTransferFunctionStr == "Tanh":
			self['DynamicTransferFunction'] = lambda __PulsationComplex:self.ZeroStaticTransferFunctionFloat/(1.+__PulsationComplex*self.RateTimeFloat)

		print('Check that this is rate stable...')
		print('')

		#Check that it is not rate instable
		self.IsRateStableBool=True
		self.RatePerturbationsArray=np.diag(
								[1. for Int in xrange(self.UnitsInt)]
								)-self.ZeroStaticTransferFunctionFloat*self.ConnectionsArray


		'''
		print(
				map( 
				lambda __RowingArray:
				sum(__RowingArray),
				self.RatePerturbationsArray
				),
				map( 
				lambda __RowingArray:
				sum(__RowingArray)<0.,
				self.RatePerturbationsArray
				)
			)

		self.IsRateStableBool=not any(
				map( 
						lambda __RowingArray:
						sum(__RowingArray)<-0.1,
						self.RatePerturbationsArray
					)
		)
		'''

		#If it is rate stable then compute the hopf instablity
		if self.IsRateStableBool:

			print('Ok this is rate stable...')
			print('')

			print('Check if this is Hopf stable...')
			print('')

			#Find the solutions of the self consistent hopf equations
			self.InitialFrequencyFloatsList=[0.1,5.,10.,50.,100.,500.,1000.] if self.HopfSolvingMethodStr=='Determinant' else [0.1,5.,10.,50.,100.,500.,1000.] #(Hz)
			self.IsHopfStableBool=True
			self.HopfFrequency=0.

			#Test hdfclose to the Hopf delay one unit solution
			print('Test reference at the one unit Hopf delay solution...')
			self.testWithFloatsList([
										#85.46264698,
										-0.1,
										1651.29848033
									])

			if self.HopfFrequency>0.:

				#Print
				print('self.HopfFrequency is ',self.HopfFrequency)
				print('Ok the single unit hopf solution works also')

			else:

				#Print
				print('Have to scan again...')

				#Scan the frequency again
				for IndexInt,InitialFrequencyFloat in enumerate(self.InitialFrequencyFloatsList):

					#Find a solution
					self.testWithFloatsList([-0.1,InitialFrequencyFloat*2.*np.pi])

					if self.HopfFrequency>0.:

						#Get outside the loop
						break

			#set te Eigen values of the connection matrix
			if self.SymmetrizingFloat==1. and self.IsDilutedSymmetryBool==False:
				EigenConnectionComplexesArray=np.linalg.eigvalsh(self.ConnectionsArray)
				print('Symmetric case')
			else:
				EigenConnectionComplexesArray=np.linalg.eigvals(self.ConnectionsArray)
				print('Non Symmetric case')
			self.EigenConnectionsArray=np.array(
													[
														np.real(EigenConnectionComplexesArray),
														np.imag(EigenConnectionComplexesArray)
													]
												)

			#Get the EigenPerturbationsArray when it is not stable, 
			#or if it is stable plot the one hdfclose to the control one unit hopf frequency
			self.PerturbatingPulsation=self.HopfFrequency*2.*np.pi if self.HopfFrequency>0. else 1651.29848033

			if self.UnitsInt==1 and self.DelayTimeFloat>0.:
				print()
				print('HopfFrequency should be for the case N=1 : ',self.ZeroStaticTransferFunctionFloat*np.pi/(
					2.*self.DelayTimeFloat))
				print('JHopf should be : ',self.RateTimeFloat*np.pi/(2.*self.DelayTimeFloat))
				
			#set the self.EigenHopfPerturbationsArray
			self.HopfPerturbationsArray=self.ConnectionsArray*np.exp(-1j*self.PerturbatingPulsation*self.DelayTimeFloat)
			EigenHopfPerturbationComplexesArray=np.linalg.eigvals(self.HopfPerturbationsArray)
			self.EigenHopfPerturbationsArray=np.array(
												[
													np.real(EigenHopfPerturbationComplexesArray),
													np.imag(EigenHopfPerturbationComplexesArray)
												]
											)

		else:

			print('It is rate unstable')

	#</DefineHookMethods>
	
	#<DefineTriggeringHookMethods>
	def bindStaticTransferFunctionAfter(self):

		#Bind with InverseStaticTransferFunction setting
		self.InverseStaticTransferFunction=lambda StationaryRateFloat:scipy.optimize.fmin_powell(
														lambda TotalCurrentFloatsList:
														abs(self.StaticTransferFunction(
												TotalCurrentFloatsList[0])-StationaryRateFloat)
														,[0.]
														)

		#Bind with DerivativeStaticTransferFunction setting
		self.DerivativeStaticTransferFunction=lambda TotalCurrentFloat: (self.StaticTransferFunction(
			TotalCurrentFloat+self.DifferentialCurrentStepFloat
			)-self.StaticTransferFunction(
			TotalCurrentFloat-self.DifferentialCurrentStepFloat
			))/(2.*self.DifferentialCurrentStepFloat)

	def bindDynamicTransferFunctionAfter(self):
		self.DynamicCoefficientFunction=lambda __PulsationComplex:self.ZeroStaticTransferFunctionFloat
		self.LeakCoefficientFunction=lambda __PulsationComplex:(1.+__PulsationComplex*self.RateTimeFloat)
		
	def bindConnectionsArrayAfter(self):
		#Use a complex version of the ConnectionComplexesArray
		self.ConnectionComplexesArray=self.ConnectionsArray.astype(complex)

	#</DefineTriggeringHookMethods>

	#</DefineMethods>
	def testWithFloatsList(self,_FloatsList):
		
		#Get the HopfFloatsList
		HopfFloatsList=self.getHopfFloatsListWithInititalFloatsList(_FloatsList)

		print(HopfFloatsList)
		#Stop if it is found unstable
		if HopfFloatsList[0]>0.1:

			#Definition the UnstableFrequencyFloat
			UnstableFrequencyFloat=HopfFloatsList[1]/(2.*np.pi)
			
			#Print
			print("It is unstable for : "+str(UnstableFrequencyFloat)+'Hz')

			#set IsHopfStableBool to false
			self.IsHopfStableBool=False

			#set the HopfFrequency
			self.HopfFrequency=UnstableFrequencyFloat


	def getPerturbationsArrayWithComplex(self,_Complex):

		#set first the PerturbationArray with the LeakCoefficientFunction
		PerturbationsArray=self.LeakCoefficientFunction(_Complex)*np.diag([1. for 
			Int in xrange(self.UnitsInt)])

		#Compute the possible PerturbationsArray
		ConnectingPerturbationsArray = None
		if self.ConnectionsArray.any()!=0.:
			ConnectingPerturbationsArray = self.DynamicCoefficientFunction(_Complex
				)*self.ConnectionComplexesArray
		else:
			ConnectingPerturbationsArray = None
		#print("ConnectingPerturbationsArray")
		#print(ConnectingPerturbationsArray)

		#Add if it is the case the Connection modulation
		if type(ConnectingPerturbationsArray)==np.ndarray:
			PerturbationsArray-=np.exp(-_Complex*self.DelayTimeFloat
				)*ConnectingPerturbationsArray

		#print("PerturbationsArray")
		#print(PerturbationsArray)

		#Return PerturbationsArray
		return PerturbationsArray

	#set the DeterminantFunction
	def getDeterminantTupleWithComplexTuple(self,_ComplexTuple):

		#Definition the DeterminantComplex
		DeterminantComplex=np.linalg.det(self.getPerturbationsArrayWithComplex(_ComplexTuple[0]+1j*_ComplexTuple[1]))
		#print("DeterminantComplex")
		#print(DeterminantComplex)

		#Return its real and imag part
		return (DeterminantComplex.real,DeterminantComplex.imag)

	def getStrongestLambdaTupleTupleWithComplexTuple(self,_ComplexTuple):

		#Get the Complex
		Complex=_ComplexTuple[0]+1j*_ComplexTuple[1]

		#Definition the ComplexContour
		ContourComplexesArray=-(1.+Complex*self.RateTimeFloat
			)+np.exp(-Complex*self.DelayTimeFloat
				)*np.array(
						map(
								lambda __XFloat,YFloat:
								__XFloat+1j*YFloat,
								self.XEllipseContourArray,
								self.YEllipseContourArray
							)
					)

		#Find all the RealPertubationEllipseContourArray and the max one
		RealPertubationEllipseContourArray=np.real(ContourComplexesArray)
		MaxRealFloat=RealPertubationEllipseContourArray.max()
		IndexInt=np.argmax(RealPertubationEllipseContourArray==MaxRealFloat)
								
		#Return its real and imag part
		return (
					RealPertubationEllipseContourArray[IndexInt],
					float(np.imag(ContourComplexesArray[IndexInt]))
				)

	#Definition the Function to find the HopfFloatsList
	def getHopfFloatsListWithInititalFloatsList(self,_InititalFloatsList):

		#Print
		print('')
		print('getHopfFloatsListWithInititalFloatsList Initial : '+str(_InititalFloatsList))

		if self.HopfSolvingMethodStr=='Determinant':

			#Get the solve of the ScipyOptimizeRoot
			ScipyOptimizeRoot=scipy.optimize.root(
					self.getDeterminantTupleWithComplexTuple,
					_InititalFloatsList,
					#method='lm',
					#tol=0.001
					options={
								#'maxiter':1000,
								#'ftol':0.001,
								#'direc':np.array([-0.1,0.1])
							},
					)

			#Print
			if ScipyOptimizeRoot.success:

				print('SUCCESS...getHopfFloatsListWithInititalFloatsList Final : '+str(ScipyOptimizeRoot.x))
				print(ScipyOptimizeRoot)
				TargetsTuple=self.getDeterminantTupleWithComplexTuple(ScipyOptimizeRoot.x)
				print('Retest the solution x0 = '+str(ScipyOptimizeRoot.x)+' : f(x0)='+str(TargetsTuple))
				if sum(np.array(TargetsTuple)**2)<0.01:
					return ScipyOptimizeRoot.x
				else:
					print('Scipy says that it has converged but not good in fact..')
					return (-1.,0.)

			else:

				print('NOT SUCCESS...getHopfFloatsListWithInititalFloatsList Final : '+str(ScipyOptimizeRoot.x))
				print(ScipyOptimizeRoot)
				TargetsTuple=self.getDeterminantTupleWithComplexTuple(ScipyOptimizeRoot.x)
				print('Retest the solution x0 = '+str(ScipyOptimizeRoot.x)+' : f(x0)='+str(TargetsTuple))
				if sum(np.array(TargetsTuple)**2)<0.01:
					print('The solution is nevertheless good...')
					return ScipyOptimizeRoot.x
				else:
					return (-1.,0.)

		elif self.HopfSolvingMethodStr=='Contour':

			#Get the solve of the ScipyOptimizeRoot
			ScipyOptimizeRoot=scipy.optimize.root(
					self.getStrongestLambdaTupleTupleWithComplexTuple,
					_InititalFloatsList,
					#method='lm',
					#tol=0.001
					options={
								#'maxiter':1000,
								'ftol':0.001,
								#'direc':np.array([-0.1,0.1])
							},
					)

			#Print
			if ScipyOptimizeRoot.success:

				print('SUCCESS...getHopfFloatsListWithInititalFloatsList Final : '+str(ScipyOptimizeRoot.x))
				print(ScipyOptimizeRoot)
				TargetsTuple=self.getStrongestLambdaTupleTupleWithComplexTuple(ScipyOptimizeRoot.x)
				print('Retest the solution x0 = '+str(ScipyOptimizeRoot.x)+' : f(x0)='+str(TargetsTuple))
				if sum(np.array(TargetsTuple)**2)<0.01:
					return ScipyOptimizeRoot.x
				else:
					print('Scipy says that it has converged but not good in fact..')
					return (-1.,0.)

			else:

				print('NOT SUCCESS...getHopfFloatsListWithInititalFloatsList Final : '+str(ScipyOptimizeRoot.x))
				print(ScipyOptimizeRoot)
				TargetsTuple=self.getStrongestLambdaTupleTupleWithComplexTuple(ScipyOptimizeRoot.x)
				print('Retest the solution x0 = '+str(ScipyOptimizeRoot.x)+' : f(x0)='+str(TargetsTuple))
				if sum(np.array(TargetsTuple)**2)<0.01:
					print('The solution is nevertheless good...')
					return ScipyOptimizeRoot.x
				else:
					return (-1.,0.)

	def plotAfter(self,**_LocalPlotingVariablesDict):

		#set the Figure and the Axe
		Axe=self.PlotedFigure.add_subplot(self.PlotingRowsInt,self.PlotingColsInt,self.PlotedInt)
		self.PlotedInt+=1

		#Add the Wiener Ellipse
		Ellipse=matplotlib.patches.Ellipse(
												xy=(self.AutaptingMeanWeigthFloat,0.), 
											 	width=2.*self.HalfWidthFloat,
											 	height=2.*self.HalfHeigthFloat,
											 	color='r',
										)
		Ellipse.set_alpha(0.2)
		Axe.add_artist(Ellipse)
		Axe.plot(
					self.XEllipseContourArray,
					self.YEllipseContourArray,
					'-',
					color='r',
					lw=2
				)
		Axe.plot(	
					self.EigenConnectionsArray[0,:],
					self.EigenConnectionsArray[1,:],
					'o',
					markersize=3,
					color='blue',
					
				)
		Axe.plot(
					self.EigenHopfPerturbationsArray[0,:],
					self.EigenHopfPerturbationsArray[1,:],
					'o',
					markersize=3,
					color='red' if self.HopfFrequency>0. else 'green'
				)
		Axe.plot(self.LimitingFloatsList,[0.,0.],'-',color='blue')
		Axe.plot([0.,0.],self.LimitingFloatsList,'-',color='blue')
		Axe.plot([1.,1.],self.LimitingFloatsList,'--',color='red')
		print('LambdaTau is ',self.PerturbatingPulsation*self.RateTimeFloat)
		Axe.plot(
					self.LimitingFloatsList,
					np.ones(2)*self.PerturbatingPulsation*self.RateTimeFloat,
					'--',
					color='red' if self.HopfFrequency>0. else 'green'
				)
		Axe.set_xlim(self.LimitingFloatsList)
		Axe.set_ylim(self.LimitingFloatsList)
		Axe.set_xlabel("$Re(\lambda)$")
		Axe.set_ylabel("$Im(\lambda)$")
		FeaturedTuplesList=[
								('UnitsInt',str(self.UnitsInt)),
								('AutaptingMeanWeigthFloat',str(self.AutaptingMeanWeigthFloat)),
								('DeviationWeigthFloat',str(self.DeviationWeigthFloat)),
								('DelayTimeFloat',str(1000.*self.DelayTimeFloat)+' ms'),
								('LateralingMeanWeigthFloat',str(self.LateralingMeanWeigthFloat)),
								('RateTimeFloat',str(1000.*self.RateTimeFloat)+' ms'),
								('SymetrizingFloat',str(100.*self.SymmetrizingFloat)+'%')
			]
		FeaturedJoinStr="\n Features : \n "+'\n'.join(map(
					lambda __Tuple:
					'('+__Tuple[0]+','+__Tuple[1]+')',
					FeaturedTuplesList
					))+'\n'
		OutputedTuplesList=[
								('IsRateStableBool',str(self.IsRateStableBool)),
								('IsHopfStableBool',str(self.IsHopfStableBool)),
								('HopfFrequency',str(self.HopfFrequency)+' Hz')
			]
		OutputedJoinStr="\n Outputs : \n"+'\n'.join(map(
					lambda __Tuple:
					'('+__Tuple[0]+','+__Tuple[1]+')',
					OutputedTuplesList
					))+'\n'
		Axe.set_title("\n"+FeaturedJoinStr+'\n'+OutputedJoinStr,position=(1.8,0.1))


#</DefineClass>

#<DefineAttestingFunctions>
def attest_default():
	return SYS.DynamicClass()

def attest_output():

	#Append a default output
	SYS.Config.seed(5)

	#Return the object __repr__
	TestedVariable=SYS.PerturbatingDynamicClass().output()
	print(TestedVariable)
	return TestedVariable

def attest_store():

	#Insert the default output
	SYS.Config.seed(5)
	PerturbatingDynamic=SYS.PerturbatingDynamicClass().organize().output().collect().output().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+PerturbatingDynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

def attest_scan():

	#Insert with all the scanning featuring values
	PerturbatingDynamic=SYS.PerturbatingDynamicClass().organize().scan().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+PerturbatingDynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

#</DefineAttestingFunctions>
