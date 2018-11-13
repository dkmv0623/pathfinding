class Global(object):
    nofpaths = 0


def main():
    f = open("a.txt", 'r')
    X = [] #list for N*N grid
    N = 0 #size of grid(N*N)

    while True:
        line = f.readline() #read input
        if not line : break

        linelength = len(line)
        for i in range(0, linelength):
            x = line[i]
            if x != '\n':
                x = int(x)
                X.append(x)
                if i == 0:
                    N = N+1

    visited = [False]*(N**2) #list for labeling each nodes whether I already visited or not
    path(X, N, 0, visited)
    print("number of paths:", Global.nofpaths)


def path(X, N, i, visited): #path finding using DFS
    visited[i] = True #label the node to visited
    r = i // N
    c = i % N   #x, y coordinate of node X[i]

    if i == N**2-1: #we arrived at destination, so update the number of paths
        Global.nofpaths += 1

    else: #recursively apply the path finding function to adjacent available nodes that I haven't visited yet
        if c < N-1 and visited[right(N, i)] == False and X[right(N, i)] == 0:
            path(X, N, right(N, i), visited)
        if c > 0 and visited[left(N, i)] == False and X[left(N, i)] == 0:
            path(X, N, left(N, i), visited)
        if r < N-1 and visited[down(N, i)] == False and X[down(N, i)] == 0:
            path(X, N, down(N, i), visited)
        if r > 0 and visited[up(N, i)] == False and X[up(N, i)] == 0:
            path(X, N, up(N, i), visited)

    visited[i] = False

#functions for adjacent nodes
def right(N, i):
    return i+1

def left(N, i):
    return i-1

def down(N, i):
    return i+N

def up(N, i):
    return i-N

main()