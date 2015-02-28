#ImportModules
import ShareYourSystem as SYS
	
#Define
MyProcesser=SYS.ProcesserClass(
	).get(
		'$which python'
	)

#Define
print("MyProcesser['$which python '] is ")
SYS._print(MyProcesser['$which python '])
	
#get 
MyProcesser.get('$python&')

#print
print("SYS.Processer.status('Python')is ")
print(SYS.Processer.status('Python'))

#Define and kill all the python processes except itself
MyProcesser=SYS.ProcesserClass(
	).get(
		'$kill '+SYS.Processer.status(
					'Python',
					**{'PythonSkipSelfBool':True}
				)
		)