#include <ranges>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>

#include <ranges>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <vector>
#include <iostream>

template<class Collection>
auto map_reduce(const Collection& c, auto fn, auto init, auto acc) {
  std::vector<typename Collection::value_type> transformed {};
  std::transform(
    c.begin(),
    c.end(),
    std::back_inserter(transformed),
    fn);
  return std::accumulate(
    transformed.begin(),
    transformed.end(),
    init, acc);
}

template<std::ranges::range Range>
auto map_reduce_range(const Range& r,
  auto fn, auto init, auto acc) {
  auto transformed = r | std::views::transform(fn);
  return std::reduce(
    transformed.begin(),
    transformed.end(),
    init, acc);
}

int main() {
    std::vector<int> x {1,2,3,4,5};

    int result = map_reduce_range(x, [](auto x) { return x + 1; } , 0, [](auto x, auto y) {
        return x + y;
    });

    std::cout << result << std::endl;
}
