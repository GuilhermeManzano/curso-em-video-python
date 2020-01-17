# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o vzlor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite um último número: ')))

print(f'Você digitou os números: {n}')
print(f'O valor 9 foi digitado {n.count(9)} vezes')
print(f'O valor 3 apareceu na posição {n.index(3)+1}°')
p = 0
for x in n:
     if x % 2 == 0:
        p += 1
print(f'Os valores pares digitados foram {p}')
