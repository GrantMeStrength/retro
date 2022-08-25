# Rust Programming

Some notes on learning Rust, a strongly-typed compiled language designed to combine the speed and flexibility of C, with the memory-safety and convenience of Python. 

Useful summary video [here](https://youtu.be/zF34dRivLOw).

## Installing Rust

[Piece of cake](https://www.rust-lang.org/tools/install). A single command line operation for almost all OSs. If there is a scary looking error message when compilation is first attempted, maybe try ```xcode-select --install```.

## Cargo

While the Rust compiler is called **rustc** like this..

```
rustc my_rust_code.rs
```


..it is more usual to use the **cargo** command to compile, run and manage Rust programs (and packages, called 'crates'). For example, to create a new Rust project:

```
cargo new my_new_project
```

and to build and run it:

```
cd my_new_project
cargo run
```

**Note:** If you are using an IDE such as Visual Studio Code, there are ways to build and run within the editor with a few keypresses (Ctrl Alt N) or menu options.

## Printing

Use the println! macro to display to the terminal. You can optionally use positional arguments, and named arguments.

```
println!("This is a {} {}", "silly", "test");

println!("This is a {0} {1} {2} which is {0} {1}", "very", "silly", "test");

println!("This is a {adjective} {noun}", adjective="silly", noun="test");

println!("This is a binary number: {:b} and a hex number {:x}",240,15);

// And for debugging..

println!("{:?}", (1, true, "soup"));

```

## Rust source files

By convention, Rust source files end with the *.rs* suffix.

Rust uses { } to delimit blocks of code (like C, C++, C# and so on, and not idents with tabs or spaces Python-style). Semi-colons at the ends of lines are (almost always) required.

## Variables and Consts

```
fn main() {
	// Comments are defined like this or /* */
	let x = 0;
	let y : u32 = 0; // Explicit type
	let z = “Hello”;
	const MYPI : f32 = 3.14159; // Style says use caps
	let state = true; // 1 = true, 0 = false
	x++; // Not allowed ;-(
}
```

You can *shadow* a variable, by redefining it. Sounds a little risky, but it allows you to throw away the original definition. I imagine the intent is to make sure you don't *accidentally* use a variable with the same name, you really nuke the first version of it. You can also completely ignore the original variable type.

```
    let x = 2;
	let x = x + 1; // Before x is replaced, it's value is used
	println!("{}", x);
	let x = "monkey tennis";
	println!("{}", x);
```

## Common datatypes

### Scalar types

|Datatype |Examples |
|-|-|
Integers |	 i32, i16, i8 and larger. Also u32, u16, u8
Floating point |	f32, f64
Boolean |	bool
Character	| char

### Compound types

*Tuple*

```
let tup1 = (1, true, 's');
let tup2 : (i32, bool, char) = (2, false, 't');
println!("{:?}", tup1);
println!("{}, {}", tup1.0, tup2.0);

// Another way to extract values from a tuple
let (a,b,c) = tup1;
println!("{}, {}, {}", a, b, c);
```

*Array*	

```
// Arrays have a fixed number of elements
let arr = [1,2,3,4];
let x = arr[1];
let mut arr2 : [i32; 5] = [1,2,3,4,5]; 
```

*2D array*	
```
let mut grid = [[0 as u8; 10] ; 10];
let mut array_2d: [[i32; 16]; 8];
grid[5][5] = 1;
println!("{:?}", grid);
```

*Struct*

A new type made from existing types. There are several forms of *struct* definition.

```

fn main() {

	// Declare a classic Struct
	struct ComputerSpec {
    	name: String,
    	memory: u16,
    	functional: bool
	}

	// Declare a tuple struct
	struct Resolution(u16, u16, u8);

	// Create instances
	let pc = ComputerSpec {name: String::from("IBM"), memory:1024, functional:true};
	let monitor = Resolution(1024, 768,8);

	// Access members
	println!("{} {} {}",pc.name, pc.memory, pc.functional);
	println!("{} {} {}", monitor.0, monitor.1, monitor.2);

}

```


*Enum*
```
enum Soup {
	TomatoSoup,
	ChickenSoup,
}

fn main() {
	println!("{}", Soup::TomatoSoup as i32);
}
```


*Vector*

A **Vec()** is an array that can grow dynamically.

```
fn main() {
    
	let list = "\
	list, 4
	of, 2
	lots, 4
	of, 2
	words, 5
	separated, 8
	by, 2
	commas, 6";

	let words = list.lines();
	let mut myVec: Vec<_> = words.collect();
	
	myVec.push("soup, 4"); // Add new item
	myVec.push("bread, 5"); // Add new item
	myVec.pop(); // Remove last item

	for word in myVec {
		println!("{}", word);
	}
}
```
Here is how to iterate over a Vec.

```
fn main() {

	let mut letters = vec!["a", "b", "c"];
	letters.push("d");

	for alpha in letters {
		println!("{}", alpha);
	}	

}
```

## Logic

| Logic| Rust|
|--|--|
| And	| && |
| Or	| &#124;&#124; |
| Not	| ! |
| ==	| Equals |


```
if 2 < 3 && 3 > 2 {
	println!(“2 is less than 3”);
} else {
	println!(“Should not happen”);
}

```
There is an **else-if** structure too.


## Casting / type conversion

```
	let p  = (MYPI).round() as u16;
	let f = x as f32;

	// String to number
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let newNumber = input.trim().parse::<i32>().unwrap();
```


## Loops

The simplest loop will keep looping until you **break**. You cannot use **break** other than in a loop, by the way.

```
fn main() {
	// Loop until condition
	loop {

		// keep looping until break; statement

	}
}
```

You can return a value from a loop, because a Rust statement becomes an expression when you leave out the semi-colon (see *Functions*):

```
let result = loop {

	if some_contition {
		break 42
	}

}
```

There is also the ```while``` keyword:

```
let mut n = 2;

while n < 10 {
	println!("{}", n);
	n += 1;
}
```

Looping over items in an array is done like this:

```
fn main() {
	array = ["One", "Two", "Three"];

	for item in array.iter() {
		println!("{}", item); // Sometimes &item
	}
}
```

## Input

```
use std::io;

fn main() {
    println!("ok, say something: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    println!("ok, sure you entered {}", input);
}
```

## Functions

Every program has a main() function.

```
fn main() {
	// Execution starts here
}
```

Other functions in the same file can be defined before _or_ after they are referenced. A **return** keyword is not required in all case (don't use a semicolon if no return statement).

```
fn main() {
	let x = my_func1(42);
	let y = my_func2(42);

	println!("{} {}", x, y);
}

fn my_func1(x : i32) -> i32
{
	2 + x
}

fn my_func2(x : i32) -> i32
{
	return my_func1(x) + 1;
}

```

## Separating code over files

You can spread the code over multiple files. For example, add a new file called bob.rs:

```
// This is a file called bob.rs

pub fn otherFunction()
{
	// pub is essential
}
```

and then in main.rs:

```
// This is main.rs

mod bob;

fn main()
{
	bob::otherFunction();
}
```

To create variables that are "global", you don't use ```let``` but ```const``` or ```static``` like this:

```
// This is a file called bob.rs

static bobvar : UIn32 = 0;

pub fn otherFunction()
{
	// pub is essential
}
```
You can then access bobvar in other code. However, applying ```mut``` to make this a value that can be changed is deliberately difficult, requiring unsafe compilation and thread control: all to make it safer. The message is clear: don't use global variables if at all possible.


## Comparisons and Match 

### Match


The ```match``` keyword is like ```switch``` but (they say) is more powerful. It has a new syntax.

A convenient way to test a value, is to use ```Ordered``` which can be imported from the standard library (Note: Rust likes to stay small, so requires you to opt-in to things like this).

```
use std::cmp::Ordering;

fn main() {

    let x = 2;

	match x {
		1 => println!("one"),
		2 => {println!("two"); println!("I said 2")}, // Note: a block is required here
		3 => println!("three"),
		_ => println!("anything"),
	}

	match x.cmp(&2)  { // Note use of &
		Ordering::Less => println!("less than 2"), // Note ,
		Ordering::Greater => println!("greater than 2"),
		Ordering::Equal => println!("equal to 2"),
	}

}
```
### If 

```If``` statements work as you expect, although unlike some langauges, the condition being tested does not need to be contained in brackets.

``` 
let n = 2;

if n == 2 {
	println!("Yes, n is 2");
} else {
	println!("Weird - n is not 2");
}
```

Rememeber how leaving out a semicolon can return a value? You can use this to combine ```if``` and ```let``` in a neat way:

```
let m = if n == 2 {
	println!("Yes, n is 2 so make m true");
	true		// There is no ; so a value is returned
} else {
	println!("Weird - n is not 2 so make m false");
	false
};

println!("m is {}", m);

```

## Ownership

Rust does not have a garbage collector mechanism, but neither does it require you to remember to dealloc everything you do on the heap. Instead, it has a strict "out of scope? you're done!" approach to variables and other data that's on the heap.

Note: The *stack* is used by the compiler when passing values into functions, the *heap* is used when you declare new objects that are of user-defined size - like strings. Because using the heap requires work to find space and remember it, it can be an expensive operation.

Rust will, by default, do a shallow copy that is so shallow, it's really a *move*.

```
fn main() {

	// This works fine, as "Hello, world!" is a string literal
	let s1 = "Hello";
	let s2 = s1;

	println!("{}", s1);
	println!("{}", s2);

	// This doesn't work as s3 is allocated on the heap as a new object - it won't even compile because Rust knows s3 is invalid by the time it has to print it.

	let s3 = String::from("Hello");
	let s4 = s3;

	println!("{}", s3); // s3 is invalid by now.
	println!("{}", s4);

}
```

If you really want to copy s3 so that s3 is still valid, you need to *clone* it, like this:

```
let s4 = s3.clone();
```


