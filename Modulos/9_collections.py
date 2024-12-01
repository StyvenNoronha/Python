from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Conta itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pera", "Uva","Maçã", "Uva", "Banana"]
print(Counter(fruits))


# 3 - Ordenando dicionários
studants = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)