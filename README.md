# Raport - sortowanie topologiczne grafów

## Testowanie dla n = 100
### Parametry wejściowe (fragment pliku):
```text
100 2475
68 98
74 75
30 84
32 51
73 76
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s] | Wynik (fragment)                         |
|:---------|:-------------------|:---------|:-----------------------------------------|
| Kahna    | Macierz Incydencji | 0.065243 | [1, 4, 6, 2, 3, ..., 98, 94, 95, 99, 96] |
| Kahna    | Lista Poprzedników | 0.000143 | [1, 4, 6, 2, 3, ..., 98, 94, 95, 99, 96] |
| Tarjana  | Macierz Incydencji | 0.041055 | [4, 1, 3, 7, 2, ..., 98, 94, 95, 96, 99] |
| Tarjana  | Lista Poprzedników | 0.000179 | [4, 1, 3, 7, 2, ..., 98, 94, 95, 96, 99] |
---

## Testowanie dla n = 250
### Parametry wejściowe (fragment pliku):
```text
250 15562
21 165
93 137
137 230
43 189
149 164
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s] | Wynik (fragment)                              |
|:---------|:-------------------|:---------|:----------------------------------------------|
| Kahna    | Macierz Incydencji | 0.748140 | [1, 2, 5, 3, 4, ..., 245, 247, 248, 249, 250] |
| Kahna    | Lista Poprzedników | 0.000648 | [1, 2, 5, 3, 4, ..., 245, 247, 248, 249, 250] |
| Tarjana  | Macierz Incydencji | 0.787507 | [5, 2, 3, 1, 4, ..., 246, 247, 248, 249, 250] |
| Tarjana  | Lista Poprzedników | 0.001035 | [5, 2, 3, 1, 4, ..., 246, 247, 248, 249, 250] |
---

## Testowanie dla n = 400
### Parametry wejściowe (fragment pliku):
```text
400 39900
78 299
41 345
2 73
94 268
204 397
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s] | Wynik (fragment)                              |
|:---------|:-------------------|:---------|:----------------------------------------------|
| Kahna    | Macierz Incydencji | 3.240142 | [1, 2, 3, 7, 4, ..., 396, 399, 397, 398, 400] |
| Kahna    | Lista Poprzedników | 0.001777 | [1, 2, 3, 7, 4, ..., 396, 399, 397, 398, 400] |
| Tarjana  | Macierz Incydencji | 3.204943 | [7, 3, 2, 4, 1, ..., 396, 397, 398, 399, 400] |
| Tarjana  | Lista Poprzedników | 0.002815 | [7, 3, 2, 4, 1, ..., 396, 397, 398, 399, 400] |
---

## Testowanie dla n = 550
### Parametry wejściowe (fragment pliku):
```text
550 75487
148 297
87 216
87 474
375 459
1 214
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s] | Wynik (fragment)                              |
|:---------|:-------------------|:---------|:----------------------------------------------|
| Kahna    | Macierz Incydencji | 8.458380 | [1, 2, 3, 4, 5, ..., 547, 546, 548, 549, 550] |
| Kahna    | Lista Poprzedników | 0.004030 | [1, 2, 3, 4, 5, ..., 547, 546, 548, 549, 550] |
| Tarjana  | Macierz Incydencji | 8.635438 | [1, 2, 3, 4, 6, ..., 548, 547, 546, 549, 550] |
| Tarjana  | Lista Poprzedników | 0.006098 | [1, 2, 3, 4, 6, ..., 548, 547, 546, 549, 550] |
---

## Testowanie dla n = 700
### Parametry wejściowe (fragment pliku):
```text
700 122325
248 549
471 648
408 508
274 549
35 348
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]  | Wynik (fragment)                              |
|:---------|:-------------------|:----------|:----------------------------------------------|
| Kahna    | Macierz Incydencji | 17.774747 | [1, 2, 4, 3, 6, ..., 695, 696, 700, 697, 699] |
| Kahna    | Lista Poprzedników | 0.008392  | [1, 2, 4, 3, 6, ..., 695, 696, 700, 697, 699] |
| Tarjana  | Macierz Incydencji | 17.953235 | [2, 1, 3, 4, 5, ..., 695, 696, 700, 697, 699] |
| Tarjana  | Lista Poprzedników | 0.010965  | [2, 1, 3, 4, 5, ..., 695, 696, 700, 697, 699] |
---

## Testowanie dla n = 850
### Parametry wejściowe (fragment pliku):
```text
850 180412
116 798
354 465
257 725
442 621
4 194
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]  | Wynik (fragment)                              |
|:---------|:-------------------|:----------|:----------------------------------------------|
| Kahna    | Macierz Incydencji | 32.399001 | [1, 2, 3, 4, 5, ..., 846, 848, 847, 849, 850] |
| Kahna    | Lista Poprzedników | 0.013779  | [1, 2, 3, 4, 5, ..., 846, 848, 847, 849, 850] |
| Tarjana  | Macierz Incydencji | 34.015965 | [3, 2, 1, 4, 5, ..., 847, 846, 848, 849, 850] |
| Tarjana  | Lista Poprzedników | 0.020765  | [3, 2, 1, 4, 5, ..., 847, 846, 848, 849, 850] |
---

