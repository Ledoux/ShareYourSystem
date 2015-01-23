
#ImportModules
import ShareYourSystem as SYS

#Definition of a MakerClass decorated by a DoerClass instance
@SYS.DoerClass()
class MakerClass(SYS.InitiatorClass):
	pass

#Definition of a derived BuilderClass decorated by a Deriver
@SYS.DeriverClass()
class BuilderClass(MakerClass):
	pass

#Print
#print('MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList))

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList)
	]
) 

#Print
