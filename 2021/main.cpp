#include "day1.hpp"
#include "day2.hpp"
#include <iostream>


int main(int argc, char const *argv[])
{
	auto day_1_answer = day_1_part_1();
	auto day_1_2_answer = day_1_part_2();

	std::cout << "Day 1 Part 1: " << day_1_answer << std::endl;
	std::cout << "Day 1 Part 2: " << day_1_2_answer << std::endl;

	int day_2_part_1_result = day_2_part_1();
	int day_2_part_2_result = day_2_part_2();

	std::cout << "Day 2 Part 1: " << day_2_part_1_result << std::endl;
	std::cout << "Day 2 Part 2: " << day_2_part_2_result << std::endl;

	return 0;
}