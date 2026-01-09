Aluno = (input('digite o nome do aluno: '))

Nota1 = int(input('digite a primeira nota: '))
Nota2 = int(input('digite a segunda nota: '))
Nota3 = int(input('digite a terceira nota: '))

media = int(Nota1 + Nota2 + Nota3) / 3
print ('o aluno(a)', Aluno, 'tem a media de', media)

match media:
    case _ if media < 5:
        print("O aluno precisa melhorar")
    case _ if media < 8:
        print("O aluno é exemplar")
    case _ if media == 10:
        print("Espetacular!")
    case _:
        print("Bom desempenho")