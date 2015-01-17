#<Import Modules>
import ShareYourSystem as SYS
#</Import Modules>

#SYS.sys.path.append("__file__")

#FolderString="/".join(__file__.split("/")[0:-1])
#print(FolderString)
#SYS.os.popen("cd "+FolderString+";make")
#SYS.os.popen("cd "+FolderString)
#print(SYS.os.popen("ls").read())
#SYS.os.popen("make")
#SwigModuleString="C"+__file__.split("/")[-1].split(".")[0].split("Swig")[0]
#SYS.sys.path.append(FolderString)
#SYS.importlib.import_module(SwigModuleString)
#print(SYS.sys.modules[SwigModuleString])

#<DefineClass>
class IntegrateAndFireTransferFunctionSwigClass(SYS.ObjectClass):

	#<DefineHookMethods>
	def initAfterBasesWithIntegrateAndFireTransferFunctionSwig(self):

		#<DefineSpecificDict>
		#</DefineSpecificDict>

		#Update the TypeStringToKeyStringsListDict
		self.TypeStringToKeyStringsListDict["IntegrateAndFireTransferFunctionSwig"]=[
												]
	#</DefineHookMethods>

	#<DefineBindingHookMethods>
	#</DefineBindingHookMethods>

	#<DefineMethods>
	#</DefineMethods>
#</DefineClass>

