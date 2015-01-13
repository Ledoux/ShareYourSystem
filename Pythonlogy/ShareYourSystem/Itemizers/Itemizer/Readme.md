
#Itemizer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Itemizer...





<!--
FrozenIsBool False
-->

View the Itemizer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Itemizers/Installer)




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Itemizer

class MakerClass(Itemizer.ItemizerClass):

    def __getitem__(self,_KeyVariable):

        #Debug
        print('_KeyVariable is ',_KeyVariable)
        print('')

        #return
        return object.__getattribute__(self,
                        'My'+str(_KeyVariable)+'Int'
                    )

#Definition of a derive maker itemizer class
MyMaker=MakerClass()
MyMaker.My1Int=1

#Definition the AttestedStr
SYS._attest(
    [
        'MyMaker is'+SYS._str(
            MyMaker,
            **{
                'RepresentingAlineaIsBool':False,
            }
        ),
        'MyMaker[1] is '+str(MyMaker[1]),
        #'MyMaker.Item_1 is '+str(MyMaker.Item_1),
    ]
)

#Print



```


```console
>>>
('_KeyVariable is ', 1)



*****Start of the Attest *****

MyMaker is< (MakerClass), 4465250256>
   /{
   /  '<New><Instance>IdString' : 4465250256
   /  '<New><Instance>My1Int' : 1
   /}

------

MyMaker[1] is 1

*****End of the Attest *****



```

