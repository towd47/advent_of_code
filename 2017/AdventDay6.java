import java.util.*;
import java.io.*;

public class AdventDay6 {
	private static String input;
	public static void main(String[] args) {
		readFromFile("AdventDay6.txt");
		System.out.println(redistributionOfBlocksLoop());
	}

	public static int redistributionOfBlocks() {
		int redistributions = 0;
		String[] inputs = input.split(" ");
		int[] blocks = new int[inputs.length];
		for (int i = 0; i < inputs.length; i++) {
			blocks[i] = Integer.parseInt(inputs[i]);
		}
		HashSet<String> patterns = new HashSet<String>();
		while(patterns.add(intArrayToPattern(blocks))) {
			blocks = redistributeBlocks(blocks);
			redistributions++;
		}
		return redistributions;
	}

	public static int redistributionOfBlocksLoop() {
		int redistributions = 0;
		String[] inputs = input.split(" ");
		int[] blocks = new int[inputs.length];
		for (int i = 0; i < inputs.length; i++) {
			blocks[i] = Integer.parseInt(inputs[i]);
		}
		HashSet<String> patterns = new HashSet<String>();
		while(patterns.add(intArrayToPattern(blocks))) {
			blocks = redistributeBlocks(blocks);
		}
		String pattern = intArrayToPattern(blocks);
		blocks = redistributeBlocks(blocks);
		redistributions++;
		while(!intArrayToPattern(blocks).equals(pattern)) {
			blocks = redistributeBlocks(blocks);
			redistributions++;
		}
		return redistributions;
	}

	public static int[] redistributeBlocks(int[] blocks) {
		int max = blocks[0];
		int indexOfMax = 0;
		for (int i = 1; i < blocks.length; i++) {
			if (blocks[i] > max) {
				max = blocks[i];
				indexOfMax = i;
			}
		}
		int amountToAdd = max / 16;
		int remainder = max % 16;
		blocks[indexOfMax] = amountToAdd;
		for (int i = 1; i < blocks.length; i++) {
			int index = (indexOfMax + i) % 16;
			blocks[index] += amountToAdd;
			if (i <= remainder) {
				blocks[index]++;
			}
		}
		return blocks;

	}

	public static String intArrayToPattern(int[] blocks) {
		String pattern = "";
		for (int i = 0; i < blocks.length; i++) {
			pattern = pattern + blocks[i];
			if (i != blocks.length - 1) {
				pattern = pattern + " ";
			}
		}
		return pattern;
	}

	public static void readFromFile(String fileName) {
		Scanner fileReader;
		try {
			fileReader = new Scanner(new File(fileName));
			input = fileReader.nextLine();
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
}