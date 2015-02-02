# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Predispiker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Brianer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
from ShareYourSystem.Specials.Simulaters import Neurongrouper,Synapser
import operator
#</ImportSpecificModules>

#<DefineFunctions>
#</DefineFunctions>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
})
class PredispikerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
						]

	def default_init(self,
						_PredictedDerivePredicterVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#
		self.collect(
				'Components',
				'Lifer',
				SYS.LiferClass()
			)


	def do_predispike(self):	

		#Check
		if hasattr(self,'NodePointDeriveNoder'):

			#debug
			self.debug(
				[
					#('self.',self,['NodePointDeriveNoder']),
				]
			)

			#point
			self.point(
				self.NodePointDeriveNoder,
				'PredictedDerivePredicterVariable'
			)

		else:

			#point
			self.point(
				SYS.PredicterClass(),
				'PredictedDerivePredicterVariable'
			)


		#Definition
		self.produce(
				"Neurongroupers",
				['P'],
				SYS.NeurongrouperClass,
				#Here are defined the brian classic shared arguments for each pop
				{
					'NeurongroupingKwargVariablesDict':
					{
						'model':
						'''
							dv/dt = (-(v+'''+self.LifingRestFloat+'''*mV))/('''+self.LifingConstantTimeFloat+'''*ms) : volt
							dge/dt = -ge/(5*ms) : volt
							dgi/dt = -gi/(10*ms) : volt
						''',
						'threshold':'v>'+self.LifingThresholdFloat+'*mV',
						'reset':'v='+self.LifingResetFloat+'*mV'
					},
					'produce':
					SYS.ApplyDictClass(
						{
							'LiargVariablesList':
								[
									"SpikeMoniters",
									['Spike'],
									SYS.MoniterClass
								]
						}
					)		
				}
			).__setitem__(
				'Dis_<Neurongroupers>',
				#Here are defined the brian classic specific arguments for each pop
				[
					{
						'PopulatingUnitsInt':3200,
						'ConnectingGraspClueVariablesList':
						[
							SYS.GraspDictClass(
								{
									'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>'+'P'+'Neurongrouper',
									'SynapsingKwargVariablesDict':
									{
										'pre':'ge+=1.62*mV',
									},
									'SynapsingProbabilityVariable':0.02
								}
							),
							SYS.GraspDictClass(
								{
									'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>'+'P'+'Neurongrouper',
									'SynapsingKwargVariablesDict':
									{
										'pre':'ge+=1.62*mV',
									},
									'SynapsingProbabilityVariable':0.02
								}
							)
						]
					},
				]
			).network(
					**{
						'RecruitingConcludeConditionTuplesList':[
							(
								'MroClassesList',
								operator.contains,
								SYS.NeurongrouperClass
							)
						]
					}
				).brian()
		
#</DefineClass>
