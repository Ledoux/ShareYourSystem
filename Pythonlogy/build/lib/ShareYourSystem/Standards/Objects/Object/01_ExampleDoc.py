
#ImportModules
import ShareYourSystem as SYS

#Need to define before either it is not setted
SYS.ObjectClass.MyInt=0

#Define an Object
MyObject=SYS.ObjectClass(**{'MyInt':4})
		
#print
print('MyObject is '+str(MyObject)) 

#print
print('MyObject.__dict__ is '+str(MyObject.__dict__)) 


