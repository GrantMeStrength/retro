# Rust Programming

Some notes on learning Rust.

## Variables and Consts

```
fn main() {
	// Comments are like this and /* */
	let x = 0;
	let y : u32 = 0;
	let z = “Hello”;
	const MYPI : f32 = 3.14159;
	let state = true; // 1
	x++; // Not allowed
}
```

## Datatypes

### Scalar types

|Datatype |Examples |
|-|-|
Integers |	 i32, i16, i8 and larger. Also u32, u16, u8
Floating point |	f32, f64
Boolean |	bool
Character	| char

### Compound types

tuple	

```
let tup1 = (1, true, 's');

let tup2 : (i32, bool, char) = (2, false, 't');

println!("{:?}", tup1);

println!("{}, {}", tup1.0, tup2.0);
```

### array	

```
let arr = [1,2,3,4];
let x = arr[1];
let mut arr2 : [i32; 5] = [1,2,3,4,5]; 
```

2D array	
```
let mut grid = [[0 as u8; 10] ; 10];
let mut array_2d: [[i32; 16]; 8];
grid[5][5] = 1;
println!("{:?}", grid);
```

## Logic

| Logic| Rust|
|--|--|
| And	| && |
| Or	| &#124;&#124; |
| Not	| ! |
| ==	| Equals |


```
if 2 < 3 {
	println!(“2 is less than 3”);
} else {
	println!(“Should not happen”);
}
```
## Casting
```
	let p  = (MYPI).round() as u16;
	let f = x as f32;

	// String to number
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let newNumber = input.trim().parse::<i32>().unwrap();
```


## Loops
```
fn main() {
	// Loop until condition
	loop {

		// keep looping until break; statement

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
