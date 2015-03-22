# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Lifer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Neurongrouper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineLocals>
'''
class SingleSpikeThreshold1(Threshold):
	def __init__(self, _AlreadySpikedBool):
		self.AlreadySpikedBool=_AlreadySpikedBool;

	def __call__(self,_P):

		#Check
		if self.self.AlreadySpikedBool==False:

			#find
			SpikesList = (_P.v >_P.T).nonzero()[0]

			#Only keep the first (could also be a random one, etc) spike if there is more than one
			if len(SpikesList)>0:
				IndexIntsList=randint(len(SpikesList));
				self.AlreadySpikedBool=True;
				SpikesList=SpikesList[IndexIntsList:(IndexIntsList+1)];
				_P.v[SpikesList]=_P.T[SpikesList];

			#return
			return SpikesList;

		else:
			#one neuron has already crossed threshold and wait for an inhibitory reset at this next dt...
			#...So we don't need to count an other new spike for it.
			self.AlreadySpikedBool=False;

			#return 
			return SpikesList;
'''

def getSpecificThresholdBool(_NeuronGroup):

	#debug
	print('_NeuronGroup is \n')
	print(_NeuronGroup)
	print('')

	#return
	return _NeuronGroup.v>self.LifingThresholdVariable

def setSpecificResetVariable(_NeuronGroup,_SpikeIndexIntsList):
	_NeuronGroup[_SpikeIndexIntsList]=self.LifingResetVariable

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class LiferClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'LifingRestVariable',
								'LifingConstantTimeVariable',
								'LifingThresholdVariable',
								'LifingResetVariable',
								'LifedRestVariableStr',
								'LifedConstantTimeVariableStr',
								'LifedThresholdVariableStr',
								'LifedResetVariableStr'
							]

	def default_init(self,
						_LifingRestVariable=-60.,
						_LifingConstantTimeVariable=20.,
						_LifingThresholdVariable=-50.,
						_LifingResetVariable=-70.,
						_LifedRestVariableStr="",
						_LifedConstantTimeVariableStr="",
						_LifedThresholdVariableStr="",
						_LifedResetVariableStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_lif(
				self,
			):	

		#debug
		self.debug(
					('self.',self,[
									'LifingRestVariable'
								])
				)

		#init
		self.NeurongroupingKwargVariablesDict={
			'model':"",
			'threshold':'v>'+str(self.LifingThresholdVariable)+'*mV',
			'reset':'v='+str(self.LifingResetVariable)+'*mV'
		}
		self.NeurongroupingVariableStrToGetStrDict={}

		#Vm
		if type(self.LifingRestVariable)==float:
			self.LifedRestVariableStr=str(self.LifingRestVariable)
		else:
			self.LifedRestVariableStr='Vm'
			self.NeurongroupingKwargVariablesDict['model']+='''Vm : 1\n'''
			self.NeurongroupingVariableStrToGetStrDict['Vm']='LifingRestVariable'

		#Taum
		if type(self.LifingConstantTimeVariable)==float:
			self.LifedConstantTimeVariableStr=str(self.LifingConstantTimeVariable)
		else:
			self.LifedConstantTimeVariableStr='taum'
			self.NeurongroupingKwargVariablesDict['model']+='''taum : 1\n'''
			self.NeurongroupingVariableStrToGetStrDict['taum']='LifingConstantTimeVariable'
		
		#Vt		
		if type(self.LifingThresholdVariable)==float:
			self.LifedThresholdVariableStr=str(self.LifingThresholdVariable)
		else:
			self.LifedThresholdVariableStr='Vt'
			self.NeurongroupingKwargVariablesDict['model']+='''Vt : 1\n'''
			#self.NeurongroupingKwargVariablesDict['threshold']=getSpecificThresholdBool
			#self.NeurongroupingKwargVariablesDict['threshold']=self.LifingThresholdVariable
			#self.NeurongroupingKwargVariablesDict['threshold']=brian2.Threshold(0.*mV)
			self.NeurongroupingKwargVariablesDict['threshold']='v>Vt*mV'
			self.NeurongroupingVariableStrToGetStrDict['Vt']='LifingThresholdVariable'

		#Vr
		if type(self.LifingResetVariable)==float:
			self.LifedResetVariableStr=str(self.LifingResetVariable)
		else:
			#self.LifedResetVariableStr='Vr'
			self.NeurongroupingKwargVariablesDict['model']+='''Vr : 1\n'''
			self.NeurongroupingKwargVariablesDict['reset']='v=Vr*mV'
			#self.NeurongroupingKwargVariablesDict['reset']=setSpecificResetVariable
			self.NeurongroupingVariableStrToGetStrDict['Vr']='LifingResetVariable'

		#set
		self.NeurongroupingKwargVariablesDict['model']+='''
				dv/dt = (-(v+('''+self.LifedRestVariableStr+'''*mV))+11*mV)/('''+str(
						self.LifedConstantTimeVariableStr
						)+'''*ms) : volt
			'''

		

		
#</DefineClass>
