
#ImportModules
import ShareYourSystem as SYS


import scipy.optimize
import numpy as np

TauFloat=0.01
DelayFloat=0.002
ConnectivityFloat=7.86
ConnectivityFloatHopf=np.pi*TauFloat/(2.*DelayFloat)
N=4

def determinantII(_OmegaFloat):
	#print(0)
	#print(_OmegaFloat*TauFloat)
	return np.tan(_OmegaFloat*DelayFloat)+_OmegaFloat*TauFloat
def determinantEI(_OmegaFloat):
	#print((1.-(_OmegaFloat*TauFloat)**2))
	#print(2.*_OmegaFloat*TauFloat)
	return np.tan(2.*_OmegaFloat*DelayFloat)+(
			2.*_OmegaFloat*TauFloat/(1.-(_OmegaFloat*TauFloat)**2)
			)
def determinantN(_OmegaFloat):
	LeakComplex=(1.+1j*_OmegaFloat*TauFloat)**N
	LeakRealFloat=LeakComplex.real
	#print(LeakRealFloat)
	LeakImagFloat=LeakComplex.imag
	#print(LeakImagFloat)
	return np.tan(N*_OmegaFloat*DelayFloat)+(LeakImagFloat/LeakRealFloat)

for __LoopStr in ['II','EI','N']:

	#print
	Str=__LoopStr
	if __LoopStr=='N':
		Str+=' (N='+str(N)+')'
	print(Str)

	#
	StartOmegaFloat=2.*np.pi*0.25/DelayFloat
	if __LoopStr=='N':
		StartOmegaFloat/=float(N)

	#get the function
	DeterminantFunction=globals()['determinant'+__LoopStr]
	print('det(w0)='+str(DeterminantFunction(StartOmegaFloat)))

	#rootf
	RootFrequencyFloat=scipy.optimize.fsolve(
		DeterminantFunction,
		StartOmegaFloat
	)/(2.*np.pi)
	print('For '+__LoopStr+', RootFrequencyFloat is '+str(RootFrequencyFloat[0])+'Hz')

	#print
	print('')


import math

def arrangement(k,n):
	return math.factorial(n)/math.factorial(k)

def count(_LoopInt,_UnitsInt):
	
	FirstCountInt=(
		(
			_UnitsInt**(_LoopInt+1)
		)/np.prod([2.**i for i in xrange(1,_LoopInt+2)])
	)
	print('FirstCountInt is '+str(FirstCountInt))

	SecondCountInt=(
		sum(
			[arrangement(2*i+1,_LoopInt+1) for i in xrange(1+_LoopInt/2)]
		)+(1 if _LoopInt%2==1 else 0)
	)
	print(_LoopInt)
	print(arrangement(1,_LoopInt+1))
	print('SecondCountInt is '+str(SecondCountInt))

	#return
	return FirstCountInt*SecondCountInt

from matplotlib import pyplot
UnitIntsList=[100,1000]
LoopIntsList=xrange(1,5)
CountIntsList=map(lambda __LoopInt:count(__LoopInt,1000),LoopIntsList)
print(CountIntsList)
#pyplot.plot(LoopIntsList,map(lambda __LoopInt:count(__LoopInt,1000),LoopIntsList))
#pyplot.show()


