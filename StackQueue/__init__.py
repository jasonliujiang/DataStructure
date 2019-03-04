"""
栈和队列
栈（先进后出）
pop
push
top,peak

队列
pop
push
top,peak


深度优先遍历（DFS）：基于栈
宽度优先遍历（BFS）：基于队列

递归函数实际上用到了提供的函数系统栈

用两个栈实现队列结构：
StackPush+StackPop
1.往pop导数据一次性全部倒入
2.若pop中有数据，push不能导数据
"""
