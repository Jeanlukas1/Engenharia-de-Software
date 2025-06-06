import java.util.ArrayList;

public class Curso {
    String nome;
    String descricao;
    String carga_horaria;
    String vagas;
    ArrayList<Curso> inscritos;

    public Curso(String nome, String descricao, String carga_horaria, String vagas) {
        this.nome = nome;
        this.descricao = descricao;
        this.carga_horaria = carga_horaria;
        this.vagas = vagas;
    }

    public void adicionar_curso(ArrayList<Curso> cursos) {
        Curso curso = new Curso(this.nome, this.descricao, this.carga_horaria, this.vagas);
        cursos.add(curso);
    }

    public String apresentacao() {
        return "\n Nome: " + this.nome + "\n Endereço: " + this.descricao + "\n E-mail: " + this.carga_horaria + "\n Telefone: " + this.vagas + "\n";
    }
}
