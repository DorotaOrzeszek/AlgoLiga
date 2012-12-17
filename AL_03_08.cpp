#include <cstdio>

int max1 = -1;
int max2 = -1;

int main() {
while (true) {
  int n;
  scanf("%d",&n);
  if (n == 0) {
    break;
  } 
  else {
    if (n > max1) {
      max2 = max1;
      max1 = n;
    }
    else if (n != max1 && n > max2) {
      max2 = n;
    }
  }
}
if (max2 == -1) {
  printf("%d\n",max1);
}
else {
  printf("%d\n",max2);
}
return 0;
}
