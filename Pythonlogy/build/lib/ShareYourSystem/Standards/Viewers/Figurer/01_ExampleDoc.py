
#ImportModules
import ShareYourSystem as SYS

#figure
MyFigurer=SYS.FigurerClass(
	).array(
    [['-Panels'],['|A','|B'],['-Axes'],['/|a/?^','/|b/?']]
  )

"""
  .figure(
  ).view(
    #ViewingQtBool
    True,
    #ViewingMpld3Bool
    True
  )
"""

#print
print('MyFigurer is ')
SYS._print(MyFigurer)

