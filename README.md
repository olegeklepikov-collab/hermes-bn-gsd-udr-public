# Hermes BN · GSD and UDR

Обезличенный комплект для самостоятельной нативной установки на **macOS Apple Silicon**. Публичный репозиторий и установочные материалы доступны без аккаунта GitHub и без пароля.

**[Полная инструкция установки на новый Mac](INSTALL-macOS-Apple-Silicon.md)**

Нужны **оба слоя** из [recovery-set.json](recovery-set.json): очищенная основа и обновление r2, всего 18 721 636 694 байта загрузки. Файловое дерево содержит исходники и документацию; полные исполняемые среды находятся в [материалах выпуска](https://github.com/olegeklepikov-collab/hermes-bn-gsd-udr-public/releases/tag/public-2026-10-17-gsd-udr-r2). Один git clone не является полной установкой.

```sh
python3 restore.py --download --parts-dir ../hermes-parts --output-dir ../hermes-archives
```

Команда проверяет размеры и SHA-256 всех частей и обоих архивов; службы не запускает. Исследовательские аккаунты, ключи, история, материалы и полномочия прежнего владельца отсутствуют. Для модели, эмбеддингов и внешних источников используются собственные доступы.

[Версии](deployment-template/CURRENT-VERSIONS.json) · [Подготовка](deployment-template/CURRENT-SETUP.md) · [Приёмка и ограничения](deployment-template/ACCEPTANCE.md) · [Состав публичной копии](PUBLICATION-NOTE.md).
