#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<int> get_data();
int day_1_part_1();

int main()
{
	int day_1_part_1_answer = day_1_part_1();
	std::cout << day_1_part_1_answer << std::endl;
	return 0;
}

int day_1_part_1() {
	std::vector<int> data = get_data();

	int higher_than_count = 0;
	
	for (auto it = data.begin() + 1; it != data.end(); it++) {
		if (*it > *(it - 1)) {
			higher_than_count++;
		}
	}

	return higher_than_count;
}

std::vector<int> get_data() {
	std::string word;
	std::ifstream day_1_input ("day_1_input.txt");
	std::vector<int> data;

	while (day_1_input >> word) {
		data.push_back(std::stoi(word));
	}

	return data;
}

// int day_1_part_2() {
// 	std::string line;
// 	std::ifstream day_1_input("day_1_input.txt");
// 	int higher_than_count = 0;

// 	if (day_1_input.is_open()) {
// 		std::vector<int> v;
// 		int last;

// 		while (v.size() < 3) {
// 			getline(day_1_input, line);
// 			last = std::stoi(line);
// 			v.push_back(last);
// 		}
// 		last = sum(v);
// 		while (getline(day_1_input, line)) {
// 			v.erase(v.begin());
// 			int next = std::stoi(line);
// 			v.push_back(next);
// 			int next_sum = sum(v);
			
// 			if (next_sum > last)
// 				higher_than_count++;

// 			last = next_sum;
// 		}

// 		day_1_input.close();
// 	}
// 	return higher_than_count;
// }



