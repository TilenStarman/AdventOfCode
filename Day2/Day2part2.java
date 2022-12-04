import java.io.*;

public class Day2part2 {
    public static void main(String[] args) throws IOException {
        String vhodnaDatoteka = args[0];
        BufferedReader vhod = new BufferedReader(new FileReader(vhodnaDatoteka));
        String vrstica;

        int vsota = 0;


        while ((vrstica = vhod.readLine()) != null) {
            
            String[] vrst = vrstica.split(" ");
            String njegovo = vrst[0];
            String moje = vrst[1];

            if (moje.equals("X")) {
                vsota += 0;

                if (njegovo.equals("A")) vsota += 3;
                else if (njegovo.equals("B")) vsota += 1;
                else if (njegovo.equals("C")) vsota += 2;

            }

            else if (moje.equals("Y")) {
                vsota += 3;

                if (njegovo.equals("A")) vsota += 1;
                else if (njegovo.equals("B")) vsota += 2;
                else if (njegovo.equals("C")) vsota += 3;

            }

            else if (moje.equals("Z")) {
                vsota += 6;

                if (njegovo.equals("A")) vsota += 2;
                else if (njegovo.equals("B")) vsota += 3;
                else if (njegovo.equals("C")) vsota += 1;

            }



        }

        System.out.println(vsota);
        
    }


}
