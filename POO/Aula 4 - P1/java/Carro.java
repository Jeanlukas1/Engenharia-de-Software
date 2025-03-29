public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private String cor;
    private String placa;
    private boolean isRunning;
    private int velocidade;
    private int marcha; // Marcha ré será -1

    // Construtor
    public Carro(String marca, String modelo, int ano, String cor, String placa) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.cor = cor;
        this.placa = placa;
        this.isRunning = false;
        this.velocidade = 0;
        this.marcha = 0; // Neutro
    }

    // Método de apresentação
    @Override
    public String toString() {
        return "O carro de Marca " + marca + " e modelo " + modelo +
               "\ndo ano " + ano + " e cor " + cor +
               " saiu da loja e hoje tem a placa " + placa;
    }

    // Método para ligar o carro
    public void ligarCarro() {
        if (!isRunning) {
            isRunning = true;
            System.out.println("O carro foi ligado... RUMRUMRUMRUM");
        } else {
            System.out.println("O carro já está ligado!!!");
        }
    }

    // Método para acelerar com base na marcha
    public void acelerar() {
        if (!isRunning) {
            System.out.println("O carro " + modelo + " está desligado, precisa ligar o carro primeiro!!!");
        } else if (marcha == 0) {
            marcha = 1;
            velocidade += 30;
        } else if (marcha == 1) {
            marcha = 2;
            velocidade += 25;
        } else if (marcha == 2) {
            marcha = 3;
            velocidade += 15;
        } else if (marcha == 3) {
            marcha = 4;
            velocidade += 10;
        } else if (marcha == 4) {
            marcha = 5;
            velocidade += 5;
        } else if (marcha == 5) {
            marcha = 6;
            velocidade += 5;
            if (velocidade > 160) {
                velocidade = 160;
            }
        }
        System.out.println("O carro está na marcha " + marcha + " e a velocidade é " + velocidade + " km/h");
    }

    // Método para passar para a marcha ré
    public void passarMarchaRe() {
        if (isRunning && (marcha == 0 || marcha == 1)) {
            marcha = -1;
            velocidade += 3;
            System.out.println("O carro está na marcha Ré e a velocidade é " + velocidade + " km/h");
        } else {
            System.out.println("Não é possível engatar a marcha ré com o carro em movimento!");
        }
    }

    // Método para frear
    public void frear() {
        if (isRunning && velocidade > 0) {
            velocidade -= 5;
            System.out.println("A velocidade do carro é " + velocidade + " km/h");
        } else {
            System.out.println("O carro " + modelo + " está desligado ou sua velocidade já é 0 km/h!");
        }
    }

    // Método principal para testar a classe
    public static void main(String[] args) {
        Carro meuCarro = new Carro("Toyota", "Corolla", 2022, "Preto", "ABC-1234");
        System.out.println(meuCarro);

        meuCarro.ligarCarro();
        for (int i = 0; i < 5; i++) {
            meuCarro.acelerar();
        }
        for (int i = 0; i < 5; i++) {
            meuCarro.frear();
        }
        meuCarro.passarMarchaRe();
    }
}