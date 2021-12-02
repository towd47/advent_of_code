#include <iostream>
#include <fstream>
#include <string>
#include <vector>


int day_1_part_1();

int day_1_part_2();

int sum(std::vector<int> v);

int main(int argc, char const *argv[])
{
	int day_1_answer = day_1_part_1();

	std::cout << "Day 1 Part 1 answer: " << day_1_answer << "\n";

	int day_1_2_answer = day_1_part_2();

	std::cout << "Day 1 Part 2 answer: " << day_1_2_answer << "\n";

	return 0;
}

int day_1_part_1() {
	std::string line;
	std::ifstream day_1_input ("day_1_input.txt");

	int higher_than_count = 0;

	if (day_1_input.is_open()) {
		int last;
		getline(day_1_input, line);

		last = std::stoi(line);
		while (getline (day_1_input, line)) {
			int next = std::stoi(line);
			if (next > last)
				higher_than_count++;
			last = next;
		}

		day_1_input.close();
	}

	return higher_than_count;
}

int day_1_part_2() {
	std::string line;
	std::ifstream day_1_input("day_1_input.txt");
	int higher_than_count = 0;

	if (day_1_input.is_open()) {
		std::vector<int> v;
		int last;

		while (v.size() < 3) {
			getline(day_1_input, line);
			last = std::stoi(line);
			v.push_back(last);
		}
		last = sum(v);
		while (getline(day_1_input, line)) {
			v.erase(v.begin());
			int next = std::stoi(line);
			v.push_back(next);
			int next_sum = sum(v);
			
			if (next_sum > last)
				higher_than_count++;

			last = next_sum;
		}

		day_1_input.close();
	}
	return higher_than_count;
}

int sum(std::vector<int> v) {
	int total = 0;
	for (int e : v)
		total += e;
	return total;
}



