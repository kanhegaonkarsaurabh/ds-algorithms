/* Name: library-qsort.c
 * Description: Code to use in-built qsort to compare an array of strings in C 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int cmpstring (const void *p1, const void *p2) {
  return strcmp(*(char * const * )p1, *(char * const *)p2);     /* Use the backwards rule to understand the casting and de-reference */
}

int main() {
  char * names[5];
  names[0] = "Saurabh";
  names[1] = "Abhay";
  names[2] = "Ruha";
  names[3] = "Hello";
  names[4] = "Damn";

  qsort(names, 5, sizeof(char *), cmpstring); 
  printf("%s", names[4]);
}
