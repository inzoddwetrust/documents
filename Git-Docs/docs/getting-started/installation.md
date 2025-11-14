# Установка

Руководство по установке необходимых инструментов для работы с документацией.

## Требования

Перед началом убедитесь, что у вас установлено:

- **Python 3.7+**
- **pip** (менеджер пакетов Python)
- **Git**

## Установка MkDocs

### macOS

```bash
# Установка через Homebrew
brew install python

# Установка MkDocs
pip3 install mkdocs mkdocs-material
```

### Linux (Ubuntu/Debian)

```bash
# Обновление системы
sudo apt update

# Установка Python и pip
sudo apt install python3 python3-pip

# Установка MkDocs
pip3 install mkdocs mkdocs-material
```

### Windows

```bash
# Установка через Chocolatey
choco install python

# Или скачайте Python с официального сайта
# https://www.python.org/downloads/

# Установка MkDocs
pip install mkdocs mkdocs-material
```

## Проверка установки

Проверьте, что всё установлено корректно:

```bash
# Проверка MkDocs
mkdocs --version

# Должно вывести что-то вроде:
# mkdocs, version 1.5.3
```

## Установка дополнительных плагинов

```bash
# Плагин для отображения даты последнего обновления
pip install mkdocs-git-revision-date-localized-plugin

# Минификация HTML
pip install mkdocs-minify-plugin
```

## Альтернатива: Docker

Если не хотите устанавливать локально, можете использовать Docker:

```bash
# Запуск MkDocs в Docker контейнере
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material

# Откройте http://localhost:8000
```

## Что дальше?

После установки переходите к [Быстрому старту](quickstart.md)

## Решение проблем

### Ошибка: "command not found: mkdocs"

Убедитесь, что путь к Python пакетам добавлен в PATH:

```bash
# Для macOS/Linux
export PATH="$HOME/.local/bin:$PATH"

# Добавьте эту строку в ~/.bashrc или ~/.zshrc
```

### Ошибка: "Permission denied"

Используйте `--user` флаг при установке:

```bash
pip install --user mkdocs mkdocs-material
```

## См. также

- [Быстрый старт](quickstart.md)
- [Конфигурация](../guides/configuration.md)
