
from math import gcd
t=int(input())
for _ in range(t):
	no=int(input())
	ad=[list for x in range(n)]
	for i in range(n-1):
      u,v=map(int,input().strip().split())
	  adj[u-1].append(v-1)
	   adj[v-1].append(u-1)
	v=list(map(str,input().strip().split()))
	m=list(map(str,input().strip().split())

	factors=[0]*n
	leaves=[]
	parent=[1]*n
	queue=[0]
	for i in queue:
		children=set(adj[i])-set([parent[i]])
		if(parent[i]==-1):
		  factors[i]=v[i]
		else:
		  factors[i]=gcd(factors[parent[i],v[i])
		if(len(children)<=0):
		  leavs.append(i)
		for q in children:
		  parent[q]=i
		   queue.append(q)
	sorted(leaves)
	re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
	print(*re)

SAMPLE  INPUT-1
1
5
1 2
2 5
1 3
3 4
2 3 4 6 7
1 2 3 2 10
SAMPLE OUTPUT:1
0 9
