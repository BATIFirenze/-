import hashlib
class Node(object):
    def __init__(self,left=None,right=None,data=None,number=None):
        self.lchild = left
        self.rchild = right
        self.data = data
        self.number =number
        
def createtree(nodes):
    list_len = len(nodes)
    if list_len == 0:
        return 0
    else:
        while list_len %2 == 1:
            nodes.extend(nodes[-1:])
            list_len = len(nodes)
        secondary = []
        for k in [nodes[x:x+2] for x in range(0,list_len,2)]:
            d1 = k[0].data.encode('utf-8')
            d2 = k[1].data.encode('utf-8')
            md5 = hashlib.md5()
            md5.update(d1+d2)
            data0 = md5.hexdigest()
            node = Node(left=k[0],right=k[1],data=data0,number=d1+d2)
            secondary.append(node)
        if len(secondary) == 1:
            return secondary[0]
        else:
            return createtree(secondary)

def dfs(root):
    if  root != None:
        print("data:",root.data)
        dfs(root.lchild)
        dfs(root.rchild)

def bfs(root):
    print('start bfs')
    queue = []
    queue.append(root)
    while(len(queue)>0):
        e = queue.pop(0)
        print(e.data)
        if e.lchild != None:
            queue.append(e.lchild)
        if e.rchild != None:
            queue.append(e.rchild)


if __name__ == "__main__":
    blocks = ['1','2','3','4']
    nodes = []
    print("leaf hash")
    for e in blocks:
        md5 = hashlib.md5()
        md5.update(e.encode('utf-8'))
        d=md5.hexdigest()
        nodes.append(Node(data=d,number=e))
        print(d)
    root = createtree(nodes)
    dfs(root)
    bfs(root)
