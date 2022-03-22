package labs.lab1.task1;

import java.util.ArrayList;
import java.util.Objects;

public class Account {

    // STATE
    public String name;
    public int currentBalance;
    public int creditLimit;
    public ArrayList<Transaction> transactions;

    // CONSTRUCTOR
    public Account(String name, int creditLimit) {
        this.name = name;
        this.creditLimit = creditLimit;
        transactions =  new ArrayList<>();
    }

    // BEHAVIOR
    public boolean checkTransactions(Transaction transaction){
        if(Objects.equals(transaction.type, "credit")) {
            return (transaction.amount + currentBalance) < creditLimit;
        }else{
            return transaction.amount < currentBalance;
        }
    }

    public void post(Transaction transaction){
        if(transaction.amount>0){
            if(Objects.equals(transaction.type, "credit")){
                currentBalance += transaction.amount;
                transactions.add(transaction);
            }else{
                if(transaction.amount<currentBalance){
                    currentBalance-=transaction.amount;
                }else{
                    System.out.println("ERROR >> Requested amount is greater than current amount");
                }
            }
        }else{
            System.out.println("ERROR >> Amount must be greater then 0");
        }
    }
}
