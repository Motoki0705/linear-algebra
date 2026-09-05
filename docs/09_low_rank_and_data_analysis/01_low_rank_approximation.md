# 低ランク近似

SVD

\[
A=\sum_{i=1}^r\sigma_i u_i v_i^\top
\]

で特異値を大きい順に並べます。

上位 `k` 個だけ残した

\[
\boxed{A_k=\sum_{i=1}^k\sigma_i u_i v_i^\top}
\]

はランク `k` 以下です。

## Eckart–Young–Mirsky 定理

驚くべきことに `A_k` は、すべての rank ≤ k の行列の中で `A` に最も近い行列です。

\[
A_k=\arg\min_{\operatorname{rank}(B)\le k}\|A-B\|_F
\]

さらに

\[
\|A-A_k\|_F^2=\sum_{i>k}\sigma_i^2
\]

です。

## 意味

SVD は単に「大きい成分を残す経験則」ではありません。指定されたランク制約の下で数学的に最適な近似を与えます。

特異値が急速に減衰する行列は、低次元構造を持つと考えられます。
