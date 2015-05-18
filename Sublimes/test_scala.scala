#!/bin/sh
exec scala "$0" "$@"
!#
class HelloWorld {
	def main(args: Array[String]) {
		println("Hello, world! " + args.toList)
	}
}
new HelloWorld().main(Array("And you","And you ! "))

