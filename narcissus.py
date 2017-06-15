#-*-coding: utf-8-*-

print '''
问题：
水仙花数指三位数中，每个数字的立方和和自身相等的数字，
例如370，3 × 3 × 3 + 7 × 7 × 7 + 0 × 0 × 0 =370，请输出所有的水仙花数。

该问题中体现了一个基本的算法——数字拆分，需要把一个数中每位的数字拆分出来，然后才可以实现该逻辑。
'''

def func():
    '''
    '''
    for i in range(100, 1000):
        single_digit = i % 10
        ten_digit = i / 10 % 10
        hundred_digit = i / 100
        if single_digit**3 + ten_digit**3 + hundred_digit**3 == i:
            print 'find: ', i

if __name__ == '__main__':
    print func.__doc__
    func()
