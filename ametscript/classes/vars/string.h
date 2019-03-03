#include "object.h"

class astring:public object{
protected:
  std::string value;
public:
  astring(std::string v);
};
