# Метод Бубнова — Галёркина

Построение конечномерного приближения к решению краевой задачи для 
дифференциального уравнения второго порядка, представленного ниже:
    
<!-- 
\begin{cases}
y'' - 3' \cdot y' - y = x- 3,\\ 
y(0) = 0, \ y(1) = 3, x\ \epsilon \ [0, 1];
\end{cases}
-->

<p align="center">
  <img src="data/images/equation.svg">
</p>

## Ход решения
Решение представлено в виде разложения по базисным функциям, 
умноженным на соответствующие веса.


## Запуск кода
Находясь в текущей папке, ввести в терминал:
```commandline
python3 src/main.py
```

## Пример работы

<p align="center">
  <img src="https://github.com/Donskoy-Andrey/Numeric_Methods/blob/master/Galerkin%20Method/data/images/output-128.png?raw=true">
</p>

<p align="center">
  <img src="https://github.com/Donskoy-Andrey/Numeric_Methods/blob/master/Galerkin%20Method/data/images/deviation.png?raw=true">
</p>
