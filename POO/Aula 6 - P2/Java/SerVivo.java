// Classe SerVivo
public class SerVivo {
    protected String nome;
    protected int idade;

    public SerVivo(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void respirar() {
        System.out.println(nome + " está respirando.");
    }

    public void mover() {
        System.out.println(nome + " está se movendo.");
    }
}

public class Humano extends SerVivo {
    private String profissao;

    public Humano(String nome, int idade, String profissao) {
        super(nome, idade);
        this.profissao = profissao;
    }

    public void trabalhar() {
        System.out.println(nome + " está trabalhando como " + profissao + ".");
    }

    public static void main(String[] args) {
        Humano humano1 = new Humano("Alice", 30, "Engenheira");
        humano1.respirar();
        humano1.mover();
        humano1.trabalhar();
    }
}

