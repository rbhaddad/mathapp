import random


class Aluno:
def __init__(self, nome):
self.nome = nome
self.nivel = 1
self.acertos = 0
self.erros = 0
self.historico = []


def gerar_pergunta(self):
a = random.randint(1, self.nivel * 5)
b = random.randint(1, self.nivel * 5)
return a, b


def responder(self, resposta, correta):
if resposta == correta:
self.acertos += 1
self.historico.append(True)
if self.acertos % 3 == 0:
self.nivel += 1
return True
else:
self.erros += 1
self.historico.append(False)
return False


aluno = None
pergunta_atual = None


def iniciar_aluno(nome):
global aluno
aluno = Aluno(nome)
return aluno.nivel


def nova_pergunta():
global pergunta_atual
a, b = aluno.gerar_pergunta()
pergunta_atual = (a, b)
return f"Quanto é {a} + {b}?", a + b


def verificar(resposta):
correta = pergunta_atual[0] + pergunta_atual[1]
return aluno.responder(resposta, correta), aluno.nivel