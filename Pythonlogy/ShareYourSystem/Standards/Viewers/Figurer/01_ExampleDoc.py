
#ImportModules
import ShareYourSystem as SYS

#figure
MyFigurer=SYS.FigurerClass(
	).array(
    [['-Panels'],['|A','|B'],['-Axes'],['|a','|b']]
  ).parent(
    _DownBool=True
  ).figure(
  ).view(
    #ViewingQtBool
    True,
    #ViewingMpld3Bool
    True
  )


