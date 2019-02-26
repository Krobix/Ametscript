#ifndef ERROR_H
#define ERROR_H


class error{
private:
  std::string id;
  std::string msg;
  std::string raisedBy;
public:
  error(std::string id);
  void raise(std::string callback, std::string msg); 
};



#endif
