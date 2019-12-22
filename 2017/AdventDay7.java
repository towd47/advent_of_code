import java.io.*;
import java.util.*;

public class AdventDay7 {

	private static String[] input;
	private static AdventDay7Node[] nodes;

	public static void main(String[] args) {
		FileReader reader = new FileReader("AdventDay7.txt");
		input = reader.toStringArray();
		if (input == null) {
			System.out.println("Failed to find file.");
			return;
		}
		convertToNodes();
		setChildren();
		AdventDay7Node head = findBottom();
		setStackWeight(head);

		AdventDay7Node unbalancePoint = findUnbalancePoint(head);

		System.out.println("Unbalanced: " + unbalancePoint.name);
		for (int i = 0; i < unbalancePoint.children.length; i++) {
			System.out.println("Child: " + unbalancePoint.children[i].name + " stackWeight: " + unbalancePoint.children[i].stackWeight + " weight: " + unbalancePoint.children[i].weight);
		}
	}

	private static AdventDay7Node findUnbalancePoint(AdventDay7Node startingNode) {
		AdventDay7Node deepestUnbalanced = startingNode;
		if (!isBalanced(startingNode)) {
			for(int i = 0; i < startingNode.children.length; i++) {
				if (!isBalanced(startingNode.children[i])) {
					deepestUnbalanced = findUnbalancePoint(startingNode.children[i]);
					break;
				}
			}
		}
		return deepestUnbalanced;
	}

	private static boolean isBalanced(AdventDay7Node node) {
		if (node.children == null || node.children.length == 1) {
			return true;
		}

		int lastWeight = node.children[0].stackWeight;
		for (int i = 1; i < node.children.length; i++) {
			if (node.children[i].stackWeight != lastWeight) {
				return false;
			}
		}
		return true;
	}

	private static void setStackWeight(AdventDay7Node node) {
		node.stackWeight = node.weight;
		if (node.children != null) {
			for (int j = 0; j < node.children.length; j++) {
				if (node.children[j].stackWeight == 0) {
					setStackWeight(node.children[j]);
					node.stackWeight += node.children[j].stackWeight;
				}
			}
		}
	}

	private static AdventDay7Node findBottom() {
		HashSet<String> stackedNodes = new HashSet<String>();
		for (int i = 0; i < nodes.length; i++) {
			if (nodes[i].holding != null) {
				for (int j = 0; j < nodes[i].holding.length; j++) {
					stackedNodes.add(nodes[i].holding[j]);
				}
			}
		}
		for (int i = 0; i < nodes.length; i++) {
			if (!stackedNodes.contains(nodes[i].name)) {
				return nodes[i];
			}
		}
		return null;
	}

	private static void setChildren() {
		for (int i = 0; i < nodes.length; i++) {
			if (nodes[i].holding != null) {
				AdventDay7Node[] children = new AdventDay7Node[nodes[i].holding.length];
				for (int j = 0; j < nodes[i].holding.length; j++) {
					for (int k = 0; k < nodes.length; k++) {
						if (nodes[i].holding[j].equals(nodes[k].name)) {
							children[j] = nodes[k];
							nodes[k].parent = nodes[i];
						}
					}
				}
				nodes[i].setChildren(children);
			}
		}
	}

	private static void convertToNodes() {
		nodes = new AdventDay7Node[input.length];
		for (int i = 0; i < input.length; i++) {
			nodes[i] = new AdventDay7Node(input[i]);
		}
	}

	private static void printNodeDescriptions() {
		for (int i = 0; i < input.length; i++) {
			System.out.println(input[i]);
			System.out.println("Name: " + nodes[i].name + " Weight: " + nodes[i].weight);
			if (nodes[i].holding != null) {
				for (int j = 0; j < nodes[i].holding.length; j++) {
					System.out.println("Holding " + j + ": " + nodes[i].holding[j]);
					System.out.println("Child " + j + ": " + nodes[i].children[j].name);
				}
			}
		}
	}
}