
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
														[0,1,2]
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
														[2,1,0]
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
								'PyplotingShiftVariable':[2,0],
								'-Draws':[
									('|0',{
										'PyplotingDrawVariable':
										[
											(
												'plot',
												{
													'#liarg':[
														[1,2,3],
														[1,1,1]
													],
													'#kwarg':{
														'linestyle':"-",
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
				),
				('|B',
					{
						'PyplotingShiftVariable':[2,0],
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
														[-1,2,-2]
													],
													'#kwarg':{
														'linestyle':"-",
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
				),
				('|C',
					{
						'PyplotingShiftVariable':["top",3],
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
														[4,2,4]
													],
													'#kwarg':{
														'linestyle':"-",
														'marker':'o'
													}
												}
											)
										]
									})
								]
							}),('|b',{
								'-Draws':[
									('|0',{
										'PyplotingDrawVariable':
										[
											(
												'plot',
												{
													'#liarg':[
														[1,2,3],
														[0,10,1]
													],
													'#kwarg':{
														'linestyle':"-",
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


"""

"""

"""

"""