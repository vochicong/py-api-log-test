# PythonでAPI作成、ログとテスト

PythonでAPIを作成する際の、雛形プロジェクトです。

パッケージ管理は `poetry` を使います。

主な道具

* `fastapi`
* `loguru`
* `pytest`

## ログ

`from loguru import logger` ですぐに使いやすい `logger` が出来上がります。
`lib.util.set_logger` で少し手を加えています。

* `DEBUG_LOG_FILE` ("/var/log/app_debug.log") に `DEBUG` レベルのログを記録
* 標準エラー出力 `stderr` には、 `LOG_LEVEL` 環境変数で定義するレベル( `INFO` など)のログを出力

## テスト

`lib.util.ApiClient` は、
APIの `get` , `post` をテストするために、
`BASE_URL` 環境変数が `http://localhost` などとして定義されているかによって、
 `requests`
と
 `fastapi.testclient.TestClient`
を使い分けます。
