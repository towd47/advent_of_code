import java.util.*;

public class AdventDay14 {
	
	public static void main(String[] args) {
		String input = args[0];
		int occupied = 0;
		int grid[][] = new int[128][128];

		for (int i = 0; i < 128; i++) {
			String inputForI = input + "-" + i;
			grid = occupiedInRow(knotHash(inputForI), grid, i);
		}

		System.out.println("Number of regions: " + getNumRegions(grid));
	}

	private static int getNumRegions(int[][] grid) {
		int regions = 0;
		LinkedList<Coord> queue = new LinkedList<Coord>();
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[0].length; j++) {
				if (grid[i][j] == 1) {
					queue.add(new Coord(i, j));
					regions++;
				}
				while (queue.peek() != null) {
					Coord coord = queue.poll();
					if (coord.x > 0 && grid[coord.x - 1][coord.y] == 1) {
						queue.add(new Coord(coord.x - 1, coord.y));
					}
					if (coord.y > 0 && grid[coord.x][coord.y-1] == 1) {
						queue.add(new Coord(coord.x, coord.y - 1));
					}
					if (coord.x < grid.length - 1 && grid[coord.x + 1][coord.y] == 1) {
						queue.add(new Coord(coord.x + 1, coord.y));
					}
					if (coord.y < grid[0].length - 1 && grid[coord.x][coord.y + 1] == 1) {
						queue.add(new Coord(coord.x, coord.y + 1));
					}
					grid[coord.x][coord.y] = 0;
				}
			}
		}
		return regions;
	}

	private static int[][] occupiedInRow(String hash, int[][] grid, int row) {

		String binary = "";
		for (int i = 0; i < hash.length(); i++) {
			String hex = hash.substring(i, i+1);
			int decimal = Integer.parseInt(hex, 16);
			String bi = Integer.toBinaryString(decimal);
			while (bi.length() < 4) {
				bi = "0" + bi;
			}
			binary = binary + bi;
		}
		
		for (int i = 0; i < binary.length(); i++) {
			if (binary.charAt(i) == '1') {
				grid[row][i] = 1;
			}
		}
		return grid;
	}

	private static String knotHash(String input) {
		int currentPosition = 0;
		int skipSize = 0;

		int[] list = new int[256];
		for (int i = 0; i < list.length; i++) {
			list[i] = i;
		}

		int[] inputs = new int[input.length() + 5];
		for (int i = 0; i < input.length(); i++) {
			inputs[i] = (int)input.charAt(i);
		}
		inputs[input.length()] = 17;
		inputs[input.length() + 1] = 31;
		inputs[input.length() + 2] = 73;
		inputs[input.length() + 3] = 47;
		inputs[input.length() + 4] = 23;

		for (int j = 0; j < 64; j++) {
			for (int i = 0; i < inputs.length; i++) {
				reverseSection(currentPosition, inputs[i], list);
				currentPosition = (currentPosition + inputs[i] + skipSize) % list.length;
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

	private static void reverseSection(int currentPosition, int length, int[] list) {
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