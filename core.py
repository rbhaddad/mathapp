import random, json
import js

OPERACOES = ["adição", "subtração", "multiplicação", "divisão"]

class EstadoAluno:
    def __init__(self):
        self.nome = ""
        self.nivel = {op: 1 for op in OPERACOES}
        self.historico = {op: [] for op in OPERACOES}

    def salvar(self):
        js.localStorage.setItem(
            f"mathapp_{self.nome}",
            json.dumps({
                "nivel": self.nivel,
                "historico": self.historico
            })
        )

    def carregar(self):
        dados = js.localStorage.getItem(f"mathapp_{self.nome}")
        if dados:
            dados = json.loads(dados)
            self.nivel = dados["nivel"]
            self.historico = dados["historico"]

estado = EstadoAluno()

def gerar_questao():
    op = random.choice(OPERACOES)
    n = estado.nivel[op]

    if op == "adição":
        a, b = random.randint(1, n*10), random.randint(1, n*10)
        res = a + b
        txt = f"{a} + {b} = ?"

    elif op == "subtração":
        a, b = random.randint(1, n*10), random.randint(1, n*10)
        res = a - b
        txt = f"{a} - {b} = ?"

    elif op == "multiplicação":
        a, b = random.randint(1, n+5), random.randint(1, n+5)
        res = a * b
        txt = f"{a} × {b} = ?"

    elif op == "divisão":
        b = random.randint(1, n+5)
        res = random.randint(1, n+5)
        a = b * res
        txt = f"{a} ÷ {b} = ?"

    alternativas = {res}
    while len(alternativas) < 4:
        alternativas.add(res + random.randint(-5, 5))

    return {
        "op": op,
        "texto": txt,
        "resposta": res,
        "alternativas": list(alternativas)
    }

def responder(op, correta, resposta):
    acerto = correta == resposta
    estado.historico[op].append(acerto)

    if len(estado.historico[op]) >= 5:
        if estado.historico[op][-5:].count(True) >= 4:
            estado.nivel[op] += 1

    estado.salvar()
    return acerto
