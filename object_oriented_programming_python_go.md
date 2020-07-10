# Object-Oriented Programming in Go and Python

## Table of Contents

- Object-Oriented Programming
- Benefits of OOP
- Syntax Differences Between Go and Python
- Functional Differences Between Go and Python

## Object-Oriented Programming

Object-Oriented Programming (OOP) is a software development paradigm where objects are
constructed with a defined set of associated characteristics and actions. The actions
of an object, called methods, are used to modify the object's characteristics, called
attributes. This structure limits the functionality of a given object, and is in contrast
to procedural programming, where variables flow through the code and are modified by any
function desired and expanded to include any attributes desired.

## Benefits of OOP

This constraining structure standardizes common code elements to facilitate efficient
replication of these objects as a software project expands. A generalized template, called
a class, defines the attributes and methods for a type of object. When a new object is
instantiated within a class, it contains the attributes common to the class and may be
modified by the methods associated with the class.

## Syntax Differences Between Go and Python

Go and Python provide different syntaxes for OOP, but the fundimental concept remains the
the same. In Go the class is defined as a high-level type, and methods are added outside
of the type declaration. In the following example, a type `car` is defined as a `struct`
containing the attributes `make` and `mileage`.

```go
type car struct {
	make string
	mileage int
}
```

Methods can be added by designating the type before the method name.

```go
func (c car) addMile() {
	c.mileage++
}
```

A class and its attributes and methods can exported (made accessable outside of the file they
are defined in) by capitalizing the first letter of their names. Now a `car` object can be
instantiated.

```go
myCar := car{
		make: "Ford",
		mileage: 50000,
}
```


