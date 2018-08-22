#include <iostream>
#include <cstdlib>
using namespace std;

int max3(int x, int y, int z) {
 	if(x >= y) {
		if(x >= z) {
      		return x;


}
int main(int argc,char *argv[]) {

    int x1, y1, z1, x2, y2, z2, x3, y3, z3;
    x1=atoi(argv[1]);
    y1=atoi(argv[2]);
    z1=atoi(argv[3]);
    
    x2=atoi(argv[4]);
    y2=atoi(argv[5]);
    z2=atoi(argv[6]);
    
    x3=atoi(argv[7]);
    y3=atoi(argv[8]);
    z3=atoi(argv[9]);
    //cin >> x;
   // cin >> y;
    //cin >> z;
    cout << max3(x1, y1, z1) << max3(x2, y2, z2) << max3(x3, y3, z3) << endl;
    return 0;
}


