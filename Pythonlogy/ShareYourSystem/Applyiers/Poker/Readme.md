
#Poker
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Poker instances





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
Doer l.132 : DoerStr is Walker
DoStr is Walk
DoMethodStr is walk
DoingStr is Walking
DoneStr is Walked

Doer l.132 : DoerStr is Cumulater
DoStr is Cumulate
DoMethodStr is cumulate
DoingStr is Cumulating
DoneStr is Cumulated

Doer l.132 : DoerStr is Visiter
DoStr is Visit
DoMethodStr is visit
DoingStr is Visiting
DoneStr is Visited

Doer l.132 : DoerStr is Recruiter
DoStr is Recruit
DoMethodStr is recruit
DoingStr is Recruiting
DoneStr is Recruit

Doer l.132 : DoerStr is Mobilizer
DoStr is Mobilize
DoMethodStr is mobilize
DoingStr is Mobilizing
DoneStr is Mobilized

Doer l.132 : DoerStr is Router
DoStr is Route
DoMethodStr is route
DoingStr is Routing
DoneStr is Routed

Doer l.132 : DoerStr is Grabber
DoStr is Grab
DoMethodStr is grab
DoingStr is Grabbing
DoneStr is Grabbed

Doer l.132 : DoerStr is Poker
DoStr is Poke
DoMethodStr is poke
DoingStr is Poking
DoneStr is Poked



*****Start of the Attest *****

MyPoker is < (PokerClass), 4365222032>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365222032
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PokomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPoker' : < (PokerClass), 4365385040>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4365385040
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4365222032>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365456920>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'SecondChildPoker' : < (PokerClass), 4365385360>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4365385360
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4365222032>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365456920>
   /   /   /  '<Spe><Class>PokingGetStrsList' : None
   /   /   /  '<Spe><Class>PokingNodeStr' :
   /   /   /}
   /   /  'ThirdChildPoker' : < (PokerClass), 4365484816>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4365484816
   /   /   /  '<New><Instance>NodeCollectionStr' : Pokome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildPoker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PokerClass),
4365222032>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365456920>
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

