### 1. Elementos Sintáticos

Funções são amplamente utilizadas em Rust. Uma função Rust apresenta a seguinte sintaxe, declarada com a palavra-chave ***fn***:

`funcao -> "fn" ID "(" params ")" ["->" TIPO] "{" stmts "}"`

Onde ***ID*** representa o nome da função seguindo a convenção snake_case **(letras minúsculas separadas por underline)**. ***params*** representa os parâmetros da função, cada um obrigatoriamente anotado com seu tipo. O trecho opcional ***"->" TIPO*** indica o tipo do valor de retorno, quando omitido, a função não retorna um valor explícito. Por último, ***stmts***, que representa um ou mais comandos no corpo da função.

Uma função em Rust é composta por declarações **(statements)** e, opcionalmente, uma expressão final. A distinção é importante: declarações executam ações e não retornam valor (ex.: `let y = 6;`), enquanto expressões avaliam e retornam um valor (ex.: `x + 1`). Expressões não terminam com ponto e vírgula, já que adicioná-lo as converte em declarações, anulando o retorno.

Quanto ao valor de retorno, o Rust retorna implicitamente o valor da última expressão do corpo da função, sem necessidade da palavra-chave return. O tipo de retorno é declarado após uma seta `->`. Exemplo:

```
fn soma_um(x: i32) -> i32 {
    x + 1
}
```

## 1.1 Comandos da Linguagem Rust

Com relação aos comandos de controle de fluxo, Rust lida com o comando condicional ***if/else***, os comandos de repetição ***loop***, ***while*** e ***for*** conforme apresentado nas seguintes regras:

```
stm → "if" exp "{" stmts "}" [ "else" "{" stmts "}" ]
      | "loop" "{" stmts "}"
      | "while" exp "{" stmts "}"
      | "for" ID "in" iter "{" stmts "}"
```

O comando ***if*** inicia com a palavra reservada ***if***, seguida obrigatoriamente por uma expressão booleana, diferentemente de linguagens como **C** e **JavaScript**, Rust não converte automaticamente outros tipos em booleano, exigindo que a condição seja explicitamente do tipo bool. Em seguida, apresenta uma sequência de comandos envolvida por chaves. Opcionalmente, pode ser acompanhado da cláusula else, também envolvida por chaves, executada quando a condição é falsa. É possível encadear múltiplas condições através de ***else if***. Uma característica particular do Rust é que if é uma expressão, podendo ser usada do lado direito de uma declaração ***let***, desde que todos os ramos retornem valores do mesmo tipo.

O comando ***loop*** inicia com a palavra reservada ***loop***, seguida de uma sequência de comandos envolvida por chaves. Ele repete o bloco de código indefinidamente, até que uma instrução ***break*** seja encontrada explicitamente dentro do corpo do laço.

O comando ***while*** inicia com a palavra reservada ***while***, seguida por uma expressão booleana e, obrigatoriamente, uma sequência de comandos envolvida por chaves. O bloco é executado repetidamente enquanto a condição for verdadeira, e, ao tornar-se falsa, o laço é encerrado.

O comando ***for*** inicia com a palavra reservada ***for***, seguida por um identificador ***ID*** que representa a variável de iteração, a palavra reservada ***in***, e um iterador iter, que pode ser uma coleção, um intervalo **(Range)** ou qualquer tipo que implemente o protocolo de iteração do Rust. Em seguida, apresenta obrigatoriamente uma sequência de comandos envolvida por chaves. O laço ***for*** é preferido em Rust por ser mais seguro e conciso, eliminando o risco de acessos fora dos limites da coleção.

## 1.2 Expressões em Rust

Rust dá suporte a expressões aritméticas de adição, subtração, multiplicação, divisão e resto. Adicionalmente, também dá suporte a chamadas de função ***(call)***, blocos delimitados por chaves e literais numéricos. A sintaxe das expressões em Rust é apresentada pela seguinte regra:

```
exp → exp "+" exp
    | exp "-" exp
    | exp "*" exp
    | exp "/" exp
    | exp "%" exp
    | call
    | "{" stmts exp "}"
    | NUM
    | ID
```

As expressões aritméticas operam sobre valores numéricos e avaliam um resultado. Uma chamada de função **(call)**** é uma expressão e, portanto, também avalia o valor de retorno da função invocada. Um bloco **{ }** também é uma expressão: ele é composto por zero ou mais declarações seguidas de uma expressão final **(sem ponto e vírgula)**, cujo valor é o resultado avaliado pelo bloco inteiro. Por fim, expressões também podem ser literais numéricos **(NUM)** e identificadores de variáveis **(ID)**.

## 1.2.1 Chamadas de Função e Atribuição

Rust dá suporte a chamadas de função com e sem parâmetros. Um parâmetro de função deve ter seu tipo obrigatoriamente declarado na assinatura da função. Adicionalmente, quando há múltiplos parâmetros, eles são separados por vírgula. As regras para chamada de função e seus parâmetros são apresentadas a seguir:

```
call   → ID "(" params ")"
       | ID "(" ")"

params → exp "," params
       | exp

param_decl → ID ":" TIPO "," param_decl
           | ID ":" TIPO
```

Uma chamada de função **(call)** é composta pelo nome da função **(ID)** seguido de um par de parênteses. Quando a função possui parâmetros, eles são listados entre os parênteses **(params)**, onde cada argumento pode ser qualquer expressão válida em Rust. Quando não há parâmetros, os parênteses permanecem vazios.

Quanto à declaração dos parâmetros **(param_decl)**, diferentemente da chamada, cada parâmetro na definição da função exige que seu tipo seja anotado explicitamente na forma **ID : TIPO**. Essa é uma decisão deliberada do design do Rust: ao exigir a anotação de tipo na definição, o compilador raramente precisará inferi-la em outros pontos do código. Quando há múltiplos parâmetros, suas declarações são separadas por vírgula, e os tipos de cada parâmetro não precisam ser iguais entre si.

### Exemplos de Código

A seguir, alguns exemplos de códigos na linguagem Rust.

```
fn soma_parabola(a: i32, b: i32, c: i32) -> i32 {
    return a + b + c;
}
```

```
fn soma(a: i32, b: i32) -> i32 {
    let mut x = a;
    let mut y = b;
    x = 88 + 44;
    y = 70;
    soma_parabola(1, 2, 3);
    let mut c = 38;
    while c != 0 {
        c = c - 1;
        soma_parabola(5, 1, 0);
        while c != 0 {
            soma_parabola(5, 1, 1);
        }
    }
    return x + y;
}
```

```
fn soma_parabola_c(a: i32) -> i32 {
    return a;
}
```
