import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);

        String color;
        long result = 0, a;

        for(int i = 1; i >= 0; i--){
            color = stdin.nextLine();

            if (Objects.equals(color, "black")) a = 0;
            else if (Objects.equals(color, "brown")) a = 1;
            else if (Objects.equals(color, "red")) a = 2;
            else if (Objects.equals(color, "orange")) a = 3;
            else if (Objects.equals(color, "yellow")) a = 4;
            else if (Objects.equals(color, "green")) a = 5;
            else if (Objects.equals(color, "blue")) a = 6;
            else if (Objects.equals(color, "violet")) a = 7;
            else if (Objects.equals(color, "grey")) a = 8;
            else if (Objects.equals(color, "white")) a = 9;
            else a = -1;


            //System.out.println(a);
            result += a * Math.pow(10, i);
        }

        color = stdin.nextLine();

        if (Objects.equals(color, "black")) a = 0;
        else if (Objects.equals(color, "brown")) a = 1;
        else if (Objects.equals(color, "red")) a = 2;
        else if (Objects.equals(color, "orange")) a = 3;
        else if (Objects.equals(color, "yellow")) a = 4;
        else if (Objects.equals(color, "green")) a = 5;
        else if (Objects.equals(color, "blue")) a = 6;
        else if (Objects.equals(color, "violet")) a = 7;
        else if (Objects.equals(color, "grey")) a = 8;
        else if (Objects.equals(color, "white")) a = 9;
        else a = -1;

        //System.out.println(a);
        result *= Math.pow(10, a);


        System.out.print(result);
    }
}
