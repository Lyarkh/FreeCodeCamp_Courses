package main

import "fmt"

func main() {
	// Criando variável indicando o valor
	var i int = 42
	var j float32 = 10.
	var k float64 = 20.
	var l string = "foo"

	// inferencia de variável
	a := 42
	b := 10.
	c := 20.
	d := "foo"

	fmt.Printf("%v, %T\n", i, i)
	fmt.Printf("%v, %T\n", j, j)
	fmt.Printf("%v, %T\n", k, k)
	fmt.Printf("%v, %T\n", l, l)

	fmt.Printf("%v, %T\n", a, a)
	fmt.Printf("%v, %T\n", b, b)
	fmt.Printf("%v, %T\n", c, c)
	fmt.Printf("%v, %T\n", d, d)

}
