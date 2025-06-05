/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package br.com.biblioteca.model;

/**
 *
 * @author Pichau
 */

public class Livro {
    // ... (Cole aqui o código completo da classe Livro da resposta anterior)
    private int id;
    private String titulo;
    private String autor;
    private int anoPublicacao;

    public Livro(String titulo, String autor, int anoPublicacao) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }
    
    // ... Getters, Setters e toString()...
    @Override
    public String toString() {
        return "Livro Cadastrado {" +
                "titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", ano=" + anoPublicacao +
                '}';
    }
}
