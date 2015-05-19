
#/###################/#
# Import modules
#

#import
import ShareYourSystem as SYS

#define
MyLifer=SYS.LiferClass(
	).lif(
		_PerturbLambdaVariable=0.1+10.*1j
	)

#print
print('MyLifer is')
SYS._print(MyLifer)
