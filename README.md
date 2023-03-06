# Price-checker

## Описание

Программа на Python, которая в реальном времени (с заданной задержкой) следит за ценой фьючерса ETHUSDT и используя определяет собственные движение цены фьючерса ETHUSDT, исключив из них движения вызванные влиянием цены BTCUSDT. 
При изменении цены на 1% за последние 60 минут, программа выводит сообщение в консоль. При этом программа продолжает работать дальше, постоянно считывая актуальную цену.

### Применяемый метод

Предполагаю, что изменение цены ETH относительно BTC влияют на собственные движения цены фьючерса ETHUSDT.
Решил брать изменения ETH / BTC и прибавлять их к изменению ETHBTC.
В таком случае: рост ETH/BTC усиливает рост ETHUSTD, а снижение ETH/BTC - ослабевает.
Моих знаний в области технического анализа криптовалютного рынка пока не достаточно, чтобы применять индикаторы, осциляторы и скользящие средние.

Данные получаю с платформы https://www.bybit.com/
Для получения данных необходимы api-key и secret-key с данной платформы. Их можно быстро получить после регистрации.

## Как запустить программу:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Astapoff/trade_bot.git
```

```
cd trade_bot
```

Обновить pip:

```
py -m pip install --upgrade pip
```

Установить библиотеку pybit:

```
pip install pybit
```

Создать файл .env с двумя переменными:

```
api_key = 'Ваш api-key'
secret = 'Ваш secret-key'
```

Запустить программу:

```
py main.py
```
