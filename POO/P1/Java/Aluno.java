import java.util.ArrayList;

public class Aluno {
    String nome;
    String endereco;
    String email;
    String telefone;

    public Aluno(String nome, String endereco, String email, String telefone) {
        this.nome = nome;
        this.endereco = endereco;
        this.email = email;
        this.telefone = telefone;
    }

    public void adicionar_aluno(ArrayList<Aluno> alunos) {
        Aluno aluno = new Aluno(this.nome, this.endereco, this.email, this.telefone);
        alunos.add(aluno);
    }

    public String apresentacao() {
        return "\n Nome: " + this.nome + "\n Endereço: " + this.endereco + "\n E-mail: " + this.email + "\n Telefone: " + this.telefone + "\n";
    }
}
