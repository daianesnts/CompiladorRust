# 🪙 Linguagem Rust - Elementos Léxicos

#### 1. Identificadores

Os identificadores são nomes criados pelos programadores para referenciar elementos do programa, tais como variaveis, funções, enums, structs, módulos e constantes. Para isso, é importante que o compilador reconheça e consiga destinguir das palavras reservadas da linguagem.

**Regras dos Identificadores:**
- Deve começar com letras[a-z, A-Z] ou underscore(_)
- Os caractes podem ser seguidos de digitos e underscore
- Não podem ser iguais as palavras reservadas
- São case-sensitive, a mesma palavra com letras maiuscula e minuscula diferentes, são identificadores diferentes
- underscore(_) solitário é valido, significa valor ignorado.

**Expressões regulares:**

Exemplo: `[a-zA-Z_][a-zA-Z0-9_]*`

Exemplos válidos: `x`, `nome`, `_valor`, `calcular_media`, `Pessoa`, `x1`

Exemplos inválidos: `1x`, `meu-nome`, `@var`, `let`

---

#### 2. Comentários

Comentários são trechos do código-fonte ignorados pelo compilador. Eles existem para documentar e explicar o código para os programadores. O analisador léxico deve reconhecê-los e descartá-los, sem gerar tokens que cheguem ao analisador sintático.

**Tipos de comentários comuns:**
- Linha: `//texto até o fim da linha`
- Blocos: `/*Textos que podem ser multilinhas*/`

**Tipos de comentários de documentação:**
- Doc de item (linha): `///texto`
- Doc de item (Bloco): `/** texto*/`
- Doc de modulo (linha): `//!texto`
- Doc de modulo (Bloco): `/*!texto*/`

**Comportamento:**

Ao reconhecer a estrutura de um comentário, o compilador o ignora por completo, eliminando assim a criação de tokens a partir dele.

---

#### 3. Delimitadores

Os delimitadores são símbolos utilizados para estruturar e organizar o código-fonte da linguagem, separando expressões, parâmetros e blocos de comandos. O analisador léxico deve reconhecê-los e gerar os tokens correspondentes.

**Tipos de delimitadores:**

| Símbolo | Descrição |
|:-------:|-----------|
| `{ }` | Delimitação de blocos |
| `( )` | Agrupamento de expressões e parâmetros |
| `[ ]` | Vetores e índices |
| `;` | Finalização de instruções |
| `,` | Separação de parâmetros |
| `:` | Associação de identificador e tipo |
| `::` | Acesso a módulos e namespaces |

---

#### 4. Operadores

Os operadores são símbolos responsáveis por realizar operações aritméticas, lógicas, relacionais e de atribuição entre valores.

**Tipos de operadores aritméticos:**

| Operador | Operação |
|:--------:|----------|
| `+` | Soma |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `%` | Resto da divisão |

**Tipos de operadores relacionais:**

| Operador | Operação |
|:--------:|----------|
| `==` | Igualdade |
| `!=` | Diferença |
| `<` | Menor que |
| `>` | Maior que |
| `<=` | Menor ou igual |
| `>=` | Maior ou igual |

**Tipos de operadores lógicos:**

| Operador | Operação |
|:--------:|----------|
| `&&` | "E" |
| `\|\|` | "OU" |
| `!` | "NÃO" |

**Tipos de operadores de atribuição:**

| Operador | Operação |
|:--------:|----------|
| `=` | Atribuição simples |
| `+=` | Atribuição com adição |
| `-=` | Atribuição com subtração |
| `*=` | Atribuição com multiplicação |
| `/=` | Atribuição com divisão |

**Tipos de operadores bit a bit:**

| Operador | Operação |
|:--------:|----------|
| `&` | "E" |
| `\|` | "OU" |
| `^` | "OU exclusivo" |
| `!` | "NOT" |
| `<<` | Deslocamento à esquerda |
| `>>` | Deslocamento à direita |

**Precedência de operadores:**

