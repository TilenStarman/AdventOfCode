import java.io.*;

public class Day2 {
    public static void main(String[] args) throws IOException {
        String vhodnaDatoteka = args[0];
        BufferedReader vhod = new BufferedReader(new FileReader(vhodnaDatoteka));
        String vrstica;

        int vsota = 0;


        while ((vrstica = vhod.readLine()) != null) {
            
            String[] vrst = vrstica.split(" ");
            String njegovo = vrst[0];
            String moje = vrst[1];

            if (moje.equals("X")) vsota += 1;
            else if (moje.equals("Y")) vsota += 2;
            else if (moje.equals("Z")) vsota += 3;

            if (njegovo.equals("A") && moje.equals("X")) vsota += 3;
            else if (njegovo.equals("A") && moje.equals("Y")) vsota += 6;
            else if (njegovo.equals("A") && moje.equals("Z")) vsota += 0;

            if (njegovo.equals("B") && moje.equals("X")) vsota += 0;
            else if (njegovo.equals("B") && moje.equals("Y")) vsota += 3;
            else if (njegovo.equals("B") && moje.equals("Z")) vsota += 6;

            if (njegovo.equals("C") && moje.equals("X")) vsota += 6;
            else if (njegovo.equals("C") && moje.equals("Y")) vsota += 0;
            else if (njegovo.equals("C") && moje.equals("Z")) vsota += 3;


        }

        System.out.println(vsota);
        
    }


}
