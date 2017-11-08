Vertex

A vertex (also called a “node”) is a fundamental part of a graph. 
It can have a name, which we will call the “key.” 
A vertex may also have additional information. We will call this additional information the “payload.”

Edge

An edge (also called an “arc”) is another fundamental part of a graph. 
An edge connects two vertices to show that there is a relationship between them. 
Edges may be one-way or two-way. If the edges in a graph are all one-way, 
we say that the graph is a directed graph, or a digraph. 
The class prerequisites graph shown above is clearly a digraph since you must take some classes before others.

Weight

Edges may be weighted to show that there is a cost to go from one vertex to another. 
For example in a graph of roads that connect one city to another, 
the weight on the edge might represent the distance between the two cities.

With those definitions in hand we can formally define a graph. 
A graph can be represented by GG where G=(V,E)G=(V,E). 
For the graph GG, VV is a set of vertices and EE is a set of edges. 
Each edge is a tuple (v,w)(v,w) where w,v∈Vw,v∈V. 
We can add a third component to the edge tuple to represent a weight. 
A subgraph ss is a set of edges ee and vertices vv such that e⊂Ee⊂E and v⊂Vv⊂V.

Formally we can represent this graph as the set of six vertices:
V={V0,V1,V2,V3,V4,V5}
V={V0,V1,V2,V3,V4,V5}
and the set of nine edges:
E={(v0,v1,5),(v1,v2,4),(v2,v3,9),(v3,v4,7),(v4,v0,1),(v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)}
E={(v0,v1,5),(v1,v2,4),(v2,v3,9),(v3,v4,7),(v4,v0,1),(v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)}

Path

A path in a graph is a sequence of vertices that are connected by edges. 
Formally we would define a path as w1,w2,...,wnw1,w2,...,wn such that (wi,wi+1)∈E(wi,wi+1)∈E for all 1≤i≤n−11≤i≤n−1. 
The unweighted path length is the number of edges in the path, specifically n−1n−1. 
The weighted path length is the sum of the weights of all the edges in the path. 
The edges are {(v3,v4,7),(v4,v0,1),(v0,v1,5)}{(v3,v4,7),(v4,v0,1),(v0,v1,5)}.

Cycle

A cycle in a directed graph is a path that starts and ends at the same vertex. 
A graph with no cycles is called an acyclic graph. 
A directed graph with no cycles is called a directed acyclic graph or a DAG. 
We will see that we can solve several important problems if the problem can be represented as a DAG.
