# Git команды

Справочник по основным Git командам для работы с документацией.

## Базовые команды

### Конфигурация

```bash
# Установить имя пользователя
git config --global user.name "Ваше Имя"

# Установить email
git config --global user.email "email@example.com"

# Проверить настройки
git config --list
```

### Инициализация и клонирование

```bash
# Создать новый репозиторий
git init

# Клонировать репозиторий
git clone https://github.com/username/repo.git

# Клонировать конкретную ветку
git clone -b branch-name https://github.com/username/repo.git
```

## Работа с изменениями

### Просмотр статуса

```bash
# Показать статус файлов
git status

# Краткий вывод
git status -s

# Показать изменения
git diff

# Показать изменения в staged файлах
git diff --staged
```

### Добавление и коммит

```bash
# Добавить файл
git add filename.md

# Добавить все измененные файлы
git add .

# Добавить файлы в папке
git add docs/

# Создать коммит
git commit -m "docs: описание изменения"

# Добавить и закоммитить одной командой
git commit -am "docs: описание"
```

### Отмена изменений

```bash
# Отменить изменения в файле (до add)
git checkout -- filename.md

# Убрать файл из staged (после add)
git reset HEAD filename.md

# Изменить последний коммит
git commit --amend -m "новое сообщение"
```

## Работа с ветками

### Создание и переключение

```bash
# Посмотреть список веток
git branch

# Создать новую ветку
git branch feature-name

# Переключиться на ветку
git checkout feature-name

# Создать и переключиться одной командой
git checkout -b feature-name

# Новый способ (Git 2.23+)
git switch feature-name
git switch -c feature-name  # создать и переключиться
```

### Удаление веток

```bash
# Удалить локальную ветку
git branch -d branch-name

# Принудительное удаление
git branch -D branch-name

# Удалить удаленную ветку
git push origin --delete branch-name
```

## Работа с удаленным репозиторием

### Синхронизация

```bash
# Добавить удаленный репозиторий
git remote add origin https://github.com/username/repo.git

# Посмотреть удаленные репозитории
git remote -v

# Получить изменения (не применяя)
git fetch origin

# Получить и применить изменения
git pull origin main

# Отправить изменения
git push origin main

# Отправить новую ветку
git push -u origin feature-name
```

### Настройка upstream

```bash
# Добавить upstream репозиторий
git remote add upstream https://github.com/original/repo.git

# Синхронизация с upstream
git fetch upstream
git checkout main
git merge upstream/main
```

## Просмотр истории

```bash
# Показать историю коммитов
git log

# Краткий вывод
git log --oneline

# С графиком веток
git log --graph --oneline --all

# Последние N коммитов
git log -n 5

# История конкретного файла
git log -- filename.md

# Поиск по сообщениям коммитов
git log --grep="docs"
```

## Теги

```bash
# Создать тег
git tag v1.0.0

# Аннотированный тег
git tag -a v1.0.0 -m "Version 1.0.0"

# Посмотреть теги
git tag

# Отправить тег
git push origin v1.0.0

# Отправить все теги
git push origin --tags
```

## Работа с конфликтами

```bash
# При конфликте после pull или merge
# 1. Посмотреть файлы с конфликтами
git status

# 2. Открыть файл, найти и разрешить конфликты
# Конфликт выглядит так:
# <<<<<<< HEAD
# ваши изменения
# =======
# чужие изменения
# >>>>>>> branch-name

# 3. После разрешения конфликта
git add filename.md
git commit -m "docs: resolve merge conflict"
```

## Полезные команды для документации

### Работа с несколькими файлами

```bash
# Добавить все .md файлы
git add *.md

# Добавить все файлы в docs/
git add docs/

# Посмотреть изменения во всех .md файлах
git diff '*.md'
```

### Коммит для документации

```bash
# Conventional Commits для документации
git commit -m "docs: add installation guide"
git commit -m "docs: update API reference"
git commit -m "docs: fix typo in quickstart"
```

### Проверка перед push

```bash
# Посмотреть что будет отправлено
git log origin/main..HEAD

# Проверить статус
git status

# Проверить различия с удаленной веткой
git diff origin/main
```

## .gitignore

Создайте файл `.gitignore` для игнорирования ненужных файлов:

```gitignore
# MkDocs
site/

# Python
__pycache__/
*.pyc

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

## Алиасы (shortcuts)

Добавьте в `~/.gitconfig` для ускорения работы:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    cm = commit -m
    ca = commit -am
    df = diff
    lg = log --graph --oneline --all
    last = log -1 HEAD
```

Использование:

```bash
git st      # вместо git status
git co main # вместо git checkout main
git lg      # красивый лог
```

## Полезные ссылки

- [Pro Git Book](https://git-scm.com/book/ru/v2)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Conventional Commits](https://www.conventionalcommits.org/ru/)

## См. также

- [Быстрый старт](../getting-started/quickstart.md)
- [Работа с GitHub](../guides/github-workflow.md)
