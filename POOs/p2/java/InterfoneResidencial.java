public class InterfoneResidencial extends Interfone {
    String nome_proprietario, telefone_proprietario;

    public InterfoneResidencial(String modelo, String endereco, String nome_proprietario, String telefone_proprietario) {
        super(modelo, endereco);
        this.nome_proprietario = nome_proprietario;
        this.telefone_proprietario = telefone_proprietario;
    }

    public InterfoneResidencial cadastro(String modelo, String endereco, String nome_proprietario, String telefone_proprietario) {
        return new InterfoneResidencial(modelo, endereco, nome_proprietario, telefone_proprietario);
    }

    @Override
    public void ligar_para_proprietario() {
        System.out.println("\n Ligando para o \"" + this.nome_proprietario + "\" no numero \"" + this.telefone_proprietario + "\", do endereco \"" + this.endereco + "\" ...");
    }

    @Override
    public void registrar_chamada() {
        System.out.println("\n Chamada registrada as 14:35 ...\n Duracao: 00:02:15 ...");
    }
    
    @Override
    public String toString() {
        return "\n Modelo: " + this.modelo + "\n Endereco: " + this.endereco + "\n Nome do proprietario: " + this.nome_proprietario + "\n Telefone do proprietario: " + this.telefone_proprietario;
    }
}
