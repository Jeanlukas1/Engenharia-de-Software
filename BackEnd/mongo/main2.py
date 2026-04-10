import random
from datetime import datetime, timedelta
from pymongo import MongoClient

class MongoDBDataGenerator:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="sistema_escolar"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def gerar_cursos(self, quantidade):
        print(f"Criando {quantidade} cursos...")
        departamentos = ["Engenharia", "Direito", "Medicina", "Administração", "Artes", "Ciência da Computação"]
        cursos = []
        for i in range(quantidade):
            curso = {
                "_id": i + 1,
                "nome": f"Curso {i + 1}",
                "departamento": random.choice(departamentos)
            }
            cursos.append(curso)
        self.db.cursos.insert_many(cursos)
        print("Cursos criados!")

    def gerar_turmas(self, quantidade):
        print(f"Criando {quantidade} turmas...")
        semestres = ["2024_1", "2024_2", "2025_1", "2025_2"]
        turmas = []
        for i in range(quantidade):
            turma = {
                "_id": i + 1,
                "codigo": f"T{i + 1000}",
                "curso_id": random.randint(1, self.db.cursos.count_documents({})),
                "semestre": random.choice(semestres)
            }
            turmas.append(turma)
        self.db.turmas.insert_many(turmas)
        print("Turmas criadas!")

    def gerar_alunos(self, quantidade):
        print(f"Criando {quantidade} alunos...")
        nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]
        cidades = ["Rio de Janeiro", "São Paulo", "Belo Horizonte", "Curitiba", "Porto Alegre"]
        alunos = []
        for i in range(quantidade):
            nome = random.choice(nomes) + f" {random.choice(['Silva', 'Souza', 'Oliveira', 'Pereira'])}"
            aluno = {
                "_id": i + 1,
                "nome": nome,
                "email": f"{nome.lower().replace(' ', '.')}@exemplo.com",
                "cpf": f"{random.randint(10000000000, 99999999999)}",
                "curso_id": random.randint(1, self.db.cursos.count_documents({})),
                "ativo": random.choice([True, False]),
                "bolsista": random.choice([True, False]),
                "data_matricula": datetime.now() - timedelta(days=random.randint(0, 1000)),
                "endereco": {
                    "cidade": random.choice(cidades)
                },
                "telefone": f"55{random.randint(100000000, 999999999)}"
            }
            alunos.append(aluno)
        self.db.alunos.insert_many(alunos)
        print("Alunos criados!")

    def gerar_professores(self, quantidade):
        print(f"Criando {quantidade} professores...")
        nomes = ["Lucas", "Mariana", "Paulo", "Renata", "Sérgio", "Tatiana", "Vitor", "Wanda"]
        departamentos = ["Engenharia", "Direito", "Medicina", "Administração", "Artes", "Ciência da Computação"]
        professores = []
        for i in range(quantidade):
            nome = random.choice(nomes) + f" {random.choice(['Costa', 'Lima', 'Melo', 'Ribeiro'])}"
            professor = {
                "_id": i + 1,
                "nome": nome,
                "email": f"{nome.lower().replace(' ', '.')}@universidade.com",
                "departamento": random.choice(departamentos)
            }
            professores.append(professor)
        self.db.professores.insert_many(professores)
        print("Professores criados!")

    def gerar_contadores(self):
        print("Criando contadores...")
        
        contadores = [
            {
                "_id": "matriculas",
                "valor": random.randint(2024001, 2024999),
                "descricao": "Contador para números de matrícula"
            },
            {
                "_id": "turmas",
                "valor": random.randint(100, 999),
                "descricao": "Contador para códigos de turma"
            },
            {
                "_id": "professores",
                "valor": random.randint(1000, 9999),
                "descricao": "Contador para IDs de professores"
            }
        ]
        
        self.db.contadores.insert_many(contadores)
        print("Contadores criados!")
    
    def criar_indices(self):
        """Cria índices para performance"""
        print("Criando índices...")
        
        try:
            # Índices para alunos
            self.db.alunos.create_index([("nome", 1)])
            self.db.alunos.create_index([("email", 1)], unique=True)
            self.db.alunos.create_index([("cpf", 1)], unique=True)
            self.db.alunos.create_index([("curso_id", 1), ("ativo", 1)])
            self.db.alunos.create_index([("data_matricula", -1)])
            self.db.alunos.create_index([("endereco.cidade", 1)])
            self.db.alunos.create_index([("nome", "text")])
            self.db.alunos.create_index([("telefone", 1)], sparse=True)
            
            # Índices para cursos
            self.db.cursos.create_index([("nome", 1)])
            self.db.cursos.create_index([("departamento", 1)])
            
            # Índices para turmas
            self.db.turmas.create_index([("codigo", 1)], unique=True)
            self.db.turmas.create_index([("curso_id", 1), ("semestre", 1)])
            
            # Índices para professores
            self.db.professores.create_index([("nome", 1)])
            self.db.professores.create_index([("email", 1)], unique=True)
            self.db.professores.create_index([("departamento", 1)])
            
            print("Índices criados com sucesso!")
            
        except Exception as e:
            print(f"Erro ao criar índices: {e}")
    
    def gerar_estatisticas(self):
        """Gera estatísticas do banco"""
        print("\nESTATÍSTICAS DO BANCO GERADO:")
        print("=" * 40)
        
        # Contagens básicas
        total_cursos = self.db.cursos.count_documents({})
        total_turmas = self.db.turmas.count_documents({})
        total_alunos = self.db.alunos.count_documents({})
        total_professores = self.db.professores.count_documents({})
        
        print(f"Total de cursos: {total_cursos}")
        print(f"Total de turmas: {total_turmas}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Total de professores: {total_professores}")
        
        # Estatísticas de alunos
        alunos_ativos = self.db.alunos.count_documents({"ativo": True})
        bolsistas = self.db.alunos.count_documents({"bolsista": True})
        
        print(f"Alunos ativos: {alunos_ativos}")
        print(f"Bolsistas: {bolsistas}")
        
        # Distribuição por departamento
        print("\nDISTRIBUIÇÃO POR DEPARTAMENTO:")
        pipeline = [
            {"$lookup": {
                "from": "cursos",
                "localField": "curso_id",
                "foreignField": "_id",
                "as": "curso"
            }},
            {"$unwind": "$curso"},
            {"$group": {
                "_id": "$curso.departamento",
                "total_alunos": {"$sum": 1}
            }},
            {"$sort": {"total_alunos": -1}}
        ]
        
        for dept in self.db.alunos.aggregate(pipeline):
            print(f"  {dept['_id']}: {dept['total_alunos']} alunos")
        
        # Distribuição por cidade
        print("\nTOP 5 CIDADES:")
        pipeline = [
            {"$group": {
                "_id": "$endereco.cidade",
                "total": {"$sum": 1}
            }},
            {"$sort": {"total": -1}},
            {"$limit": 5}
        ]
        
        for cidade in self.db.alunos.aggregate(pipeline):
            print(f"  {cidade['_id']}: {cidade['total']} alunos")
        
        print("\nBANCO POPULADO COM SUCESSO!")
        print("Pronto para os exercícios da apresentação!")
    
    def executar_geracao_completa(self):
        """Executa toda a geração de dados"""
        print("Iniciando geração de dados...")
        print("=" * 50)
        
        self.gerar_cursos(25)  # 25 cursos
        self.gerar_turmas(75)  # 75 turmas
        self.gerar_alunos(300)  # 300 alunos
        self.gerar_professores(60)  # 60 professores
        self.gerar_contadores()
        
        self.criar_indices()
        self.gerar_estatisticas()
        
        return True

def main():
    print("Gerador de Dados para MongoDB - Sistema Escolar")
    print("=" * 60)
    
    try:
        gerador = MongoDBDataGenerator()
        sucesso = gerador.executar_geracao_completa()
        
        if sucesso:
            print("\nGeração concluída! O banco está pronto para uso.")
            print("Agora você pode:")
            print("   - Executar consultas na apresentação HTML")
            print("   - Testar operações CRUD avançadas")
            print("   - Praticar com os exercícios propostos")
        
    except Exception as e:
        print(f"Erro durante a geração: {e}")
        print("Verifique se o MongoDB está rodando e acessível")

if __name__ == "__main__":
    main()