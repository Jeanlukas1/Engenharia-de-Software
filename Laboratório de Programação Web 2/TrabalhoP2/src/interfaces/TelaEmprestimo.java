/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package interfaces;
 // Usaremos a classe de data do Java
import javax.swing.table.DefaultTableModel;
import classes.Emprestimo;
import classes.Livro;
import classes.Membro;
import java.time.LocalDate;
import javax.swing.JOptionPane;


/**
 *
 * @author UNIVASSOURAS
 */
public class TelaEmprestimo extends javax.swing.JFrame {
    private Livro livroSelecionado = null;
    private Membro membroSelecionado = null;
    private static java.util.ArrayList<Emprestimo> listaEmprestimos = new java.util.ArrayList<>();
    /**
     * Creates new form TelaEmprestimo
     */
    public TelaEmprestimo() {
        initComponents();
        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        campoBuscaLivro = new javax.swing.JTextField();
        botaoBuscaLivro = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        tabelaLivros = new javax.swing.JTable();
        campoLivroSelecionado = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jPanel2 = new javax.swing.JPanel();
        jLabel3 = new javax.swing.JLabel();
        campoBuscaMembro = new javax.swing.JTextField();
        botaoBuscarMembro = new javax.swing.JButton();
        jScrollPane2 = new javax.swing.JScrollPane();
        tabelaMembros = new javax.swing.JTable();
        jLabel4 = new javax.swing.JLabel();
        campoMembroSelecionado = new javax.swing.JTextField();
        jPanel3 = new javax.swing.JPanel();
        jLabel5 = new javax.swing.JLabel();
        campoDataDevolucao = new javax.swing.JTextField();
        botaoConfirmar = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder("1. Selecionar Livro"));

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/icons/icons/pesquisar.png"))); // NOI18N
        jLabel1.setText("Busca por Título");

