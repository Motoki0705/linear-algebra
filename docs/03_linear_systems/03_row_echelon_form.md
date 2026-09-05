# 階段行列

行基本変形によって得られる row echelon form は、行列の構造を読みやすくします。

## Pivot

pivot の個数はランクに一致します。

`n` 個の未知数に対して pivot が `r` 個なら、自由変数は

\[
n-r
\]

個です。これは rank-nullity theorem と同じ内容です。

## RREF

reduced row echelon form まで変形すると、各 pivot 列は単位ベクトル型になり、解空間を直接読み取れます。

数値計算では必ずしも RREF が最良の手法ではありませんが、理論理解には非常に有用です。
