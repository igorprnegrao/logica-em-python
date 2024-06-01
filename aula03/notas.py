nota1 = float(input('Digite a nota téorica: '))
nota2 = float(input('Digite a nota prática: '))
nota3 = float(input('Digite a nota do trabalho: '))

media = (nota1 + nota2 + nota3) / 3
print(f'A média do aluno foi: {media}')
if (media >= 70):
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado')
