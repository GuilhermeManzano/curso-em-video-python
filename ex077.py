# Crie um programa que tenha uma tulpa com várias palavras (sem acento). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

for p in palavras:
   print(f'\nNa palavra {p} temos ', end='')
   for letra in p:
     if letra in 'aAeEiIoOuU':
         print(letra, end=' ')
