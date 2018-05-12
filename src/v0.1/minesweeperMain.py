static = [[0, 1, 0, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0, 0]]  # 用于存储是否被翻开 0表示未翻开，1表示翻开
unknown = [[0, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1]]  # 用于存储需要预测的地区，0不需要，1需要
openDate = [[-1, 3, -1, -1, 1, 1, 1], [2, -1, -1, -1, 2, -1, -1], [1, -1, -1, 2, -1, -1, -1]]  # 用于存储翻开后的数据 -1表示未知
closeDate = [[1, 0, 1, -1, 0, 0, 0], [0, -1, -1, -1, 0, -1, -1],
             [0, -1, -1, 0, -1, -1, -1]]  # 用于存储有雷的数据 1表示有  0表示没有  -1表示未知

result = [[], [], []]

def initList(list, v):
    '''
    用于二维数组初始化
    :param i: 需要初始化的值
    :param list: 需要初始化数组
    :return:
    '''
    for i in range(0, len(list)):
        for j in range(0, 7):
            list[i].append(v)


def getRimList(x, y):
    '''
    获取周边所有位置
    :param x:
    :param y:
    :return: 返回一个元组
    '''
    if x == 2:
        xBegan, xEnd = (x - 1, x)
    elif x == 0:
        xBegan, xEnd = (x, x + 1)
    else:
        xBegan, xEnd = (x - 1, x + 1)

    if y == 6:
        yBegan, yEnd = (y - 1, y)
    elif y == 0:
        yBegan, yEnd = (y, y + 1)
    else:
        yBegan, yEnd = (y - 1, y + 1)

    x_y = []

    for i in range(xBegan, xEnd + 1):
        for j in range(yBegan, yEnd + 1):
            if not (i == x and j == y):
                x_y.append((i, j))
    return x_y


def getRimKnownNum(x, y):
    '''
    获取周边已知雷的个数
    :param x:
    :param y:
    :return:
    '''
    x_y = getRimList(x, y)
    i = 0
    for a, b in x_y:
        if closeDate[a][b] == 1:
            i += 1
    return i


def getRimUnknow(x, y):
    '''
    获取周边的未知的位置区域
    :param x:
    :param y:
    :return: 返回一个list元组
    '''
    print('获取[{}][{}]周边位置'.format(x, y))
    location = []
    for a, b in getRimList(x, y):
        if unknown[a][b] == 1:
            location.append((a, b))
    return location


def getRimUnknowNum(x, y):
    '''
    获取周边位置区域的个数
    :param x:
    :param y:
    :return:
    '''
    print('获取[{}][{}]周边未知的个数'.format(x, y))
    return len(getRimUnknow(x, y))


def calculate(x, y):
    print('开始进行概率计算[{}][{}]'.format(x, y))
    pro = 1 - (openDate[x][y] - getRimKnownNum(x, y)) / getRimUnknowNum(x, y)  # 计算该已知点周边  未知区域的 没有雷区概率
    for a, b in getRimUnknow(x, y):
        result[a][b] += pro


def main():
    for j in range(0, 3):
        for i in range(0, 7):
            print('static[{}][{}]:{}'.format(j, i, static[j][i]))
            if static[j][i] == 1:
                # 表示需要进行概率计算
                print('需要进行概率计算', j, i)
                calculate(j, i)


if __name__ == '__main__':
    initList(result, 0.0)  # 将储存结果数组初始化
    main()
    print(result)
    a, b, a_bValue = '', '', 0.0
    for j in range(0, 3):
        for i in range(0, 7):
            if result[j][i] > a_bValue:
                a, b, a_bValue = j, i, result[j][i]
    print('无雷概率最大位置为第{}行第{}列：{}'.format(a + 1, b + 1, a_bValue))
