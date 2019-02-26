#ifndef ERROR_H
#define ERROR_H


class error{
private:
  std::string id;
public:
  error(std::string id);
  void raise(std::string callback, std::string msg); 
};



#endif
