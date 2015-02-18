
#ImportModules
import ShareYourSystem as SYS

#define and team
MyTeamer=SYS.TeamerClass()

#Note that just a get will create a Manager
print("MyTeamer['&Partners'] is ")
SYS._print(MyTeamer['&Partners'])

#Now build a longer Chain
MyTeamer['/&Clients/$First/&Banks/$Nef']

#print
print('MyTeamer is ')
SYS._print(MyTeamer)

