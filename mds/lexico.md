# 🔐 Linguagem Rust - Elementos Léxicos

## 1. Introdução
A linguagem Rust é uma linguagem compilada e estaticamente tipada, desenvolvida com foco em desempenho, segurança de memória e confiabilidade. Para possibilitar a implementação de um compilador dentro do escopo acadêmico da disciplina, será definido um subconjunto da linguagem original, preservando suas principais características.

A análise léxica corresponde à primeira etapa do processo de compilação e tem como objetivo realizar a leitura do código-fonte, identificando e classificando os elementos da linguagem em tokens, que serão utilizados pelas etapas posteriores do compilador.

A seguir, são apresentados os principais elementos léxicos reconhecidos pelo compilador, incluindo palavras reservadas, identificadores, literais, operadores, delimitadores e comentários.

---

## 2. Palavras Reservadas

As listas a seguir contêm palavras reservadas para uso atual pela linguagem Rust. Como tal, elas não podem ser usadas como identificadores (exceto como identificadores brutos, conforme discutiremos na seção “Identificadores Brutos”). Identificadores são nomes de funções, variáveis, parâmetros, campos de estruturas, módulos, crates, constantes, macros, valores estáticos, atributos, tipos, traits ou tempos de vida (*lifetimes*).

**Palavras reservadas em uso**

Estas são as palavras-chave atualmente utilizadas pela linguagem, com suas respectivas funções:

| Palavra-chave | Descrição |
|:-------------:|-----------|
| `as` | Realiza casting primitivo, desambigua traits ou renomeia itens em `use`. |
| `break` | Sai de um loop imediatamente. |
| `const` | Define itens constantes ou ponteiros crus constantes. |
| `continue` | Avança para a próxima iteração do loop. |
| `else` | Fluxo de exceção para construções `if` e `if let`. |
| `enum` | Define uma enumeração. |
| `false` | Literal booleano falso. |
| `fn` | Define uma função ou o tipo de ponteiro de função. |
| `for` | Itera sobre itens, implementa uma trait ou especifica *higher ranked lifetimes*. |
| `if` | Ramifica a execução com base em uma condição. |
| `impl` | Implementa funcionalidades inerentes ou de traits. |
| `in` | Parte da sintaxe do loop `for`. |
| `let` | Vincula uma variável. |
| `loop` | Executa um loop incondicionalmente. |
| `mut` | Denota mutabilidade em referências, ponteiros ou vínculos de padrão. |
| `pub` | Denota visibilidade pública em campos, blocos `impl` ou módulos. |
| `ref` | Vincula por referência. |
| `return` | Retorna de uma função. |
| `Self` | Alias de tipo para o tipo que está sendo definido ou implementado. |
| `static` | Variável global ou tempo de vida que dura toda a execução do programa. |
| `struct` | Define uma estrutura. |
| `trait` | Define uma trait. |
| `true` | Literal booleano verdadeiro. |
| `union` | Define uma união (palavra-chave apenas quando usada em declarações `union`). |
| `unsafe` | Denota código, funções, traits ou implementações inseguras. |
| `where` | Denota cláusulas que restringem um tipo. |
| `while` | Executa um loop condicionalmente baseado em uma expressão. |

**Identificadores Brutos (Raw Identifiers)**

Identificadores brutos são a sintaxe que permite usar palavras-chave onde elas normalmente não seriam permitidas. Você utiliza um identificador bruto prefixando uma palavra-chave com `r#`.

Isso é útil, por exemplo, para manter a interoperabilidade com diferentes edições do Rust ou para usar nomes de variáveis que coincidam com palavras reservadas.

---

## 3. Operadores

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
| `!` | "NÃO" |
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

---

## 4. Delimitadores

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

## 5. Identificadores

Os identificadores são nomes criados pelos programadores para referenciar elementos do programa, tais como variáveis, funções, enums, structs, módulos e constantes. Para isso, é importante que o compilador reconheça e consiga distinguir das palavras reservadas da linguagem.

**Regras dos Identificadores:**
- Deve começar com letras[a-z, A-Z] ou underscore(_)
- Os caracteres podem ser seguidos de dígitos e underscore
- Não podem ser iguais às palavras reservadas
- São case-sensitive, a mesma palavra com letras maiúsculas e minúsculas diferentes, são identificadores diferentes
- underscore(_) solitário é válido, significa valor ignorado.

**Expressões regulares:**

Exemplo: `[a-zA-Z_][a-zA-Z0-9_]*`

Exemplos válidos: `x`, `nome`, `_valor`, `calcular_media`, `Pessoa`, `x1`

Exemplos inválidos: `1x`, `meu-nome`, `@var`, `let`

---

## 6. Palavras Literais

