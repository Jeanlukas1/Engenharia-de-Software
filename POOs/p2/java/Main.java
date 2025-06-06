public class Main {
    public static void main(String[] args) {
        InterfoneResidencial interfone1 = new InterfoneResidencial("A123", "Rua A", "Leandro", "00000-0000");
        System.out.println(interfone1);
        InterfoneResidencial interfone2 = new InterfoneResidencial("E321", "Rua B", "Policia", "190");
        System.out.println(interfone2);
        InterfoneResidencial interfone3 = new InterfoneResidencial("E213", "Rua C", "Bombeiros", "193");
        System.out.println(interfone3);
        InterfoneResidencial interfone4 = new InterfoneResidencial("E312", "Rua D", "SAMU", "192");
        System.out.println(interfone4 + "\n");
    }
}
