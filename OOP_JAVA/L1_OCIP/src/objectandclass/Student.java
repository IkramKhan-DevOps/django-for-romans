package objectandclass;

public class Student {

    // ATTRIBUTES/DATA-MEMBERS      -- STATE OF CLASS
    public String name;
    public String fatherName;
    public String city;
    public String nationality;
    public int obtainedMarks;
    public int totalMarks;

    // METHODS/FUNCTIONS/PROCEDURE  -- BEHAVIOUR OF CLASS

    public void registration(String name, String fatherName, String city, String nationality, int obtainedMarks){
        this.name=name;
        this.fatherName=fatherName;
        this.city=city;
        this.nationality=nationality;
        this.obtainedMarks=obtainedMarks;
    }

    public void showResults(){
        System.out.println("RESULTS FOR SHERAZ");
        System.out.println("MARKS      : "+ obtainedMarks);
        System.out.println("TOTAL      : "+ totalMarks);
        System.out.println("GRADE      : "+ calculateGrade());
        System.out.println();
    }

    public void personalDetails(){
        System.out.println("INFORMATION FOR SHERAZ");
        System.out.println("NAME        : "+ name);
        System.out.println("FATHER NAME : "+ fatherName);
        System.out.println("CITY        : "+ city);
        System.out.println("NATIONALITY : "+ nationality);
        System.out.println("MARKS       : "+ obtainedMarks);
        System.out.println("TOTAL       : "+ totalMarks);
        System.out.println("GRADE       : "+ calculateGrade());
        System.out.println();
    }

    public String calculateGrade(){
        if (obtainedMarks >= 50 && obtainedMarks < 75) {
            return "C";
        }else if (obtainedMarks >= 75 && obtainedMarks < 90) {
            return "B";
        }else if (obtainedMarks >= 90 && obtainedMarks < 100) {
            return "A";
        }
        return "F";
    }

}
