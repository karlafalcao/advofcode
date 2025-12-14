
#include <stdio.h>


int main(void) {
  const char* ops_list = 
  R"""(123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  )""";

  printf("%s", ops_list);

  return 0;  
}
