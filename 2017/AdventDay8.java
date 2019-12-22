import java.util.*;
import java.io.*;

public class AdventDay8 {
	private static String[] inputs;
	private static ArrayList<String[]> commands;
	private static ArrayList<AdventDay8Register> registers;
	private static int highest;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay8.txt");
		inputs = reader.toStringArray();

		convertInputs();
		highest = 0;

		for (String[] s: commands) {
			doCommand(s);
		}

		System.out.println("Highest during: " + highest);
		System.out.println("Highest at end: " + findHighestVal());
	}

	private static void convertInputs() {
		HashSet<String> registerNames = new HashSet<String>();
		registers = new ArrayList<AdventDay8Register>();
		commands = new ArrayList<String[]>();
		for (String s: inputs) {
			String[] input = s.split(" ");
			if (registerNames.add(input[0])) {
				AdventDay8Register register = new AdventDay8Register(input[0]);
				registers.add(register);
			}
			String[] command = new String[6];
			command[0] = input[4];
			command[1] = input[5];
			command[2] = input[6];
			command[3] = input[1];
			command[4] = input[2];
			command[5] = input[0];
			commands.add(command);
		}
	}

	private static int findHighestVal() {
		int highest = -10000000;
		for (AdventDay8Register reg: registers) {
			if (reg.value > highest) {
				highest = reg.value;
			}
		}
		return highest;
	}

	private static void doCommand(String[] command) {
		AdventDay8Register reg = new AdventDay8Register("");
		AdventDay8Register regToChange = new AdventDay8Register("");
		for (AdventDay8Register register: registers) {
			if (command[0].equals(register.name)) {
				reg = register;
			}
			if (command[5].equals(register.name)) {
				regToChange = register;
			}
		}
		int compareVal = Integer.parseInt(command[2]);
		boolean shouldDoCommand = false;

		if (command[1].equals("==")) {
			shouldDoCommand = (reg.value == compareVal);
		} else if (command[1].equals("!=")) {
			shouldDoCommand = (reg.value != compareVal);
		} else if (command[1].equals(">")) {
			shouldDoCommand = (reg.value > compareVal);
		} else if (command[1].equals(">=")) {
			shouldDoCommand = (reg.value >= compareVal);
		} else if (command[1].equals("<")) {
			shouldDoCommand = (reg.value < compareVal);
		} else if (command[1].equals("<=")) {
			shouldDoCommand = (reg.value <= compareVal);
		} else {
			System.out.println("ERROR");
		}

		if (shouldDoCommand) {
			if (command[3].equals("inc")) {
				regToChange.value += Integer.parseInt(command[4]);
			}
			else {
				regToChange.value -= Integer.parseInt(command[4]);
			}
			if (regToChange.value > highest) {
				highest = regToChange.value;
			}
		}
	}
}