public class A {
    public static void main(String[] args) {
        new B().hello();
        new pkg.C().hello();
        new sub.D().hello();
    }
}