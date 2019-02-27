#ifndef OBJECT_H
#define OBJECT_H


struct object{
protected:
  bool isConst;
  std::string name;
public:
  object(std::string name, bool con);
};



#endif
