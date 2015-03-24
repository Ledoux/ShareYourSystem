
#ImportModules
import ShareYourSystem as SYS

#figure
MyPyploter=SYS.PyploterClass(
	).mapSet(
		{
			#'#plot':{
			#	'#liarg':[
			#		[1,2,3],
			#		[2,6,3]
			#	],
			#	'#kwarg':{
			#		'linestyle':"--"
			#	}
			#},
			'PyplotingDrawVariable':
			{
				'plot':{
					'#liarg':[
						[1,2,3],
						[2,6,3]
					],
					'#kwarg':{
						'linestyle':"--"
					}
				}
			}
		}
	).pyplot(
	)

#print
print('MyPyploter is ')
SYS._print(MyPyploter)

#show
SYS.matplotlib.pyplot.show()
