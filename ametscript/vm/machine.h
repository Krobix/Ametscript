#ifndef MACHINE_H
#define MACHINE_H
#include "opcode.h"
#include "../classes/vars/object.h"


enum ops{
    LOAD_CORE, //0x00
    EXIT_CORE, //0x01
    NEW_OBJ,   //0x02
    GET_VAR,   //0x03
    SET_VAR,   //0x04
    DEF_FUNC,  //0x05
    CALL_FUNC, //0x06
    IMPORT_MOD,//0x07
    CREATE_MOD,//0x08
    
    //Mathematical Operations
    BIN_ADD = 160,   //0xA0
    BIN_SUBTRACT = 161,//0xA1
    BIN_MULT = 162,//0xA2
    BIN_DIV = 163,//0xA3
    CMP_EQUAL = 164,//0xA4
    CMP_LESS = 165,//0xA5
    CMP_GREAT = 166//0xA6
    
    
 };

class machine{
private:
     
};


#endif
