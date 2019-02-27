#include "error.h"

error::error(std::string id){
  this->name = id;
}
void error::raise(std::string callback, std::string msg){
  std::cout << this->id << ":\n";
  std::cout << callback << ", details:" << msg << "\n";
}


