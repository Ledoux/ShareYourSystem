
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Sharer

#Explicit expression
MySharer=Sharer.SharerClass().__setitem__(
	'__class__.MyStr',
	'I am setted at the level of the class'
)

#Return
SYS._attest(
	[

		'MySharer is '+SYS._str(
				MySharer,
				**{
				'RepresentingBaseKeyStrsListBool':False
				}
			),
		'MySharer.__class__.MyStr is '+MySharer.__class__.MyStr,
		'MySharer["__class__.MyStr"] is '+MySharer['__class__.MyStr'],
	]
)

#Print

