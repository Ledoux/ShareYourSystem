# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Lifer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Rebooter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<MakeSwig>
FolderString="/".join(__file__.split("/")[0:-1])
#SYS.os.popen("cd "+FolderString+";make")
#SYS.os.popen("cd "+FolderString)
#print(SYS.os.popen("ls").read())
#SYS.os.popen("make")
#</MakeSwig>

#<ImportSwig>
#SwigModuleString="C"+__file__.split("/")[-1].split(".")[0].split("Swig")[0]
SwigModuleString="CIntegrateAndFireTransferFunction"
SYS.sys.path.append(FolderString)
SYS.importlib.import_module(SwigModuleString)
#</ImportSwig>

#<DefineClass>
class Lifer(SYS.FunctorClass):

	#Definition
	RepresentingKeyStrsList=[
								'LifingMembraneConstantTimeFloat', 
								'LifingRefractoryPeriodFloat',
								'LifingTotalStationaryCurrentFloat', 
								'LifingVoltageNoiseFloat', 
								'LifingVoltageResetFloat', 
								'LifingVoltageThresholdFloat',
								'LifedStationaryRateFloat'
							]

	def default_init(
						self,
						_LifingMembraneConstantTimeFloat=0.02, 
						_LifingRefractoryPeriodFloat=0.,
						_LifingTotalStationaryCurrentFloat=-55., 
						_LifingVoltageNoiseFloat=5., 
						_LifingVoltageResetFloat=-70., 
						_LifingVoltageThresholdFloat=-50.,
						_LifedStationaryRateFloat=0.
					):

	
		map(
				lambda __KeyStr:
				'Lifing'.join(
					'Float'.join(__KeyStr.split('Float')[:-1]).split('Lifing')[1:]
				)
				self.__class__.DoingAttributeVariablesOrderedDict.keys()
			)

		self.LifTransferFunctorSwig=getattr(
			sys.modules[SwigModuleString],
			SwigModuleString+"Class"
		)()

	def do_lif(
		self,_TotalStationaryCurrentFloat):

		#Set inside the Swig
		self.LifTransferFunctorSwig.setDicts(
			*SYS.getCArgsFromDict(
				SYS.getFilterDictByType(**dict
					(
						
						[
							('MembraneConstantTime',self.LifingMembraneConstantTimeFloat),
							('RefractoryPeriod',self.LifingMembraneConstantTimeFloat) 
												self.LifingRefractoryPeriodFloat),
												self.LifingTotalStationaryCurrentFloat), 
												self.LifingVoltageNoiseFloat), 
												self.LifingVoltageResetFloat), 
												self.LifingVoltageThresholdFloat=-50. 


						]
						filter(
							lambda ItemTuple:
							ItemTuple[0] in [
												"MembraneConstantTime",
												"RefractoryPeriod",
												"VoltageNoise",
												"VoltageReset",
												"VoltageThreshold"
											],
							self.__dict__.items()
							)
					)
				)
			)
		)
		self.LifTransferFunctorSwig.DoubleDict["TotalStationaryCurrent"]=_TotalStationaryCurrentFloat;
		
		#Compute the IntegralLowerBound and the IntegralUpperBound
		self.LifTransferFunctorSwig.computeIntegralLowerBound();
		self.LifTransferFunctorSwig.computeIntegralUpperBound();
    	
		#Return
		return self.LifTransferFunctorSwig.getLIFStationaryRate();

#</DefineClass>

