# 直交射影

単位ベクトル `q` が張る直線への `x` の射影は

\[
\operatorname{proj}_q(x)=(q^\top x)q
\]

です。

正規直交列を持つ `Q` が部分空間を張るなら

\[
\boxed{P=QQ^\top}
\]

が射影行列です。

一般の full-column-rank 行列 `A` の列空間への射影は

\[
\boxed{P=A(A^\top A)^{-1}A^\top}
\]

です。

## 最小二乗との接続

`Ax=b` が解けない場合、`b` を `Col(A)` に直交射影した点 `\hat b` を探します。

\[
\hat b=Ax_*
\]

残差

\[
r=b-Ax_*
\]

は列空間と直交するので

\[
A^\top r=0
\]

となり、正規方程式

\[
A^\top Ax_*=A^\top b
\]

が導かれます。
