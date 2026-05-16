/*
Esta é a função main de um programa em rust.

OBS: O léxico ainda não está completo.
*/
fn main() {
	let x = 67;	// Aqui é uma variável não mutável
	let mut y = 42; // Aqui é variável mutável
	
	while y < x && x >= y {
		y = y + 1;
	}
	/* fim do programa */
}