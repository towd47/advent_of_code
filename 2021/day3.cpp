#include <vector>
#include <string>
#include <iterator>
#include <fstream>
#include <iostream>
#include <bitset>

int day_3_part_1();

int main(int argc, char const *argv[])
{
	auto part_1_answer = day_3_part_1();

	std::cout << "Day 3 Part 1: " << part_1_answer << std::endl;
	return 0;
}

int day_3_part_1() {
	std::string word;
	std::ifstream day_3_input ("day_3_input.txt");

	std::vector<std::string> data;

	while (day_3_input >> word) {
		data.push_back(word);
	}

	std::string s = data.at(0);
	std::vector<int> counts(s.size(), 0);
	for (std::string e : data) {
		for (int i = 0; i < e.size(); i++) {
			if (e.at(i) == '1')
				counts[i] += 1;
			else
				counts[i] -= 1;
		}
	}

	std::string binary;
	for (auto e : counts) {
		if (e > 0)
			binary.append("1");
		else
			binary.append("0");
	}

	std::bitset<12> b3(binary);

	return b3.to_ulong() * b3.flip().to_ulong();
}
