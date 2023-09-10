# FastAPI と Strawberry を Docker で動かすための環境を用意してみる
## 起動方法
- $ docker compose build --no-cache
- $ docker compose up

## テスト
- $ task test
    - テストの前に、autoflake, black, isort, pyupgrade によるフォーマット、mypy による型チェックを実施します。

## モジュール追加
docker compose run --entrypoint "poetry add hoge" demo-app
