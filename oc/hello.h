#import <Foundation/Foundation.h>

@interface Hello : NSObject {
  NSString* name;
}

+ (NSString*) details;

- (NSString*) name;
- (void) setName : (NSString)newName;

@end
