# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha = []
e = str(input('Digite uma expressão válida: '))
for sim in e:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está inválida!')
