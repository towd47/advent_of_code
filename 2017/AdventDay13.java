import java.util.*;

public class AdventDay13 {

	private static int[] layers;
	private static int severityScore;
	private static int collisionIfOffset[];

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay13.txt");
		String[] inputs = reader.toStringArray();
		layers = new int[Integer.parseInt(inputs[inputs.length -1].split(":")[0]) + 1];
		for (String s: inputs) {
			layers[Integer.parseInt(s.split(":")[0])] = Integer.parseInt(s.split(": ")[1]);
		}

		int[] movesToHit = new int[layers.length];
		collisionIfOffset = new int[10000000];
		int offset = 0;

		for (int i = 0; i < layers.length; i++) {
			if (layers[i] == 0) {
				movesToHit[i] = 1;
			} else {
				offset = 0;
				while (scannerPos(i, offset) != 0) {
					offset++;
				}
				movesToHit[i] = i + offset;
			}
		}
		
		severityScore = 0;
		for (int i = 0; i < layers.length; i++) {
			if (layers[i] != 0 && scannerPos(i, offset) == 0) {
			
				severityScore += i * layers[i];
			}
		}

		fillCollisionIfOffset();
		for (int i = 0; i < collisionIfOffset.length; i++) {
			if (collisionIfOffset[i] == 0) {
				System.out.println("Pass through at offset of: " + i);
				break;
			}
		}

		//System.out.println("offset: " + offset);
		System.out.println("severityScore: " + severityScore);
	}

	private static int scannerPos(int index, int offset) {

		int range = layers[index];
		int moves = index + offset;
		int pos = 0;
		boolean increasing = true;
		for (int i = 0; i < moves; i++) {
			if (increasing) {
				pos++;
			}
			else {
				pos--;
			}

			if (pos == range - 1) {
				increasing = false;
			}
			if (pos == 0) {
				increasing = true;
			}
		}
		return pos;
	}

	private static void fillCollisionIfOffset() {
		for (int i = 0; i < layers.length; i++) {
			if (layers[i] != 0) {
				int j = 0;
				while (getPos(i,j) < collisionIfOffset.length) {
					collisionIfOffset[getPos(i,j)] = 1;
					j++;
				}
			}
		}
	}

	private static int getPos(int x, int y) {
		if (x > 0) {
			return movesForLoop(layers[x]) * y + (movesForLoop(layers[x]) - (x%movesForLoop(layers[x])));
		}
		return movesForLoop(layers[x]) * y;
	}

	private static int movesForLoop(int n) { 
		return (n-1) * 2;
	}
}