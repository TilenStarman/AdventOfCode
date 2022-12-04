import java.io.*;

public class Day1 {
    public static void main(String[] args) throws IOException {
        String vhodnaDatoteka = args[0];
        BufferedReader vhod = new BufferedReader(new FileReader(vhodnaDatoteka));
        String vrstica;


        int vsota = 0;
        int i = 0;
        int cal = 0;

        int[] a = new int[1000];

        while ((vrstica = vhod.readLine()) != null) {
            
            if (!vrstica.trim().equals("")) {
                cal = Integer.parseInt(vrstica);
                vsota += cal;
            }

            else {
                
                a[i] = vsota;
                i++;

                vsota = 0;
            }

        }

        // umazan fix
        if (vsota != 0) a[i] = vsota;

        // sort array a
        sort(a, i);

        int rez = a[i-2] + a[i-1] + a[i];
        System.out.println(rez);
        
    }

    public static int[] sort(int[] a, int length) {

        for (int i = 0; i < length - 1; i++) {
            for (int j = 0; j <= length - i - 1; j++) {
                if (a[j] > a[j+1]) {
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                }
            }
        }


        return a;
    }

}
