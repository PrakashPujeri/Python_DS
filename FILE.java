import java.io.File;
import java.io.FileWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.Writer;
import java.util.Scanner;

public class FILE {
    public static void main(String[] args) throws IOException {
        File file=new File("C:/Users/Prakash/Documents/rcb.txt");
        FileInputStream f=new FileInputStream(file);
        Scanner sc= new Scanner(f);
        StringBuffer b=new StringBuffer();
        while (sc.hasNextLine()){
            b.append(" "+sc.nextLine());
        }
        System.out.println(b);
        File d=new File("C:/Users/Prakash/Documents/rcb.txt");
        FileWriter writer=new FileWriter(d);
        writer.write(b.toString());
        writer.close();
        
    System.out.println("successfulyy...");
     }
    }

