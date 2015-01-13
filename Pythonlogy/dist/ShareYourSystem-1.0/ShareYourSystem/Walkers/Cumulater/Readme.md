
#Cumulater
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Cumulater pick and





<!--
FrozenIsBool False
-->

View the Cumulater sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Walkers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater
import operator

#Definition a Filter instance that is grouped
MyCumulater=Cumulater.CumulaterClass().update(
        [
            (
                '<Filterome>FirstChildCumulater',
                Cumulater.CumulaterClass().update(
                    [
                        (
                            '<Filterome>GrandChildFilter',
                            Cumulater.CumulaterClass()
                        )
                    ]
                )
            ),
            (
                '<Filterome>SecondChildFilter',
                Cumulater.CumulaterClass()
            ),
            (
                '<Filterome>ThirdChildFilter',
                Cumulater.CumulaterClass()
            )
        ]
    )

#Walk inside the group in order to parent
MyCumulater.walk(
            {
                'BeforeUpdateList':
                [
                    (
                        'ConcludingConditionTuplesList',[
                            (
                                'NodeIndexInt',
                                lambda _TestInt,_AttestInt:
                                    operator.lt(_TestInt,_AttestInt) and
operator.lt(-1,_TestInt)
                                    if _TestInt!=None else False,
                                2
                            )
                        ]
                    ),
                    (
                        'PickingGetKeyVariablesList',['NodeKeyStr']
                    ),
                    ('cumulate',{'LiargVariablesList':[]})
                ],
                'GatherVariablesList':['<Filterome>']
            }
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyCumulater is '+SYS._str(
        MyCumulater,
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
Doer l.132 : DoerStr is Itemizer
DoStr is Itemize
DoMethodStr is itemize
DoingStr is Itemizing
DoneStr is Itemized

Doer l.132 : DoerStr is Getter
DoStr is Get
DoMethodStr is get
DoingStr is Getting
DoneStr is Getted

Doer l.132 : DoerStr is Setter
DoStr is Set
DoMethodStr is set
DoingStr is Setting
DoneStr is Setted

Doer l.132 : DoerStr is Deleter
DoStr is Delete
DoMethodStr is delete
DoingStr is Deleting
DoneStr is Deleted

Doer l.132 : DoerStr is Attributer
DoStr is Attribute
DoMethodStr is attribute
DoingStr is Attributing
DoneStr is Attributed

Doer l.132 : DoerStr is Restricter
DoStr is Restrict
DoMethodStr is restrict
DoingStr is Restricting
DoneStr is Restricted

Doer l.132 : DoerStr is Pather
DoStr is Path
DoMethodStr is path
DoingStr is Pathing
DoneStr is Pathed

Doer l.132 : DoerStr is Sharer
DoStr is Share
DoMethodStr is share
DoingStr is Sharing
DoneStr is Shared

Doer l.132 : DoerStr is Executer
DoStr is Execute
DoMethodStr is execute
DoingStr is Executing
DoneStr is Executed

Doer l.132 : DoerStr is Pointer
DoStr is Point
DoMethodStr is point
DoingStr is Pointing
DoneStr is Pointed

Doer l.132 : DoerStr is Applyier
DoStr is Apply
DoMethodStr is apply
DoingStr is Applying
DoneStr is Applied

Doer l.132 : DoerStr is Mapper
DoStr is Map
DoMethodStr is map
DoingStr is Mapping
DoneStr is Mapped

Doer l.132 : DoerStr is Picker
DoStr is Pick
DoMethodStr is pick
DoingStr is Picking
DoneStr is Pick

Doer l.132 : DoerStr is Gatherer
DoStr is Gather
DoMethodStr is gather
DoingStr is Gathering
DoneStr is Gathered

Doer l.132 : DoerStr is Updater
DoStr is Update
DoMethodStr is update
DoingStr is Updating
DoneStr is Updated

Doer l.132 : DoerStr is Filterer
DoStr is Filter
DoMethodStr is filter
DoingStr is Filtering
DoneStr is Filterer

Doer l.132 : DoerStr is Noder
DoStr is Node
DoMethodStr is node
DoingStr is Noding
DoneStr is Noded

Doer l.132 : DoerStr is Appender
DoStr is Append
DoMethodStr is append
DoingStr is Appending
DoneStr is Appended

Doer l.132 : DoerStr is Instancer
DoStr is Instance
DoMethodStr is instance
DoingStr is Instancing
DoneStr is Instanced

Doer l.132 : DoerStr is Adder
DoStr is Add
DoMethodStr is add
DoingStr is Adding
DoneStr is Added

Doer l.132 : DoerStr is Distinguisher
DoStr is Distinguish
DoMethodStr is distinguish
DoingStr is Distinguishing
DoneStr is Distinguished

Doer l.132 : DoerStr is Parenter
DoStr is Parent
DoMethodStr is parent
DoingStr is Parenting
DoneStr is Parented

Doer l.132 : DoerStr is Storer
DoStr is Store
DoMethodStr is store
DoingStr is Storing
DoneStr is Stored

Doer l.132 : DoerStr is Pusher
DoStr is Push
DoMethodStr is push
DoingStr is Pushing
DoneStr is Pushed

Doer l.132 : DoerStr is Producer
DoStr is Produce
DoMethodStr is produce
DoingStr is Producing
DoneStr is Produced

Doer l.132 : DoerStr is Catcher
DoStr is Catch
DoMethodStr is catch
DoingStr is Catching
DoneStr is Catched

Doer l.132 : DoerStr is Commander
DoStr is Command
DoMethodStr is command
DoingStr is Commanding
DoneStr is Commanded

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



*****Start of the Attest *****

MyCumulater is < (CumulaterClass), 4558051088>
   /{
   /  '<New><Instance>ApplyingIsBool' : False
   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildCumulater' : < (CumulaterClass), 4558889936>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildFilter' : < (CumulaterClass), 4558890896>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdString' : 4558890896
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildFilter
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(CumulaterClass), 4558889936>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4558902808>
   /   /   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4558889936
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildCumulater
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4558051088>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4558903104>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /  'SecondChildFilter' : < (CumulaterClass), 4558892368>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4558892368
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildFilter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4558051088>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4558903104>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /  'ThirdChildFilter' : < (CumulaterClass), 4558892624>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4558892624
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildFilter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4558051088>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4558903104>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /}
   /  '<New><Instance>IdString' : 4558051088
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>CumulatedVariablesList' :
   /   /[
   /   /  0 : None
   /   /  1 : ['FirstChildCumulater']
   /   /  2 : ['GrandChildFilter']
   /   /  3 : ['SecondChildFilter']
   /   /  4 : None
   /   /]
   /}

*****End of the Attest *****



```

