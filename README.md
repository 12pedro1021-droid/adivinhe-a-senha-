# Adivinha Senha

Este é um jogo simples de terminal feito em Python. A ideia é descobrir uma
senha numérica secreta antes que as tentativas acabem.

## História

Você acorda dentro de uma sala digital trancada. Na porta existe um painel que
pede uma senha numérica. Para sair, você precisa testar seus palpites e prestar
atenção nas dicas do sistema.

## Objetivo

Descobrir a senha correta e desbloquear a porta usando no máximo 7 tentativas.

## Como executar

```bash
python main.py
```

## Como jogar

O jogo sorteia uma senha entre 1 e 100. A cada tentativa, ele informa se o seu
palpite foi muito alto, muito baixo ou se você acertou.

Se você digitar uma entrada inválida, como texto ou um número fora do intervalo,
o jogo avisa o erro e não desconta tentativa.

## Exemplo de partida

```text
=== Adivinha Senha ===
Voce acordou dentro de uma sala digital trancada.
No painel da porta existe uma senha numerica escondida.
Descubra a senha correta para desbloquear a saida.
A senha esta entre 1 e 100.
Voce tem 7 tentativas.
Digite sua tentativa: 50
Muito alto.
Tentativas restantes: 6
Digite sua tentativa: 25
Muito baixo.
Tentativas restantes: 5
Digite sua tentativa: 42
Acertou! A porta foi desbloqueada.
Voce precisou de 3 tentativa(s).
```

## Rodar testes

```bash
python -m unittest
```

## Estrutura do projeto

```text
.
├── main.py
├── test_main.py
├── README.md
└── LICENSE
```

## Conceitos praticados

- Entrada de dados
- Condicionais
- Laço de repetição
- Variáveis
- Funções
- Testes automatizados
