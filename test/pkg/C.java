package pkg;
import sub.D;

public class C {

    static D d = new D();

    public C() {
        System.out.println("D in ctor: " + d);
    }

    public void hello() {
        System.out.println("D: " + new D());
    }    
}