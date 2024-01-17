#include "walk.h"
using std::vector;
using std::string;
using std::pair;
Walk::Walk(vector<string> input) {
    this->input = input;
    this->steps = 0;
    this->start = {0, 1};
    this->end = {input.size() - 1,(input.size() * input[0].length()) - 2};
}

int Walk::getSteps(vector<string> input, pair<int, int> start, pair<int, int> end) {
    int cols = this->input[0].length();
    int rows = this->input.size();
    // move top
    if (start.first - 1 >= 0) {
        if (input[start.first - 1][start.second] == '.' || input[start.first - 1][start.second] == '^') {
            return 1 + getSteps(input, {start.first - 1, start.second}, end);
        }
        if (input[start.first - 1][start.second] == 'v') {
            return 1 + getSteps(input, {start.first + 1, start.second}, end);
        }
        if (input[start.first - 1][start.second] == '>') {
            return 1 + getSteps(input, {start.first, start.second + 1}, end);
        }
        if (input[start.first - 1][start.second] == '<') {
            return 1 + getSteps(input, {start.first, start.second - 1}, end);
        }
    }
    // move right
    if (start.second + 1 < cols) {
        if (input[start.first][start.second + 1] == '.' || input[start.first][start.second + 1] == '>') {
            return 1 + getSteps(input, {start.first, start.second + 1}, end);
        }
        if (input[start.first][start.second + 1] == 'v') {
            return 1 + getSteps(input, {start.first, start.second + 1}, end);
        }
        if (input[start.first][start.second + 1] == '<') {
            return 1 + getSteps(input, {start.first, start.second - 1}, end);
        }
        if (input[start.first][start.second + 1] == '^') {
            return 1 + getSteps(input, {start.first - 1, start.second}, end);
        }
    }
    // move bottom
    if (start.first + 1 < rows) {
        if (input[start.first + 1][start.second] == '.' || input[start.first + 1][start.second] == 'v') {
            return 1 + getSteps(input, {start.first + 1, start.second}, end);
        }
        if (input[start.first + 1][start.second] == '>') {
            return 1 + getSteps(input, {start.first, start.second + 1}, end);
        }
        if (input[start.first + 1][start.second] == '<') {
            return 1 + getSteps(input, {start.first, start.second - 1}, end);
        }
        if (input[start.first + 1][start.second] == '^') {
            return 1 + getSteps(input, {start.first - 1, start.second}, end);
        }
    }
    // move left
    if (start.second - 1 >= 0) {
        if (input[start.first][start.second - 1] == '.' || input[start.first][start.second - 1] == '<') {
            return 1 + getSteps(input, {start.first, start.second - 1}, end);
        }
        if (input[start.first][start.second - 1] == 'v') {
            return 1 + getSteps(input, {start.first + 1, start.second}, end);
        }
        if (input[start.first][start.second - 1] == '>') {
            return 1 + getSteps(input, {start.first, start.second + 1}, end);
        }
        if (input[start.first][start.second - 1] == '^') {
            return 1 + getSteps(input, {start.first - 1, start.second}, end);
        }
    }
    // get blocked by #
    if (input[start.first][start.second] == '#') {
        return getSteps(input, {start.first, start.second - 1}, end);
    }
    
}