# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Predicter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Controllers.Systemer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineFunctions>
#</DefineFunctions>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
})
class PredicterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
						]

	def default_init(self,
						_PredictingDaleBool=False,
						_PredictingOnAndOffBool=False,
						_PredictingPrincAndAuxBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predict(self):	

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
									'SynapsingProbabilityVariable':0.02,
									'AttentionUpdateVariable':
									{
										'PostModelInsertStrsList':['dgi/dt = -gi/(10*ms) : volt'],
										'PostModelAddDict':{'v':['gi']}
									}
								}
							),
							SYS.GraspDictClass(
								{
									'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>'+'P'+'Neurongrouper',
									'SynapsingKwargVariablesDict':
									{
										'pre':'ge+=1.62*mV',
									},
									'SynapsingProbabilityVariable':0.02,
									'AttentionUpdateVariable':
									{
										'PostModelInsertStrsList':['dgi/dt = -gi/(10*ms) : volt'],
										'PostModelAddDict':{'v':['gi']}
									}
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
