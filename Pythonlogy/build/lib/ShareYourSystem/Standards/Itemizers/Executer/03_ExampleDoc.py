
#ImportModules
import ShareYourSystem as SYS

#Definition and update with an exec Str
MyExecuter=SYS.ExecuterClass()

#print
print("MyExecuter['>>self.__dict__.keys()'] is ")
SYS._print(MyExecuter['>>self.__dict__.keys()'])
