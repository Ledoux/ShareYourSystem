
#ImportModules
import ShareYourSystem as SYS

#Definition a Getter
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
MyGetter.MyStr="hello"
		
#print
print(
	'get ["MyInt","MyStr"] returns '+str(
		MyGetter.get(
			SYS.MapList(['MyInt','MyStr'])
		)
	)
)



