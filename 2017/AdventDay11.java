import java.util.*;

public class AdventDay11 {
	private static String[] steps;
	private static int ringNumber;
	private static int positionInRing;
	private static int largestDistance;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay11.txt");
		steps = reader.contentAsString().split(",");
		ringNumber = 0;
		positionInRing = 0;
		largestDistance = 0;

		for (String step: steps) {
			updatePosition(step);
			if (ringNumber > largestDistance) {
				largestDistance = ringNumber;
			}
		}
		System.out.println("Steps: " + steps.length);
		System.out.println("Ring: " + ringNumber);
		System.out.println("Position: " + positionInRing);
		System.out.println("Furthest distance: " + largestDistance);
	}

	private static void updatePosition(String direction) {
		switch (direction) {
			case "n":
				if (positionInRing <= ringNumber || positionInRing >= ringNumber * 5) {
					if (positionInRing >= ringNumber * 5) {
						positionInRing += 6;
					}
					ringNumber++;
				} else if (positionInRing > ringNumber && positionInRing <= ringNumber * 2) {
					positionInRing--;
				} else if (positionInRing > ringNumber * 4 && positionInRing < ringNumber * 5) {
					positionInRing++;
				} else {
					ringNumber--;
					positionInRing -= 3;
				}
				break;
			case "ne":
				if (positionInRing >= 0 && positionInRing <= ringNumber * 2) {
					ringNumber++;
					positionInRing++;
				} else if (positionInRing > ringNumber * 2 && positionInRing <= ringNumber * 3) {
					positionInRing--;
				} else if (positionInRing >= ringNumber * 5) {
					positionInRing++;
				} else {
					ringNumber--;
					positionInRing -= 4;
				}
				break;
			case "se":
				if (positionInRing >= ringNumber && positionInRing <= ringNumber * 3) {
					ringNumber++;
					positionInRing += 2;
				} else if (positionInRing > ringNumber * 3 && positionInRing <= ringNumber * 4) {
					positionInRing--;
				} else if (positionInRing >= 0 && positionInRing < ringNumber) {
					positionInRing++;
				} else {
					ringNumber--;
					positionInRing -= 5;
				}
				break;
			case "s":
				if (positionInRing >= ringNumber * 2 && positionInRing <= ringNumber * 4) {
					ringNumber++;
					positionInRing += 3;
				} else if (positionInRing >= ringNumber && positionInRing < ringNumber * 2) {
					positionInRing++;
				} else if (positionInRing > ringNumber * 4 && positionInRing <= ringNumber * 5) {
					positionInRing--;
				} else {
					ringNumber--;
					if (positionInRing > ringNumber * 5) {
						positionInRing -= 6;
					}
				}
				break;
			case "sw":
				if (positionInRing >= ringNumber * 3 && positionInRing <= ringNumber * 5) {
					ringNumber++;
					positionInRing += 4;
				} else if (positionInRing >= ringNumber * 2 && positionInRing < ringNumber * 3) {
					positionInRing++;
				} else if (positionInRing > ringNumber * 5 || positionInRing == 0) {
					positionInRing--;
					if (positionInRing < 0) {
						positionInRing += ringNumber * 6;
					}
				} else {
					ringNumber--;
					positionInRing--;
				}
				break;
			case "nw":
				if (positionInRing >= ringNumber * 4 || positionInRing == 0) {
					if (positionInRing == 0) {
						positionInRing += ringNumber * 6;
					}
					ringNumber++;
					positionInRing += 5;
				} else if (positionInRing <= ringNumber) {
					positionInRing--;
				} else if (positionInRing >= ringNumber * 3) {
					positionInRing++;
				} else {
					ringNumber--;
					positionInRing -= 2;
				}
				break;
			default:
				System.out.println(direction);
		}
	}
}