#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Appender

#Append with a TuplesList
MyAppender=Appender.AppenderClass().append([
									('NodeCollectionStr','Tree'),
									('NodeKeyStr','MyTuplesList'),
									('MyStr','Hello')
								]
							)

#Append with a dict
MyAppender.append({
					'NodeCollectionStr':'Tree',
					'NodeKeyStr':'MyDict',
					'MyOtherStr':'Bonjour'
					}
				)

#Append with an instance
MyAppender.append(
					Appender.AppenderClass().update(
						[
							('NodeCollectionStr','Tree'),
							('NodeKeyStr','MyAppender')
						]
					)
				)

#Definition the AttestedStr
SYS._attest(
	[
		'MyAppender is '+SYS._str(
		MyAppender,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

