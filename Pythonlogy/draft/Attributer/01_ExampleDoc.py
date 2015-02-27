
#ImportModules
import ShareYourSystem as SYS

#define at the level of the class
SYS.AttributerClass.OneStr="hello"

#define and set with attr
MyAttributer=SYS.AttributerClass(
	)['#map@set'](
		{
			'<Instance>MyInt':0,
			'<Class>OurList':[5],
			'<Instance>OneStr':"bonjour"
		}
	)
		
#Definition the AttestedStr
print('MyAttributer is ')
SYS._print(MyAttributer)

#Check for the shared attributes
print('SYS.AttributerClass().OurList is ')
print(SYS.AttributerClass().OurList)

#get
print("MyAttributer['<Instance>OneStr']")
print(MyAttributer['<Instance>OneStr'])
print("MyAttributer['<Class>OneStr']")
print(MyAttributer['<Class>OneStr'])