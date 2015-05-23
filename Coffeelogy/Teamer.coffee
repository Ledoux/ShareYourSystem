$ = require 'jquery'

jsdom = require "jsdom"

class Animal
  price: 5

  sell: =>
    alert "Give me #{@price} shillings!"

animal = new Animal

