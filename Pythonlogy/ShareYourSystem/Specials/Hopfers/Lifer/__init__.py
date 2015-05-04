# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import types
BaseModuleStr="ShareYourSystem.Standards.Recorders.Leaker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Lifer','Lif','Lifing','Lifed')
#</DefineAugmentation>

#<DefineLocals>
def getFilterDictByType(**Dict):
    FilteredDict={'DoubleDict':{},'IntDict':{},'StringDict':{}};
    for Key,Value in Dict.items():
        TypeDictName=getCTypeNameFromPythonType(type(Value))+'Dict';
        FilteredDict[TypeDictName][Key]=Value;
    return FilteredDict;
SYS.getFilterDictByType=getFilterDictByType
def getCTypeNameFromPythonType(PythonType):
    if PythonType in [float]:
        return 'Double';
    elif PythonType in [int]:
        return 'Int';
    elif PythonType in [str]:
        return 'String'; 
SYS.getCTypeNameFromPythonType=getCTypeNameFromPythonType
def getCArgsFromDict(Dict):
    CArgs=[]
    DictOrderedKeys=Dict.keys()
    for Key in sorted(Dict):
        CArgs.append(Dict[Key]);
    return CArgs;
SYS.getCArgsFromDict=getCArgsFromDict
#</DefineLocals>

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class LiferClass(BaseClass):
	
	def default_init(self, 
			_LifingMembraneConstantTimeFloat=0.02, 
			_LifingRefractoryPeriodFloat=0.,
			_LifingTotalStationaryCurrentFloat=-55., 
			_LifingVoltageNoiseFloat=5., 
			_LifingVoltageResetFloat=-70., 
			_LifingVoltageThresholdFloat=-50.,
			_LifingPerturbVariable=True,
			_LifedSwigVariable=None,
			_LifedStationaryRateVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_lif(self):
		
		#/##################/#
		# Get the swig function
		#

		#Check
		if self.LifedSwigVariable==None:

			#import
			import CIntegrateAndFireTransferFunction

			#get
			self.LifedSwigVariable=CIntegrateAndFireTransferFunction.CIntegrateAndFireTransferFunctionClass()

		#debug
		'''
		self.debug(
			[
				'We have getted dthe Lif swig variable',
				('self.',self,[
						'LifedSwigVariable'
					])
			]
		)
		'''

		#/##################/#
		# Look if the stationary point was already computed
		#

		#Check
		if self.LifedStationaryRateVariable==None:

			#Set inside the Swig
			self.LifedSwigVariable.setDicts(
				*getCArgsFromDict(
					getFilterDictByType(**{
							'MembraneConstantTime':self.LifingMembraneConstantTimeFloat,
							'RefractoryPeriod':self.LifingRefractoryPeriodFloat,
							'TotalStationaryCurrent':self.LifingTotalStationaryCurrentFloat, 
							'VoltageNoise':self.LifingVoltageNoiseFloat, 
							'VoltageReset':self.LifingVoltageResetFloat, 
							'VoltageThreshold':self.LifingVoltageThresholdFloat
						}
					)
				)
			)

			#Compute the IntegralLowerBound and the IntegralUpperBound
			self.LifedSwigVariable.computeIntegralLowerBound();
			self.LifedSwigVariable.computeIntegralUpperBound();
	    	
			#set
			self.LifedStationaryRateFloat=self.LifedSwigVariable.getLIFStationaryRate();

		#/##################/#
		# Compute a perturbaton
		#

		#Check
		if type(self.LifingPerturbVariable)!=None.__class__:

			#debug
			self.debug(
				[
					'We compute a LIF perturbation here'
				]
			)

			#type
			LifedFrequencyType=type(self.LifingPerturbVariable)

			#import 
			import numpy as np

			#Check
			if LifedFrequencyType in [list,np.ndarray]

				#get
				LifedPulsationFloatsArray=np.array(
					self.LifingPerturbVariable
				)*2.*np.pi;

			else:

				#Frequencies=np.array(logspace(0,3,100));
				#Pulsations=[0.00000001]+linspace(0.1,1000.,100);
				pass


		elif self.LifingPerturbVariable==0.:

			#get
			self.LifedNullPerturbFloat=self.LifedSwigVariable.getLIFPerturbativeRate0();

		#get
		LifedPerturbMethod=getattr(
			self.LifedSwigVariable,
			'get'+self.LifingPerturbMethodStr+'LIFPerturbativeRate'
		)

		self.LifedPerturbComplexesArray=map(
			lambda __LifedPulsationFloat:
			LifedPerturbMethod,
			LifedPulsationFloatsArray
		)

	def pyplot(self):

		pass

		"""
		###PLOT#####
		VoltageNoises=[0.,1.,2.5,5.]
		colors=["black","black","black","black"];
		linestyle=[":","--","-.","-"];
		TotalStationaryCurrents=arange(-70.,-40.,0.1);
		for VoltageNoiseIdx in xrange(len(VoltageNoises)):    
		    myLIFTransfer.DoubleDict["VoltageNoise"]=VoltageNoises[VoltageNoiseIdx];
		    plot(TotalStationaryCurrents,
		         map(getFrequencyFromTotalStationaryCurrent,TotalStationaryCurrents),
		         linestyle=linestyle[VoltageNoiseIdx],color=colors[VoltageNoiseIdx],
		         lw=5,label="$\sigma=%.0f\ mV$"%VoltageNoises[VoltageNoiseIdx]);

		###BEAUTIFY PLOY
		legend()
		xlabel('$\mu_{0}\ (mV)$',fontsize=25)
		ylabel('$f\ (Hz)$',fontsize=25)
		"""
		
		"""
		####PLOT#####
		subplot(2,2,1);
		plot(Frequencies,abs(CurrentBrunelLIFPerturbativeRates)/r0,color='brown',linestyle=linestyle[VoltageNoiseIdx],lw=10);
		plot(Frequencies,abs(CurrentHakimLIFPerturbativeRates)/r0,color='red',linestyle=linestyle[VoltageNoiseIdx],lw=5);
		subplot(2,2,3);
		plot(Frequencies,(180./np.pi)*np.angle(CurrentBrunelLIFPerturbativeRates),color='brown',linestyle=linestyle[VoltageNoiseIdx],lw=10);
		plot(Frequencies,(180./np.pi)*np.angle(CurrentHakimLIFPerturbativeRates),color='red',linestyle=linestyle[VoltageNoiseIdx],lw=5);
		subplot(2,2,2);
		plot([-1.,-1.],[-1.,-1.],color='black',linestyle=linestyle[VoltageNoiseIdx],label="$\sigma=%.0f\,mV$"%VoltageNoise,lw=5);
		plot(Frequencies,abs(NoiseBrunelLIFPerturbativeRates)/r0,color='brown',linestyle=linestyle[VoltageNoiseIdx],lw=10);
		plot(Frequencies,abs(NoiseHakimLIFPerturbativeRates)/r0,color='red',linestyle=linestyle[VoltageNoiseIdx],lw=5);
		subplot(2,2,4);
		plot(Frequencies,(180./np.pi)*np.angle(NoiseBrunelLIFPerturbativeRates),color='brown',linestyle=linestyle[VoltageNoiseIdx],lw=10);
		plot(Frequencies,(180./np.pi)*np.angle(NoiseHakimLIFPerturbativeRates),color='red',linestyle=linestyle[VoltageNoiseIdx],lw=5);
		    
		_maxMu=max(_maxMu,max((abs(CurrentBrunelLIFPerturbativeRates)/r0).max(),(abs(CurrentHakimLIFPerturbativeRates)/r0).max()));
		_maxSigma=max(_maxSigma,max((abs(NoiseBrunelLIFPerturbativeRates)/r0).max(),(abs(NoiseHakimLIFPerturbativeRates)/r0).max()));

		####BEAUTIFY PLOTS###
		ax=subplot(2,2,1);
		ax.plot([-1.,-1.],[-1.,-1.],color='brown',linestyle=linestyle[VoltageNoiseIdx],label="Brunel",lw=5);
		ax.plot([-1.,-1.],[-1.,-1.],color='red',linestyle=linestyle[VoltageNoiseIdx],label="Hakim",lw=5);
		ax.legend();
		ax.set_xscale('log');
		ax.set_xticks([0.1,1.,10.,100.,1000.]);
		ax.set_xticklabels([]);
		ax.set_xlim([min(Frequencies),max(Frequencies)]);
		ax.set_ylabel('$|\\tilde{R}_{\mu_{0}}(f=\\frac{\omega}{2\pi})|/r_{0} $',fontsize=25);
		ax.set_ylim([0,_maxMu]);
		ax=subplot(2,2,3);
		ax.set_xlabel('$f\ (Hz)$',fontsize=25);
		ax.set_xscale('log');
		ax.set_xticks([0.1,1.,10.,100.,1000.]);
		ax.set_xlim([min(Frequencies),max(Frequencies)]);
		ax.set_ylabel('$\Phi(\\tilde{R}_{\mu_{0}}(f=\\frac{\omega}{2\pi})) $',fontsize=25);
		ax.set_ylim([-180.,180.]);
		ax=subplot(2,2,2);
		ax.legend();
		ax.set_xscale('log');
		ax.set_xticks([0.1,1.,10.,100.,1000.]);
		ax.set_xticklabels([]);
		ax.set_xlim([min(Frequencies),max(Frequencies)]);
		ax.set_ylabel('$|\\tilde{R}_{\sigma}(f=\\frac{\omega}{2\pi})|/r_{0} $',fontsize=25);
		ax.set_ylim([0,_maxSigma]);
		ax=subplot(2,2,4);
		ax.set_xlabel('$f\ (Hz)$',fontsize=25);
		ax.set_xscale('log');
		ax.set_xticks([0.1,1.,10.,100.,1000.]);
		ax.set_xlim([min(Frequencies),max(Frequencies)]);
		ax.set_ylabel('$\Phi(\\tilde{R}_{\sigma}(f=\\frac{\omega}{2\pi})) $',fontsize=25);
		ax.set_ylim([-180.,180.]);
		"""


#</DefineClass>

#</DefinePrint>
LiferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'LifingMembraneConstantTimeFloat', 
		'LifingRefractoryPeriodFloat',
		'LifingTotalStationaryCurrentFloat', 
		'LifingVoltageNoiseFloat', 
		'LifingVoltageResetFloat', 
		'LifingVoltageThresholdFloat',
		'LifedSwigVariable',
		#'LifedStationaryRateFloat'
	]
)
#<DefinePrint>