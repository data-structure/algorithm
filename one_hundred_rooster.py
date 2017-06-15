#-*-coding: utf-8-*-

print '''
问题描述：
每只母鸡3元，每只公鸡4元，每只小鸡0.5元，如果花100元钱买100只鸡，请问有哪些可能？
说明：每种鸡的数量都可以为零。

其实这个问题是数学上的组合问题，只需要把所有的情况列举出来，然后来判断是否符合要求即可。
这样的重复列举的问题，在程序上可以使用循环进行解决。
'''

def func():
    '''
    @param hen: 母鸡的数量
    @param rooster: 公鸡的数量
    @param chick: 小鸡仔的数量
    @return: hen=, rooster=, chick=
    '''
    for i in range(26):
        tmp = (100 - 4 * i) / 3
        for j in range(tmp + 1):
            k = 100 - i - j
            if (i * 4 + j * 3 + k * 0.5) != 100:
                continue
            print 'hen: ', j, ', rooster: ', i, ', chick: ', k

if __name__ == '__main__':
    print func.__doc__
    func()
