#ifndef STRING_H
#define STRING_H
#include "object.h"

class astring:public object{
protected:
  std::string value;
  int length;
public:
  astring(std::string v);
};


#endif
