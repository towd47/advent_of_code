public class AdventDay3 {
	public static void main(String[] args) {
		int input = Integer.parseInt(args[0]);
		//part1(input);
		part2(input);
	}

	public static void part2(int input) {
		int[][] grid = new int[3][3];
		int x = 1;
		int y = 1;
		grid[x][y] = 1;
		y++;
		int next = fillNext(grid, x, y);
		while (next <= input) {
			grid[x][y] = next;
			if (x == grid.length - 1 && y == x){
				grid = increaseGrid(grid);
				//printGrid(grid);
				x++;
				y++;
			}
			if (y < grid.length - 1 && grid[x][y+1] == 0) {
				y++;
			}
			else if (x > 0 && grid[x-1][y] == 0) {
				x--;
			}
			else if (y > 0 && grid[x][y-1] == 0) {
				y--;
			}
			else {
				x++;
			}
			next = fillNext(grid, x, y);
		}
		System.out.println(next);
	}

	public static int fillNext(int[][] grid, int x, int y) {
		int sum = 0;
		if (x - 1 >= 0) {
			sum += grid[x-1][y];
			if (y - 1 >= 0) {
				sum += grid[x-1][y-1];
			}
			if (y + 1 < grid.length) {
				sum += grid[x-1][y+1];
			}
		}
		if (x + 1 < grid.length) {
			sum += grid[x+1][y];
			if (y - 1 >= 0) {
				sum += grid[x+1][y-1];
			}
			if (y + 1 < grid.length) {
				sum += grid[x+1][y+1];
			}
		}
		if (y -1 >= 0) {
			sum += grid[x][y-1];
		}
		if (y + 1 < grid.length) {
			sum += grid[x][y+1];
		}
		return sum;
	}

	public static int[][] increaseGrid(int[][] grid) {
		int[][] newGrid = new int[grid.length+2][grid.length+2];
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid.length; j++) {
				newGrid[i+1][j+1] = grid[i][j];
			}
		}
		return newGrid;
	}

	public static void part1(int input) {
		if (input == 1) {
			System.out.println(0);
			return;
		}
		int highCap = 1;
		while (highCap * highCap < input) {
			highCap += 2;
		}
		int numsInRow = (highCap - 1) / 2 * 8;
		int diffBetweenHighCapAndInput = highCap * highCap - input;
		int offset = diffBetweenHighCapAndInput % (highCap - 1);
		if (offset > (highCap - 1)/2) {
			offset = highCap - 1 - offset;
		}
		System.out.println("Part1: " + ((highCap - 1) - offset));
	}

	public static void printGrid(int[][] grid) {
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid.length; j++) {
				System.out.print(grid[i][j] + " ");
			}
			System.out.println();
		}
	}
}