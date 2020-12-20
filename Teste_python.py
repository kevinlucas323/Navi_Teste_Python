import math

#Teste 1
    #Basta multiplicarmor 49, 37 e 2 e vermos quantos multiplos desse número são menores que 5 milhões

mult = 3626 #49.37.2
n = 1

while mult*(n+1) < 5000000:
    n = n + 1

print("Temos um total de", n ,"múltiplos simultâneos de 2, 37 e 49");
print("\n")
#Teste 2
i = 0
X = [0]*10
Sum = 0
for i in range(0,10):
    if (i % 2 == 0):
        X[i] = math.pow(3,i) + 7*math.factorial(i)
    else:
        X[i] = math.pow(2,i) + 4*math.log(i)
    if(X[i] == max(X)):
        pos = i
    Sum = Sum + X[i]
        
Media = round(Sum/len(X),2)
print("O maior número está na posição", pos ,"(vale lembrar que o primeiro numero está na posição 0) e a média é dada por",Media)
print("\n")
#Teste 3
    #Considerarei que, como não foie especificado, a nota dos alunos estão em uma matriz (Notas) semelhante ao Dicionario
i = 0
Maior_nota = 0
Maior_aluno = ""
Dic = []
for i in range(5):
    Dic = Dic + [[0]*2]
    
m = 0
n = 0    
for m in range(5):
    Dic[m][0] = Notas[m][0]
    Dic[m][1] = Notas[m][1]
    if (Dic[m][1] > Maior_nota):
        Maior_nota = Dic[m][1]
        Maior_aluno = Dic[m][0]
        
print("O aluno com maior nota é", Maior_aluno, "e sua nota é", Maior_nota)
