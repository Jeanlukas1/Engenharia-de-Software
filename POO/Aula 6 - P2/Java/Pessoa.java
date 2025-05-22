package Aula 6.Java;

public class Pessoa {
    protected String nome;
    protected int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String apresentar() {
        return "Olá, meu nome é " + nome + " e tenho " + idade + " anos.";
    }
}

public class Aluno extends Pessoa {
    private String matricula;

    public Aluno(String nome, int idade, String matricula) {
        super(nome, idade);
        this.matricula = matricula;
    }

    @Override
    public String apresentar() {
        return super.apresentar() + " Sou aluno e minha matrícula é " + matricula + ".";
    }
}

public class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    @Override
    public String apresentar() {
        return super.apresentar() + " Sou professor de " + disciplina + ".";
    }
}

public class Principal {
    public static void apresentarPessoa(Pessoa p) {
        System.out.println(p.apresentar());
    }

    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Carlos", 40);
        Aluno a1 = new Aluno("Ana", 21, "20250123");
        Professor prof1 = new Professor("Roberta", 35, "Matemática");

        apresentarPessoa(p1);
        apresentarPessoa(a1);
        apresentarPessoa(prof1);
    }
}

// Classe abstrata Pessoa
public abstract class Pessoa {
    protected String nome;
    protected int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public abstract String apresentar();
}

// Subclasse Aluno que herda de Pessoa
public class Aluno extends Pessoa {
    private String matricula;

    public Aluno(String nome, int idade, String matricula) {
        super(nome, idade);
        this.matricula = matricula;
    }

    @Override
    public String apresentar() {
        return "Olá, meu nome é " + nome + " e tenho " + idade + " anos. Sou aluno e minha matrícula é " + matricula + ".";
    }
}

// Subclasse Professor que herda de Pessoa
public class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade, String disciplina) {
        super(nome, idade);
        this.disciplina = disciplina;
    }

    @Override
    public String apresentar() {
        return "Olá, meu nome é " + nome + " e tenho " + idade + " anos. Sou professor de " + disciplina + ".";
    }
}

// Classe principal
public class Principal {
    public static void apresentarPessoa(Pessoa pessoa) {
        System.out.println(pessoa.apresentar());
    }

    public static void main(String[] args) {
        Pessoa aluno = new Aluno("Ana", 21, "20250123");
        Pessoa professor = new Professor("Roberta", 35, "Matemática");

        apresentarPessoa(aluno);
        apresentarPessoa(professor);
    }
}
