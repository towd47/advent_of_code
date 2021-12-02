#include <iostream>
#include <string>
#include <fstream>
#include <cstring>

int day_2_part_1();

int day_2_part_2();

int main(int argc, char const *argv[])
{
	int day_2_part_1_result = day_2_part_1();

	std::cout << "Day 2 Part 1: " << day_2_part_1_result << "\n";

	int day_2_part_2_result = day_2_part_2();

	std::cout << "Day 2 Part 2: " << day_2_part_2_result << "\n";

	return 0;
}

int day_2_part_1() {
	std::string word;
	std::ifstream day_2_input("day_2_input.txt");

	int forward = 0;
	int depth = 0;

	if (day_2_input.is_open()) {
		while (day_2_input >> word) {
			std::string direction = word;
			day_2_input >> word;
			int amnt = std::stoi(word);

			if (strncmp(&direction[0], "f", 1) == 0)
				forward += amnt;
			else if (strncmp(&direction[0], "d", 1) == 0)
				depth += amnt;
			else
				depth -= amnt;
		}
		day_2_input.close();
	}

	return forward * depth;
}

int day_2_part_2() {
	std::string word;
	std::ifstream day_2_input("day_2_input.txt");

	int forward = 0;
	int depth = 0;
	int aim = 0;

	if (day_2_input.is_open()) {
		while (day_2_input >> word) {
			std::string direction = word;
			day_2_input >> word;
			int amnt = std::stoi(word);

			if (strncmp(&direction[0], "f", 1) == 0) {
				forward += amnt;
				depth += aim * amnt;
			}
			else if (strncmp(&direction[0], "d", 1) == 0)
				aim += amnt;
			else
				aim -= amnt;
		}
		day_2_input.close();
	}

	return forward * depth;
}