//Definindo os Atributos 
public class Carro {
    public String marca;
    public String modelo;
    public Integer ano;
    public String cor;
    public String placa;
    public Boolean is_runnig;
    public Integer velocidade;

    //Definindo o método Construtor
    public Carro(String marca, String modelo, Integer ano, String cor, String placa){
       this.marca = marca;
       this.modelo = modelo;
       this.ano = ano;
       this.cor = cor;
       this.placa = placa;
       this.is_runnig = false;
       this.velocidade = 0;
    }
}