| Grau | Operador(es) | Associatividade |
|:----:|:------------:|:---------------:|
| 1 | `=` `+=` `-=` `*=` `/=` | Direita para esquerda |
| 2 | `\|\|` | Esquerda para direita |
| 3 | `&&` | Esquerda para direita |
| 4 | `==` `!=` `<` `>` `<=` `>=` | Sem associatividade |
| 5 | `\|` | Esquerda para direita |
| 6 | `^` | Esquerda para direita |
| 7 | `&` | Esquerda para direita |
| 8 | `<<` `>>` | Esquerda para direita |
| 9 | `+` `-` | Esquerda para direita |
| 10 | `*` `/` `%` | Esquerda para direita |
| 11 | `!` | Direita para esquerda |

**Comportamento do analisador léxico:**
- Operadores compostos como `==` e `+=` devem ser reconhecidos antes dos simples, evitando que `==` seja tokenizado como dois `=` separados.
- A distinção entre `!` lógico e `!` bit a bit é resolvida pelo analisador sintático, o léxico gera o mesmo token para ambos os casos.

#### 5. Palavras reservadas.

As listas a seguir contêm palavras reservadas para uso atual pela linguagem Rust. Como tal, elas não podem ser usadas como identificadores (exceto como identificadores brutos, conforme discutiremos na seção “Identificadores Brutos”). Identificadores são nomes de funções, variáveis, parâmetros, campos de estruturas, módulos, crates, constantes, macros, valores estáticos, atributos, tipos, traits ou tempos de vida (lifetimes).

**Palavras reservadas em Uso**

Estas são as palavras-chave atualmente utilizadas pela linguagem, com suas respectivas funções:

| Palavra-chave | Descrição |
|:-------------:|-----------|

| `as` | Realiza casting primitivo, desambigua traits ou renomeia itens em use. |
| `async` | Retorna um Future em vez de bloquear a thread atual. |
| `await` |Suspende a execução até que o resultado de um Future esteja pronto. |
| `break` | Sai de um loop imediatamente. |
| `const` | Define itens constantes ou ponteiros crus constantes. |
| continue | Avança para a próxima iteração do loop. |
| `crate` | Em um caminho de módulo, refere-se à raiz da crate. |
| `dyn` | Despacho dinâmico para um objeto de trait. |
| `else` | Fluxo de exceção para construções if e if let. |
| `enum` | Define uma enumeração. |
| `extern` | Vincula uma função ou variável externa. |
| `false` | Literal booleano falso. |
| `fn` | Define uma função ou o tipo de ponteiro de função. |
| `for` | Itera sobre itens, implementa uma trait ou especifica higher ranked lifetimes. |
| `if` | Ramifica a execução com base em uma condição. |
| `impl` | Implementa funcionalidades inerentes ou de traits. |
| `in` | Parte da sintaxe do loop for. |
| `let` |Vincula uma variável. |
| `loop` | Executa um loop incondicionalmente. |
| `match` | Associa um valor a padrões (patterns) |
| `mod` | Define um módulo. |
| `move` | Faz com que um fechamento (closure) tome posse de suas capturas.|
| `mut` | Denota mutabilidade em referências, ponteiros ou vínculos de padrão. |
| `pub` | Denota visibilidade pública em campos, blocos impl ou módulos. |
| `ref` | Vincula por referência. |
| `return` | Retorna de uma função. |
| `Self` | Alias de tipo para o tipo que está sendo definido ou implementado. |
| `self` | Assunto do método ou módulo atual. |
| `static` | Variável global ou tempo de vida que dura toda a execução do programa. |
| `struct` | Define uma estrutura. |
| `super` | Módulo pai do módulo atual. |
| `trait` | Define uma trait. |
| `true` | Literal booleano verdadeiro. |
| `type` | Define um alias de tipo ou tipo associado. |
| `union` | Define uma união (palavra-chave apenas quando usada em declarações union). |
| `unsafe` | Denota código, funções, traits ou implementações inseguras. |
| `use` | Traz símbolos para o escopo. |
| `where` | Denota cláusulas que restringem um tipo. |
| `while` | Executa um loop condicionalmente baseado em uma expressão. |


**Identificadores Brutos (Raw Identifiers)**

Identificadores brutos são a sintaxe que permite usar palavras-chave onde elas normalmente não seriam permitidas. Você utiliza um identificador bruto prefixando uma palavra-chave com r#.

Isso é útil, por exemplo, para manter a interoperabilidade com diferentes edições do Rust ou para usar nomes de variáveis que coincidam com palavras reservadas.