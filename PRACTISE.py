
# def bubblesort(list):
# # Swap the elements to arrange in order
#    for iter_num in range(len(list)-1,0,-1):
#       for idx in range(iter_num):
#         print(idx, end="")
#         if list[idx]>list[idx+1]:
#             temp = list[idx]
#             list[idx] = list[idx+1]
#             list[idx+1] = temp
# list = [3,5,8,9,10,12,14,20,95,90,60,40,35,23,18,0]
# bubblesort(list)
# print(list)


# 0.003988981246948242

# # Python program to illustrate functions
# # Functions can return another function

# def create_adder(x):
# 	def adder(y):
# 		return x+y

# 	return adder

# add_15 = create_adder(15)
# print(add_15(2))
# # print(add_15(10))

# BFS algorithm in Python


# import collections

# # BFS algorithm
# def bfs(graph, root):

#     visited, queue = set(), collections.deque([root])
#     visited.add(root)

#     while queue:

#         # Dequeue a vertex from queue
#         vertex = queue.popleft()
#         print(str(vertex) + " ", end="")

#         # If not visited, mark it as visited, and
#         # enqueue it
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)


# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     print("Following is Breadth First Traversal: ")
#     bfs(graph, 0)


# # DFS algorithm in Python
# def dfsOfGraph(V, adj):
#     # code here
#     def recur(adj, s, visited, ans):
#         visited[s] = 1
#         ans.append(s)
#         for j in adj[s]:
#             if visited[j] == 0:
#                 recur(adj, j, visited,ans)
#     ans = []
#     visited = [0]*V
#     # calling dfs for every vertex
#     for i in range(V):
#         if (visited[i] == 0):
#             recur(adj, i, visited, ans)
#     return ans

# V = 5
# adj = [[2,3,1] , [0], [0,4], [0], [2]]
# print(dfsOfGraph(V, adj))


# Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return self.data

# class LinkedList:
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next

#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)
    
# llist =  LinkedList(["a", "b", "c", "d", "e"])
# print(llist)


# Python3 program to detect loop
# in the linked list

# Node class
class Node:

	# Constructor to initialize
	# the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new
	# node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print it
	# the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		s = set()
		temp = self.head
		while (temp):

			# If we already have
			# this node in hashmap it
			# means there is a cycle
			# (Because we are encountering
			# the node second time).
			if (temp in s):
				return True

			# If we are seeing the node for
			# the first time, insert it in hash
			s.add(temp)

			temp = temp.next

		return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop Found")
else:
	print("No Loop ")

# This code is contributed by Gitanjali.
