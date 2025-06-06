import javax.swing.JOptionPane;

abstract class Pessoa {
    protected String nome;

    public Pessoa(String nome) {
        this.nome = nome;
    }

    public abstract String apresentar();
}

class Aluno extends Pessoa {
    private String curso;

    public Aluno(String nome, String curso) {
        super(nome);
        this.curso = curso;
    }

    @Override
    public String apresentar() {
        return "Sou o aluno " + nome + " e curso " + curso + ".";
    }
}

class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, String disciplina) {
        super(nome);
        this.disciplina = disciplina;
    }

    @Override
    public String apresentar() {
        return "Sou o professor " + nome + " e leciono " + disciplina + ".";
    }
}

public class Main {
    public static void main(String[] args) {
        Pessoa aluno = new Aluno("Zé da Manga", "Engenharia de Software");
        Pessoa professor = new Professor("Zé da Couve", "POO");

        String mensagem = aluno.apresentar() + "\n" + professor.apresentar();

        JOptionPane.showMessageDialog(null, mensagem, "Apresentações", JOptionPane.INFORMATION_MESSAGE);
    }
}