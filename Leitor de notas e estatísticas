while True:
    try:
        quantidade = int(input("Quantas notas deseja inserir? "))
        break
    except ValueError:
        print("Erro. Digite somente números ")

notas = []


for i in range(quantidade):
    try:
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    except  ValueError:
        print("Erro. Digite somente números ")

print("Notas:", notas)
print("Nota mais alta:", max(notas))
print("Nota mais baixa:", min(notas))
print("Média:", sum(notas) / len(notas))
