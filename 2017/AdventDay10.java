public class AdventDay10 {

	private static int[] inputLengths;
	private static int[] list;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay10.txt");
		String input = reader.contentAsString();
		inputLengths = new int[input.length() + 5];
		for (int i = 0; i < input.length(); i++) {
			inputLengths[i] = (int)input.charAt(i);
		}
		inputLengths[input.length()] = 17;
		inputLengths[input.length() + 1] = 31;
		inputLengths[input.length() + 2] = 73;
		inputLengths[input.length() + 3] = 47;
		inputLengths[input.length() + 4] = 23;

		list = new int[256];
		for (int i = 0; i < list.length; i++) {
			list[i] = i;
		}

		System.out.println(knotHash());

	}

	private static String knotHash() {
		int currentPosition = 0;
		int skipSize = 0;

		for (int j = 0; j < 64; j++) {
			for (int i = 0; i < inputLengths.length; i++) {
				reverseSection(currentPosition, inputLengths[i]);
				currentPosition = (currentPosition + inputLengths[i] + skipSize) % list.length;
				skipSize++;
			}
		}

		String hash = "";
		for (int i = 0; i < 16; i++) {
			int val = 0;
			for (int j = 0; j < 16; j++) {
				if (j == 0) {
					val = list[16 * i];
				}
				else {
					val = val ^ list[16 * i + j];
				}
			}
			if (Integer.toHexString(val).length() < 2) {
				hash = hash + "0";
			}
			hash = hash + Integer.toHexString(val);
		}
		return hash;
	}

	private static void reverseSection(int currentPosition, int length) {
		if (length > list.length) {
			return;
		}
		int[] sectionToReverse = new int[length];
		for (int i = 0; i < length; i++) {
			sectionToReverse[i] = list[(currentPosition + i) % list.length];
		}
		for (int i = 0; i < length; i++) {
			list[(currentPosition + i) % list.length] = sectionToReverse[length - 1 - i];
		}
	}
}