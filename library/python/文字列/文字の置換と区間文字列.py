def count_substrings(S: list[str], T: list[str]) -> int:
    """
    文字列Sの中で、文字列Tと一致する部分文字列の数を数える

    Args:
        S (list[str]): 検索対象の文字列（文字のリスト）
        T (list[str]): 検索する部分文字列（文字のリスト）

    Returns:
        int: Sの中でTと一致する部分文字列の数
    
    計算量: s=len(S), t=len(T)として
    - O(s*t)
    """

    count = 0
    for i in range(len(S) - len(T) + 1):
        if S[i:i+len(T)] == T:
            count += 1
    return count

def count_substrings_after_swap(S: list[str], T: list[str], count: int, x: int, c: str) -> int:
    """
    x番目の文字をcに変更したときの、部分文字列で、文字列Tと一致するものの個数を数える

    Args:
        S (list[str]): 検索対象の文字列（文字のリスト）
        T (list[str]): 検索する部分文字列（文字のリスト）
        count (int): 変更前の部分文字列で、文字列Tと一致するものの個数
        X (int): 変更する文字の位置（最初の文字の位置は0である）
        c (str): 変更後の文字

    Returns:
        int: 変更後の部分文字列で、文字列Tと一致するものの個数
    
    計算量: s=len(S), t=len(T)として
    - O(s*t)
    """
    def check(S:list[str], T:list[str]) -> bool:
        for i in range(len(T)):
            if S[x] == T[i]:
                start = x - i
                end = start + len(T)
                if start < 0 or end > len(S):
                    continue
                elif S[start:end] == T:
                    return True
        return False
    # 変更前の文字列のチェック
    if check(S, T):
      count -= 1
    # 変更後の文字列のチェック
    S[x] = c
    if check(S, T):
      count += 1
    return count
