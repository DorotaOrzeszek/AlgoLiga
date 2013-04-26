#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
	int t;	// number of test cases
	cin >> t;
	while (t > 0) {
		string graphtype;
		cin >> graphtype;
		string edgesymbol;
		if (graphtype == "gw" || graphtype == "g") {
			cout << "graph {\n";
			edgesymbol = " -- ";
		} else if (graphtype == "dw" || graphtype == "d") {
			cout << "digraph {\n";
			edgesymbol = " -> ";
		}
		int n;	// number of nodes
		cin >> n;
		cin.ignore();
		string line;
		for (int i = 0; i < n; i++) {
			getline(cin, line);
			istringstream stream(line);
			string temp;	// node name or weight
			stream >> temp;
			cout << temp << edgesymbol;
			stream >> temp;
			cout << temp;
			if (graphtype == "gw" || graphtype == "dw") {
				stream >> temp;
				cout << " [label = " << temp << "];\n";
			} else {
				cout << ";\n";
			}
		}
		cout << "}\n";
		t--;		
	}
}
