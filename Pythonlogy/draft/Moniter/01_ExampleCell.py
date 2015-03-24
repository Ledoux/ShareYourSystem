#ImportModules
import ShareYourSystem as SYS

#array
MyArray=SYS.numpy.array([
							[1,2,5,6],
							[3,5,7,8],
							[5,4,3,5]
						])

#Definition of a Moniter instance
MyMoniter=SYS.MoniterClass(
	).trace(
		MyArray
	).monit(
		[0,1],
		[1,2]
	)
		
#Define
print('MyMoniter is ')
SYS._print(MyMoniter)
