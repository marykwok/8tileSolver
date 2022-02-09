import heapq
import copy

def succ(state):
    idx = state.index(0)
    x = int(idx/3); y= idx%3
    adj_idx = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    states = []
    for n in adj_idx:
        if 0<=n[0]<=2 and 0<=n[1]<=2:
            new_state = copy.deepcopy(state)
            new_state[int(n[0]*3+n[1])] = 0
            new_state[idx] = state[int(n[0]*3+n[1])]
            states.append(new_state)
    states.sort()
    return states

def print_succ(state):
    states = succ(state)
    for new_state in states:
        print(str(new_state) + " h=" + str(h_func(new_state)))

def h_func(state):
    h = 0
    solved = [1,2,3,4,5,6,7,8,0]
    for n in state:
        if n==0: continue
        idx = state.index(n)
        s_idx = solved.index(n)
        h += abs(int(idx/3)-int(s_idx/3)) + abs(idx%3-s_idx%3)
    return h

def solve(state):
    goal = [1,2,3,4,5,6,7,8,0]
    open = []; closed = []
    heapq.heappush(open, (h_func(state),state,(0,h_func(state),-1)))
    while len(open)!=0:
        n = heapq.heappop(open)
        closed.append(n)
        if n[1]==goal: break
        for n_succ in succ(n[1]):
            g = n[2][0]+1
            h = h_func(n_succ)
            parent_index = closed.index(n)
            if not any(n_succ in x for x in closed+open):
                heapq.heappush(open,(g+h,n_succ,(g,h,parent_index)))
            else:
                for x in closed+open:
                    if n_succ == x[1] and g < x[2][0]:
                            if x in open: open.remove(x)
                            heapq.heappush(open,(g+h,n_succ,(g,h,parent_index)))
    path = [closed[-1]]
    idx = closed[-1][2][2]
    while idx !=-1:
        path.insert(0,closed[idx])
        idx = closed[idx][2][2]
    for x in path:
        print(str(x[1]) + " h="+str(x[2][1])+" moves: "+str(x[2][0]))




