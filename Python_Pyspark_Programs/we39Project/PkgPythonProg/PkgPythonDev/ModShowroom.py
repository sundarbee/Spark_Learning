class cls1: #class is a template or a program contains variables and functions
    cls_attrib=100 #class attribute or a member variable
    def funct1(self,a,b): #member function of class cls1
        return a+b
    def funct2(self,a,b): #member function of class cls1
        return a-b

class cls2: #class is a template or a program contains variables and functions
    cls_attrib=200 #class attribute or a member variable
    def funct1(self,a,b): #member function of class cls2
        return a+b+self.cls_attrib
    def funct2(self,a,b): #member function of class cls2
        return a+b-self.cls_attrib