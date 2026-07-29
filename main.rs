static X: i32 = 31415;

fn main() {
	let mut a = 0;
	let x = 1;
	while a <= 5 {
		let x = 6;
		a = soma(a, x);
	}
	a = a - X;
	
	println("Print final");
}

fn soma(a: i32, b: i32) -> i32 {
	return a + b;
}
