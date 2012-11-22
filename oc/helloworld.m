#include "hello.h"

int main(int n, const char* argv[]) {
  NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
  NSString* s = [Hello details];
  printf("Result from static call: %s\n", [s UTF8String]);

  Hello* hello = [[Hello alloc] init];
  printf("Name is not initialized: %s\n", [[hello name] UTF8String]);

  [hello setName @"jeff"];
  printf("Your name is %s\n", [[hello name] UTF8String]);

  return 0;
}
