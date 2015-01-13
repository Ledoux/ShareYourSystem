
#Linker
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Linker maps a point





<!--
FrozenIsBool False
-->

View the Linker sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Applyiers/Installer)




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
from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Applyiers import Linker

#Update several things
MyLinker=Linker.LinkerClass().update(
    map(
            lambda __Int:
            (str(__Int)+'Pather',Pather.PatherClass()),
            xrange(3)
        )
)

#link
MyLinker.link(
        map(
                lambda __Int:
(str(__Int)+'Pather','/'+str(__Int-1)+'Pather/'+str(__Int)+'Pather')
                if __Int>0
                else
                (str(0)+'Pather','/2Pather/0Pather'),
                xrange(3)
            )
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyLinker is '+SYS._str(
        MyLinker,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Linker
DoStr is Link
DoMethodStr is link
DoingStr is Linking
DoneStr is Linked



*****Start of the Attest *****

MyLinker is < (LinkerClass), 4365180176>
   /{
   /  '<New><Instance>0Pather' : < (PatherClass), 4365180048>
   /   /{
   /   /  '<New><Instance>1Pather' : < (PatherClass), 4365179664>
   /   /   /{
   /   /   /  '<New><Instance>2Pather' : < (PatherClass), 4365180688>
   /   /   /   /{
   /   /   /   /  '<New><Instance>0Pather' : {...}< (PatherClass), 4365180048>
   /   /   /   /  '<New><Instance>IdString' : 4365180688
   /   /   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /   /   /  '<Spe><Class>PathingKeyStr' :
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4365179664
   /   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /   /  '<Spe><Class>PathingKeyStr' :
   /   /   /}
   /   /  '<New><Instance>IdString' : 4365180048
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>1Pather' : {...}< (PatherClass), 4365179664>
   /  '<New><Instance>2Pather' : {...}< (PatherClass), 4365180688>
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365180176
   /  '<Spe><Instance>LinkingPointListsList' :
   /   /[
   /   /  0 : ('0Pather', '/2Pather/0Pather')
   /   /  1 : ('1Pather', '/0Pather/1Pather')
   /   /  2 : ('2Pather', '/1Pather/2Pather')
   /   /]
   /}

*****End of the Attest *****



```

