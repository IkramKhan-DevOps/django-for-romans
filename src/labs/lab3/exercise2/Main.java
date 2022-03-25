package labs.lab3.exercise2;

public class Main {

    public static void main(String[] args){
        BasicCombo basicCombo =  new ComboCreationLogic();

        Combo comboOffice = basicCombo.createCombo("office");
        Combo comboCasual = basicCombo.createCombo("casual");
        Combo comboCasualOffice = basicCombo.createCombo("casualoffice");

        comboCasualOffice.shirts();

    }
}
