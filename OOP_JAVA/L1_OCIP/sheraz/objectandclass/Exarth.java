package objectandclass;
// CLASS OBJECTS or INSTANCE OF CLASS
public class Exarth {
    String dev_name;
    String dev_feild;
    String dev_experience;
    String dev_skills;

//METHOD OF CLASS 

 void interni_Exarth(String dev_name,String dev_feild ,String dev_experience ,String dev_skills)
 {
    this.dev_name=dev_name;
    this.dev_feild=dev_feild;
    this.dev_experience=dev_experience;
    this.dev_skills=dev_skills;


 }
 void cv_interni(){
    System.out.println("Devloper Name:"+dev_name);
    System.out.println("Devloper Fields:"+dev_feild);
    System.out.println("Devloper Experience:"+dev_experience);
    System.out.println("Devloper Skills:"+dev_skills);

    
 }

    
}
