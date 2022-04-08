from abc import ABCMeta, abstractmethod


class Layer(metaclass=ABCMeta):
    '''
    作为所有层的基类，包含正向和反向两个方法，所有负责具体功能的层都从Layer类继承
    '''
    @abstractmethod
    def forward(self, *args):
        pass

    @abstractmethod
    def backward(self, *args):
        pass