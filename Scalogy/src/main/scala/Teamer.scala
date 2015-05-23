/** This is a brief description of what's being documented.
  *
  * This is further documentation of what we're documenting.  It should
  * provide more details as to how this works and what it does. 
  */

package scala.Teamer

//<DefineClass>
class TeamerClass(
		//var TeamMap : Option[ Map[String,TeamerClass] ] = None,
		var TeamMap : Map[String,TeamerClass] = Map(),
		var TeamedParentVariable : Option[TeamerClass] = None
	){

	def team(
			TeamingKeyStr:String,
			TeamingValueVariable:TeamerClass
	)={

		//Debug
		println("We team here")
		println("TeamingKeyStr is "+TeamingKeyStr)
		println("TeamingValueVariable is "+TeamingValueVariable)
		println("TeamMap is "+TeamMap)
		
		//update
		TeamMap += (TeamingKeyStr->TeamingValueVariable)

		//parent
		TeamingValueVariable.TeamedParentVariable=Some(this)

		//Debug
		println("In the end of team")
		println(TeamMap)

	}

}
//</DefineClass>






