package labs.lab1;

public class Transaction {

    // STATE
    public int amount;
    public String type;


    // CONSTRUCTOR
    public Transaction(int amount, String type) {
        this.amount = amount;
        this.type = type;
    }

    // BEHAVIOR
    public int getAmount() {
        return amount;
    }

    public String getType() {
        return type;
    }
}
