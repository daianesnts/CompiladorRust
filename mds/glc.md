# GLC da linguagem Rust
A seguinte gramática será utilizada para desenvolver o analisador sintático do compilador deste projeto. Terminais nesta gramática são consideradas quaisquer sequência de caractere em MAIÚSCULO ou que esteja entre aspas duplas (").

```
program → funcdecl | funcdecl program

funcdecl → signature body

signature → "fn" ID"("sigparams")" rettype

rettype → "->" TYPE | ε

sigparams → sigparam | ε

sigparam → ID":" TYPE | ID":" TYPE, sigparam

body → "{"stmts"}"

stmts → stm | stm stmts

stm → decl |
      exp |
      ifr |
      "loop" "{"stmts"}" |
      "while" exp "{"stmts"}"
      
ifr → ifri | ifrii

ifri → "if" exp "{"ifri"}" "else" "{"ifri"}"

ifrii → "if" exp "{"ifr"}" |
       "if" exp "{"ifri"}" "else" "{"ifrii"}"
       
decl → decllet | declmut | declcons | declexp

decllet → "let" IDtypedecl "=" exp";"

declmut → "let" "mut" IDtypedecl "=" exp";"

declcons → "const" ID":" TYPE "=" NUM";"

declexp → ID "=" exp";"

typedecl → ":" TYPE | ε

exp → exp "+" exp |
      exp "-" exp |
      exp "*" exp |
      exp "/" exp |
      exp "%" exp |
      call |
      "{"stmts exp"}"
      NUM |
      ID
      
call → ID"("params")" | ID"("")"

params → exp"," params | exp
```
