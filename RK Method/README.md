# Метод Рунге-Кутты

Трехстадийный метод Рунге-Кутты третьего порядка точности для решения задачи Коши, заданной 
для дифференциального уравнения второго порядка:
    
<!-- 
\begin{cases}
\frac{d^2 y}{d x^2} + y \cdot cos(x) = 0,\\ 
y(0) = 1, \ y'(0) = 0;
\end{cases}
-->

<p align="center">
  <img src="data/images/equation.svg">
</p>


## Ход решения
Дифференциальное уравнение второго порядка сведено к системе двух уравнений первого порядка,
после чего к ней применен метод Хойна с помощью соответствующей таблицы Бутчера.


## Запуск кода
Находясь в текущей папке, ввести в терминал:
```commandline
python3 src/main.py data/data.csv
```

## Пример работы
![](https://github.com/Donskoy-Andrey/Numeric_Methods/blob/master/RK%20Method/data/images/output-0.025.png?raw=true)

![](https://github.com/Donskoy-Andrey/Numeric_Methods/blob/master/RK%20Method/data/images/deviation.png?raw=true)