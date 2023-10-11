#include<iostream>
#include "ArrayList.cpp"
using namespace std;

template<typename T>
class Stack {
private:
    ArrayList<T> array;
public:
    T top(); // возвращает элемент сверху стека
    bool empty(); // True, если = 0
    int size();
    T pop();
    void del();
    void print();
    void push(T obj); // кладет элемент на верхушку стека

    
};




template<typename T>
T Stack<T>::top()
{
    return array.get(array.len() - 1);
}

template<typename T>
bool Stack<T>::empty()
{
    if (array.len() > 0) return false;
    return true;
}

template<typename T>
int Stack<T>::size()
{
    return array.len();
}

template<typename T>
T Stack<T>::pop()
{
    T element = array.get(array.len() - 1);
    array.del(array.len() - 1);
    return element;
}

template<typename T>
void Stack<T>::del()
{
    array.del(array.len() - 1);
}
template<typename T>
void Stack<T>::print()
{
    for (int i = 0; i < array.len(); i++) {
        cout << array.get(i) << "\n";
        cout << "--";
        cout << "\n";
    }
}
template<typename T>
void Stack<T>::push(T obj)
{
    array.put(obj);
}
