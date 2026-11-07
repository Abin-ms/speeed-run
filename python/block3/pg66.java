import java.util.Arrays;
import java.util.Scanner;
public class pg66 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first string : ");
        String s1 = sc.nextLine();
        System.out.println("Enter the second string : ");
        String s2 = sc.nextLine();
        if(s1.length()!=s2.length()){
            System.out.println("String1 and string2 are not Anagrams!!!");
            return;
        }
        char[] s1Array = s1.toCharArray();
        char[] s2Array = s2.toCharArray();
        Arrays.sort(s1Array);
        Arrays.sort(s2Array);

        if(Arrays.equals(s1Array,s2Array)){
            System.out.println("string1 and string2 are anagrams ");
        }
        
    }
}
