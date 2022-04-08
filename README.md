# numpy_mnist
## 1.数据
使用数据为MNIST文件夹中MNIST.zip解压得到的trainset.npz和testset.npz
## 2.训练步骤
+ 将trainset.npz进一步划分为训练集和验证集，验证集比例为0.2
+ 使用<code>trainSearch</code>函数进行超参数搜索
+ 搜索得到的参数输入模型进行训练，epoch=10
+ 存储模型参数
## 3.测试步骤
+ 导入参数，将模型应用于testset.npz
+ 计算准确率</br>
详细代码和输出见<code>numpy_mnist.ipynb</code>
