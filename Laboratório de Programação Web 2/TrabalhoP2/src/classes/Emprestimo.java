/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

import java.time.LocalDate; // Usaremos a classe de data do Java
/**
 *
 * @author UNIVASSOURAS
 */
public class Emprestimo {
    private static int contadorId = 0;
    private int id;
    private Livro livro;       // O livro que foi emprestado
    private Membro membro;     // O membro que pegou o livro
    private LocalDate dataEmprestimo;
    private LocalDate dataDevolucao;
    private boolean devolvido;

    // Construtor
    public Emprestimo(Livro livro, Membro membro, LocalDate dataDevolucao) {
        this.id = ++contadorId;
        this.livro = livro;
        this.membro = membro;
        this.dataEmprestimo = LocalDate.now(); // Pega a data atual automaticamente
        this.dataDevolucao = dataDevolucao;
        this.devolvido = false; // Todo empréstimo começa como "não devolvido"
    }

    // --- Getters e Setters ---
    public int getId() {
        return id;
    }

    public Livro getLivro() {
        return livro;
    }

    public Membro getMembro() {
        return membro;
    }

    public LocalDate getDataEmprestimo() {
        return dataEmprestimo;
    }

    public LocalDate getDataDevolucao() {
        return dataDevolucao;
    }

    public boolean isDevolvido() {
        return devolvido;
    }

    public void setDevolvido(boolean devolvido) {
        this.devolvido = devolvido;
    }
}
