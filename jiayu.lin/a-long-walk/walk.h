#include <iostream>
#include <string>
#include <vector>

class Walk {
public:
   std::vector<std::string> input;
   int steps;
   std::pair<int, int> start;
   std::pair<int, int> end;

   int getSteps(vector<string> input, std::pair<int, int> start, std::pair<int, int> end);
   Walk(std::vector<std::string> input);
};