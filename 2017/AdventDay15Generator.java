public class AdventDay15Generator {
	private int lastVal;
	private int multiplier;
	private int mustBeMultipleOf;

	public AdventDay15Generator(int startingVal, int multiplier, int mustBeMultipleOf) {
		lastVal = startingVal;
		this.multiplier = multiplier;
		this.mustBeMultipleOf = mustBeMultipleOf;
	}

	public int getNext() {
		lastVal = (int)(((long)lastVal * (long)multiplier) % 2147483647);
		while (lastVal % mustBeMultipleOf != 0) {
			lastVal = (int)(((long)lastVal * (long)multiplier) % 2147483647);
		}
		return lastVal;
	}
}