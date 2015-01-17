#<ImportModules>
import ShareYourSystem as SYS
#</ImportModules>

#<MakeSwig>
FolderString="/".join(__file__.split("/")[0:-1])
#print(FolderString)
#SYS.os.popen("cd "+FolderString+";make")
#SYS.os.popen("cd "+FolderString)
#print(SYS.os.popen("ls").read())
#SYS.os.popen("make")
#</MakeSwig>

#<ImportSwig>
SwigModuleString="C"+__file__.split("/")[-1].split(".")[0].split("Swig")[0]
#SYS.sys.path.append(FolderString)
#SYS.importlib.import_module(SwigModuleString)
#print(SYS.sys.modules[SwigModuleString])
#</ImportSwig>

#<DefineFunction>
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
#<DefineFunction>

#<DefineClass>
class SwigClass(SYS.ObjectClass):

	#<DefineHookMethods>
	pass
	#</DefineHookMethods>

	#<DefineBindingHookMethods>
	#</DefineBindingHookMethods>

	#<DefineMethods>
	#</DefineMethods>
#</DefineClass>

