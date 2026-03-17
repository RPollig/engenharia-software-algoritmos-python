Lista de Exercícios: Algoritmos de Busca em Python
PARTE 1 – Busca Sequencial
(Percorre o vetor do início ao fim – O(n))
1. Básico
Escreva uma função busca_sequencial(lista, alvo) que retorna o índice da primeira ocorrência
do alvo na lista. Se não encontrar, retorne -1.
2. Contagem de ocorrências
Modifique a função anterior para retornar quantas vezes o alvo aparece na lista (retorne 0 se
não existir).
3. Menor índice
Dada uma lista de números, encontre o índice do menor valor usando apenas busca
sequencial (sem usar min()).
4. Busca em lista de strings
Crie uma função que recebe uma lista de nomes e um nome alvo. Retorne o índice (caseinsensitive).
5. Busca com condição
Em uma lista de dicionários [{"nome": "João", "idade": 25}, ...], encontre o primeiro aluno com
idade ≥ 18 e retorne o nome.
6. Busca em matriz (2D)
Dada uma matriz 3x3, use busca sequencial para encontrar se um número existe e retorne a
posição (linha, coluna) ou (-1, -1).
7. Busca com limite
Encontre o primeiro número maior que 50 em uma lista de 100 elementos aleatórios. Retorne
índice e valor.
8. Busca em lista ordenada (sem aproveitar ordenação)
Mesmo sabendo que a lista está ordenada, implemente busca sequencial e compare o tempo
com a binária (exercício 11).
9. Desafio – Busca com múltiplos critérios
Em uma lista de tuplas (nome, nota), encontre o primeiro aluno com nota ≥ 7 e nome
começando com “A”. Retorne o nome ou “Não encontrado”.