**Tipos Escalares**

Representam um único valor. Rust possui quatro tipos principais.

**A. Inteiros**
Números sem casas decimais.

| Tamanho | Com Sinal (`i`) | Sem Sinal (`u`) | Exemplo de Uso |
|:-------:|:-------------:|:-------------:|:--------------:|
| `8-bit` | `i8` | `u8` | Pequenos contadores |
| `16-bit` | `i16` | `u16` | Compatibilidade com sistemas legados |
| `32-bit` | `i32` | `u32` | Padrão do Rust (Equilíbrio de performance) |
| `64-bit` | `i64` | `u64` | Números grandes (ex: timestamps) |
| `128-bit` | `i128` | `u128` | Cálculos astronômicos ou criptográficos |
| `Dinâmico` | `isize` | `usize` | Tamanho da arquitetura (ponteiros/índices) |

**B. Outros Escalares**

| Tipo | Descrição | Tamanho / Exemplo |
|:------:|:---------:|:-----------------:|
| `f32` | Ponto Flutuante (Precisão simples) | `let x: f32 = 3.0;` |
| `f64` | Ponto Flutuante (Padrão, precisão dupla) | `let y = 2.0;` |
| `bool` | Booleano (Verdadeiro ou falso) | `true`, `false` (1 byte) |
| `char` | Caractere Unicode (4 bytes) | `'z'`, `'ℤ'`, `'😻'` |

**Tipos Compostos**
Agrupam múltiplos valores em uma única variável.

| Tipo | Homogeneidade | Tamanho | Acesso aos Elementos |
|:------:|:-------------:|:-------:|:--------------------:|
| `Tupla` | Pode conter tipos diferentes | Fixo | Por ponto (`tup.0`) ou desestruturação |
| `Matriz` | Apenas o mesmo tipo | Fixo | Por colchetes e índice (`a[0]`) |

**Inteiros Literais**
Formatos especiais para escrever números no código.

| Formato | Exemplo |
|:---------|:-------:|
| `Decimal` | `98_222` |
| `Hexadecimal` | `0xff` |
| `Octal` | `0o77` |
| `Binário` | `0b1111_0000` |
| `Byte (u8 apenas)` | `b'A'` |

**Diferenças: Array vs. Vetor**
Embora ambos armazenem dados do mesmo tipo, o Rust os trata de formas distintas:

| Característica | Matriz (*Array*) | Vetor (`Vec<T>`) |
|:----------------:|:--------------:|:--------------:|
| **Tamanho** | Fixo (Imutável após definição) | Dinâmico (Pode crescer/diminuir) |
| **Alocação** | Pilha (*Stack*) | Monte (*Heap*) |
| **Flexibilidade** | Baixa (Ideal para dados estáticos) | Alta (Mais comum no dia a dia) |

---

## 7. Comentários

Comentários são trechos do código-fonte ignorados pelo compilador. Eles existem para documentar e explicar o código para os programadores. O analisador léxico deve reconhecê-los e descartá-los, sem gerar tokens que cheguem ao analisador sintático.

**Tipos de comentários comuns:**
- Linha: `//texto até o fim da linha`
- Blocos: `/*Textos que podem ser multilinhas*/`

**Tipos de comentários de documentação:**
- Doc de item (linha): `///texto`
- Doc de item (Bloco): `/** texto*/`
- Doc de módulo (linha): `//!texto`
- Doc de módulo (Bloco): `/*!texto*/`

**Comportamento:**

Ao reconhecer a estrutura de um comentário, o compilador o ignora por completo, eliminando assim a criação de tokens a partir dele.

---

## 8. Erros Léxicos

Erros léxicos ocorrem quando o analisador léxico encontra símbolos ou sequências de caracteres que não pertencem às regras definidas pela linguagem.

Qualquer elemento que não possa ser reconhecido como identificador, palavra reservada, literal, operador, delimitador ou comentário válido será considerado um erro léxico.

Exemplos de erros léxicos:

| Exemplo | Motivo do erro |
|:-------:|----------------|
| `@variavel` | Símbolo @ inválido para identificadores |
| `12abc` | Identificador iniciado por número |
| `"texto` | String não finalizada |
| `'ab'` | Literal char com mais de um caractere |
| `~` | Símbolo não reconhecido pela linguagem |
| `!=>` | Operador inválido |

Comportamento do analisador léxico:
- Ao identificar um erro léxico, o compilador deve informar o símbolo inválido e a linha em que o erro ocorreu.
- Espaços em branco, tabulações e quebras de linha devem ser ignorados, exceto para controle de posicionamento e numeração de linhas.
- O analisador pode interromper a compilação ou continuar a análise para detectar múltiplos erros no código-fonte.
