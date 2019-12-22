import java.util.*;
import java.io.*;

public class FileReader {

	Scanner fileReader;

	public FileReader(String name) {
		try {
			fileReader = new Scanner(new File(name));
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public String[] toStringArray() {
		ArrayList<String> lines = new ArrayList<String>();
		
		if (fileReader == null) {
			return null;
		}

		while (fileReader.hasNextLine()) {
			String line = fileReader.nextLine();
			lines.add(line);
		}

		fileReader.close();

		return lines.toArray(new String[0]);
	}

	public String contentAsString() {
		String fileContent = "";
		while (fileReader.hasNextLine()) {
			fileContent = fileContent + fileReader.nextLine();
		}

		fileReader.close();

		return fileContent;
	}
}