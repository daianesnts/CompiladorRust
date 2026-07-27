# GLC da linguagem Rust
A seguinte gramática será utilizada para desenvolver o analisador sintático do compilador deste projeto. Terminais nesta gramática são consideradas quaisquer sequência de caractere em MAIÚSCULO ou que esteja entre aspas duplas (").

```
#PROGRAMA

program  → topdecl | topdecl program

topdecl  → funcdecl | structdecl | traitdecl | declstatic
```
```
#FUNÇÕES

funcdecl → signature body

signature → "fn" ID signaturei

signaturei → signaturep | signaturenp

signaturep → "(" sigparams ")" "->" TYPE | "(" sigparams ")" 

signaturenp → "(" ")" "->" TYPE | "(" ")"

sigparams → sigparam | sigparam "," sigparams

sigparam → ID ":" TYPE

body → "{" stmts "}"
```
```
#STRUCT E TRAIT

structdecl     → "struct" ID "{" structfields "}"

structfields   → structfield | structfield "," structfields

structfield    → ID ":" TYPE

traitdecl      → "trait" ID "{" traitbody "}"

traitbody      → traitsignatures | traitsignatures traitbody

traitsignatures → signature ";" | funcdecl | traitmethod

traitmethod    → "fn" ID traitsignature

traitsignature → traitsignaturep ";" | traitsignaturep body

traitsignaturep → traitsingleparam | traitmultiparam

traitsingleparam → "(" "&" "self" ")" | "(" "&" "self" ")" "->" TYPE

traitmultiparam → "(" "&" "self" "," sigparams ")" | "(" "&" "self" "," sigparams ")" "->" TYPE
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

declcons → "const" ID ":" TYPE "=" exp ";"

declstatic → "static" ID ":" TYPE "=" exp ";" 

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

exp_unary   → "!" exp_unary | "-" exp_unary | exp_primary

exp_primary → call |
              NUM |
              STRING |
              ID |
              "true" |
              "false" |
              "(" exp ")" |
              "{" stmts exp "}" |
              "{" stmts "}"
```
```
#CHAMADAS DE FUNÇÃO
      
call → ID "(" args ")" | ID "(" ")"

args → exp "," args | exp

```
```
# OBTENÇÃO DE TIPO

type → ID
```