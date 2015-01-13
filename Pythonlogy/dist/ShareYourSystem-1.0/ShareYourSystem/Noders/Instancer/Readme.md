
#Instancer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeStr><AppendedNodeKeyStr>





<!--
FrozenIsBool False
-->

View the Instancer sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Noders/Installer)



```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Appender,Instancer

#Append with a TuplesList
MyInstancer=Instancer.InstancerClass(**{'InstancingIsBool':True}).instance([
                                    ('AppendingNodeCollectionStr','Structure'),
                                    ('NodeKeyStr','MyInstancedAppender'),
                                    ('MyStr','Hello'),
                                    ('InstancingClass',Appender.AppenderClass)
                                ]
                            )

#Definition the AttestedStr
SYS._attest(
    [
        'MyInstancer is '+SYS._str(
        MyInstancer,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyInstancer is < (InstancerClass), 4557295760>
   /{
   /  '<New><Instance>IdStr' : 4557295760
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>InstancingClass' : None
   /  '<Spe><Instance>InstancedVariable' : < (AppenderClass), 4567774480>
   /   /{
   /   /  '<New><Instance>AppendingNodeCollectionStr' : Structure
   /   /  '<New><Instance>IdStr' : 4567774480
   /   /  '<New><Instance>InstancingClass' : <class
'ShareYourSystem.Noders.Appender.AppenderClass'>
   /   /  '<New><Instance>MyStr' : Hello
   /   /  '<New><Instance>NodeCollectionStr' : Global
   /   /  '<New><Instance>NodeIndexInt' : -1
   /   /  '<New><Instance>NodeKeyStr' : MyInstancedAppender
   /   /  '<New><Instance>NodePointDeriveNoder' : None
   /   /  '<New><Instance>NodePointOrderedDict' : None
   /   /  '<Spe><Class>AppendedNodeCollectionStr' :
   /   /  '<Spe><Class>AppendedNodeKeyStr' :
   /   /  '<Spe><Class>AppendingCollectionVariable' : None
   /   /}
   /  '<Spe><Instance>InstancingIsBool' : True
   /  '<Spe><Instance>InstancingVariable' :
   /   /[
   /   /  0 : ('AppendingNodeCollectionStr', 'Structure')
   /   /  1 : ('NodeKeyStr', 'MyInstancedAppender')
   /   /  2 : ('MyStr', 'Hello')
   /   /  3 :
   /   /   /(
   /   /   /  0 : InstancingClass
   /   /   /  1 : {...}< (type), 140533544318528>
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

