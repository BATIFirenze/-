Final assignment
完成:Pollord_Rho实现,SM3优化,SM4查表优化,SM3生日攻击,SM3长度拓展攻击

Pollord_Rho实现:
Pollord_Rho的实现需要实现函数的迭代
这里直接使用了x^2+1函数,并随机找了一组数据,最终实现了对该数的分解
后面实现对SM3的12bit碰撞

SM3优化:
SM3的算法实现是与202000460056吴善达同学一起完成的,优化部分为分开优化
优化对代码的逻辑尽可能地优化
这里的数据0x616263是国密标准提供的值,与其输出相符

SM4查表优化:
对明文串的循环中的s盒运算与非线性变换进行了合并,实现了大表

生日攻击:
使用了在线编辑器,注释掉的是实际运行代码
其中from SM3 import * 就是引用了SM3.py(网上搜到的一个文件),即注释部分多出来的一段
最终输出为true,即成立

SM3长度拓展攻击:
先使用SM3的代码,然后随机生成一个消息,为使得附加消息m'成立,需要匹配padding,计算secret+padding+m'的hash值,若攻击成功,hash2=hash3
