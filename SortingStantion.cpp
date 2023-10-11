#include<iostream>
#include <string>
#include "Stack.cpp"
using namespace std;


int priority(string i) {
    if (i == "(") return 1;
    if (i == "+" || i == "-") return 2;
    if (i == "*" || i == "/") return 3;
    if (i == "cos" || i == "sin") return 4;
    if (i == "^") return 5;
    return 0;
}



int SortingStantion(string str) {
    setlocale(0, "Rus");
    Stack <string> stc;
    string postfix = "";
    string sincos;
    string buffer = "";
    string element;
    int pr;
    for (int i = 0; i < str.size(); i++)
    {
      
        
        if ((i < str.size() - 4) && str[i] == 's' && str[i + 1] == 'i' && str[i + 2] == 'n') {
            pr = 4;
            i += 2;
            element = "sin";
            pr = priority(element);
        }
        else if ((i < str.size() - 4) && str[i] == 'c' && str[i + 1] == 'o' && str[i + 2] == 's') {
            pr = 4;
            i += 2;
            element = "cos";
            pr = priority(element);   
        }
        else {
            buffer += str[i];
            element = buffer;
            pr = priority(element);
            buffer = "";
        }


        switch (pr)
        {
            case 1: { // открывающа€с€ скобка
                postfix += " ";
                stc.push(element);
                break;
            }
            case 0: {
                if (element == ")") {
                    postfix += " ";
                    while (!stc.empty() && stc.top() != "(") {
                        postfix += " ";
                        postfix += stc.top();
                        postfix += " ";
                        stc.pop();
                    }
                    if (!stc.empty()) {
                        postfix += " ";
                        stc.pop();
                    }
                    else {
                        cout << "Ќеправильное расположение скобок, их дублирование или недостаток\n";
                        return 0;
                    }
                   
                }
                else {

                    postfix += element; // добавление символа в строку постфиксной записи
                }
                break;
            }

            default:
            {
                
                if (!stc.empty())
                {
                    postfix += " ";
                    while (!stc.empty() && priority(stc.top()) >= pr) {

                        postfix += stc.top();
                       
                        postfix += " ";
                        stc.pop();
                    }
                    
                    stc.push(element);
                    
                }
                else {
                    postfix += " ";
                  
                    stc.push(element);
                }
                

                break;
            }

        }
    }
    if (!stc.empty()) { // вытаскивание из стека отсавшихс€ операций
        postfix += " ";
        while (!stc.empty())
        {
            postfix += stc.top();
            postfix += " ";
            stc.pop();
        }
    }
    
    cout << postfix;
    return 0;
}


void main() {
    string a = "32323 + sin(3232^21) * cos(120 * 32 + (12 + 93) + (32 - 3)) * cos(3/4)";
	SortingStantion(a);
}