## Testowanie dla n = 1000
### Parametry wejściowe (fragment pliku):
```text
1000 249750
296 556
331 497
444 754
88 215
545 895
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]  | Wynik (fragment)                               |
|:---------|:-------------------|:----------|:-----------------------------------------------|
| Kahna    | Macierz Incydencji | 52.992199 | [1, 2, 4, 3, 5, ..., 996, 998, 997, 999, 1000] |
| Kahna    | Lista Poprzedników | 0.022535  | [1, 2, 4, 3, 5, ..., 996, 998, 997, 999, 1000] |
| Tarjana  | Macierz Incydencji | 53.277981 | [2, 3, 5, 6, 4, ..., 996, 997, 998, 999, 1000] |
| Tarjana  | Lista Poprzedników | 0.025022  | [2, 3, 5, 6, 4, ..., 996, 997, 998, 999, 1000] |
---

## Testowanie dla n = 1150
### Parametry wejściowe (fragment pliku):
```text
1150 330337
308 1052
191 879
243 699
735 789
655 836
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]  | Wynik (fragment)                                   |
|:---------|:-------------------|:----------|:---------------------------------------------------|
| Kahna    | Macierz Incydencji | 81.955231 | [1, 2, 3, 4, 5, ..., 1146, 1147, 1150, 1148, 1149] |
| Kahna    | Lista Poprzedników | 0.047259  | [1, 2, 3, 4, 5, ..., 1146, 1147, 1150, 1148, 1149] |
| Tarjana  | Macierz Incydencji | 81.101796 | [1, 3, 2, 4, 6, ..., 1147, 1146, 1148, 1149, 1150] |
| Tarjana  | Lista Poprzedników | 0.036211  | [1, 3, 2, 4, 6, ..., 1147, 1146, 1148, 1149, 1150] |
---

## Testowanie dla n = 1300
### Parametry wejściowe (fragment pliku):
```text
1300 422175
686 1097
282 838
154 1000
11 1250
249 649
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]   | Wynik (fragment)                                   |
|:---------|:-------------------|:-----------|:---------------------------------------------------|
| Kahna    | Macierz Incydencji | 139.459027 | [1, 4, 2, 3, 5, ..., 1295, 1296, 1298, 1299, 1300] |
| Kahna    | Lista Poprzedników | 0.076064   | [1, 4, 2, 3, 5, ..., 1295, 1296, 1298, 1299, 1300] |
| Tarjana  | Macierz Incydencji | 128.284613 | [4, 1, 2, 3, 5, ..., 1296, 1295, 1298, 1299, 1300] |
| Tarjana  | Lista Poprzedników | 0.089803   | [4, 1, 2, 3, 5, ..., 1296, 1295, 1298, 1299, 1300] |
---

## Testowanie dla n = 1500
### Parametry wejściowe (fragment pliku):
```text
1500 562125
328 1357
621 979
285 301
381 702
886 1176
...
```

### Wyniki sortowania:
| Algorytm | Reprezentacja      | Czas [s]   | Wynik (fragment)                                   |
|:---------|:-------------------|:-----------|:---------------------------------------------------|
| Kahna    | Macierz Incydencji | 952.329666 | [1, 2, 7, 6, 3, ..., 1494, 1495, 1498, 1500, 1499] |
| Kahna    | Lista Poprzedników | 0.145533   | [1, 2, 7, 6, 3, ..., 1494, 1495, 1498, 1500, 1499] |
| Tarjana  | Macierz Incydencji | 997.733246 | [7, 2, 3, 1, 6, ..., 1493, 1495, 1498, 1500, 1499] |
| Tarjana  | Lista Poprzedników | 0.127363   | [7, 2, 3, 1, 6, ..., 1493, 1495, 1498, 1500, 1499] |
---

# Wykresy
![Wykres - macierz incydencji](/Plots/plot_linear_matrix.png)
![Wykres - lista poprzedników](/Plots/plot_linear_predecessors.png)
![Wykres - algorytm Kahna](/Plots/plot_log_kahn.png)
![Wykres - algorytm Tarjana](/Plots/plot_log_tarjan.png)


## Porównanie reprezentacji grafów
| Reprezentacja          | Zalety                                                                                                                 | Wady                                                                                                                       |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| **Macierz Incydencji** | Łatwa identyfikacja końców krawędzi; dobra do multigrafów (wielokrotne połączenia).                                    | Skrajnie nieefektywna pamięciowo ($O(V \cdot E)$), wyszukiwanie sąsiadów trwa $O(E)$, co drastycznie spowalnia sortowanie. |
| **Lista Poprzedników** | Oszczędność pamięci ($O(V+E)$), natychmiastowy dostęp do stopnia wejściowego (Kahn) i szybkie przeszukiwanie sąsiadów. | Bardziej złożona implementacja, wolniejsze sprawdzanie istnienia konkretnej krawędzi.                                      |
