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
		if y > 10 {
			x += 10;
		} else if j < 20 {
			y += 20;
		} else {
			j = j + 25 * x + 20;
		}
	}
	call();
	test += 10;
	test -= 10;
	test *= 10;
	test /= 10;
	/* fim do programa */
}

trait Describable {
	fn describe(name : i32) -> String;
	fn describe(nome: i32);
	fn describe(&self) -> String;
	fn descbrie(&self);
}