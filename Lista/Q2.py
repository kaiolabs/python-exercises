N = int(input('Quantos alunos? '))

students = dict()

for i in range(1, N+1):
  nome = input(f'Nome do aluno {i}: ')
  grades = []

  for j in range(1, 5):
    grade = float(input(f'Nota {j} do aluno {i}: '))
    grades.append(grade)

  students[nome] = grades

print("\n{}\n{}Notas dos alunos{}{}{}".format("="*45," "*14, "\n", "="*45, ""))

for nome, grades in students.items():

    average = sum(grades) / len(grades)
    result = 'aprovado' if average >= 6.0 else 'reprovado'
    chave = nome
    notas = students[nome]
    print(f"| {chave} | {notas} | {result} |")

print("="*45)