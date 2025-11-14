# 📚 Documentation Artem

Репозиторий документации с использованием подхода Docs as Code.

## 🚀 Быстрый старт

### Локальная разработка

```bash
# Установка зависимостей
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin

# Запуск локального сервера
mkdocs serve

# Открыть http://localhost:8000
```

### Развертывание на GitHub

1. **Создать новый репозиторий на GitHub**
   ```bash
   # Через GitHub CLI (если установлен)
   gh repo create documentation-artem --public
   
   # Или вручную через веб-интерфейс GitHub
   ```

2. **Инициализировать Git и загрузить файлы**
   ```bash
   git init
   git add .
   git commit -m "docs: initial documentation setup"
   git branch -M main
   git remote add origin https://github.com/ваш-username/documentation-artem.git
   git push -u origin main
   ```

3. **Настроить GitHub Actions**
   - GitHub Actions уже настроен в `.github/workflows/`
   - При первом push документация автоматически соберется и задеплоится

4. **Активировать GitHub Pages**
   - Зайти в Settings → Pages
   - Source: Deploy from a branch
   - Branch: `gh-pages`
   - Сохранить

5. **Документация будет доступна по адресу:**
   ```
   https://ваш-username.github.io/documentation-artem/
   ```

## 📖 Структура документации

```
docs/
├── index.md                 # Главная страница
├── getting-started/         # Руководства по началу работы
├── guides/                  # Детальные гайды
├── reference/              # Справочная информация
├── tutorials/              # Пошаговые туториалы
└── assets/                 # Изображения и медиа
```

## 🤖 Интеграция с Claude AI

### Настройка Claude GitHub App

1. **Установить Claude App:**
   - Через Claude терминал: `/install-github-app`
   - Или вручную: https://github.com/apps/claude

2. **Добавить API ключ:**
   - Settings → Secrets and variables → Actions
   - Создать secret: `ANTHROPIC_API_KEY`

3. **Использование:**
   ```markdown
   # В Issue или PR комментарии:
   @claude обнови документацию по API
   @claude создай гайд по аутентификации
   @claude исправь битые ссылки
   ```

## 🛠 Доступные команды

```bash
# Локальная разработка
mkdocs serve                 # Запуск dev-сервера

# Сборка
mkdocs build                 # Сборка статического сайта

# Деплой на GitHub Pages
mkdocs gh-deploy --force     # Ручной деплой

# Проверка ссылок
find docs -name "*.md" -exec markdown-link-check {} \;
```

## 📝 Процесс контрибьюции

1. Создать ветку: `git checkout -b docs/название-изменения`
2. Внести изменения в документацию
3. Закоммитить: `git commit -m "docs: описание изменения"`
4. Отправить: `git push origin docs/название-изменения`
5. Создать Pull Request на GitHub

Подробнее в [CONTRIBUTING.md](CONTRIBUTING.md)

## 📋 Стайл-гайд

См. [STYLE_GUIDE.md](STYLE_GUIDE.md)

## 📚 Ресурсы

- [Полное руководство по Docs as Code](docs/guides/docs-as-code-complete-guide.md)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Write the Docs](https://www.writethedocs.org/)

## 📄 Лицензия

MIT License - см. [LICENSE](LICENSE)

## 👤 Автор

Artem

---

**Создано**: Ноябрь 2025  
**Версия**: 1.0
