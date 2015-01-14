

<!--
FrozenIsBool False
-->

View the Poker sources on [Github](https://github.com/Ledoux/ShareYourSystem/tre
e/master/ShareYourSystem/Applyiers/Installer)



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

MyPoker is < (PokerClass), 4550333776>
   /{
   /  '<New><Instance>IdInt' : 4550333776
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopPoker
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PokomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPoker' : < (PokerClass), 4550542032>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550542032
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4550333776>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550487600>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'SecondChildPoker' : < (PokerClass), 4550542160>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550542160
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4550333776>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550487600>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'ThirdChildPoker' : < (PokerClass), 4550542480>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550542480
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4550333776>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550487600>
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

