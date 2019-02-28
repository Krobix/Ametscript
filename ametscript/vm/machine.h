#ifndef MACHINE_H
#define MACHINE_H

class machine{
public:
  enum ops{
    LOAD_MAIN, //0x00
    EXIT_MAIN, //0x01
    NEW_OBJ,   //0x02
    GET_VAR,   //0x03
    SET_VAR,   //0x04
    DEF_FUNC,  //0x05
    CALL_FUNC,
    IMPORT_MOD,
    CREATE_MOD,
    BIN_ADD,
    BIN_SUBTRACT,
    BIN_MULT,
    BIN_DIV
    
  };
};

#endif
