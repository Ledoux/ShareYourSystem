#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Appender,Instancer

#Append with a TuplesList
MyInstancer=Instancer.InstancerClass(**{'InstancingIsBool':True}).instance([
									('AppendingNodeCollectionStr','Structure'),
									('NodeKeyStr','MyInstancedAppender'),
									('MyStr','Hello'),
									('InstancingClass',Appender.AppenderClass)
								]
							)

#Definition the AttestedStr
SYS._attest(
	[
		'MyInstancer is '+SYS._str(
		MyInstancer,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
)  

#Print

