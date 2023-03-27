# YaCut

### Описание

YaCut - сервис сокращения URL адресов.

### Технологии

Python 3.7
Flask 2.0.2

### Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrewYatskevich/yacut.git
```

```
cd yacut
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Выполнить миграции:

```
flask db upgrade
```

- Запустить проект:

```
flask run
```

Автор: Андрей Яцкевич https://github.com/AndrewYatskevich