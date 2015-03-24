
#ImportModules
import ShareYourSystem as SYS

#figure
MyPyploter=SYS.PyploterClass(
	).mapSet(
		{
			'-Panels':
			[
				('|A',
					{
						'-Charts':
						[
							('|a',{
								'-Draws':[
									('|0',{
										'PyplotingDrawVariable':
										[
											(
												'plot',
												{
													'#liarg':[
														[1,2,3],
														[2,6,3]
													],
													'#kwarg':{
														'linestyle':"",
														'marker':'o'
													}
												}
											)
										]
									}),
									('|1',{
										'PyplotingDrawVariable':
										[
											(
												'plot',
												{
													'#liarg':[
														[0,1,2],
														[2,3,4]
													],
													'#kwarg':{
														'linestyle':"--",
														'color':'r'
													}
												}
											)
										],
									})
								]
							}),
							('|b',{
								'-Draws':[
									('|0',{
										'PyplotingDrawVariable':
										[
											(
												'plot',
												{
													'#liarg':[
														[1,2,3],
														[2,6,3]
													],
													'#kwarg':{
														'linestyle':"",
														'marker':'o'
													}
												}
											)
										]
									})
								]
							})
						]
					}
				)
			]
		}
	).pyplot(
	)

#print
print('MyPyploter is ')
SYS._print(MyPyploter)

#show
SYS.matplotlib.pyplot.show()
