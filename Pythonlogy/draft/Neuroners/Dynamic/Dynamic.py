#<ImportSpecificModules>
import copy
import ShareYourSystem as SYS
import itertools
import numpy as np
import scipy.stats
from tables import *
import time
import operator
import os
import random
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineFunctions>
def getNotAutaptingTuplesListWithConnectionsIntAndPairsInt(_ConnectionsInt,_PairsInt):

	#Print
	print('Going to pick '+str(_PairsInt)+' pairs in a '+str(_ConnectionsInt)+' ConnectionsInt')
	print('')

	#Definition the number of rows
	RowsInt=(int)(np.sqrt(_ConnectionsInt))

	#Pick only the upper pairs
	NotAutaptingTuplesList=filter(
								lambda __Tuple:
								__Tuple[1]>__Tuple[0],
								itertools.product(xrange(RowsInt),xrange(RowsInt))
							)

	#Shuffle and pick the _SymetricPairsInt ones
	random.shuffle(NotAutaptingTuplesList)
	NotAutaptingTuplesList=NotAutaptingTuplesList[:_PairsInt]

	#Return
	return NotAutaptingTuplesList
#</DefineFunctions>

#<DefineClass>
class DynamicClass(SYS.ObjectsClass):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDo>

		#<DefineLocalFeatures>
		self.IsAntiSymmetricBool=True
		#self.SymmetrizingFloat = 0.6
		self.SymmetrizingFloat = 0.4
		self.IsDilutedSymmetryBool=True
		self.DelayTimeFloat = 5.*0.001 #(ms)
		self.DeviationWeigthFloat = 1.5
		#self.AutaptingMeanWeigthFloat=-18.
		#self.LateralingMeanWeigthFloat=-18.
		self.AutaptingMeanWeigthFloat=-2.1
		self.LateralingMeanWeigthFloat=-2.1
		self.StaticTransferFunctionStr='Tanh'
		self.RateTimeFloat = 10.*0.001 #(ms)
		self.UnitsInt = 100
		self.SlopeFloat=1.

		'''
		self.SymmetrizingFloat = 0.5
		self.DelayTimeFloat = 1.*0.001 #(ms)
		self.DeviationWeigthFloat = 2.
		#self.AutaptingMeanWeigthFloat=-18.
		#self.LateralingMeanWeigthFloat=-18.
		self.AutaptingMeanWeigthFloat=-18.
		self.LateralingMeanWeigthFloat=0.
		self.StaticTransferFunctionStr='Tanh'
		self.RateTimeFloat = 10.*0.001 #(ms)
		self.UnitsInt = 100
		self.SlopeFloat=1.
		'''

		'''
		self.SymmetrizingFloat = 0.2
		self.DelayTimeFloat = 1.*0.001 #(ms)
		self.DeviationWeigthFloat = 1.
		#self.AutaptingMeanWeigthFloat=-18.
		#self.LateralingMeanWeigthFloat=-18.
		self.AutaptingMeanWeigthFloat=-18.
		self.LateralingMeanWeigthFloat=-18.
		self.StaticTransferFunctionStr='Tanh'
		self.RateTimeFloat = 10.*0.001 #(ms)
		self.UnitsInt = 30
		self.SlopeFloat=5.
		'''
		'''
		self.SymmetrizingFloat = 0.7
		self.DelayTimeFloat = 0.*0.001 #(ms)
		self.DeviationWeigthFloat = 1.
		#self.AutaptingMeanWeigthFloat=-18.
		#self.LateralingMeanWeigthFloat=-18.
		self.AutaptingMeanWeigthFloat=0.
		self.LateralingMeanWeigthFloat=0.
		self.StaticTransferFunctionStr='Tanh'
		self.RateTimeFloat = 10.*0.001 #(ms)
		self.UnitsInt = 300
		'''
		#</DefineLocalFeatures>

		#<DefineLocalUtilities>
		self.StaticTransferFunction=None
		#</DefineLocalUtilities>

		#<DefineLocalOutputs>
		self.ConnectionsArray = np.zeros((self.UnitsInt,self.UnitsInt),dtype=float)
		self.DegreeSymmetryFloat = 0.
		self.StaticTransferFunction = None
		#</DefineLocalOutputs>

		#</DefineSpecificDo>

		#<DefineGroupedDict>
		#self['App_Group_Config'] = SYS.ConfigClass()
		#</DefineGroupedDict>


		#Display just what we want
		self.RepresentingKeyVariablesList = [
												#'GroupedOrderedDict'
											]

		'''
		#Definition the features
		self.FeaturingTuplesList = [
										#ColumnStr 	#GettingVariable 	#Col 			#VariablesList
										('DelayTimeFloat',	'DelayTimeFloat',		Float32Col(),	[1.])
									]

		#Definition the outputs
		self.OutputingTuplesList = [
									#ColumnStr 		#GettingVariable 		#Col 
									('ConnectionsArray', 'ConnectionsArray',	Float64Col(shape=(self.UnitsInt,self.UnitsInt))),
									('EigenValuesList',	 'EigenValuesList',		Float64Col(shape=(2,self.UnitsInt)))
								]
		'''

		#Definition the features
		self.FeaturingTuplesList = [
										#ColumnStr 	#GettingVariable 		#Col 			#VariablesList
										('UnitsInt', 		'UnitsInt',			Int64Col(),		[1.,10.]),
										('DelayTimeFloat',	'DelayTimeFloat',	Float64Col(),	[1.])
									]

		#Definition the outputs
		self.OutputingTuplesList = [
									#ColumnStr 		#GettingVariable 		#Col 
									('ConnectionsArray', 'ConnectionsArray',	(Float64Col,('UnitsInt','UnitsInt'))),
								]
						

	def outputAfter(self,**_LocalOutputingVariablesDict):

		#Definition the Noise deviation
		StandardDeviationFloat=(self.DeviationWeigthFloat/np.sqrt(float(self.UnitsInt)))

		#Special case of one unit, just put equal to the StandardDeviationFloat
		if self.UnitsInt==1:
			self['ConnectionsArray']=np.array([[self.AutaptingMeanWeigthFloat]])
			self.XEllipseContourArray=np.array([self.AutaptingMeanWeigthFloat])
			self.YEllipseContourArray=np.array([0.])
			self.HalfWidthFloat=0.
			self.HalfHeigthFloat=0.
			
			
		else:

			#Definition the ConnectionsInt
			self.ConnectionsInt=self.UnitsInt**2

			#Definition the SymmetricConnectionsInt
			self.SymmetricConnectionsInt=(self.UnitsInt*(self.UnitsInt-1))
			self.SymmetricPairsInt=self.SymmetricConnectionsInt/2

			#Print
			print('Going to build a symmetric matrix...')
			print('')

			#Case where if symetry can be a bit or not
			if self.IsDilutedSymmetryBool:

				#Definition a RandomArray
				RandomFloatsArray=scipy.stats.norm.rvs(size=(self.UnitsInt,self.UnitsInt))

				#Definition the
				ScaledSymmetrizingFloat=((self.SymmetrizingFloat-1.)*0.5)+1
				#ScaledSymmetrizingFloat=self.SymmetrizingFloat
				#print('ScaledSymmetrizingFloat is ',ScaledSymmetrizingFloat)
				#OtherScaledSymmetrizingFloat=2.*(self.SymmetrizingFloat-1.)+1.
				#print('OtherScaledSymmetrizingFloat is ',OtherScaledSymmetrizingFloat)

				#Build a more or less DisSymmetricRandomArray
				DisSymmetricRandomArray=2.*(
					(ScaledSymmetrizingFloat/2.)*(RandomFloatsArray+RandomFloatsArray.T)
						+(0.5-(ScaledSymmetrizingFloat/2.))*(RandomFloatsArray-RandomFloatsArray.T)
					)

				#Compute the deviation
				VarianceFloat=np.sum(
							np.array(
									filter(
											lambda __Float:
											__Float!=None,
											map(
												lambda __Tuple:
												DisSymmetricRandomArray[__Tuple]**2
												if __Tuple[0]!=__Tuple[1] else None
												,itertools.product(xrange(self.UnitsInt),xrange(self.UnitsInt))
											)
										)
									)
								)/(float(self.SymmetricConnectionsInt))
				DeviationFloat=np.sqrt(VarianceFloat)

				#Rescale the diagonal
				map(
					lambda __IndexInt:
					DisSymmetricRandomArray.__setitem__(
						(__IndexInt,__IndexInt),
						DeviationFloat*scipy.stats.norm.rvs()
						),
					xrange(self.UnitsInt)
					)

			#Case where if there is a symmetric pair, it is totally or not
			else:

				#Definition a RandomArray
				SymmetricRandomFloatsList=scipy.stats.norm.rvs(size=self.SymmetricPairsInt+self.UnitsInt)

				SymmetricRandomArray=np.zeros((self.UnitsInt,self.UnitsInt),dtype=float)
				map(
						lambda __ConnectionTuple,__ConnectionFloat:
						map(
								lambda __SymmetricConnectionTuple:
								SymmetricRandomArray.__setitem__(
											__SymmetricConnectionTuple,
											__ConnectionFloat
										)
								,
								[__ConnectionTuple,(__ConnectionTuple[1],__ConnectionTuple[0])]
							),
						filter(
								lambda __Tuple:
								__Tuple[1]>=__Tuple[0],
								itertools.product(xrange(self.UnitsInt),xrange(self.UnitsInt))
								),
						SymmetricRandomFloatsList
					)

				#Print
				print('...Symmetric matrix Built ok')
				print('')

				#Print
				print('Going to pick symmetric pairs and set a disymetrized matrix...')
				print('')

				#Pick some not autapted SymetricTuplesList
				SymetricTuplesList=getNotAutaptingTuplesListWithConnectionsIntAndPairsInt(
													self.ConnectionsInt,
													(int)(self.SymmetrizingFloat*self.SymmetricPairsInt),
												)
				OppositeSymetricTuplesList=map(
												lambda __Tuple:
												(__Tuple[1],__Tuple[0]),
												SymetricTuplesList
											)

				#Print
				print('Ok it is picked...')
				print('')

				#Init the SymetrizingArray with random
				DisSymmetricRandomArray=scipy.stats.norm.rvs(size=(self.UnitsInt,self.UnitsInt))

				#set the SymetrizingArray by either picking in RandomArray or choosing new random values
				map(
						lambda __Tuple:
						DisSymmetricRandomArray.__setitem__(
												__Tuple,
												SymmetricRandomArray[__Tuple]
												),
						SymetricTuplesList
					)
				map(
						lambda __Tuple:
						DisSymmetricRandomArray.__setitem__(
												__Tuple,
												SymmetricRandomArray[__Tuple] 
												if self.IsAntiSymmetricBool==False 
												else -SymmetricRandomArray[__Tuple] 
												),
						OppositeSymetricTuplesList
					)

				#debug
				print('Disymetrized matrix ok...')
				print('')
		
			#debug
			print('Add some Constant weigths')
			print('')

			#set the ConnectionsArray
			AutaptingMeanConnectionsArray=np.diag([
				self.AutaptingMeanWeigthFloat for Int in xrange(self.UnitsInt)
				])
			LateralingMeanConnectionsArray=((self.LateralingMeanWeigthFloat/self.UnitsInt)
				)*(np.ones((self.UnitsInt,self.UnitsInt),dtype=float)-
				np.diag([1. for Int in xrange(self.UnitsInt)]))

			#print('AutaptingMeanConnectionsArray',AutaptingMeanConnectionsArray)
			#print('LateralingMeanConnectionsArray',LateralingMeanConnectionsArray)

			self['ConnectionsArray'
			]=AutaptingMeanConnectionsArray+LateralingMeanConnectionsArray+StandardDeviationFloat*DisSymmetricRandomArray

			#Compute the CoVarianceFloat and the ellipse contour
			self.VarianceFloat=self.UnitsInt*np.sum(
							np.array(
									filter(
											lambda __Float:
											__Float!=None,
											map(
												lambda __Tuple:
												self.ConnectionsArray[__Tuple]**2
												if __Tuple[0]!=__Tuple[1] else None
												,itertools.product(xrange(self.UnitsInt),xrange(self.UnitsInt))
											)
										)
									)
								)/(float(self.SymmetricConnectionsInt))
			self.DeviationFloat=np.sqrt(self.VarianceFloat)
			print('VarianceFloat is ',self.VarianceFloat)
			print('DeviationFloat is ',self.DeviationFloat)
			self.CoVarianceFloat=self.UnitsInt*np.sum(
							np.array(
									filter(
											lambda __Float:
											__Float!=None,
											map(
												lambda __Tuple:
				(self.ConnectionsArray[__Tuple])*(self.ConnectionsArray[
												(__Tuple[1],__Tuple[0])]) 
												if __Tuple[0]!=__Tuple[1] else None
												,itertools.product(xrange(self.UnitsInt),xrange(self.UnitsInt))
											)
										)
									)
								)/(float(self.VarianceFloat*self.SymmetricConnectionsInt))
			print('CoVariance Float is ',self.CoVarianceFloat)
			
			self.HalfWidthFloat=self.DeviationFloat*(1.+self.CoVarianceFloat)
			self.HalfHeigthFloat=self.DeviationFloat*(1.-self.CoVarianceFloat)

			if self.HalfWidthFloat>0.:
				self.XEllipseFloatsArray=self.AutaptingMeanWeigthFloat+np.arange(-self.HalfWidthFloat,self.HalfWidthFloat,0.005)
				self.EllipseTuplesArray=np.array(
									filter(
										lambda __Tuple:
										__Tuple[1]==__Tuple[1],
										map(
												lambda __XFloat:
												(
													__XFloat,
													np.sqrt(
														(1.-(
															(
									(__XFloat-self.AutaptingMeanWeigthFloat)/(self.HalfWidthFloat)
									)**2
															)
														)
													)*self.HalfHeigthFloat
												),
												self.XEllipseFloatsArray
											)
										)
									)
				self.XEllipseFloatsArray,self.YEllipseFloatsArray=zip(*self.EllipseTuplesArray)
				self.XEllipseOppositeFloatsArray=copy.copy(list(self.XEllipseFloatsArray))
				self.XEllipseOppositeFloatsArray.reverse()
				self.XEllipseOppositeFloatsArray=np.array(self.XEllipseOppositeFloatsArray)
				self.YEllipseOppositeFloatsArray=list(-np.array(self.YEllipseFloatsArray))
				self.YEllipseOppositeFloatsArray.reverse()
				self.YEllipseOppositeFloatsArray=np.array(self.YEllipseOppositeFloatsArray)
				self.XEllipseContourArray=np.concatenate((self.XEllipseFloatsArray,self.XEllipseOppositeFloatsArray))
				self.YEllipseContourArray=np.concatenate((self.YEllipseFloatsArray,self.YEllipseOppositeFloatsArray))
			else:
				self.XEllipseContourArray=np.array([self.AutaptingMeanWeigthFloat])
				self.YEllipseContourArray=np.array([0.])


		#set the StaticTransferFunctionStr
		if self.StaticTransferFunctionStr == "Lif":
			self['StaticTransferFunction'] = lambda __TotalCurrentFloat:SYS.LifTransferFuncterClass().update(
				{
				}
				)('func',__TotalCurrentFloat)

		if self.StaticTransferFunctionStr == "Tanh":
			self['StaticTransferFunction'] = lambda __TotalCurrentFloat:np.tanh(self.SlopeFloat*__TotalCurrentFloat)




	#</DefineHookMethods>
	
	#<DefineTriggeringHookMethods>
	#</DefineTriggeringHookMethods>	

#</DefineClass>

#<DefineAttestingFunctions>
def attest_default():
	return SYS.DynamicClass()

def attest_output():

	#Append a default output
	SYS.Config.seed(5)

	#Return the object __repr__
	TestedVariable=SYS.DynamicClass().output()
	print(TestedVariable)
	return TestedVariable

def attest_store():

	#Insert the default output
	SYS.Config.seed(5)
	Dynamic=SYS.DynamicClass().organize().output().collect().output().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Dynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

def attest_scan():

	#Insert with all the scanning featuring values
	Dynamic=SYS.DynamicClass().organize().scan().hdfclose()

	#Return the shape of the storing hdf5
	TestedVariable=os.popen('h5ls -dlr '+Dynamic.GroupingFilePathStr).read()
	print(TestedVariable)
	return TestedVariable

#</DefineAttestingFunctions>
