# def retrace_optimal_path(memo, n):
#     points_to_retrace = tuple(range(n))
#     full_path_memo = dict((k, v) for k, v in memo.items() 
#                           if k[0] == points_to_retrace)
#     path_key = min(full_path_memo.keys(), key=lambda x: full_path_memo[x][0])
    
#     last_point = path_key[1]
#     optimal_cost, next_to_last_point = memo[path_key]
#     optimal_path = [last_point]
    
#     points_to_retrace = tuple(sorted(set(points_to_retrace).difference({last_point})))
#     while next_to_last_point is not None:
#         last_point = next_to_last_point
#         path_key = (points_to_retrace, last_point)
#         _, next_to_last_point = memo[path_key]
        
#     optimal_path = [last_point] + optimal_path
#     return optimal_path, optimal_cost

# def DP_TSP(distances_array):
#   n = len(distances_array)
#   all_points_set = set(range(n))
  
#   # memo keys: tuple(sorted_points_in_path, last_point_in_path)
#   # memo values: tuple(cost_thus_far, next_to_last_point_in_path)
#   memo = {(tuple([i]), i): tuple([0, None]) for i in range(n)}
#   queue = [(tuple([i]), i) for i in range(n)]
  
#   while queue:
#     prev_visited, prev_last_point = queue.pop(0)
#     prev_dist, _ = memo[(prev_visited, prev_last_point)]
#     to_visit = all_points_set.difference(set(prev_visited))
    
#     for new_last_point in to_visit:
#       new_visited = tuple(sorted(list(prev_visited) + [new_last_point]))
#       new_dist = (prev_dist + distances_array[prev_last_point][new_last_point])
      
#       if (new_visited, new_last_point) not in memo:
#         memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
#         queue += [(new_visited, new_last_point)]
#       else:
#         if new_dist < memo[(new_visited, new_last_point)][0]:
#           memo[(new_visited, new_last_point)] = (new_dist, prev_last_point)
          
#   optimal_path, optimal_cost = retrace_optimal_path(memo, n)
#   return optimal_path, optimal_cost

# graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
#         [15, 35, 0, 30], [20, 25, 30, 0]] 
# graph = [[0, 10], 
#          [10,0]] 
# DP_TSP(graph)

# graph=[
#   [0, 1334, 1559, 809],
#   [1334, 0, 1343, 1397],
#   [1559, 1343, 0, 921],
#   [809, 1397, 921, 0]
# ]
# def f(Ensembre_ville, v_depart, v_arrive):
#   global graph
#   if len(Ensembre_ville)==2:
#     return graph[v_depart][v_arrive]
#   Ensembre_ville.pop(v_arrive)
#   costs=[]
#   for i in Ensembre_ville:
#     if i!=v_depart:
#       costs.append(f(Ensembre_ville, v_depart, i) + graph[i][v_arrive])
#   return min(costs)
# print(f([0, 1, 2, 3], 0, 0))

#https://mchouza.wordpress.com/2010/11/21/solving-the-travelling-salesman-problem/
# d=[
#   [0, 1334, 1559, 809],
#   [1334, 0, 1343, 1397],
#   [1559, 1343, 0, 921],
#   [809, 1397, 921, 0]
# ]

#ktb nb_ville 4id
nb_villes=10
import csv
with open(r'instances2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    d=[]
    tmp=0
    for i in csv_reader:
      if tmp<nb_villes:
        d.append(list(map(int, i))[:nb_villes])
      tmp+=1


# def tsp_rec_solve(d):
#     def rec_tsp_solve(c, ts):
#       assert c not in ts
#       if ts:
#         return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc) for lc in ts)
#       return (d[0][c], 0)
 
#     best_tour = []
#     c = 0
#     cs = set(range(1, len(d)))
#     cout_optimal=-1
#     while True:
#       l, lc = rec_tsp_solve(c, cs)
#       if cout_optimal==-1: cout_optimal=l
#       if lc == 0:
#           break
#       best_tour.append(lc)
#       c = lc
#       cs = cs - set([lc])
 
#     best_tour = [0]+list(reversed(best_tour))+[0]
#     return best_tour, cout_optimal

# t00=time.time()
# print(tsp_rec_solve(d))
# t11=time.time()
# print(f"le temps {t11-t00}")



#############--------USED--------#################
import time
def tsp_rec_solve(cout, v_cible):
    def rec_tsp_solve(vv_cible, vvilles_inter):
      assert vv_cible not in vvilles_inter
      if vvilles_inter:
        return min(
          (cout[lc][vv_cible] + rec_tsp_solve(lc, vvilles_inter - set([lc]))[0], lc) 
          for lc in vvilles_inter)
      return (cout[0][vv_cible], vv_cible)
 
    meilleur_tour, taille_cout = [], len(cout)
    villes_inter = set([i for i in range(taille_cout) if i!=v_cible])
    cout_optimal=-1
    while True:
      l_cout, avant_dernier_ville = rec_tsp_solve(v_cible, villes_inter)
      if cout_optimal==-1: cout_optimal=l_cout
      if avant_dernier_ville == v_cible:
          break
      meilleur_tour.insert(0,avant_dernier_ville)
      villes_inter -= set([avant_dernier_ville])
 
    meilleur_tour = [v_cible]+meilleur_tour+[v_cible]
    return meilleur_tour,cout_optimal
t00=time.time()
for i in range(1):print(tsp_rec_solve(d,i),"ville depart=",i)
t11=time.time()
print(f"le temps {t11-t00}")
##############################