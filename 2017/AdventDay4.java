import java.util.*;
import java.io.*;

public class AdventDay4 {
	private static String[] input;

	public static void main(String[] args) {
		input = readFromFile("AdventDay4.txt");
		System.out.println(getNumValid(input));
	}

	public static String[] readFromFile(String fileName) {
		Scanner fileReader;
		ArrayList<String> lines = new ArrayList<String>();
		try {
			fileReader = new Scanner(new File(fileName));

			while (fileReader.hasNextLine()) {
				String line = fileReader.nextLine();
				lines.add(line);
			}
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return lines.toArray(new String[0]);
	}

	public static int getNumValid(String[] input) {
		int sum = 0;
		for (int i = 0; i < input.length; i++) {
			String[] passphrase = input[i].split(" ");
			HashSet<String> words = new HashSet<String>();
			for (int j = 0; j < passphrase.length; j++) {
				char[] chars = passphrase[j].toCharArray();
				Arrays.sort(chars);
				String sorted = new String(chars);
				if(!words.add(sorted)) {
					j = passphrase.length;
				}
				if(j == passphrase.length - 1) {
					sum++;
				}
			}
		}
		return sum;
	}
}