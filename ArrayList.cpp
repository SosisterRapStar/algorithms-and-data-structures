// ArrList.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
using namespace std;

template<class T>
class ArrayList {
private:
    int capacity;
    T* array;
    void rebuild();
    int size;
public:
    ArrayList();
    ~ArrayList();
    ArrayList(const ArrayList<T> &obj);
    void print();
    int len();
    int getCapacity();
    void put(T obj);
    T get(int index); // возвращает элемент массива
    T pop(int index); // удаляет элемент из массива
    T set(int index, T new_value); // обновляет элемент в массиве
    void del(int index);

};

template <class T> ArrayList<T>::ArrayList(const ArrayList<T> &obj)
{
    
    array = new T[obj->getCapacity];
    size = obj->len();

}

// метод плох, так как если в него класть объекты для которых не переопределен cout то гг
template<class T>
void ArrayList<T>::print()
{
    for (int i = 0; i < size; i++) {
        cout << "[" << array[i] << "] ";
    }
}


template <class T> ArrayList<T>::~ArrayList()
{

    delete[] array;

}

template <class T> ArrayList<T>::ArrayList()
{

    capacity = 10;
    size = 0;
    array = new T[capacity];

}


template <class T> void ArrayList<T>::put(T obj) {
    array[size] = obj;
    size += 1;
    if (size == capacity) {
        rebuild();
    }
}


template <class T> void ArrayList<T>::del(int index) {
    if (index >= size || 0 > index) {
        return;
    }

    T obj;
    array[size - 1] = obj;
    size -= 1;
    for (int i = index; i < size - 1; i++) {
        array[i] = array[i + 1];
    } 
}

template <class T> T ArrayList<T>::pop(int index) {
    if (index >= size || 0 > index) {
        return;
    }
    T element = array[index];
    array[size - 1] = 0;
    size -= 1;
    for (int i = index; i < size - 1; i++) {
        array[i] = array[i + 1];
    }
    return element;

}

template <class T> T ArrayList<T>::set(int index, T new_value) {
    if (index >= size || 0 > index) {
        return NULL;   // боже прости меня (здесь должна возвращаться ошибка)
    }
    array[index] = new_value;
}


template <class T> T ArrayList<T>::get(int index) {
    if (index >= size || 0 > index) {
        return NULL; // и еще раз 
    }
    return array[index];
}

template <class T>
int ArrayList<T>::len() {
    return size;
}

template<class T>
int ArrayList<T>::getCapacity()
{
    return capacity;

}


template <class T> void ArrayList<T>::rebuild() {
    capacity *= 2;
    T* new_arr = new T[capacity];
    for (int i = 0; i < size; i++) {
        new_arr[i] = array[i];
    }
    T* sw = array;
    array = new_arr;
    delete[] sw;
}