#<Import Modules>
import ShareYourSystem as SYS
#</Import Modules>


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
class LifTransferFunctorClass(SYS.FunctorClass):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDict>
		self.MembraneConstantTime=0.02 #(s)
		self.RefractoryPeriod=0. #(s)
		self.TotalStationaryCurrent=-55. #(mV)
		self.VoltageNoise=5. #(mV)
		self.VoltageReset=-70. #(mV)
		self.VoltageThreshold=-50. #(mV)
		self.LifTransferFunctorSwig=getattr(SYS.sys.modules[SwigModuleString],SwigModuleString+"Class")()
		self['LifFunctionTypeString']="CurrentToRate"
		#</DefineSpecificDict>

		#Don't repr the SeedInt because it is going to change for each test...
		self.__setitem__('+NotRepresentingGettingVariablesList',['LifTransferFunctorSwig'])

	#</DefineHookMethods>

	#<DefineBindingHookMethods>
	def bindLifFunctionTypeStringAfter(self):

		#Bind with unctedFunctionPointer setting
		self.setFunctingFunctionPointer()

	#</DefineBindingHookMethods>

	#<DefineMethods>
	def getStationaryRateFloatWithTotalStationaryCurrentFloat(self,_TotalStationaryCurrentFloat):

		#Set inside the Swig
		self.LifTransferFunctorSwig.setDicts(
			*SYS.getCArgsFromDict(
				SYS.getFilterDictByType(**dict
					(
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

	def setFunctingFunctionPointer(self):

		if self.LifFunctionTypeString=="CurrentToRate":
			self.FunctingFunctionPointer=self.getStationaryRateFloatWithTotalStationaryCurrentFloat
	#</DefineMethods>
#</DefineClass>

