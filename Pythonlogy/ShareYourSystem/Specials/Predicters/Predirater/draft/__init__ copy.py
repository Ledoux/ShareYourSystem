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
BaseModuleStr="ShareYourSystem.Specials.Predicters.Predisenser"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Predirater','Predirate','Predirating','Predirated')
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getThresholdArray(_Variable,_ThresholdFloat=1.):

	#Check
	if type(_Variable) in [np.float64,float,int]:

		#return
		return max(
				min(
					_Variable,
					_ThresholdFloat
					),
				-_ThresholdFloat
			)
	else:

		#return
		return map(
			lambda __ElementVariable:
			getThresholdArray(
				__ElementVariable,
				_ThresholdFloat=_ThresholdFloat
			),
			_Variable
		)
SYS.getThresholdArray=getThresholdArray
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PrediraterClass(BaseClass):
	
	def default_init(self,

						_PrediratingTransferVariable=np.tanh,
						_PrediratingMonitorIntsList=None,
											
						_PrediratedInitialRateFloatsArray=None,
						
						_PrediratedPerturbativeUnitTraceFloatsArray=None,
						_PrediratedExactUnitTraceFloatsArray=None,
						_PrediratedControlUnitTraceFloatsArray=None,
						
						_PrediratedPerturbativeDecoderTraceFloatsArray=None,
						_PrediratedExactDecoderTraceFloatsArray=None,
						_PrediratedControlDecoderTraceFloatsArray=None,

						_PredirateColorDict=None,

						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predirate(self):

		
		#/#################/#
		# Prepare the initial conditions
		#

		#random sensors
		PrediratedInitialRateFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredictingUnitsInt
		)

		#/#################/#
		# Shape the size of all the unit traces
		#

		#init perturbative rates
		self.PrediratedPerturbativeUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedPerturbativeUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init exact rates
		self.PrediratedExactUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedExactUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init leak control rates
		self.PrediratedControlUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedControlUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#/#################/#
		# Shape the size of all the decoder traces
		#

		#init perturbative decoder
		self.PrediratedPerturbativeDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedPerturbativeDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#init exact decoder
		self.PrediratedExactDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedExactDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#init leak control decoder
		self.PrediratedControlDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PredisensedTimeTraceFloatsArray))
			)
		self.PrediratedControlDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedControlDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#/#################/#
		# integrativ Loop
		#

		#for loop
		for __IndexInt in xrange(1,len(self.PredisensedTimeTraceFloatsArray)):

			"""
			#/#################/#
			# Perturbative Rate
			#

			#Input Current
			PrediratedPerturbativeUnitCurrentFloatsArray=np.dot(
				self.PredictedTotalPerturbativeInputWeigthFloatsArray,
				self.PredisensedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedPerturbativeUnitCurrentFloatsArray-=np.dot(
				self.PredictedTotalPerturbativeLateralWeigthFloatsArray,
				self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
			)

			#transfer
			PrediratedPerturbativeUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedPerturbativeUnitCurrentFloatsArray
			)

			#Leak and Cost Current (non transfered)
			PrediratedPerturbativeUnitCurrentFloatsArray-=np.dot(
				self.PredictedLeakWeigthFloatsArray,
				self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
			)
			"""

			#/#################/#
			# Exact Rate 
			#

			#Input Current
			PrediratedExactUnitCurrentFloatsArray=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray.T,
				self.PredisensedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedExactUnitCurrentFloatsArray-=np.dot(
				self.PredictedLeakExactLateralWeigthFloatsArray,
				self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#transfer
			PrediratedExactUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedExactUnitCurrentFloatsArray
			)

			#Leak Current (non transfered)
			PrediratedExactUnitCurrentFloatsArray-=np.dot(
				self.PredictedLeakWeigthFloatsArray,
				self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#debug
			self.debug(
					'PrediratedExactUnitCurrentFloatsArray is '
				)

			#/#################/#
			# Control Rate
			#

			#Input Current
			PrediratedControlUnitCurrentFloatsArray=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray.T,
				self.PredisensedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#transfer
			PrediratedControlUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedControlUnitCurrentFloatsArray
			)

			#Leal Current
			PrediratedControlUnitCurrentFloatsArray-=np.dot(
				self.PredictedLeakWeigthFloatsArray,
				self.PrediratedControlUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#/#################/#
			# Euler part
			#

			#set
			LocalDict=locals()

			#rate
			for __TagStr in [
								#'Perturbative',
								'Exact',
								'Control'
							]:	

				#set
				getattr(
					self,
					'Predirated'+__TagStr+'UnitTraceFloatsArray'
				)[:,__IndexInt]=getattr(
							self,
							'Predirated'+__TagStr+'UnitTraceFloatsArray'
						)[:,__IndexInt-1]+LocalDict[
				'Predirated'+__TagStr+'UnitCurrentFloatsArray'
				]*self.PredisensingStepTimeFloat
					

			#/#################/#
			# Post process part
			#

			"""
			#Saturate
			self.PrediratedPerturbativeUnitTraceFloatsArray[
				np.where(
					self.PrediratedPerturbativeUnitTraceFloatsArray[
							:,
							__IndexInt
						]>10.
				)
			]=10.
			self.PrediratedPerturbativeUnitTraceFloatsArray[
				np.where(
					self.PrediratedPerturbativeUnitTraceFloatsArray[
							:,
							__IndexInt
						]<-10.
				)
			]=-10.
			"""

			#/#################/#
			# Decoder part
			#

			#dot
			self.PrediratedPerturbativeDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedExactDecoderWeigthFloatsArray,
					self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
				)

			#exact control
			self.PrediratedExactDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedExactDecoderWeigthFloatsArray,
					self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
				)

			#leak control
			self.PrediratedControlDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedControlDecoderWeigthFloatsArray,
					self.PrediratedControlUnitTraceFloatsArray[:,__IndexInt-1]
				)

	def mimic_draw(self):

		#/#################/#
		# First call the base method
		#

		BaseClass.draw(self)

		#/#################/#
		# Build the colors
		#

		self.PredirateControlColorTuplesList=SYS.getColorTuplesList(
			'black','yellow',len(self.PrediratingMonitorIntsList)+3,_PlotBool=False
		)[3:]
		self.PredirateExactColorTuplesList=SYS.getColorTuplesList(
			'black','blue',len(self.PrediratingMonitorIntsList)+3,_PlotBool=False
		)[3:]
		self.PrediratePerturbativeColorTuplesList=SYS.getColorTuplesList(
			'black','red',len(self.PrediratingMonitorIntsList)+3,_PlotBool=False
		)[3:]

		#debug
		'''
		self.debug(
				[
					'We have built the colors',
					('self.',self,['PrediratePerturbativeColorTuplesList'])
				]
			)
		'''

		#/#################/#
		# Build the input-unit traces axes
		#

		#debug
		self.debug(
				[
					('self.',self,['PredisensingMonitorIntsList'])
				]
			)

		#get
		self['/-Views/|A/-Axes'].set(
			'|Unit',
			{
				'-Plots':{
					'#map@set':map(
						lambda __IntsTuple:
						(
							'|'+str(__IntsTuple[0]),
							{
								'FiguringDrawVariable':
								[
									('#plot',
										{
											'#liarg:#map@get':[
												'PredisensedTimeTraceFloatsArray',
												'>>self.PrediratedControlUnitTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
											],
											'#kwarg':{
												'label':'$r_{'+str(__IntsTuple[1])+'}^{control}$',
												'linestyle':'-',
												'linewidth':1,
												'color':self.PredirateControlColorTuplesList[__IntsTuple[0]]
											}
										}
									),
									('#plot',
										{
											'#liarg:#map@get':[
												'PredisensedTimeTraceFloatsArray',
												'>>self.PrediratedExactUnitTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
											],
											'#kwarg':{
												'label':'$r_{'+str(__IntsTuple[1])+'}^{exact}$',
												'linestyle':'-',
												'linewidth':2,
												'color':self.PredirateExactColorTuplesList[__IntsTuple[0]],
											
											}
										}
									),
									#('#plot',
									#	{
									#		'#liarg:#map@get':[
									#			'PredisensedTimeTraceFloatsArray',
									#			'>>self.PrediratedPerturbativeUnitTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
									#		],
									#		'#kwarg':{
									#			'label':'$r_{'+str(__IntsTuple[1])+'}^{perturb}$',
									#			'linestyle':'-',
									#			'linewidth':4,
									#			'color':self.PrediratePerturbativeColorTuplesList[__IntsTuple[0]]
									#		
									#		}
									#	}
									#)
								]
							}
						),
						enumerate(self.PrediratingMonitorIntsList)
					)	
				},
				'FiguringDrawVariable.extend':
				[[
					('#axes',
						[
							('set_ylabel','$r(t)$'),
							('set_ylim',{
								'#liarg:#map@get':[
									">>SYS.set(SYS,'RateLimFloatsArray',"+"".join([
										"[max(-20.,self.PrediratedControlUnitTraceFloatsArray.min()),"
										"min(20.,self.PrediratedControlUnitTraceFloatsArray.max())]"
										])+').RateLimFloatsArray'
								]
							}),
							('set_yticks',{
								'#liarg:#map@get':[
									"".join(
										[
											">>SYS.set(SYS,'RateTickFloatsArray',"
											"map(lambda __Float:float('%.2f'%__Float),",
											"SYS.getTickFloatsArray(SYS.RateLimFloatsArray,3))",
											").RateTickFloatsArray"
										]
									)
								]
							}),
							('set_yticklabels',{
								'#liarg:#map@get':[
									">>map(lambda __Float:'$'+str(__Float)+'$',SYS.RateTickFloatsArray)"
								]
							}),
							('tick_params',{
								'#kwarg':{
									'length':10,
									'width':5,
									'which':'major'
								}
							}),
							('tick_params',{
								'#kwarg':{
									'length':5,
									'width':2,
									'which':'minor'
								}
							}),
							('xaxis.set_ticks_position',
								{
									'#liarg':['bottom']
								}
							),
							('yaxis.set_ticks_position',
								{
									'#liarg':['left']
								}
							),
							('legend',{
										'#liarg':[],
										'#kwarg':{
											'fontsize':10,
											'shadow':True,
											'fancybox':True,
											'ncol':len(self.PrediratingMonitorIntsList),
											'loc':2,
											'bbox_to_anchor':(1.05, 1)
										}
									})
						]
					)
				]]
			}
		)

		#get
		self['/-Views/|A/-Axes'].set(
			'|Decoder',
			{
			'-Plots':{
					'#map@set':map(
						lambda __IntsTuple:
						(
							'|'+str(__IntsTuple[0]),
							{
								'FiguringDrawVariable':
								[
									('#plot',
										{
											'#liarg:#map@get':[
												'PredisensedTimeTraceFloatsArray',
												'>>self.PredisensedSensorTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
											],
											'#kwarg':{
												'label':'$x_{'+str(__IntsTuple[1])+'}$',
												'linestyle':'-',
												'linewidth':1,
												'color':self.PredisenseSensorColorTuplesList[__IntsTuple[0]]
											}
										}
									),
									('#plot',
										{
											'#liarg:#map@get':[
												'PredisensedTimeTraceFloatsArray',
												'>>self.PrediratedControlDecoderTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
											],
											'#kwarg':{
												'label':'$\hat{x}_{'+str(__IntsTuple[1])+'}^{control}$',
												'linestyle':'--',
												'linewidth':1,
												'color':self.PredisenseSensorColorTuplesList[__IntsTuple[0]],
											
											}
										}
									),
									('#plot',
										{
											'#liarg:#map@get':[
												'PredisensedTimeTraceFloatsArray',
												'>>self.PrediratedExactDecoderTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
											],
											'#kwarg':{
												'label':'$\hat{x}_{'+str(__IntsTuple[1])+'}^{exact}$',
												'linestyle':'--',
												'linewidth':2,
												'color':self.PredisenseSensorColorTuplesList[__IntsTuple[0]],
											
											}
										}
									),
									#('#plot',
									#	{
									#		'#liarg:#map@get':[
									#			'PredisensedTimeTraceFloatsArray',
									#			'>>self.PrediratedPerturbativDecoderTraceFloatsArray[\''+str(__IntsTuple[1])+'\']'
									#		],
									#		'#kwarg':{
									#			'label':'$\hat{x}_{'+str(__IntsTuple[1])+'}^{perturb}$',
									#			'linestyle':'--',
									#			'linewidth':4,
									#			'color':self.PredisenseSensorColorTuplesList[__IntsTuple[0]],
									#		
									#		}
									#	}
									#)
								]
							}
						),
						enumerate(self.PredisensingMonitorIntsList)
					)	
				},
				'FiguringDrawVariable.extend':
				[[
					(
						'#axes',
						[
							('set_ylabel','$x(t),\ \hat{x}(t)$'),
							('set_ylim',{
								'#liarg:#map@get':[
									">>SYS.set(SYS,'DecoderLimFloatsArray',"+"".join([
										"[max(0.,self.PrediratedControlDecoderTraceFloatsArray.min()),"
										"min(5.,self.PrediratedControlDecoderTraceFloatsArray.max())]"
										])+').DecoderLimFloatsArray'
								]
							}),
							('set_yticks',{
								'#liarg:#map@get':[
									"".join(
										[
											">>SYS.set(SYS,'DecoderTickFloatsArray',"
											"map(lambda __Float:float('%.2f'%__Float),",
											"SYS.getTickFloatsArray(SYS.DecoderLimFloatsArray,3))",
											").DecoderTickFloatsArray"
										]
									)
								]
							}),
							('set_yticklabels',{
								'#liarg:#map@get':[
									">>map(lambda __Float:'$'+str(__Float)+'$',SYS.DecoderTickFloatsArray)"
								]
							}),
							('tick_params',{
								'#kwarg':{
									'length':10,
									'width':5,
									'which':'major'
								}
							}),
							('tick_params',{
								'#kwarg':{
									'length':5,
									'width':2,
									'which':'minor'
								}
							}),
							('xaxis.set_ticks_position',
								{
									'#liarg':['bottom']
								}
							),
							('yaxis.set_ticks_position',
								{
									'#liarg':['left']
								}
							),
							('legend',{
										'#liarg':[],
										'#kwarg':{
											'fontsize':10,
											'shadow':True,
											'fancybox':True,
											'ncol':len(self.PredisensingMonitorIntsList),
											'loc':2,
											'bbox_to_anchor':(1.05, 1)
										}
									})
						]
					)
				]]
			}
		)	

	def prediplot(self):

		#/#################/#
		# Plot
		#

		#debug
		self.debug(
			[
				'len(self.PredisensedTimeTraceFloatsArray) is '+str(len(self.PredisensedTimeTraceFloatsArray)),
				'np.shape(self.PrediratedCommandFloatsArray) is '+str(np.shape(self.PrediratedCommandFloatsArray))
			]
		)

		#/#################/#
		# rates
		#

		#subplot
		PrediratedRateAxis=pyplot.subplot(3,1,2)

		#perturbative
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedPerturbativeUnitTraceFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedExactUnitTraceFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PrediratedPerturbativeUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedControlUnitTraceFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedControlUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedRateAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedRateAxis.set_ylim(
			[
				max(-10.,self.PrediratedPerturbativeUnitTraceFloatsArray.min()),
				min(10.,self.PrediratedPerturbativeUnitTraceFloatsArray.max())
			]
		)

		#/#################/#
		# decoders
		#

		#subplot
		PrediratedDecoderAxis=pyplot.subplot(3,1,3)

		#sensor
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PredisensedSensorTraceFloatsArray[__IndexInt],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PredisensedSensorTraceFloatsArray)
				else None,
				[0,1]
			)

		#perturbative
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedPerturbativeDecoderTraceFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedExactDecoderTraceFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PredisensedTimeTraceFloatsArray,
						self.PrediratedControlDecoderTraceFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedControlDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedDecoderAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedDecoderAxis.set_ylim([-0.1,1.5*self.PrediratingClampFloat])

		#show
		pyplot.show()



#</DefineClass>

#</DefinePrint>
PrediraterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PrediratingTransferVariable',
		'PrediratingMonitorIntsList',
		
		'PredisensedTimeTraceFloatsArray',
		'PrediratedCommandFloatsArray',

		'PrediratedInitialSensorFloatsArray',
		'PrediratedInitialRateFloatsArray',
		
		'PredisensedSensorTraceFloatsArray',
		'PrediratedPerturbativeUnitTraceFloatsArray',
		'PrediratedExactUnitTraceFloatsArray',
		'PrediratedControlUnitTraceFloatsArray',
		
		'PrediratedPerturbativeDecoderTraceFloatsArray',
		'PrediratedExactDecoderTraceFloatsArray',
		'PrediratedControlDecoderTraceFloatsArray',

		'PredirateControlColorTuplesList',
		'PredirateExactColorTuplesList',
		'PrediratePerturbativeColorTuplesList'
	]
)
#<DefinePrint>


"""

"""