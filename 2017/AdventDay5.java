import java.util.*;
import java.io.*;

public class AdventDay5 {
	static Integer[] input;
	public static void main(String[] args) {
		input = readFromFile("AdventDay5.txt");
		System.out.println(stepsToFindExitPart2());
	}
	
	public static Integer[] readFromFile(String fileName) {
		Scanner fileReader;
		ArrayList<Integer> lines = new ArrayList<Integer>();
		try {
			fileReader = new Scanner(new File(fileName));

			while (fileReader.hasNextLine()) {
				int line = Integer.parseInt(fileReader.nextLine());
				lines.add(line);
			}
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		return lines.toArray(new Integer[0]);
	}

	public static int stepsToFindExit() {
		int steps = 0;
		int index = 0;
		while (index >= 0 && index < input.length) {
			input[index]++;
			index += input[index] - 1;
			steps++;
		}
		return steps;
	}

	public static int stepsToFindExitPart2() {
		int steps = 0;
		int index = 0;
		while (index >= 0 && index < input.length) {
			int offset = input[index];
			if (offset >= 3) {
				input[index]--;
			}
			else {
				input[index]++;
			}
			index += offset;
			steps++;
		}
		return steps;
	}
}