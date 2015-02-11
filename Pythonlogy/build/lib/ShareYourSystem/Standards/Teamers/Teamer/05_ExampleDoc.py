
#ImportModules
import ShareYourSystem as SYS

#define and team
MyTeamer=SYS.TeamerClass()

#Build a longer Chain
MyTeamer['/*Clients/$First/*Banks/$Nef']

#print
print("MyTeamer['/*Clients/$First/<Manager'] is ")
SYS._print(MyTeamer['/*Clients/$First/<Manager'])

#print
print("MyTeamer['/*Clients/$First/<Teamer'] is ")
SYS._print(MyTeamer['/*Clients/$First/<Teamer'])

#print
print("MyTeamer['/*Clients/$First/*Banks/<Teamer'] is ")
SYS._print(MyTeamer['/*Clients/$First/*Banks/<Teamer'])

