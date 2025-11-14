# Быстрый старт

Научитесь работать с документацией за 5 минут!

## Шаг 1: Клонирование репозитория

```bash
# Клонируйте репозиторий
git clone https://github.com/username/documentation-artem.git
cd documentation-artem
```

## Шаг 2: Запуск локального сервера

```bash
# Установите зависимости (если еще не установлены)
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin

# Запустите сервер
mkdocs serve
```

Откройте в браузере: http://localhost:8000

!!! tip "Совет"
    Сервер автоматически перезагружается при изменении файлов!

## Шаг 3: Создание первого документа

Создайте новый файл в папке `docs/`:

```bash
# Создайте новый файл
touch docs/guides/my-first-guide.md
```

Откройте файл в редакторе и добавьте контент:

```markdown
# Мой первый гайд

Это мой первый документ в репозитории!

## Введение

Здесь я опишу что-то важное.

## Примеры

```bash
echo "Hello, Documentation!"
```

## Заключение

Теперь я знаю, как создавать документацию!
```

## Шаг 4: Добавление в навигацию

Откройте `mkdocs.yml` и добавьте ваш документ в секцию `nav`:

```yaml
nav:
  - Главная: index.md
  - Начало работы:
    - Установка: getting-started/installation.md
    - Быстрый старт: getting-started/quickstart.md
  - Руководства:
    - Мой первый гайд: guides/my-first-guide.md  # ← Добавьте эту строку
```

Сохраните файл и проверьте в браузере - новый документ появится в навигации!

## Шаг 5: Коммит изменений

```bash
# Добавьте файлы в Git
git add docs/guides/my-first-guide.md
git add mkdocs.yml

# Создайте коммит
git commit -m "docs: add my first guide"

# Отправьте в репозиторий
git push origin main
```

!!! success "Готово!"
    Ваши изменения автоматически задеплоятся на GitHub Pages в течение 1-2 минут!

## Основные команды

```bash
# Запуск сервера
mkdocs serve

# Сборка сайта
mkdocs build

# Деплой на GitHub Pages
mkdocs gh-deploy --force
```

## Структура проекта

```
documentation-artem/
├── docs/               # Документация
│   ├── index.md       # Главная страница
│   ├── getting-started/
│   ├── guides/
│   ├── reference/
│   └── tutorials/
├── mkdocs.yml         # Конфигурация
└── README.md          # Информация о проекте
```

## Советы

!!! tip "Совет 1: Live Reload"
    При запущенном `mkdocs serve` все изменения отображаются мгновенно!

!!! tip "Совет 2: Относительные ссылки"
    Используйте относительные ссылки между документами:
    ```markdown
    [Другой документ](../reference/api.md)
    ```

!!! tip "Совет 3: Проверка перед коммитом"
    Всегда проверяйте, что сайт корректно собирается:
    ```bash
    mkdocs build
    ```

## Что дальше?

- Изучите [Полное руководство по Docs as Code](../guides/docs-as-code-complete-guide.md)
- Узнайте про [Работу с GitHub](../guides/github-workflow.md)
- Настройте [Интеграцию с Claude](../guides/claude-integration.md)

## Нужна помощь?

- Создайте [Issue](https://github.com/username/documentation-artem/issues)
- Прочитайте [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Посмотрите [примеры](../tutorials/first-document.md)
