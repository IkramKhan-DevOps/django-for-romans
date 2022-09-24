package objectandclass;

public class Main {

    public static void main(String[] args){
        Student student =  new Student(); // 8 byte
        student.registration("Sheraz", "Fayyaz", "Mardan", "Pakistani", 10);
        student.personalDetails();

        Student student1 =  new Student(); // 8 byte
        student1.registration("Ikram", "amir", "Mardan", "Pakistani", 10);
        student1.personalDetails();

    }
}
