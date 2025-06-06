/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

/**
 *
 * @author UNIVASSOURAS
 */
public class Membro {
    private static int contadorId = 0;
    private int id;
    private String nome;
    private String endereco;
    private String telefone;

    // Construtor
    public Membro(String nome, String endereco, String telefone) {
        this.id = ++contadorId;
        this.nome = nome;
        this.endereco = endereco;
        this.telefone = telefone;
    }

    
    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
}
