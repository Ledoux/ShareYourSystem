/** This is a brief description of what's being documented.
  *
  * This is further documentation of what we're documenting.  It should
  * provide more details as to how this works and what it does. 
  */

package scala.Manager

import scala.Manager._

//<DefineClass>
class ManagerClass(
		//var ManagementMap : Option[ Map[String,ManagerClass] ] = None,
		var ManagementMap : Map[String,ManagerClass] = Map(),
		var ManagedParentVariable : Option[ManagerClass] = None
	){

	def team(
			ManagingKeyStr:String,
			ManagingValueVariable:ManagerClass
	)={

		//Debug
		println("We team here")
		println("ManagingKeyStr is "+ManagingKeyStr)
		println("ManagingValueVariable is "+ManagingValueVariable)
		println("ManagementMap is "+ManagementMap)
		
		//update
		ManagementMap += (ManagingKeyStr->ManagingValueVariable)

		//parent
		ManagingValueVariable.ManagedParentVariable=Some(this)

		//Debug
		println("In the end of team")
		println(ManagementMap)

	}

}
//</DefineClass>






