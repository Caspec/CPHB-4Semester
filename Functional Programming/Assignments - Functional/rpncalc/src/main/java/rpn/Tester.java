package rpn;

import java.util.Scanner;
import rpn.Calculator;

public class Tester {

    public static void main(String[] args) {

        Calculator c = new Calculator();
        Scanner in = new Scanner(System.in);
        boolean isAction;
        StackPath sp = new StackPath();
        System.out.println("Use the rpn calculator: 3 3 * ,  1 2 - ,  2 2 / ,  1 1 +");
        System.out.println("To stop the rpn calculator type: STOP");
        while (true) {
            String consoleInput = in.nextLine();
            if (consoleInput.equalsIgnoreCase("STOP")) {
                System.out.println("Let's stop calculating... BEEP... Im out!");
                break;
            }
            String[] rawArgs = consoleInput.split(" ");
            for (int i = 0; i < rawArgs.length; i++) {
                String rawArgument = rawArgs[i];
                isAction = false;
                switch (rawArgument) {
                    case "/":
                        sp.push(c.operationDiv(sp.pop(), sp.pop()));
                        isAction = true;
                        break;
                    case "*":
                        sp.push(c.operationMulti(sp.pop(), sp.pop()));
                        isAction = true;
                        break;
                    case "+":
                        sp.push(c.operationAdd(sp.pop(), sp.pop()));
                        isAction = true;
                        break;
                    case "-":
                        sp.push(c.operationMinus(sp.pop(), sp.pop()));
                        isAction = true;
                        break;
                }
                if (!isAction) {
                    Integer j = Integer.parseInt(rawArgument);
                    sp.push(j);
                }
            }
            Integer[] numbersToWrite = sp.peekAll();
            for (int i = 0; i < numbersToWrite.length; i++) {
                System.out.println("> " + numbersToWrite[i]);
            }
        }
    }

}
