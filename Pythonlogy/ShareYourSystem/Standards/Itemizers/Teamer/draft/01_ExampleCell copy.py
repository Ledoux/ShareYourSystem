
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Noders import Noder
		
#Definition a Noder
MyNoder=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Tree>FirstChildNoder']=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Tree>SecondChildNoder']=Noder.NoderClass()

#set with a deep short Str and append Str
MyNoder['<Tree>FirstChildNoder/MyStr']='bonjour'

#set with a deep deep short Str and append Str
MyNoder['/<Tree>FirstChildNoder/<Tree>GrandChildNoder']=Noder.NoderClass()

#Short expression and set in the appended manner
MyNoder.__setitem__('<Sort>MyInt',1)

#Short expression for setting in the append without binding
MyNoder['<Sort>MyInt']+=1

#Definition the AttestedStr
SYS._attest(
					[
						'MyNoder is '+str(
							Representer.represent(
								MyNoder,
								**{
								'RepresentingBaseKeyStrsListBool':False,
								'RepresentingAlineaIsBool':False
								}
							)
						)
					]
				) 

#Print
