#include "object.h"

object::object(std::string name, bool con){
  this->name = name;
  this->isConst = con;
}
object::object(){
  this->name = "__obj__";
  this->isConst = false;
}
