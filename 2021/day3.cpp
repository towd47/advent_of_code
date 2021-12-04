#include <vector>
#include <string>
#include <iterator>
#include <fstream>
#include <iostream>
#include <bitset>
#include <iterator>
#include <cstring>

int day_3_part_1();

int day_3_part_2();

char most_common_bit_at(std::vector<std::string> v, int pos);

int main(int argc, char const *argv[])
{
	auto part_1_answer = day_3_part_1();

	std::cout << "Day 3 Part 1: " << part_1_answer << std::endl;

	auto part_2_answer = day_3_part_2();

	std::cout << "Day 3 Part 2: " << part_2_answer << std::endl;

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

int day_3_part_2() {
	std::string word;
	std::ifstream day_3_input ("day_3_input.txt");

	std::vector<std::string> data;

	while (day_3_input >> word) {
		data.push_back(word);
	}

	std::vector<std::string> oxygen_values;
	std::vector<std::string> co2_values;

	char most_common_bit = most_common_bit_at(data, 0);

	for (auto e : data) {
		if (e.at(0) == most_common_bit) {
			oxygen_values.push_back(e);
		}
		else 
			co2_values.push_back(e);
	}

	int pos = 1;
	while (oxygen_values.size() > 1) {
		most_common_bit = most_common_bit_at(oxygen_values, pos);

		for (auto it = begin(oxygen_values); it != end (oxygen_values); ) {
			if (it -> at(pos) != most_common_bit)
				it = oxygen_values.erase(it);
			else
				it++;
		}

		pos++;
	}

	pos = 1;
	while (co2_values.size() > 1) {
		most_common_bit = most_common_bit_at(co2_values, pos);

		for (auto it = begin(co2_values); it != end (co2_values); ) {
			if (it -> at(pos) == most_common_bit)
				it = co2_values.erase(it);
			else
				it++;
		}

		pos++;
	}

	std::bitset<12> oxygen(oxygen_values.at(0));
	std::bitset<12> co2(co2_values.at(0));

	return oxygen.to_ulong() * co2.to_ulong();

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







