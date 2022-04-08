class Parameter(object):
    def __init__(self, data, requires_grad, skip_decay=False):
        self.data = data
        self.grad = None
        self.skip_decay = skip_decay
        self.requires_grad = requires_grad
    
    #@property将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改
    @property
    def T(self):
        return self.data.T