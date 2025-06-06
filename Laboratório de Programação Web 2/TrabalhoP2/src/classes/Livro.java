/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

/**
 *
 * @author Pichau
 */

public class Livro {

    // Variável estática para gerar um ID único para cada livro novo
    private static int contadorId = 0;

    // Atributos de cada livro
    private int id;
    private String titulo;
    private String autor;
    private int ano;

    // Construtor: é chamado quando você faz "new Livro(...)"
    public Livro(String titulo, String autor, int ano) {
        // Incrementa o contador e atribui o novo valor como ID deste livro
        this.id = ++contadorId;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    // --- MÉTODOS GETTERS E SETTERS ---
    // Getters são para LER os valores. Setters são para MODIFICAR.

    // AQUI ESTÁ O MÉTODO QUE PROVAVELMENTE ESTÁ FALTANDO
    public int getId() {
        return this.id;
    }

    public String getTitulo() {
        return this.titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return this.autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAno() {
        return this.ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
}