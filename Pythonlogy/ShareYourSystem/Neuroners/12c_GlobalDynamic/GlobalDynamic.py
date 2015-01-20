#<Import Modules>
import ShareYourSystem as SYS
#</Import Modules>

#<DefineClass>
class GlobalDynamicClass(SYS.ObjectClass):

	#<DefineHookMethods>
	def initAfter(self):

		#<DefineSpecificDict>
		self.PitchInt=0
		self.ConnectivityMatrix=SYS.MatrixClass();
		self.MembraneTimeConstantFloat=0.
		self.PulsationFloat=0.
		self.SynapticDelayFloat=0.
		self.PerturbativeCoefficientFloat=0.
		#</DefineSpecificDict>
		
	#</DefineHookMethods>

	#<DefineBindingHookMethods>
	#</DefineBindingHookMethods>

	#<DefineMethods>
	#</DefineMethods>
#</DefineClass>

