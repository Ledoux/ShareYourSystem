
#ImportModules
import ShareYourSystem as SYS

#init
MyListDict=SYS.ListDict()

#update
MyListDict.update(
	[
		('MyInt',66),
		('MyDict',{'n':22})
	]
)

#insert
MyListDict.insert(1,'salut')
MyListDict.insert(1,'bonjour','MyStr')

#print
print('MyListDict is ')
print(MyListDict)