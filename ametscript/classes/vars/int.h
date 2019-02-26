

class aint{
private: 
  int value;
  int maxval;
  int minval;
  bool valrestricted;

public:
  aint(int value, int minval, int maxval);
  aint(int value);
  aint();
  int getValue();
  void changeValue();
  void changeMax();
  void changeMin();

};

class restrictedInt:public aint{
public:
  restrictedInt(int value);
};
