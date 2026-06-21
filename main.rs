/*
Esta é a função main de um programa em rust.

OBS: O léxico ainda não está completo.
*/
struct User {
	username: String,
	email: String,
	sign_in_count: u64,
	active: bool
}


fn main() {
	let x = 67;	// Aqui é uma variável não mutável
	let mut y = 42; // Aqui é variável mutável
	
	while y < x && x >= y {
		y = y + 1;
	}
	call();
	test += 10;
	test -= 10;
	test *= 10;
	test /= 10;
	/* fim do programa */
}

trait Describable {
	fn describe(&self, name : i32) -> String;
}