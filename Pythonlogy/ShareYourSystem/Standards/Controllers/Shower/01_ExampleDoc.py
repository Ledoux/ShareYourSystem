#ImportModules
import ShareYourSystem as SYS

#Define
MyShower=SYS.ShowerClass(
	).draw(
		{
			'|fig1':{
				'-Panels':{
					'|A':{
						'-Axes':[
								('ManagingBeforeSetVariable',{
									'FiguringShapeIntsTuple':(3,5)
								}),
								('|a',{
									'-Plots':[
										('|0',{
											'FiguringDrawVariable':
											[
												(
													'#plot',
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
											'FiguringDrawVariable':
											[
												(
													'#plot',
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
								})
							]
						}
					}
				}
			}
	).show(
	)

#print
print('MyShower is ')
SYS._print(MyShower)