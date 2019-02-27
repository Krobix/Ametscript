#ifndef ERROR_H
#define ERROR_H
#include "vars/object.h"


class error:public object{
public:
  error(std::string id);
  void raise(std::string callback, std::string msg); 
};



#endif
