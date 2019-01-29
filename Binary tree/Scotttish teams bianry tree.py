class bNode:
    # private leftpointer : INTEGER
    # private rightpointer: INTEGER
    # private data : STRING

    def __init__(self):
        self.leftpointer = 0
        self.rightpointer = 0
        self.data = ''

    def setData(value):
        data = value

    def getData():
        return data

    def setleftpointer(value):
        leftpointer = value

    def getleftPointer():
        return leftpointer

    def setrightpointer(value):
        rightpointer = value

    def getrightPointer():
        return rightpointer


bTree = [bNode, bNode, bNode, bNode, bNode, bNode, bNode, bNode]  # 8 nodes in the binary tree
bTree[0].setData('Celtic')
bTree[0].setleftpointer(3)
bTree[0].setrightpointer(1)

bTree[1].setData('Rangers')
bTree[1].setleftpointer(2)
bTree[1].setrightpointer(5)

bTree[2].setData('Kilmarnock')
bTree[2].setleftpointer(4)
bTree[2].setrightpointer(7)

bTree[3].setData('Aberdeen')
bTree[3].setleftpointer(0)
bTree[3].setrightpointer(0)

bTree[4].setData('Hearts')
bTree[4].setleftpointer(0)
bTree[4].setrightpointer(6)

bTree[5].setData('St Johnstone')
bTree[5].setleftpointer(0)
bTree[5].setrightpointer(0)

bTree[6].setData('Hibernian')
bTree[6].setleftpointer(0)
bTree[6].setrightpointer(0)

bTree[7].setData('Motherwell')
bTree[7].setleftpointer(0)
bTree[7].setrightpointer(0)


# in order traversal SHOULD output
# Aberdeen, Celtic, Hearts, Hibernian, Kilmarnock, Motherwell, Rangers, St Johnstone

def traverse(id):
    # get the node using id
    thisNode = bTree[id]

    # if the leftpointer > 0
    if thisNode.getleftpointer() > 0:
        # call traverse with the new node id (leftpointer)
        traverse(thisNode.getleftpointer())

    # output node data item
    print(thisNode.getData())

    # if the rightpointer > 0
    if thisNode.getrightpointer() > 0:
        # call traverse with the new node id (rightpointer)
        traverse(thisNode.getrightpointer())


traverse(0)
