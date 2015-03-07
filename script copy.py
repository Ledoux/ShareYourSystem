
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins

# Define some CSS to control our custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

N = 50
df = pd.DataFrame(index=range(N))
df['x'] = np.random.randn(N)
df['y'] = np.random.randn(N)
df['z'] = np.random.randn(N)

labels = []
for i in range(N):
    label = df.ix[[i], :].T
    label.columns = ['Row {0}'.format(i)]
    # .to_html() is unicode; so make leading 'u' go away with str()
    labels.append(str(label.to_html()))

points = ax.plot(df.x, df.y, 'o', color='b',
                 mec='k', ms=15, mew=1, alpha=.6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('HTML tooltips', size=20)

tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                   voffset=10, hoffset=10, css=css)
plugins.connect(fig, tooltip)

mpld3.show()































"""
#ImportModules
import ShareYourSystem as SYS
import sympy

#compute
UnitsInt=4
Matrix=sympy.Matrix(
	[
		[
			sympy.Symbol(
				'J'+str(__RowInt)+str(__ColInt)
			) if __RowInt!=__ColInt else 1 for __ColInt in xrange(UnitsInt)
		] for __RowInt in xrange(UnitsInt)
	]
)

#define
def getAbstractChainSymbolStr(_ChainStr):
	
	#Check
	if _ChainStr[0]=='-':
		ChainStr=_ChainStr[1:]
	else:
		ChainStr=_ChainStr

	#init
	AbstractDict={}
	AbstractCompressStr="K"
	AbstractChainStr="J"

	#Switch case
	TypeStrsList=['Pre','Post']
	TypeIndexInt=1

	#for
	for __IndexInt,__IntStr in enumerate(ChainStr):

		#Print
		'''
		print('__IndexInt,__IntStr is')
		print(__IndexInt,__IntStr)
		print('')
		'''

		#Check
		if __IntStr not in AbstractDict:

			#add
			AbstractDict[__IntStr]=str(len(AbstractDict))

		#Check
		if __IndexInt!=0:

			#Check
			if TypeStrsList[TypeIndexInt]=='Post':

				#Print
				'''
				print('AbstractChainStr is')
				print(AbstractChainStr)
				print('AbstractCompressStr is ')
				print(AbstractCompressStr)
				print('')
				'''

				#Check
				if AbstractCompressStr!=False:

					#paste or not
					if AbstractChainStr[-1]==AbstractDict[__IntStr]:
						AbstractCompressStr+=AbstractDict[__IntStr]
					else:
						AbstractCompressStr=False

				#addd
				AbstractChainStr+='J'

		#switch	
		if TypeIndexInt==1:
			TypeIndexInt=0
		else:
			TypeIndexInt=1

		#add
		AbstractChainStr+=AbstractDict[__IntStr]
		

	#print
	'''
	print('In the end')
	print(_ChainStr)
	print(AbstractChainStr)
	'''

	#Check
	if _ChainStr[0]=='-':
		AbstractChainStr='-'+AbstractChainStr
		if AbstractCompressStr!=False:
			AbstractCompressStr='-'+AbstractCompressStr	

	#return
	#if AbstractCompressStr!=False:
	#	return AbstractCompressStr
	#else:
	#	return AbstractChainStr
	
	AbstractChainSymbol=1
	for __AbstractStr in AbstractChainStr.split('J'):
		if __AbstractStr!='':
			if __AbstractStr=='-':
				AbstractChainSymbol*=-1
			else:
				AbstractChainSymbol*=sympy.Symbol('J'+__AbstractStr)
	
	return AbstractChainSymbol
	
def getDetAbstractSymbol(_Matrix):

	#Element
	DetStr=str(_Matrix.det())
	DetStr=DetStr.replace('- ','+ -')
	ElementStrsList=DetStr.split('+')
	#print('ElementStrsList is ')
	#print(ElementStrsList)

	#chains
	ChainStrsList=SYS._filter(lambda __ElementStr:__ElementStr!='1',
		map(
			lambda __ElementStr:
			__ElementStr.replace('*','').replace('J','').replace(' ',''),
			ElementStrsList
		)
	)
	#print('\nChainStrsList is')
	#print(ChainStrsList)

	#abstract chains
	AbstractChainSymbolsList=map(getAbstractChainSymbolStr,ChainStrsList)	
	#print('\nAbstractChainSymbolsList is ')
	#print(AbstractChainSymbolsList)

	#sympify
	DetAbstractSymbol=1
	for __IndexInt in xrange(len(AbstractChainSymbolsList)):
		DetAbstractSymbol+=AbstractChainSymbolsList[__IndexInt]
	#print('\nDetAbstractSymbol is')
	#print(DetAbstractSymbol)

	#return
	return DetAbstractSymbol

#def getTotalDetAbstractSymbol(Matrix):



print(getDetAbstractSymbol(Matrix))

"""

"""
import scipy.stats
import numpy as np
from matplotlib import pyplot
LoopInt=4
UnitsInt=100
NormalArraysArray=[scipy.stats.norm.rvs(size=UnitsInt**2) for __Int in xrange(LoopInt)]
NormalProdArray=map(np.prod,zip(*NormalArraysArray))
pyplot.figure()
n,bins,patches=pyplot.hist(NormalArraysArray[0],np.arange(-2.,2.,0.1),color='b')
pyplot.plot(((bins[1]-bins[0])/2.)+bins[:-1],n,'k-', linewidth=3,color='g')
n,bins,patches=pyplot.hist(NormalProdArray,np.arange(-1.,1.,0.1),color='r')
pyplot.plot(((bins[1]-bins[0])/2.)+bins[:-1],n,'k-', linewidth=3,color='grey')
pyplot.xlim([-5.,5.])
pyplot.show()
"""


"""
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
"""

