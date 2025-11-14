# Интеграция с Claude AI

Руководство по настройке и использованию Claude AI для автоматизации работы с документацией.

## Введение

Claude AI может помочь вам:
- Создавать новые документы
- Обновлять существующую документацию
- Исправлять ошибки и битые ссылки
- Генерировать примеры кода
- Проводить ревью документации

## Настройка

### Шаг 1: Установка Claude GitHub App

#### Через Claude терминал (рекомендуется)

```bash
# В терминале Claude Code
/install-github-app
```

Следуйте инструкциям установщика.

#### Вручную

1. Перейдите на https://github.com/apps/claude
2. Нажмите "Install"
3. Выберите репозиторий `documentation-artem`
4. Разрешите необходимые права:
   - Read & Write для Contents
   - Read & Write для Issues
   - Read & Write для Pull Requests

### Шаг 2: Добавление API ключа

1. Получите API ключ:
   - Зайдите в https://console.anthropic.com/
   - Создайте новый API ключ
   - Скопируйте его

2. Добавьте в GitHub Secrets:
   - Откройте репозиторий на GitHub
   - Settings → Secrets and variables → Actions
   - Нажмите "New repository secret"
   - Name: `ANTHROPIC_API_KEY`
   - Value: ваш API ключ
   - Нажмите "Add secret"

### Шаг 3: Проверка workflow

Убедитесь, что файл `.github/workflows/claude.yml` существует:

```yaml
name: Claude Documentation Assistant

on:
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  pull_request:
    types: [opened, synchronize]
  pull_request_review_comment:
    types: [created]

jobs:
  claude:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
      pull-requests: write
    
    steps:
    - name: Claude Code Action
      uses: anthropics/claude-code-action@v1
      with:
        anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Использование

### Создание нового документа

**В Issue:**

```markdown
@claude создай руководство по работе с Docker

Структура:
- Введение
- Установка на разные ОС
- Основные команды
- Примеры использования
- Troubleshooting

Файл: docs/guides/docker-guide.md
```

Claude:
1. Создаст новый файл `docs/guides/docker-guide.md`
2. Заполнит его контентом по структуре
3. Добавит в навигацию `mkdocs.yml`
4. Создаст Pull Request

### Обновление существующего документа

**В Issue или PR комментарии:**

```markdown
@claude обнови docs/getting-started/installation.md

Добавь:
- Инструкции для установки на Windows
- Скриншоты процесса установки
- Раздел "Решение проблем"
```

### Исправление ошибок

```markdown
@claude исправь битые ссылки в документации
```

```markdown
@claude найди и исправь опечатки в docs/guides/
```

### Генерация примеров

```markdown
@claude добавь примеры кода на Python и JavaScript в docs/reference/api.md для каждого endpoint
```

### Ревью документации

```markdown
@claude проверь docs/guides/new-guide.md:
- Грамматика и стиль
- Полнота информации
- Работоспособность примеров
- Соответствие стайл-гайду
```

## Примеры запросов

### 1. Создание структурированного документа

```markdown
@claude создай документ docs/guides/kubernetes-basics.md

Содержание:
1. Введение в Kubernetes
   - Что такое Kubernetes
   - Основные концепции
2. Установка
   - Minikube для локальной разработки
   - kubectl CLI
3. Первое приложение
   - Создание Deployment
   - Создание Service
   - Проверка работы
4. Примеры команд
5. Полезные ссылки

Стиль: для начинающих, с примерами команд
```

### 2. Миграция из Google Docs

```markdown
@claude конвертируй содержимое этого Google Doc в Markdown:
https://docs.google.com/document/d/xxxxx

Создай файл: docs/guides/migrated-content.md
Сохрани форматирование и добавь в навигацию
```

### 3. Обновление всех примеров

```markdown
@claude обнови все примеры кода в docs/reference/ 

Требования:
- Используй последнюю версию синтаксиса
- Добавь комментарии
- Убедись что примеры работают
```

### 4. Создание API документации

```markdown
@claude сгенерируй API документацию из OpenAPI спецификации

Файл спецификации: api/openapi.yaml
Целевой файл: docs/reference/api.md

Включи:
- Описание каждого endpoint
- Примеры запросов (curl, Python, JavaScript)
- Примеры ответов
- Коды ошибок
```

### 5. Проверка актуальности

```markdown
@claude проверь документацию в docs/ на актуальность

Проверь:
- Битые ссылки
- Устаревшие версии в примерах
- Deprecated функции
- Отсутствующие разделы

Создай Issue со списком проблем
```

## CLAUDE.md файл

Файл `CLAUDE.md` в корне репозитория содержит инструкции для Claude.

**Основные секции:**

```markdown
# Инструкции для Claude

## Стиль документации
- Язык: русский
- Формат: Markdown
- Тон: профессиональный, дружелюбный

## Структура
- docs/getting-started/ - для новичков
- docs/guides/ - детальные руководства
- docs/reference/ - справочная информация
- docs/tutorials/ - пошаговые инструкции

