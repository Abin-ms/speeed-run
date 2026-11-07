import java.util.Scanner;

public class pg44 {
    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);
        System.out.println("Enter the String : ");
        String s = ss.nextLine();
        int i = 0;
        int j = s.length() - 1;
        boolean is_palindrome = true;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                is_palindrome = false;
                break;
            }
            i++;
            j--;
        }
        if (is_palindrome) {
            System.out.println(s + " is palindrome...");
        } else {
            System.out.println(s + " is not palindrome...");
        }
        ss.close();
    }
}
