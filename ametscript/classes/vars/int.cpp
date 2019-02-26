#include "int.h"
#include "../error.h"


aint::aint(int value, int minval, int maxval){
  this->value = value;
  this->minval = minval;
  this->maxval = maxval;
}
aint::aint(int value){
  this->value = value;
  this->maxval = 345259;
  this->minval = -345259;
}
aint::aint(){
  this->value = 0;
  this->maxval = 345529;
  this->minval = -345529;
}
