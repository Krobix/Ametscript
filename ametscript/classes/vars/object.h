#ifndef OBJECT_H
#define OBJECT_H


struct object{
protected:
  bool isConst;
  std::string name;
  std::string type;
public:
  object(std::string name, bool con);
  object();
  object(object obj);
};



#endif
