#include "dict.h"

dictKey::dictKey(object key, object value){
  this->value = value;
  this->type = this->value->type;
  this->key = key;
}
