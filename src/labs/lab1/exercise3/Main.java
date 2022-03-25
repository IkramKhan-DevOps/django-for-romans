package labs.lab1.exercise3;

public class Main {

    public static void main(String[] args){
        Circle c4 = new Circle();
        c4.setRadius(5.0);
        c4.setColor("Green");

        System.out.println("radius is: " + c4.getRadius());
        System.out.println("color is: " + c4.getColor());

        // returns description about the instance
        System.out.println(c4.toString()); //explicit call
        System.out.println(c4); //implicit call

    }
}
