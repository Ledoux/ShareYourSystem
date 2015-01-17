

<!--
FrozenIsBool False
-->

#Poker

##Doc
----


>
> Poker instances
>
>

----

<small>
View the Poker notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyours
ystem.ouvaton.org/Poker.ipynb)
</small>




<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Poker instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Grabber"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PokerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'PokingNodeStr',
'PokingGetStrsList'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
                                                _PokingNodeStr="",
                                                _PokingGetStrsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
Joiner.JoinerClass.model}]})
        #@Argumenter.ArgumenterClass()
        def do_poke(self):

                #debug
                '''
                self.debug(('self.',self,['PokingNodeStr','PokingGetStrsList']))
                '''

                #Apply __getitem__
                self.map('couple',map(
                                                                        lambda
__PokingGetStr:
                                                                        {
'LiargVariablesList':
[
        self.PokingNodeStr,
        __PokingGetStr
]
                                                                        },
self.PokingGetStrsList
                                                                )
                                        )

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Poker sources on <a href="https://github.com/Ledoux/ShareYourSystem/tre
e/master/Pythonlogy/ShareYourSystem/Applyiers/Poker" target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Poker

#push
MyPoker=Poker.PokerClass().push(
    [
        [
            'FirstChild',
            Poker.PokerClass()
        ],
        [
            'SecondChild',
            Poker.PokerClass()
        ],
        [
            'ThirdChild',
            Poker.PokerClass()
        ]
    ],
    **{'CollectingCollectionStr':"Pokome"}
)


MyPoker['<Pokome>ThirdChildPoker'].poke(
        'Relatome',
        [
            '/NodePointDeriveNoder/<Pokome>FirstChildPoker',
            '/NodePointDeriveNoder/<Pokome>SecondChildPoker'
        ]
    )

#Definition the AttestedStr
SYS._attest(
    [
        'MyPoker is '+SYS._str(
        MyPoker,
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


*****Start of the Attest *****

MyPoker is < (PokerClass), 4555039632>
   /{
   /  '<New><Instance>IdInt' : 4555039632
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopPoker
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PokomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPoker' : < (PokerClass), 4556365072>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556365072
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4555039632>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378192>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'SecondChildPoker' : < (PokerClass), 4556365200>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556365200
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4555039632>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378192>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'ThirdChildPoker' : < (PokerClass), 4556365520>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556365520
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4555039632>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378192>
   /   /   /  '<Spe><Instance>PokingGetStrsList' :
['/NodePointDeriveNoder/<Pokome>FirstChildPoker',
'/NodePointDeriveNoder/<Pokome>SecondChildPoker']
   /   /   /  '<Spe><Instance>PokingNodeStr' : Relatome
   /   /   /}
   /   /}
   /  '<Spe><Class>PokingGetStrsList' : None
   /  '<Spe><Class>PokingNodeStr' :
   /}

*****End of the Attest *****



```

