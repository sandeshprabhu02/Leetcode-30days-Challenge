"""
Happy Trees
You’re given a balanced bracket expression. In the forest representation of it, find the number of trees which are happy. A happy tree is a tree in which every vertex other than the leaves has the same number of children. A tree with just one vertex would also be considered happy.
Input Format

First line of input consists of an integer t denoting the number of test cases. First line of each test case consists of an integer n denoting the length of the expression. Second line consists of the bracket expression.
Output Format

For each test case, find the number of trees which are happy.
Constraints

1 <= t <= 1000
n = 2 * m where 1 <= m <= 1000
Sample Input

4
12
[[[][]][[]]]
20
[[[][][]][][[][][]]]
14
[[]][[][[]]][]
28
[[[][]][[][]]][[][]][[[[]]]]
Sample Output

0
1
2
3
Explanation

The expression [[[][]][[]]] has the following representation
[]
├── []
│   ├── []
│   └── []
└── []
    └── []
There is only one tree. Root and second child of root has two children each. First child of root has only one child. It’s not happy.
The expression [[[][][]][][[][][]]] has the following representation
[]
├── []
│   ├── []
│   ├── []
│   └── []
├── []
└── []
    ├── []
    ├── []
    └── []
There is only one tree. All non-leaf vertices have exactly 3 children. Tree is happy.
The expression [[]][[][[]]][] has the following representation
[]
└── []
[]
├── []
└── []
    └── []
[]
There are three trees. Only two of them are happy.
The expression [[[][]][[][]]][[][]][[[[]]]] has the following representation
[]
├── []
│   ├── []
│   └── []
└── []
    ├── []
    └── []
[]
├── []
└── []
[]
└── []
    └── []
        └── []
The number of happy trees is 3.
Environment

Read from STDIN and write to STDOUT.
Please check the sample program below which prints the sum of two numbers received as input

"""
def calculateHappiness(maintree):
    count=0
    if maintree:
        for i in maintree:
            if maintree[i] and len(set(maintree[i].values())) == 1:
                count+=1
    return count


def happyTrees(s):
    stack = []
    maintree = {}
    subtree = {}
    count = 0
    prev = ''
    leaf = 0
    tree = 0
    isLeafAdded = False
    for i in s:
        # print(i)
        if len(stack) == 0 and count != 0:
            tree+=1
            maintree[tree] = subtree
            count=0
            leaf = 0
            subtree = {}
        if i == '[':
            if len(stack) == 1 and count!=0 and (leaf != 0):
                subtree[count] = leaf
                leaf=0
                count+=1
                isLeafAdded = True
            elif isLeafAdded:
                isLeafAdded = False
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if prev == ']' and not isLeafAdded:
                    subtree[count] = leaf
                    leaf=0
                    count+=1
                    isLeafAdded = True
                else:
                    leaf+=1
        prev = i
        # print('count', count)
        # print('leaf', leaf)
        # print('sub', subtree)
        # print('main', maintree)
        # print('--------------')
    tree += 1
    maintree[tree] = subtree
    return calculateHappiness(maintree)


print(happyTrees("[[[][]][[]]]"))
print(happyTrees("[[[][][]][][[][][]]]"))
print(happyTrees("[[]][[][[]]][]"))
print(happyTrees("[[[][]][[][]]][[][]][[[[]]]]"))