import hashlib


#verificar os algoritmos disponíveis
print(hashlib.algorithms_available)


#algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

#utilizando sha256

algoritmo = hashlib.sha256()
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.".encode()
algoritmo.update(text)
print(algoritmo.hexdigest())


md5 = hashlib.md5()
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.".encode()
md5.update(text)
print(md5.hexdigest())
