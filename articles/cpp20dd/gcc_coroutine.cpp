
#include <coroutine>
#include <iterator>
#include <iostream>
#include <concepts>
#include <optional>

template<class T>
struct generator {
  struct promise_type;
  using handle = std::coroutine_handle<promise_type>;

  struct promise_type {
    std::optional<T> current_value;

    auto get_return_object() { return generator{handle::from_promise(*this)}; }
    auto initial_suspend() noexcept { return std::suspend_always{}; }
    auto final_suspend() noexcept { return std::suspend_always{}; }
    void unhandled_exception() { std::terminate(); }
    auto yield_value(T value) {
      current_value = std::move(value);
      return std::suspend_always{};
    }
  };

  struct iterator {

    iterator(handle coro): coro(coro) {}

    void operator++() { coro.resume(); }
    T& operator*() { return *this->coro.promise().current_value; }

    bool operator==(std::default_sentinel_t) const { return !coro || coro.done(); }
  private:
    handle coro;
  };

  explicit generator(handle h) : coro(h) {}

  generator(const generator &) = delete;
  generator& operator=(const generator&) = delete;
  generator(generator && rhs) : coro(rhs.coro) { rhs.coro = {}; }
  generator& operator=(generator && rhs) {
    if (this != &rhs) {
      if (coro) { coro.destroy(); }
      coro = rhs.coro;
      rhs.coro = {};
    }
    return *this;
  }

  iterator begin() {
    if (coro) { coro.resume(); }
    return { coro };
  }
  std::default_sentinel_t end() { return {}; }

  ~generator() { if (coro) { coro.destroy(); } }
private:
  handle coro;
};

generator<int> range(int from, int to) {
  for (int x = from; x < to; ++x) {
    co_yield x;
  }
}

int main() {
  for (auto&& i : range(0, 10)) {
    std::cout << i * i << std::endl;
  }
}
