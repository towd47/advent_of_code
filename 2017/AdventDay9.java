import java.util.*;

public class AdventDay9 {

	private static String input;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay9.txt");
		input = reader.contentAsString();

		System.out.println(getScore(cleanUpInput()));
	}

	private static int getScore(String s) {
		int total = 0;
		int scoreValue = 1;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '{') {
				total += scoreValue;
				scoreValue++;
			} else if (s.charAt(i) == '}') {
				scoreValue--;
			}
		}
		return total;
	}

	private static String cleanUpInput() {
		String cleanedUp = input.replaceAll("!!", "");
		cleanedUp = cleanedUp.replaceAll("!.", "");

		int garbageArrows = 0;

		for (int i = 0; i < cleanedUp.length(); i++) {
			if (cleanedUp.charAt(i) == '>') {
				garbageArrows++;
			}
		}
		int garbageChars = cleanedUp.length();
		cleanedUp = cleanedUp.replaceAll("<.*?>", "");
		garbageChars = garbageChars - cleanedUp.length() - garbageArrows * 2;
		System.out.println("Number of garbage characters: " + garbageChars);

		return cleanedUp;
	}
}