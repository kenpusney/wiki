
#include <iterator>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
  std::copy(
    istreambuf_iterator<char>(cin),
    istreambuf_iterator<char>(),
    ostreambuf_iterator<char>(cout));
}
