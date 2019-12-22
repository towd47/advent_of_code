public class AdventDay7Node {
	public String name;
	public int weight;
	public int stackWeight;
	public String[] holding;
	public AdventDay7Node[] children;
	public AdventDay7Node parent;

	public AdventDay7Node(String input) {
		stackWeight = 0;
		String[] parts = input.split(" ");
		name = parts[0];
		weight = Integer.parseInt(parts[1].substring(1,parts[1].length() - 1));
		if (parts.length > 2) {
			holding = new String[parts.length - 3];
			children = new AdventDay7Node[holding.length];
			for (int i = 0; i < holding.length; i++) {
				holding[i] = parts[i+3];
				if (i != holding.length - 1) {
					holding[i] = holding[i].substring(0, holding[i].length() - 1);
				}
			}
		}
	}

	public void setChildren(AdventDay7Node[] children) {
		this.children = children;
	}
}