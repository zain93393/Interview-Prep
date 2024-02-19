#include <iostream>
using namespace std;

// Base class
class Box {
protected:
    int height;
    int width;

public:
    // Constructor
    Box(int h = 0, int w = 0) : height(h), width(w) {}

    // Function to set values
    void setValues(int h, int w) {
        height = h;
        width = w;
    }

    // Function to print values
    void printValues() {
        cout << "Height: " << height << endl;
        cout << "Width: " << width << endl;
    }
};

// Derived class
class BoxWeight : public Box {
private:
    int weight;

public:
    // Constructor
    BoxWeight(int h = 0, int w = 0, int wt = 0) : Box(h, w), weight(wt) {}

    // Function to set weight
    void setWeight(int wt) {
        weight = wt;
    }

    // Function to print values including weight
    void printValues() {
        Box::printValues(); // Call base class's printValues
        cout << "Weight: " << weight << endl;
    }
};

int main() {
    // Creating objects
    Box box1(4, 5);
    BoxWeight boxWeight1(2, 3, 4);

    // Printing values
    cout << "Box1 values:" << endl;
    box1.printValues();

    cout << "\nBoxWeight1 values:" << endl;
    boxWeight1.printValues();

    return 0;
}
