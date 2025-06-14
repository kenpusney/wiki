package sub;
import pkg.C;


public class D {
    
    static C c = new C();

    public D() {
        System.out.println("C in ctor: " + c);
    }

    public void hello() {
        System.out.println("C: " + new C());
    }
}