## Форматирование
- H1 - один на страницу
- Короткие параграфы
- Примеры кода обязательны
- Относительные ссылки

## Коммиты
Формат: `docs: краткое описание`
```

## Best Practices

### DO ✅

- **Будьте конкретны** в запросах
- **Указывайте структуру** для новых документов
- **Предоставляйте контекст** при обновлении
- **Проверяйте результат** перед мерджем
- **Используйте Issues** для сложных задач

### DON'T ❌

- Не делайте слишком общие запросы
- Не ждите идеального результата с первого раза
- Не забывайте проверять и редактировать
- Не игнорируйте стайл-гайд

## Ограничения

Claude может **не** уметь:
- Получать доступ к приватным данным без разрешений
- Мержить PR автоматически (нужно одобрение)
- Получать реальное время (используйте относительные даты)

## Workflow с Claude

### Простая задача (создание документа)

```mermaid
graph TD
    A[Создать Issue] --> B[@claude запрос]
    B --> C[Claude создает PR]
    C --> D[Ревью PR]
    D --> E[Мердж]
```

### Сложная задача (обновление множества файлов)

```mermaid
graph TD
    A[Создать Issue] --> B[Детальное ТЗ]
    B --> C[@claude запрос]
    C --> D[Claude создает PR]
    D --> E[Ревью и правки]
    E --> F{Нужны изменения?}
    F -->|Да| G[@claude внеси правки]
    G --> E
    F -->|Нет| H[Мердж]
```

## Мониторинг использования

### GitHub Actions logs

Проверяйте логи выполнения:
1. Actions → Claude Documentation Assistant
2. Выберите последний run
3. Просмотрите логи

### API usage

Отслеживайте использование API на https://console.anthropic.com/

## Безопасность

!!! danger "Важно"
    - **Никогда** не коммитьте API ключи в код
    - Используйте **только** GitHub Secrets
    - Ограничьте **права** GitHub App минимумом
    - **Ревьюйте** все PR от Claude перед мерджем

## Troubleshooting

### Claude не отвечает

**Проблема**: Нет реакции на @claude

**Решения**:
1. Проверьте, установлен ли GitHub App
2. Проверьте API ключ в Secrets
3. Проверьте логи GitHub Actions
4. Убедитесь, что workflow файл существует

### Неправильный результат

**Проблема**: Claude создал не то, что нужно

**Решение**: Будьте более конкретны в запросе

❌ Плохо:
```markdown
@claude создай документ про Docker
```

✅ Хорошо:
```markdown
@claude создай пошаговое руководство по установке Docker 
для macOS, Linux и Windows в файле docs/guides/docker-install.md

Структура:
1. Требования
2. Установка для каждой ОС
3. Проверка установки
4. Первый контейнер
5. Troubleshooting

Включи примеры команд и скриншоты (placeholder)
```

### PR не создается

**Проблема**: Claude ответил, но PR не создан

**Возможные причины**:
- Недостаточно прав у GitHub App
- Ошибка в workflow
- API лимиты превышены

**Решение**: Проверьте логи Actions и права App

## Примеры реальных сценариев

### Еженедельное обновление

Создайте recurring Issue:

```markdown
# Еженедельная проверка документации

@claude выполни еженедельную проверку:

1. Проверь все ссылки в docs/
2. Обнови даты "последнего обновления"
3. Проверь актуальность версий в примерах
4. Найди TODO и FIXME комментарии

Создай PR с исправлениями или список проблем
```

### Синхронизация с кодом

При изменении API:

```markdown
@claude API изменился, обнови документацию

Изменения:
- Endpoint /users теперь /api/v2/users
- Добавлен новый параметр 'role'
- Удален параметр 'admin' (deprecated)

Обнови все упоминания в docs/reference/ и docs/guides/
```

## Расширенные возможности

### Custom prompts

Создайте специализированные промпты для частых задач:

```markdown
<!-- .github/prompts/create-api-doc.md -->

Создай API документацию для endpoint:

URL: {{url}}
Method: {{method}}
Описание: {{description}}

Включи:
- Параметры запроса
- Тело запроса (если есть)
- Примеры ответов
- Коды ошибок
- Примеры на curl, Python, JavaScript
```

### Batch operations

```markdown
@claude выполни batch обновление:

Для каждого файла в docs/guides/:
1. Добавь секцию "Что дальше?" в конце
2. Добавь ссылки на 2-3 связанных документа
3. Убедись что есть хотя бы один пример кода
```

## См. также

- [CLAUDE.md](../../CLAUDE.md) - инструкции для Claude
- [GitHub Workflow](github-workflow.md) - работа с GitHub
- [Best Practices](../reference/best-practices.md) - лучшие практики

## Ресурсы

- [Claude API Documentation](https://docs.anthropic.com/)
- [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action)
- [Anthropic Console](https://console.anthropic.com/)
