#include <vector>
#include <string>
#include <iterator>
#include <fstream>
#include <iostream>
#include <bitset>
#include <iterator>

int day_3_part_1(std::vector<std::string> data);
int day_3_part_2(std::vector<std::string> data);
std::vector<std::string> get_input();
std::string most_common_or_least_common_by_bit(std::vector<std::string> data, bool most);

char most_common_bit_at(std::vector<std::string> v, int pos);

int main(int argc, char const *argv[])
{
	std::vector<std::string> data = get_input();

	auto part_1_answer = day_3_part_1(data);
	auto part_2_answer = day_3_part_2(data);

	std::cout << "Day 3 Part 1: " << part_1_answer << std::endl;
	std::cout << "Day 3 Part 2: " << part_2_answer << std::endl;

	return 0;
}

std::vector<std::string> get_input() {
	std::string word;
	std::ifstream day_3_input ("day_3_input.txt");

	std::vector<std::string> data;

	while (day_3_input >> word) {
		data.push_back(word);
	}

	return data;
}

int day_3_part_1(std::vector<std::string> data) {
	std::string binary;
	for (int i = 0; i < data.at(0).size(); i++) {
		binary.push_back(most_common_bit_at(data, i));
	}

	std::bitset<12> b3(binary);

	return b3.to_ulong() * b3.flip().to_ulong();
}

int day_3_part_2(std::vector<std::string> data) {

	std::string oxygen_value = most_common_or_least_common_by_bit(data, true);
	std::string co2_value = most_common_or_least_common_by_bit(data, false);

	std::bitset<12> oxygen(oxygen_value);
	std::bitset<12> co2(co2_value);

	return oxygen.to_ulong() * co2.to_ulong();

}

std::string most_common_or_least_common_by_bit(std::vector<std::string> v, bool most) {
	int pos = 0;

	while (v.size() > 1) {
		char most_common_bit = most_common_bit_at(v, pos);

		for (auto it = begin(v); it != end(v); ) {
			if (most) {
				if (it -> at(pos) != most_common_bit)
					it = v.erase(it);
				else
					it++;
			}
			else {
				if (it -> at(pos) == most_common_bit)
					it = v.erase(it);
				else
					it++;
			}
		}
		pos++;
	}

	return v.at(0);
}

char most_common_bit_at(std::vector<std::string> v, int pos) {
	int swing = 0;
	for (auto e : v) {
		if (e.at(pos) == '1')
			swing += 1;
		else
			swing -= 1;
	}

	if (swing < 0)
		return '0';
	return '1';
}

