#include "object.h"

object::object(std::string name, bool isConst){
  this->name = name;
  this->isConst = isConst;
}
object::object(){
  this->name = "__obj__";
  this->isConst = false;
}
