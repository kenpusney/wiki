
#include <iostream>
#include <type_traits>

template<class T, class U = std::void_t<>>
struct IsDefaultConstructible: std::false_type {};

template<class T>
struct IsDefaultConstructible<T, std::void_t<decltype(T())>>: std::true_type {};

struct T {};
struct U { U(int) {}; };

template<class T, std::enable_if_t<IsDefaultConstructible<T>::value>* = nullptr>
struct RequiresDefaultConstructible {
    T x = T {};
};

int main() {
    static_assert(IsDefaultConstructible<T>::value == true);
    static_assert(IsDefaultConstructible<U>::value == false);
    RequiresDefaultConstructible<T> {};
    RequiresDefaultConstructible<U> {};
}
