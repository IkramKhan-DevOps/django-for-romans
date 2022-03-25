package labs.lab3.exercise1;

public class ShapeFactory {

    public Shape getShape(String shapeType){
        if(shapeType==null){
            return null;
        }

        if (shapeType.equals("circle")){
            return new Circle();
        }else if(shapeType.equals("rectangle")){
            return new Rectangle();
        }

        return null;
    }
}
