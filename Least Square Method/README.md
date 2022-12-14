# Метод наименьших квадратов

Аппроксимация заданных точек полиномом степени N.

## Ход решения
Дифференциальное уравнение второго порядка сведено к системе двух уравнений первого порядка,
после чего к ней применен метод Хойна с помощью соответствующей таблицы Бутчера.


## Запуск кода
Находясь в текущей папке, вводить в терминал:

1. Для генерации исходных данных в data/data.txt (опционально):
```commandline
python3 src/generator.py
```

2. Запуск аппроксимации:
```commandline
python3 src/LSM.py N
```
где N - порядок аппроксимации (степень полинома). Если N = 1, 
то получаем линейную аппроксимацию, если N = 2, то параболическую и т.д.\
Например:
```commandline
python3 src/LSM.py 3
```

## Пример работы
![](https://github.com/Donskoy-Andrey/Numeric_Methods/blob/master/Least%20Square%20Method/data/images/image.png?raw=true)