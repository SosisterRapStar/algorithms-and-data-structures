// DoubleLinkedList.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
using namespace std;

template <class T>
class Node {
	public:
		T data;
		Node<T>* next;
		Node<T>* prev;
};

template <class T>
class LinkedList {

	int size;
	Node<T>* head;
	Node<T>* tail;

	void putInTail(T value); // вставка в конец листа
	void putBeforeHead(T value);

	

public:
	T get(int index);
	void print();
	Node<T>* getNode(int index);
	LinkedList();
	~LinkedList();
	void del(int index);
	int len();
	void insert(int index, T value);
	void push(T value); // добавление в конец списка
};


template<class T>
LinkedList<T>::LinkedList()
{
	head = nullptr;
	tail = nullptr;
	size = 0;
}

template<class T>
LinkedList<T>::~LinkedList()
{
	for()
}



template<class T>
void LinkedList<T>::print() {
	Node<T>* node = head;
	for (int i = 0; i < size; i++) {
		cout << node->data << " <-> ";
		node = node->next;
	}
	cout << "\n";
}

template<class T>
void LinkedList<T>::putInTail(T value)
{
	Node<T>* new_node = new Node<T>;
	new_node->data = value;
	size += 1;
	new_node->next = tail->next;
	new_node->prev = tail;
	tail->next = new_node;	
	tail = new_node;
}

template<class T>
void LinkedList<T>::putBeforeHead(T value)
{
	Node<T>* new_node = new Node<T>;
	new_node->data = value;
	size += 1;
	new_node->next = head;
	new_node->prev = head->prev;
	head->prev = new_node;
	head = new_node;
}

template<class T>
void LinkedList<T>::insert(int index, T value)
{
	
	if (index >= size || 0 > index) {
		return;
	}
	if (size == 0) {
		push(value);
		return;
	}

	Node<T>* new_node = new Node<T>;
	new_node->data = value;
	
	if (index == size - 1) {
		putInTail(value);
		return;
	}
	if (index == 0) {
		putBeforeHead(value);
		return;
	}
	size += 1;
	
	Node <T>* node = head;
	for (int i = 0; i < index; i++) {
		node = node->next;
	}
	node->next->prev = new_node;
	new_node->next = node->next;
	new_node->prev = node;
	node->next = new_node;

}


template<class T>
Node<T>* LinkedList<T>::getNode(int index) {
	if (index >= size || 0 > index) return nullptr;
	Node <T>* node = head;
	for (int i = 0; i < index; i++) {
		node = node->next;
	}
	return node;
}



template<class T> T LinkedList<T>::get(int index)
{
	if (index >= size || 0 > index) return;
	Node <T>* node = head;
	for (int i = 0; i < index; i++) {
		node = node->next;
	}
	return node->data;
}





template<class T>
void LinkedList<T>::push(T value)
{
	if (size == 0) {
		size += 1;
		Node <T>* new_node = new Node<T>;
		new_node->data = value;
		new_node->next = nullptr;
		new_node->prev = nullptr;
		head = new_node;
		tail = new_node;
		return;
	}
	putInTail(value);
	return;
}

template<class T>
void LinkedList<T>::del(int index) {
	if (index >= size || 0 > index) return;
	Node<T>* node_for_del = getNode(index);
	size -= 1;
	if (size == 0) {
		tail = nullptr;
		head = nullptr;
		delete node_for_del;
		return;
	}
	if (node_for_del == tail) {
		node_for_del->prev->next = nullptr;
		tail = node_for_del->prev;
		delete node_for_del;
		return;
	}
	if (node_for_del == head) {
		node_for_del->next->prev = nullptr;
		head = node_for_del->next;
		delete node_for_del;
		return;
	}
	node_for_del->next->prev = node_for_del->prev;
	node_for_del->prev->next = node_for_del->next;
	return;
	
}
template<class T>
int LinkedList<T>::len() {
	return size;
}