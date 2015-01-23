#<ImportModules>
import ShareYourSystem as SYS
#</ImportModules>

#<DefineTestClass>
class LifTransferFunctorTesterClass(SYS.TesterClass):
	
	def test_00_default(self):
		self.TestedVariable=self.TestedClass()

	def test_01_func(self):
		self.TestedVariable=self.TestedClass()('func',-55.)

#</DefineTestClass>

#<Test>

#Get the local test class and the tested method strings
TestedClass=filter(lambda Variable:type(Variable[1])==type,locals().items())[0][1]
MethodStringsList=SYS.getTestMethodStringsListWithClass(TestedClass)

#Write the solutions to the tests
SYS.sys.modules['os'].popen("cd "+TestedClass().TestingFolderPathString+";rm *")
TestedClass().apply('testify',MethodStringsList)

#Test
TestedClass().update([
						('IsPrintedBool',True),
						('TestingClass',SYS.TestClass)
					]
					).apply('bound',MethodStringsList)
class Test(SYS.TestClass):pass
SYS.sys.modules['unittest'].main()

#</Test>
