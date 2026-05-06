#include <iostream>
#include <string>

int main()
{
    int age, adress, phone;
    std::string name, email;
    float grade;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);
    std::cout << "Enter your age: ";
    std::cin >> age;
    std::cout << "Enter your email: ";
    std::cin >> email;
    std::cout << "Enter your adress: ";
    std::cin >> adress;
    std::cout << "Enter your phone: ";
    std::cin >> phone;
    std::cout << "Enter your grade: ";
    std::cin >> grade;
    std::cout << "Your name is: " << name << std::endl;
    std::cout << "Your age is: " << age << std::endl;
    std::cout << "Your email is: " << email << std::endl;
    std::cout << "Your adress is: " << adress << std::endl;
    std::cout << "Your phone is: " << phone << std::endl;
    std::cout << "Your grade is: " << grade << std::endl;
    return 0;
}