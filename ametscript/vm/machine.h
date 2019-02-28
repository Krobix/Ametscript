#ifndef MACHINE_H
#define MACHINE_H

class machine{
public:
  enum ops{
    LOAD_MAIN,
    EXIT_MAIN,
    NEW_OBJ,
    GET_VAR,
    SET_VAR,
    DEF_FUNC,
    CALL_FUNC,
    IMPORT_MOD
    
  }
};

#endif
