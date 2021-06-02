class Array2D:
    """
        说明：
            1.构造方法需要两个参数，即二维数组的宽和高
            2.成员变量w和h是二维数组的宽和高
            3.使用：‘对象[x][y]’可以直接取到相应的值
            4.数组的默认值都是0
    """

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.data = []
        self.data = [[0 for y in range(h)] for x in range(w)]

    def showArray2D(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end=' ')
            print("")

    def __getitem__(self, item):
        return self.data[item]


class Point:
    """
    表示一个点
    """

    def __init__(self, x, y):
        self.x = x;
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return "x:" + str(self.x) + ",y:" + str(self.y)


class AStar:
    """
    AStar算法的Python3.x实现
    """

    class Node:  # 描述AStar算法中的节点数据
        def __init__(self, point, endPoint, g=0):
            self.point = point  # 自己的坐标
            self.father = None  # 父节点
            self.g = g  # g值，g值在用到的时候会重新算
            self.h = (abs(endPoint.x - point.x) + abs(endPoint.y - point.y)) * 10  # 计算h值

    def __init__(self, map2d, startPoint, endPoint, passTag=0):
        """
        构造AStar算法的启动条件
        :param map2d: Array2D类型的寻路数组
        :param startPoint: Point或二元组类型的寻路起点
        :param endPoint: Point或二元组类型的寻路终点
        :param passTag: int类型的可行走标记（若地图数据!=passTag即为障碍）
        """
        # 开启表
        self.openList = []
        # 关闭表
        self.closeList = []
        # 寻路地图
        self.map2d = map2d
        # 起点终点
        #********** Begin **********#
        self.startPoint = startPoint
        self.endPoint = endPoint
        #********** End **********#
        # 可行走标记
        self.passTag = passTag
        
    def getMinNode(self):
        """
        获得openlist中F值最小的节点
        :return: Node
        """

        #********** Begin **********#
        f = self.openList[0]
        for node in self.openList:
            if node.g + node.h < f.g + f.h:
                f = node
        return f
        #********** End **********#

    def pointInCloseList(self, point):
        for node in self.closeList:
            if node.point == point:
                return True
        return False

    def pointInOpenList(self, point):
        for node in self.openList:
            if node.point == point:
                return node
        return None

    def endPointInCloseList(self):
        for node in self.openList:
            if node.point == self.endPoint:
                return node
        return None

    def searchNear(self, minF, offsetX, offsetY):
        """
        搜索节点周围的点
        :param minF:F值最小的节点
        :param offsetX:坐标偏移量
        :param offsetY:
        :return:
        """
        # 越界检测
        #********** Begin **********#
        if minF.point.x + offsetX > 9 or minF.point.y + offsetY > 9 or minF.point.x + offsetX < 0 or minF.point.y + offsetY < 0:
            return 
        #********** End **********#
        # 如果是障碍，就忽略
        if self.map2d[minF.point.x + offsetX][minF.point.y + offsetY] != self.passTag:
            return
        # 如果在关闭表中，就忽略
        currentPoint = Point(minF.point.x + offsetX, minF.point.y + offsetY)
        if self.pointInCloseList(currentPoint):
            return
        # 设置单位花费
        if offsetX == 0 or offsetY == 0:
            step = 10
        else:
            step = 14
        # 如果不再openList中，就把它加入openlist
        #********** Begin **********#
        currentNode = self.Node(currentPoint,self.endPoint,minF.g+step)
        if self.pointInOpenList(currentPoint) == None:
            currentNode.father = minF
            self.openList.append(currentNode)
        #********** End **********#
        # 如果在openList中，判断minF到当前点的G是否更小
        if minF.g + step < currentNode.g:  # 如果更小，就重新计算g值，并且改变father
            currentNode.g = minF.g + step
            currentNode.father = minF

    def start(self):
        """
        开始寻路
        :return: None或Point列表（路径）
        """
        # 判断寻路终点是否是障碍
        if self.map2d[self.endPoint.x][self.endPoint.y] != self.passTag:
            return None

        # 1.将起点放入开启列表
        startNode = AStar.Node(self.startPoint, self.endPoint)
        self.openList.append(startNode)
        # 2.主循环逻辑
        while True:
            # 找到F值最小的点
            minF = self.getMinNode()
            # 把这个点加入closeList中，并且在openList中删除它
            self.closeList.append(minF)
            self.openList.remove(minF)
            # 判断这个节点的上下左右节点
            #********** Begin **********#
            for i in [1,1,-1,-1]:
                for j in [0,0,1,-1,1,-1,1,-1]:
                    self.searchNear(minF,i,j)
            #********** End **********#
            # 判断是否终止
            point = self.endPointInCloseList()
            if point != None:  # 如果终点在关闭表中，就返回结果
                # print("关闭表中")
                cPoint = point
                pathList = []
                while True:
                    if cPoint.father:
                        pathList.append(cPoint.point)
                        cPoint = cPoint.father
                    else:
                        return list(reversed(pathList))
            if len(self.openList) == 0:
                return None

if __name__ == '__main__':
    #创建一个10*10的地图
    map2d=Array2D(10,10)
    #设置障碍
    map2d[4][0]= 1
    map2d[4][1] = 1
    map2d[4][2] = 1
    map2d[4][3] = 1
    map2d[4][4] = 1
    map2d[4][5] = 1
    map2d[4][6] = 1
    #显示地图当前样子
    #map2d.showArray2D()
    #创建AStar对象,并设置起点为0,0终点为9,0
    aStar=AStar(map2d,Point(0,0),Point(9,0))
    #开始寻路
    pathList=aStar.start()
    print(pathList)
    #遍历路径点,在map2d上以'8'显示
    for point in pathList:
        map2d[point.x][point.y]=8
        print(point)
    print("----------------------")
    #再次显示地图
    map2d.showArray2D()

