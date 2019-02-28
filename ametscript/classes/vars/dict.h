#ifndef DICT_H
#define DICT_H
#include "object.h"

class dictKey:public object{
private:
  std::string *key;
  object *value;
public:
  dictKey(object key, object value);  
};

class dict:public object{
  
};

#endif
