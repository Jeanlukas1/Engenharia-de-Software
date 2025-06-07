
afinidades = {
    "Mago": ["Anão"],
    "Elfo": ["Arqueiro", "Anão"],
    "Arqueiro": ["Mago", "Elfo", "Bardo"],
    "Anão": ["Mago", "Arqueiro"],
    "Bardo": ["Mago", "Arqueiro", "Anão", "Elfo"]
}

class Objeto:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def definir_tipo_objeto(self, definir: str):
        self.tipo = definir

class Personagem():
    def __init__(self, tipo: str, vida: int, objeto: Objeto):
        self._tipo = tipo
        self.vida = vida
        self.objeto = objeto

    def apresentacao(self):
        pass

    def conversar(self):
        pass

    def defesa(self):
        pass

    def ataque(self):
        pass

    def pegar(self):
        pass

class Personagem_NPC(Personagem):
    def __init__(self, tipo: str, vida: int, objeto: Objeto):
        super().__init__(tipo, vida, objeto)

    def apresentacao(self):
        print(f"""
            NPC do tipo: {self._tipo}
            Vida: {self.vida}              
            """)

    def conversar(self, personagem):
        print("NPC: Olá, viajante!")

    def defesa(self, atacante):
        print("NPC tenta se defender, mas é fraco.")
        self.vida -= 2  

    def ataque(self, alvo):
        print("NPC ataca fracamente.")
        if alvo:
            alvo.vida -= 1 

    def pegar(self, novo_objeto):
        if novo_objeto:
            print("NPC pega um objeto simples.")
            self.objeto = novo_objeto

class Personagem_RPG(Personagem):
    def __init__(self, nome: str, tipo: str, vida: int, objeto: Objeto):
        super().__init__(tipo, vida, objeto)
        self.nome = nome

    def definir_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    def apresentacao(self):
        print(f"{self.nome}, do tipo {self._tipo} \nvida: {self.vida}")

    def conversar(self, personagem):
        if personagem:
            print(f"{self.nome} conversa com {getattr(personagem, 'nome', 'NPC')}.")

    def defesa(self, atacante):
        print(f"{self.nome} se defende do ataque de {getattr(atacante, 'nome', 'NPC')}.")
        if atacante and atacante._tipo in afinidades.get(self._tipo, []):
            self.vida -= 5
            print("Defesa!")
        else:
            self.vida -= 2

    def ataque(self, alvo):
        if alvo:
            print(f"{self.nome} ataca {getattr(alvo, 'nome', 'NPC')}.")
            VisitanteAtaque().visitar(self, alvo)

    def pegar(self, novo_objeto):
        if novo_objeto:
            print(f"{self.nome} pega o objeto {novo_objeto.tipo}.")
            self.objeto = novo_objeto

class VisitanteAtaque:
    def visitar(self, atacante: Personagem, defensor: Personagem):
        tipo_atacante = atacante._tipo
        tipo_defensor = defensor._tipo
        if tipo_defensor in afinidades.get(tipo_atacante, []):
            print("Ataque!")
            defensor.vida -= 10
        else:
            defensor.vida -= 4
        print(f"Vida do defensor agora: {defensor.vida}")

class Ambiente:
    def __init__(self, ambiente: str):
        self.ambiente = ambiente
        self.participantes = []

    def apresentar_participantes(self):
        print(f"Ambiente: {self.ambiente}")
        for p in self.participantes:
            p.apresentacao()

    def adicionar_participantes(self, personagem: Personagem):
        self.participantes.append(personagem)


espada = Objeto("Espada")
cajado = Objeto("Cajado")
arco = Objeto("Arco")

p1 = Personagem_RPG("Arthas", "Mago", 30, cajado)
p2 = Personagem_RPG("Legolas", "Arqueiro", 28, arco)

npc = Personagem_NPC(tipo="Anão", vida=15, objeto=espada)

floresta = Ambiente("Floresta Encantada")
print("-" *100)
floresta.adicionar_participantes(p1)
floresta.adicionar_participantes(p2)
floresta.adicionar_participantes(npc)
floresta.apresentar_participantes()
print("-" *100)

print("-" *100)
p1.conversar(p2)
p2.conversar(npc)
npc.conversar(p1)
print("-" *100)

print("-" *100)
p1.ataque(p2) 
print()
p2.defesa(p1)
print("-" *100)

print("-" *100)
p2.ataque(npc)
print()
npc.defesa(p2)
print("-" *100)

print("-" *100)
p1.pegar(espada)
print()
npc.pegar(cajado)
print("-" *100)

floresta.apresentar_participantes()
