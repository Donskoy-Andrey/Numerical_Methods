# Метод Адамса
Интерполяционная разностная схема Адамса 4 порядка для решения задачи Коши, заданной для
обыкновенного дифференциального уравнения первого порядка.

<p align="center">
  <img src="data/images/img.png">
</p>

## Ход решения
Вычисление значений происходит в два этапа:
1. Экстраполяция по формуле Адамса 4 порядка на следующее значение.
2. Корректировка полученного значения с помощью интерполяционного многочлена Адамса.

## Запуск кода
Находясь в текущей папке, ввести в терминал:
```commandline
python3 src/main.py
```

## Пример работы
![](https://github.com/Donskoy-Andrey/Numerical_Methods/blob/master/Adam%20Method/data/images/output-0.0625.png?raw=true)
![](https://github.com/Donskoy-Andrey/Numerical_Methods/blob/master/Adam%20Method/data/images/deviation.png?raw=true)
