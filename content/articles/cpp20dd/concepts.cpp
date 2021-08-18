
template<class T>
concept DefaultConstructible = requires {
    T {};
};

template<DefaultConstructible T>
struct RequiresDefaultConstructible {
    T x = T {};
};

struct T {};

struct U { U(int x) {} };

int main() {
    RequiresDefaultConstructible<T> {};
    // RequiresDefaultConstructible<U> {};
}
