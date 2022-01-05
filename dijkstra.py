import sys
from collections import defaultdict

# ensemble des sommets
V = ["Agadir", "Marakesh", "Casablanca", "Meknes", "Oujda", "Al hoceima", "Tangier"]
# l'ensemble des arêtes
E = [[["Agadir", "Casablanca"], 976.5], [["Agadir", "Marakesh"], 528.5], [["Marakesh", "Meknes"], 313.5],
     [["Marakesh", "Casablanca"], 484.5], [["Casablanca", "Meknes"], 456], [["Casablanca", "Tangier"], 679],
     [["Tangier", "Meknes"], 513.5], [["Meknes", "Al hoceima"], 578], [["Al hoceima", "Tangier"], 436.5],
     [["Meknes", "Oujda"], 778.5], [["Oujda","Al hoceima"],385.5]]

# L'algorithme de Dijkstra

def Dij(S, V, E):
    L = {}
    L = defaultdict(lambda:sys.maxsize, L)
    P = {}
    P = defaultdict(lambda:0, P)
    M = []
    L[S] = 0
    P[S] = 0
    for sommet in V:
        if sommet != S:
            for Ar in E:
                if ([S, sommet] in Ar) or ([sommet, S] in Ar):
                    L[sommet] = Ar[1]
                    P[sommet] = S
    M.append(S)
    while len(M) != len(V):
        tmp_L = L.copy()
        tmp_V = V.copy()

        for sommet in L:
            if sommet in M:
                tmp_L.pop(sommet)
                tmp_V.remove(sommet)
        x = min(tmp_L, key=tmp_L.get)
        for y in tmp_V:
            for Ar in E:
                if ([x, y] in Ar) or ([y, x] in Ar):
                    if L[y] > L[x] + Ar[1]:
                        L[y] = Ar[1] + L[x]
                        P[y] = x

        M.append(x)
    return M

# le plus court chemin :
best_path = Dij("Agadir", V, E)
print("le chemin optimal pour visiter tous les sommets\n",best_path)

print('------------------------------------------------------')

# le chemin optimal pour revenir à la racine sans visiter tous les sommets

def back_to_root(G, S, V, E):
    L = {}
    L = defaultdict(lambda: sys.maxsize, L)
    P = {}
    P = defaultdict(lambda: 0, P)
    M = []
    L[S] = 0
    P[S] = 0
    for sommet in V:
        if sommet != S:
            for Ar in E:
                if ([S, sommet] in Ar) or ([sommet, S] in Ar):
                    L[sommet] = Ar[1]
                    P[sommet] = S
    M.append(S)
    while len(M) != len(V):
        tmp_L = L.copy()
        tmp_V = V.copy()
        for sommet in L:
            if sommet in M:
                tmp_L.pop(sommet)
                tmp_V.remove(sommet)
        for y in tmp_V:
            if y == G:
                for Ar in E:
                    if ([M[-1], y] in Ar) or ([y, M[-1]] in Ar):
                        M.append(y)
                        M.reverse()
                        return M
        x = min(tmp_L, key=tmp_L.get)
        if(x==G):
            M.append(x)
            M.reverse()
            return M
        for y in tmp_V:
            for Ar in E:
                if ([x, y] in Ar) or ([y, x] in Ar):
                    if L[y] > L[x] + Ar[1]:
                        L[y] = Ar[1] + L[x]
                        P[y] = x
        M.append(x)
    M.reverse()
    return M

back_path = back_to_root(best_path[-1], best_path[0], V, E)
print("Meilleur chemin du retour\n",back_path)