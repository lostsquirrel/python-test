

class Example(object):
    
    class_field="111111111111"
    def __init__(self, obj_field):
        self.obj_field = obj_field
        
a = Example("aaaaa")
print a.class_field
print a.obj_field
a.class_field = "2222222222222222"
print a.class_field
print 
b = Example("bbbb")
print b.class_field
print b.obj_field