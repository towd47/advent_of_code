#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

int day_4_part_1();
int day_4_part_2();
int sum_card(std::vector<std::string> card);
std::vector<std::vector<std::string>> create_cards(std::vector<std::string> &called_numbers);
bool check_bingo(std::vector<std::string> card);
int check_bingos(std::vector<std::vector<std::string>> cards);
void tic_number_on_card(std::vector<std::string> &card, std::string number_to_check);
void tic_number_on_all_cards(std::vector<std::vector<std::string>> &cards, std::string number_to_check);

int main(int argc, char const *argv[])
{

	int day_4_part_1_answer = day_4_part_1();
	std::cout << "Day 4 Part 1: " << day_4_part_1_answer << std::endl;

	int day_4_part_2_answer = day_4_part_2();
	std::cout << "Day 4 Part 2: " << day_4_part_2_answer << std::endl;

	return 0;
}

std::vector<std::vector<std::string>> create_cards(std::vector<std::string> &called_numbers) {
	std::string line;
	std::ifstream day_4_input ("day_4_input.txt");

	std::vector<std::string> data;

	while (getline(day_4_input, line)) {
		data.push_back(line);
	}

	std::istringstream called_numbers_stream(data.at(0));

	while (called_numbers_stream) {
		std::string number;
		if (!getline(called_numbers_stream, number, ',')) break;
		called_numbers.push_back(number);
	}

	data.erase(begin(data));
	data.erase(begin(data));

	std::vector<std::vector<std::string>> cards;
	std::vector<std::string> card;

	for (auto e : data) {
		if (!e.empty()) {
			std::istringstream ss(e);
			while (ss) {
				std::string number;
				if (!getline(ss, number, ' ')) 
					break;
				if (!number.empty())
					card.push_back(number);
			}
		}
		else {
			cards.push_back(card);
			card.clear();
		}
	}

	return cards;
}

int day_4_part_1() {
	std::vector<std::string> called_numbers;
	auto cards = create_cards(called_numbers);

	auto it = begin(called_numbers);
	for (int i = 0; i < 5; i++) {
		tic_number_on_all_cards(cards, *it);
		it++;
	}

	int card_num = check_bingos(cards);
	while (card_num == -1) {
		tic_number_on_all_cards(cards, *it);
		it++;
		card_num = check_bingos(cards);
	}
	it--;
	int final_num = stoi(*it);

	std::vector<std::string> winning_card = cards.at(card_num);
	
	int card_sum = sum_card(winning_card);
	
	return card_sum * final_num;
}

int day_4_part_2() {

	// generate bingo cards and the order of numbers from input
	std::vector<std::string> called_numbers;
	auto cards = create_cards(called_numbers);


	// check first 5 numbers on cards
	auto it = begin(called_numbers);
	for (int i = 0; i < 5; i++) {
		tic_number_on_all_cards(cards, *it);
		it++;
	}


	// removes all cards with bingos while continuing to check of numbers until only 1 card remains
	int card_num = check_bingos(cards);
	while (cards.size() > 1) {
		tic_number_on_all_cards(cards, *it);
		it++;
		card_num = check_bingos(cards);
		while (card_num != -1) {
			cards.erase(cards.begin() + card_num);
			card_num = check_bingos(cards);
		}
	}

	// continues until bingo exists on final card
	while (card_num == -1) {
		tic_number_on_all_cards(cards, *it);
		it++;
		card_num = check_bingos(cards);
	}
	it--;


	// calculates bingo card result
	int final_num = stoi(*it);
	auto final_card = cards.at(card_num);
	
	auto card_sum = sum_card(final_card);

	return card_sum * final_num;
}

int sum_card(std::vector<std::string> card) {
	int card_sum = 0;

	for (auto e : card) {
		if (e != "x") {
			card_sum += stoi(e);
		}
	}

	return card_sum;
}

int check_bingos(std::vector<std::vector<std::string>> cards) {
	for (int i = 0; i < cards.size(); i++) {
		if (check_bingo(cards.at(i))) {
			return i;
		}
	}
	return -1;
}

bool check_bingo(std::vector<std::string> card) {
	for (int i = 0; i < 5; i++) {
		bool bingo = true;
		for (int j = i; j < card.size(); j+=5) {
			if (card.at(j) != "x") {
				bingo = false;
				break;
			}
		}
		if (bingo) {
			return true;
		}
	}
	for (int i = 0; i < card.size() - 5; i+= 5) {
		bool bingo = true;
		for (int j = i; j < i + 5; j++) {
			if (card.at(j) != "x") {
				bingo = false;
				break;
			}
		}
		if (bingo) {
			return true;
		}
	}
	return false;
}

void tic_number_on_all_cards(std::vector<std::vector<std::string>> &cards, std::string number_to_check) {
	for (auto &card : cards) {
		tic_number_on_card(card, number_to_check);
	}
}

void tic_number_on_card(std::vector<std::string> &card, std::string number_to_check) {
	auto it = begin(card);

	while (it != end(card)) {
		if (*it == number_to_check) {
			*it = "x";
			return;
		}
		it++;
	}
}



