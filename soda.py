#-*-coding: utf-8-*-

print '''
问题：
共有1000瓶汽水，每喝完后一瓶得到的一个空瓶子，每3个空瓶子又能换1瓶汽水，
喝掉以后又得到一个空瓶子，问总共能喝多少瓶汽水，最后还剩余多少个空瓶子？

这个问题其实是个比较典型的递推问题，每3个空瓶都可以再换1瓶新的汽水，
这样一直递推下去，直到最后不能换到汽水为止。
'''

def func(num, drinkNum, emptyNum):
    '''
    @param num: 当前多少瓶汽水
    @param drinkNum: 已经喝了多少瓶汽水
    @param emptyNum: 剩余多少空瓶子
    @return : drinkNum=1499, emptyNum=2
    '''
    drinkNum += num
    if num > 3:
        func((num + emptyNum)/ 3, drinkNum, (num + emptyNum) % 3)
    else:
        print '计算结果 drinkNum:', drinkNum, 'emptyNum:', num

if __name__ == '__main__':
    print func.__doc__
    func(1000, 0, 0)
