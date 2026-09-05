# 解答 08 — 最小二乗と逆問題

## 1

\[
A=\begin{bmatrix}0&1\\1&1\\2&1\end{bmatrix},\quad
x=\begin{bmatrix}a\\b\end{bmatrix},\quad
y=\begin{bmatrix}1\\2\\2\end{bmatrix}.
\]

正規方程式は

\[
\begin{bmatrix}5&3\\3&3\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}
=\begin{bmatrix}6\\5\end{bmatrix}.
\]

これを解くと `a=1/2`, `b=7/6` です。

## 2

\[
\|Ax-b\|^2=(Ax-b)^T(Ax-b)
=x^TA^TAx-2b^TAx+b^Tb.
\]

勾配を0に置けば `A^TAx=A^Tb` です。

## 3

`P^T=P` と `P^2=P` を確認できます。また `Px` は `A` の列の一次結合なので列空間上にあり、列空間上の `y=Ac` に対して `Py=y` です。従って直交射影です。

## 4

可逆なら全特異値が正で `Σ^+=Σ^{-1}`。したがって

\[
A^+=VΣ^{-1}U^T=(UΣV^T)^{-1}=A^{-1}.
\]

## 5

\[
\kappa_2(A)=10/10^{-4}=10^5.
\]

ある方向が別方向に比べて10万倍弱く観測されるため、逆算時には相対誤差が大きく増幅され得ます。
