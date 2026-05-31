# GLC da linguagem Rust
A seguinte gramática será utilizada para desenvolver o analisador sintático do compilador deste projeto. Terminais nesta gramática são consideradas quaisquer sequência de caractere em MAIÚSCULO ou que esteja entre aspas duplas (").

```
#PROGRAMA

program  → topdecl | topdecl program

topdecl  → funcdecl | structdecl | traitdecl
```
```
#FUNÇÕES

funcdecl → signature body

signature → "fn" ID "(" sigparams ")" rettype

rettype → "->" TYPE | ε

sigparams → sigparam | ε

sigparam → ID ":" TYPE | ID ":" TYPE "," sigparam

body → "{" stmts "}"
```
```
#STRUCT E TRAIT

structdecl   → "struct" ID "{" structfields "}"

structfields → structfield | structfield "," structfields | ε

structfield  → ID ":" TYPE

traitdecl    → "trait" ID "{" traitbody "}"

traitbody    → signature ";" traitbody | ε
```
```
#COMANDOS

stmts → stm | stm stmts

stm → decl |
      exp ";" |
      ifr |
      "loop" "{" stmts "}" |
      "while" exp "{" stmts "}" |
      "return" exp ";" |
      "break" ";" |
      "continue" ";"

#IF ELSE

ifr → "if" exp "{" stmts "}" |
      "if" exp "{" stmts "}" "else" "{" stmts "}" |
      "if" exp "{" stmts "}" "else" ifr
```
```
#DECLARAÇÕES

decl → decllet | declmut | declcons | declexp

decllet → "let" ID typedecl "=" exp ";"

declmut → "let" "mut" ID typedecl "=" exp ";"

declcons → "const" ID ":" TYPE "=" NUM ";"

declexp → ID "=" exp ";"

typedecl → ":" TYPE | ε
```
```
#EXPRESSÕES

exp → exp_assign

exp_assign  → ID "=" exp_assign |
              ID "+=" exp_assign |
              ID "-=" exp_assign |
              ID "*=" exp_assign |
              ID "/=" exp_assign |
              exp_or

exp_or      → exp_or "||" exp_and | exp_and

exp_and     → exp_and "&&" exp_rel | exp_rel

exp_rel     → exp_bitor "==" exp_bitor |
              exp_bitor "!=" exp_bitor |
              exp_bitor "<"  exp_bitor |
              exp_bitor ">"  exp_bitor |
              exp_bitor "<=" exp_bitor |
              exp_bitor ">=" exp_bitor |
              exp_bitor

exp_bitor   → exp_bitor "|" exp_bitxor | exp_bitxor

exp_bitxor  → exp_bitxor "^" exp_bitand | exp_bitand

exp_bitand  → exp_bitand "&" exp_shift | exp_shift

exp_shift   → exp_shift "<<" exp_add | exp_shift ">>" exp_add | exp_add

exp_add     → exp_add "+" exp_mul | exp_add "-" exp_mul | exp_mul

exp_mul     → exp_mul "*" exp_unary |
              exp_mul "/" exp_unary |
              exp_mul "%" exp_unary |
              exp_unary

exp_unary   → "!" exp_unary | exp_primary

exp_primary → call |
              NUM | 
              ID |
              "true" |
              "false" |
              "(" exp ")" |
              "{" stmts exp "}" |
              "{" stmts "}"
```
```
#CHAMADAS DE FUNÇÃO
      
call → ID "(" params ")" | ID "(" ")"

params → exp "," params | exp

```
