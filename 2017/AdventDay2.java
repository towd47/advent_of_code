public class AdventDay2 {
	public static void main(String[] args) {
		int sum = 0;
		int sum2 = 0;
		String input = args[0];
		String[] rows = input.split(",");
		for (int i = 0; i < rows.length; i++) {
			int high = 0;
			int low = 0;
			String[] rowVals = rows[i].split("-");
			low = Integer.parseInt(rowVals[0]);
			for (int j = 0; j < rowVals.length - 1; j++) {
				for (int k = j + 1; k < rowVals.length; k++) {
					if (Integer.parseInt(rowVals[j]) % Integer.parseInt(rowVals[k]) == 0) {
						sum2 = sum2 + Integer.parseInt(rowVals[j]) / Integer.parseInt(rowVals[k]);
						k = rowVals.length;
						j = rowVals.length;
					}
					else if (Integer.parseInt(rowVals[k]) % Integer.parseInt(rowVals[j]) == 0) {
						sum2 = sum2 + Integer.parseInt(rowVals[k]) / Integer.parseInt(rowVals[j]);
						k = rowVals.length;
						j = rowVals.length;
					}
				}
				/*if (Integer.parseInt(rowVals[j]) > high) {
					high = Integer.parseInt(rowVals[j]);
				}
				else if (Integer.parseInt(rowVals[j]) < low) {
					low = Integer.parseInt(rowVals[j]);
				}*/
			}
			sum = sum + high - low;
		}
		System.out.println("Checksum: " + sum);
		System.out.println("Even sums: " + sum2);
	}
}