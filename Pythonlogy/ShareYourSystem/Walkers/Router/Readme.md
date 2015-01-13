
#Router
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Router




```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Router

#Definition a Router instance that has Tree nodes
MyRouter=Router.RouterClass().update(
    [
        (
            '<Tree>FirstChildRouter',
            Router.RouterClass().update(
                [
                    (
                        '<Tree>GrandChildRouter',
                        Router.RouterClass()
                    )
                ]
            )
        ),
        (
            '<Tree>SecondChildRouter',
            Router.RouterClass()
        )
    ]
)

#Walk inside the Tree in order to parent
MyRouter.walk(
    {
        'BeforeUpdateList':
        [
            ('route',{'LiargVariablesList':[
['NodedTreeInt','NodedTreeKeyStr']
                                                #['/']
                                            ]
                    })
        ],
        'GatherVariablesList':['<Tree>']
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyRouter is '+SYS._str(
        MyRouter,
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

MyRouter is < (RouterClass), 4558963472>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4558963472
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildRouter' : < (RouterClass), 4559176592>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4559176592
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildRouter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RouterClass),
4558963472>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4558904288>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildRouter' : < (RouterClass), 4558964240>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /  '<New><Instance>IdString' : 4558964240
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildRouter
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(RouterClass), 4559176592>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559020704>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' :
['NodedTreeInt', 'NodedTreeKeyStr']
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list),
4559144864>
   /   /   /}
   /   /  'SecondChildRouter' : < (RouterClass), 4559076432>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4559076432
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildRouter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RouterClass),
4558963472>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4558904288>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list),
4559144864>
   /   /   /}
   /   /}
   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /{
   /   /  'NodedTreeInt' : None
   /   /  'NodedTreeKeyStr' : None
   /   /  '0' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /  '1' :
   /   /   /   /{
   /   /   /   /  'NodedTreeInt' : None
   /   /   /   /  'NodedTreeKeyStr' : None
   /   /   /   /}
   /   /   /}
   /   /  '2' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list), 4559144864>
   /}

*****End of the Attest *****



```

