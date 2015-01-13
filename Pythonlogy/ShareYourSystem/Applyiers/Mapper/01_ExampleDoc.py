
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Mapper

#Definition a Getter
MyMapper=Mapper.MapperClass().map(
	'__setitem__',
	[
		{'LiargVariablesList':['MyStr',"Hello"]},
		{'LiargVariablesList':['MyThirdStr',"GutenTag"]},
		{'LiargVariablesList':['map',
										{
											'LiargVariablesList':
											[
												'__setitem__',
												[
													{
														'LiargVariablesList':
														['MyInt',0]
													},
													{
														'LiargVariablesList':
														['MyFloat',0.1]
													}
												]
											]
										}
									
							]},
		{'LiargVariablesList':['MyNotLostStr',"ben he"]},
	]
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMapper is '+SYS._str(
		MyMapper,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
)  

#Print

