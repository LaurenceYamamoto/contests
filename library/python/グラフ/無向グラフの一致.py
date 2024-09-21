def make_isomorphic(G: list[list[bool]], H: list[list[bool]], A: list[list[int]]|None =None) -> int:
    """
    無向グラフGとHを一致させるための最小コストを計算する。

    Args:
        G: list[list[bool]]
        H: list[list[bool]]
        - G,Hはグラフの初期状態を表す二次元配列。
        - G[i][j]がTrueのとき、頂点iと頂点jの間に辺があることを表す。
        A: list[list[int]] (OPTIONAL)
        - 辺の状態変更コストを表す二次元配列
        - G[i][j]は頂点[i][j]間の状態を変更するコストを表す
        - 省略された場合は、全ての辺の状態変更コストが1として扱われる

    Returns:
        int: グラフGとHを一致させるための最小コスト

    Note:
        - G[i][j]とH[i][j]がTrueの場合、頂点iと頂点jの間に辺が存在することを示す
        - Aが指定されない場合、全ての辺の状態変更コストは1として扱われる
    
    計算量：グラフの頂点数をNとして
        - O(N!*N^2*logN)
        - この関数は頂点数N<=9の場合に効率的に動作する（約1秒以内）
    """

    N = len(G)
    import itertools
    permutations = list(itertools.permutations(range(N)))
    cost = float('inf')
    for perm in permutations:
        costTmp = 0
        for i in range(N):
            for j in range(i+1, N):
                if G[perm[i]][perm[j]] != H[i][j]:
                    if A is None:
                        costTmp += 1
                    else:
                        costTmp += A[i][j]
        cost = min(cost, costTmp)
    return cost
