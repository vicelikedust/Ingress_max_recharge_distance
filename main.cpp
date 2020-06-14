#include <iostream>
#include <algorithm>
using namespace std;

int leveldist[] = {0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000,3250,3500,3750,4000};

int get_level(){
    int level;
    cout << "What is your player level? ";
    cin >> level;

    while(level == 0 || level >= 17){
        cout << "That is an invaild level \nLevel " << level << " doesn't exist" << endl;
        cout << "What is your player level? ";
        cin >> level;
    }

    return level;
}

int get_distance(){
    int distance;
    cout << "What is the distance in km? ";
    cin >> distance;

    return distance;
}

void calc(){
    int efficiency;
    int level = get_level();
    int distance = get_distance();

    if(distance > leveldist[level]){
        cout << "Portal is too far \nThe max distance for level " << level << " is " << leveldist[level] << " km" << endl;
    } else {
        efficiency = 100 - (distance)/(5 * level);
        cout << efficiency << "%" << endl;
    }
}

int main()
{
    string ans = "yes";
    while(ans == "yes" || ans == "y"){
        calc();
        cout << "Do you want to calculate another one? ";
        cin >> ans;
        transform(ans.begin(), ans.end(), ans.begin(), ::tolower);
    }
    cout << endl << "Program closing...";
    return 0;
}
