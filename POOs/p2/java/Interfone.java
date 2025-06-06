public abstract class Interfone {
    String modelo, endereco;

    public Interfone(String modelo, String endereco) {
        this.modelo = modelo;
        this.endereco = endereco;
    }

    public abstract void ligar_para_proprietario();

    public abstract void registrar_chamada();
}
