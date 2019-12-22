import java.util.*;

public class AdventDay15 {
	private static AdventDay15Generator genA;
	private static AdventDay15Generator genB;

	public static void main(String[] args) {
		genA = new AdventDay15Generator(618, 16807, 4);
		genB = new AdventDay15Generator(814, 48271, 8);

		int repititions = 0;
		int matches = 0;
		while (repititions < 5000000) {
			if (same16Bits()) {
				matches++;
			}
			repititions++;
		}

		System.out.println("Matches: " + matches);
	}

	public static boolean same16Bits() {
		String binaryA = Integer.toBinaryString(genA.getNext());
		String binaryB = Integer.toBinaryString(genB.getNext());
		while (binaryA.length() < 16) {
			binaryA = "0" + binaryA;
		}
		while (binaryB.length() < 16) {
			binaryB = "0" + binaryB;
		}
		if (binaryA.length() > 16) {
			binaryA = binaryA.substring(binaryA.length() - 16);
		}
		if (binaryB.length() > 16) {
			binaryB = binaryB.substring(binaryB.length() - 16);
		}
		return binaryA.equals(binaryB);
	}
}