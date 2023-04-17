package content

import "fmt"

func declaring() {
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

	fmt.Printf("%v, %T", i, i)
	fmt.Printf("%v, %T", j, j)
	fmt.Printf("%v, %T", k, k)
	fmt.Printf("%v, %T", l, l)

	fmt.Printf("%v, %T", a, a)
	fmt.Printf("%v, %T", b, b)
	fmt.Printf("%v, %T", c, c)
	fmt.Printf("%v, %T", d, d)

}
