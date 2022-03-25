package labs.lab3.exercise2;

public class BasicCombo {

    public Combo createCombo(String comboType){
        if(comboType==null){
            return null;
        }

        switch (comboType) {
            case "casual":
                return new Casual();
            case "office":
                return new Office();
            case "casualoffice":
                return new CasualOffice();
        }

        return null;
    }

}
