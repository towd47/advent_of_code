public class AdventDay1 {
	private static String input;
	private static int part;
	public static void main(String[] args) {
		part = 0;
		if (args.length > 0) {
			input = args[0];
		}
		else {
			input = "";
		}
		if (args.length > 1) {
			part = Integer.parseInt(args[1]);
		}
		if (part == 0) {
			System.out.println(captchaSum());
		}
		else {
			System.out.println(captchaSum2());
		}
	}

	public static int captchaSum() {
		int sum = 0;
		String[] inputArray = input.split("");
		int[] inputNumArray = new int[inputArray.length];
		for (int i = 0; i < inputArray.length; i++) {
			inputNumArray[i] = Integer.parseInt(inputArray[i]);
		}
		for(int i = 0; i < inputNumArray.length; i++) {
			int j;
			if (i == inputNumArray.length - 1) {
				j = 0;
			}
			else {
				j = i + 1;
			}
			if (inputNumArray[i] == inputNumArray[j]) {
				sum = sum + inputNumArray[i];
			}
		}
		return sum;
	}

	public static int captchaSum2() {
		int sum = 0;
		String[] inputArray = input.split("");
		int[] inputNumArray = new int[inputArray.length];
		for (int i = 0; i < inputArray.length; i++) {
			inputNumArray[i] = Integer.parseInt(inputArray[i]);
		}
		for(int i = 0; i < inputNumArray.length / 2; i++) {
			int j = inputNumArray.length / 2 + i;
			if (inputNumArray[i] == inputNumArray[j]) {
				sum = sum + inputNumArray[i];
			}
		}
		return sum;
	}
}