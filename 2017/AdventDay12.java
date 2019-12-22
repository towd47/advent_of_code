import java.util.*;

public class AdventDay12 {
	private static ArrayList<int[]> programs;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay12.txt");
		String[] inputs = reader.toStringArray();
		programs = new ArrayList<int[]>();
		for (String s: inputs) {
			String[] input = s.split(" ");
			int[] connections = new int[input.length - 2];
			for (int i = 0; i < connections.length; i++) {
				if (input[i+2].charAt(input[i+2].length() - 1) == ',') {
					input[i+2] = input[i+2].substring(0,input[i+2].length() - 1);
				}
				connections[i] = Integer.parseInt(input[i+2]);
			}
			programs.add(connections);
		}

		int numberOfGroups = 0;
		int currentProgram = 0;
		HashSet<Integer> set = new HashSet<Integer>();
		while (currentProgram < programs.size()) {
			if (set.contains(currentProgram)) {
				currentProgram++;
			} else {
				set.addAll(programsInGroup(currentProgram));
				numberOfGroups++;
			}
		}

		System.out.println(numberOfGroups);
	}

	private static HashSet<Integer> programsInGroup(int firstProgram) {
		HashSet<Integer> set = new HashSet<Integer>();
		PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
		queue.add(firstProgram);
		set.add(firstProgram);
		while (queue.peek() != null) {
			int currentProgram = queue.poll();
			for (int connection: programs.get(currentProgram)) {
				if (set.add(connection)) {
					queue.add(connection);
				}
			}
		}
		return set;
	}
}