#include <coroutine>
#include <iterator>
#include <iostream>

template<class T>
struct task {
  struct promise_type;

  using handle = std::coroutine_handle<promise_type>;

  struct promise_type {
    T current_value;
    static auto get_return_object_on_allocation_failure() { return task{nullptr}; }
    auto get_return_object() noexcept { return task{handle::from_promise(*this)}; }
    auto initial_suspend() noexcept { return std::suspend_always{}; }
    auto final_suspend() noexcept { return std::suspend_always{}; }
    [[noreturn]]
    void unhandled_exception() { throw; }
    void return_value(T value) noexcept { current_value = value; }
    auto await_transform(auto&& task) noexcept { return std::move(task); }
  };

  task(nullptr_t): coro(nullptr) {}
  task(handle coro): coro(coro) {}
  task(task const&) = delete;
  task(task && rhs) : coro(rhs.coro) { rhs.coro = nullptr; }
  ~task() { if (coro) coro.destroy(); }

  bool await_ready() {
    return this->coro.done();
  }

  void await_suspend(std::coroutine_handle<> awaiting) {
    this->coro.resume();
    awaiting.resume();
  }

  auto await_resume() {
    return this->coro.promise().current_value;
  }

  T operator()() {
    coro.resume();
    return coro.promise().current_value;
  }

private:
  handle coro;

};

task<int> hello() {
  co_return 1;
}

task<int> world() {
  int x = co_await hello();
  int y = co_await hello();

  co_return x + y;
}

int main() {
   auto t = world();

   std::cout << t();
}