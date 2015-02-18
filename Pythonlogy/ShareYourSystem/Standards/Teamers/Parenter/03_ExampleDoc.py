#ImportModules
import ShareYourSystem as SYS

#
MyParenter=SYS.ParenterClass(
	).command(
		'/&Nodes/$First',
		[
			('point','<Teamer')
		]
	)


#.array(
#		[['&Nodes'],['$First','$Second']]
#	)

"""
	
"""

#print
print('MyParenter is ')
SYS._print(MyParenter)