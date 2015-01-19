#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Parenter

#Short expression and set in the appended manner
MyParenter=Parenter.ParenterClass().__setitem__(
	'<Tree>ChildParenter',
	Parenter.ParenterClass().__setitem__(
		'<Tree>GrandChildParenter',
		Parenter.ParenterClass()
	)
)

#Parent for the children
#MyParenter['<Tree>ChildParenter'].parent('Tree')
MyParenter['<Tree>ChildParenter']['<Tree>GrandChildParenter'].parent(['IdInt'])

#Definition the AttestedStr
SYS._attest(
	[
		'MyParenter is '+SYS._str(
		MyParenter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