        botaoBuscaLivro.setText("Buscar Livro");
        botaoBuscaLivro.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botaoBuscaLivroActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1)
                .addGap(35, 35, 35)
                .addComponent(campoBuscaLivro, javax.swing.GroupLayout.PREFERRED_SIZE, 222, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(40, 40, 40)
                .addComponent(botaoBuscaLivro)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(campoBuscaLivro, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(botaoBuscaLivro))
                .addContainerGap(26, Short.MAX_VALUE))
        );

        tabelaLivros.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null},
                {null, null},
                {null, null},
                {null, null}
            },
            new String [] {
                "ID", "Título"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        tabelaLivros.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                tabelaLivrosMouseClicked(evt);
            }
        });
        jScrollPane1.setViewportView(tabelaLivros);

        jLabel2.setText("Livro Selecionado:");

        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder("2. Selecionar Membro\n"));

        jLabel3.setText("Busca por Nome");

        botaoBuscarMembro.setText("Buscar Membro");
        botaoBuscarMembro.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botaoBuscarMembroActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel3)
                .addGap(18, 18, 18)
                .addComponent(campoBuscaMembro, javax.swing.GroupLayout.PREFERRED_SIZE, 221, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(botaoBuscarMembro)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(campoBuscaMembro, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(botaoBuscarMembro))
                .addContainerGap(27, Short.MAX_VALUE))
        );

        tabelaMembros.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null},
                {null, null},
                {null, null},
                {null, null}
            },
            new String [] {
                "ID", "Nome"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        tabelaMembros.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                tabelaMembrosMouseClicked(evt);
            }
        });
        jScrollPane2.setViewportView(tabelaMembros);

        jLabel4.setText("Membro Selecionado:");

        jPanel3.setBorder(javax.swing.BorderFactory.createTitledBorder("3. Finalizar\n"));

        jLabel5.setText("Data de Devolução (DD/MM/AAAA):");

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel5)
                .addGap(18, 18, 18)
                .addComponent(campoDataDevolucao, javax.swing.GroupLayout.PREFERRED_SIZE, 357, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(91, Short.MAX_VALUE))
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGap(36, 36, 36)
                .addGroup(jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(campoDataDevolucao, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(18, Short.MAX_VALUE))
        );

        botaoConfirmar.setText("Confirmar Empréstimo");
        botaoConfirmar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botaoConfirmarActionPerformed(evt);
            }
        });

        jButton1.setText("Voltar");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(24, 24, 24)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jScrollPane1)
                            .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jScrollPane2)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jPanel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGap(81, 81, 81))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jLabel4)
                                .addGap(18, 18, 18)
                                .addComponent(campoMembroSelecionado, javax.swing.GroupLayout.PREFERRED_SIZE, 275, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jLabel2)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(campoLivroSelecionado, javax.swing.GroupLayout.PREFERRED_SIZE, 304, javax.swing.GroupLayout.PREFERRED_SIZE))))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(40, 40, 40)
                        .addComponent(jButton1)
                        .addGap(102, 102, 102)
                        .addComponent(botaoConfirmar, javax.swing.GroupLayout.PREFERRED_SIZE, 268, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(27, 27, 27)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 173, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(27, 27, 27)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(campoLivroSelecionado, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel2))
                .addGap(40, 40, 40)
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 172, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(34, 34, 34)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(campoMembroSelecionado, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 30, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(botaoConfirmar)
                    .addComponent(jButton1))
                .addGap(19, 19, 19))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void botaoBuscarMembroActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botaoBuscarMembroActionPerformed
        // TODO add your handling code here:
        // 1. Pega o texto que o usuário digitou e converte para minúsculas para uma busca sem distinção de maiúsculas/minúsculas.
        String busca = campoBuscaMembro.getText().toLowerCase();

        // 2. Pega o modelo da nossa tabela de resultados de membros.
        DefaultTableModel modelo = (DefaultTableModel) tabelaMembros.getModel();

        // 3. Limpa a tabela de quaisquer resultados de buscas anteriores.
        modelo.setRowCount(0);

        // 4. Pega a lista completa de todos os membros cadastrados no sistema.
        // Usamos o "portal" que criamos na TelaCadastroMembros.
        for (Membro membro : TelaCadastroMembros.getListaDeMembros()) {

            // 5. Se o nome do membro (em minúsculas) contém o texto da busca...
            if (membro.getNome().toLowerCase().contains(busca)) {

                // 6. ...adiciona uma nova linha na tabela de resultados com o ID e o Nome do membro.
                modelo.addRow(new Object[]{
                    membro.getId(),
                    membro.getNome()
                });
            }
        }
    }//GEN-LAST:event_botaoBuscarMembroActionPerformed

    private void botaoBuscaLivroActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botaoBuscaLivroActionPerformed
        // TODO add your handling code here:
        String busca = campoBuscaLivro.getText().toLowerCase();
        DefaultTableModel modelo = (DefaultTableModel) tabelaLivros.getModel();
        modelo.setRowCount(0);

        for (Livro livro : TelaCadastroLivros.getListaDeLivros()) {
            if (livro.getTitulo().toLowerCase().contains(busca)) {
                modelo.addRow(new Object[]{livro.getId(), livro.getTitulo()});
            }
        }
    }//GEN-LAST:event_botaoBuscaLivroActionPerformed

    private void tabelaLivrosMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_tabelaLivrosMouseClicked
        // TODO add your handling code here:
        int linha = tabelaLivros.getSelectedRow();
        if (linha != -1) {
            int id = (int) tabelaLivros.getValueAt(linha, 0);
            for (Livro livro : TelaCadastroLivros.getListaDeLivros()) {
                if (livro.getId() == id) {
                    this.livroSelecionado = livro;
                    campoLivroSelecionado.setText(livro.getId() + " - " + livro.getTitulo());
                    break;
                }
            }
        }
    }//GEN-LAST:event_tabelaLivrosMouseClicked

    private void botaoConfirmarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botaoConfirmarActionPerformed
        // TODO add your handling code here:
        // 1. Validar se um livro e um membro foram selecionados
        if (livroSelecionado == null || membroSelecionado == null) {
            JOptionPane.showMessageDialog(this, "É necessário selecionar um livro e um membro.", "Erro", JOptionPane.ERROR_MESSAGE);
            return;
        }

        // 2. Validar e converter a data
        try {
            java.time.format.DateTimeFormatter formatador = java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy");
            LocalDate dataDevolucao = LocalDate.parse(campoDataDevolucao.getText(), formatador);

            // 3. Criar e salvar o empréstimo
            Emprestimo novoEmprestimo = new Emprestimo(livroSelecionado, membroSelecionado, dataDevolucao);
            listaEmprestimos.add(novoEmprestimo);

            JOptionPane.showMessageDialog(this, "Empréstimo registrado com sucesso!");

            // 4. Limpar a tela para o próximo
            // (crie um método limparTela() para zerar todos os campos e variáveis)

        } catch (java.time.format.DateTimeParseException e) {
            JOptionPane.showMessageDialog(this, "Formato de data inválido. Use DD/MM/AAAA.", "Erro na Data", JOptionPane.ERROR_MESSAGE);
        }
    }//GEN-LAST:event_botaoConfirmarActionPerformed

    private void tabelaMembrosMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_tabelaMembrosMouseClicked
        // TODO add your handling code here:
        // 1. Pega o número da linha em que o usuário clicou.
        int linhaSelecionada = tabelaMembros.getSelectedRow();

        // 2. Se o clique foi em uma linha válida (e não fora da tabela)...
        if (linhaSelecionada != -1) {

            // 3. ...pega o ID que está na primeira coluna (coluna 0) daquela linha.
            int idMembro = (int) tabelaMembros.getValueAt(linhaSelecionada, 0);

            // 4. Agora, procuramos na lista COMPLETA de membros qual deles tem esse ID.
            for (Membro membro : TelaCadastroMembros.getListaDeMembros()) {
                if (membro.getId() == idMembro) {

                    // 5. ACHAMOS! Armazenamos o objeto Membro inteiro na nossa variável de controle.
                    this.membroSelecionado = membro;

                    // 6. Atualizamos o campo de texto para mostrar ao usuário qual membro foi selecionado.
                    campoMembroSelecionado.setText(membro.getId() + " - " + membro.getNome());

                    // 7. Saímos do loop, pois já encontramos o membro único que queríamos.
                    break;
                }
            }
        }
    }//GEN-LAST:event_tabelaMembrosMouseClicked

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
        this.dispose();
    }//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(TelaEmprestimo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(TelaEmprestimo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(TelaEmprestimo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(TelaEmprestimo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new TelaEmprestimo().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton botaoBuscaLivro;
    private javax.swing.JButton botaoBuscarMembro;
    private javax.swing.JButton botaoConfirmar;
    private javax.swing.JTextField campoBuscaLivro;
    private javax.swing.JTextField campoBuscaMembro;
    private javax.swing.JTextField campoDataDevolucao;
    private javax.swing.JTextField campoLivroSelecionado;
    private javax.swing.JTextField campoMembroSelecionado;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTable tabelaLivros;
    private javax.swing.JTable tabelaMembros;
    // End of variables declaration//GEN-END:variables
}
