class AccumulateSum:
    """
    AccumulateSum クラス

    このクラスは、与えられた位置と値のペアのリストに対して累積和を計算し、
    指定された区間の和を効率的に求めるための機能を提供する。

    主な機能:
    - 初期化時に累積和を計算
    - 指定された区間の和を高速に計算

    使用例:
    values = [[1, 10], [3, 20], [5, 30]]
    acc_sum = AccumulateSum(values)
    result = acc_sum.query(2, 4)

    注意:
    - 位置は整数または浮動小数点数で指定可能
    - 値は整数または浮動小数点数
    - 区間の指定は閉区間か開区間を選択可能

    計算量: N = len(values), クエリ数をQとして
    - 累積和の計算にO(N+logN)
    - クエリにO(Q)
    """
    def __init__(self, values:list[list[int|float]|tuple[int|float]]):

        """
        累積和を計算するためのクラスを初期化する。

        引数:
        values: list[list[int|float]|tuple[int|float]] - [位置, 値]の組のリスト
            例: [[1, 10], [3, 20], [5, 30]]

        注意:
        - 入力リストは自動的に位置でソートされるため、事前のソートは不要。
        - 位置は整数または浮動小数点数で指定可能。
        - 値は整数または浮動小数点数。

        計算量： N = len(values)として
        - ソートにO(NlogN)
        - 計算にO(N)
        - 全体でO(N+NlogN)
        """

        self.size = len(values)

        self.values = sorted(values, key=lambda x: x[0])
        self.pos = [value[0] for value in self.values]
        self.values = [value[1] for value in self.values]
        self.accumulate_sum = [0] * (self.size + 1)
        for i in range(self.size):
            self.accumulate_sum[i + 1] = self.accumulate_sum[i] + self.values[i]


    def query(self, left:int|float, right:int|float, left_include:bool=True, right_include:bool=False):
        """
        指定された区間の累積和を計算する。

        引数:
        left: int|float - 区間の左端
        right: int|float - 区間の右端
        left_include: bool=True - 左端を含むかどうか
        right_include: bool=False - 右端を含むかどうか
        
        戻り値:
        int|float - 指定された区間の累積和

        計算量：
        - O(1)
        """
        from bisect import bisect_left, bisect_right

        if left_include:

            left_index = bisect_left(self.pos, left)
        else:
            left_index = bisect_right(self.pos, left)
        if right_include:
            right_index = bisect_right(self.pos, right)
        else:
            right_index = bisect_left(self.pos, right)
        return self.accumulate_sum[right_index] - self.accumulate_sum[left_index]