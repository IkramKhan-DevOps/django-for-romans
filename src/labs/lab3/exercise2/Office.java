package labs.lab3.exercise2;

public class Office implements Combo {

    @Override
    public void shirts() {
        System.out.println("Office shirts available");
    }

    @Override
    public void trousers() {
        System.out.println("Office trousers available");
    }

    @Override
    public void shoes() {
        System.out.println("Office shoes available");
    }
}
