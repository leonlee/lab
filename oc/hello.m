#include "hello.h"

@implementation Hello

+ (NSString*) details {
  return @"This is a string";
}

- (NSString*) name {
  return name;
}

- (void) setName: (NSString*)newName {
  [name release];
  name = [newName retain];
}
