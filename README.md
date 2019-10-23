# selenium

## 概要

Selenium の環境構築が面倒だったため、Docker 上で開発環境を再現できるように設定ファイルとサンプルスクリプトをまとめました。
`docker-compose up -d`するだけで Selenium と Python および Headless Chrome の環境が出来上がります。ブラウザを用いた処理を自動化したい場合や、テスト自動化のベースとしてご利用ください。Headless なので GUI 環境のないサーバー上でも動作します。

## 事前準備

Docker をインストールして、docker コマンドと docker-compose コマンドが使用できるようにしてください。

## 使い方

### インストールと起動方法

```bash
$ git clone https://github.com/sikkimtemi/selenium
$ cd selenium
$ docker-compose up -d
```

正常に起動できていれば下記のようになります。

```bash
$ docker-compose ps
    Name               Command           State           Ports
-----------------------------------------------------------------------
chrome         /opt/bin/entry_point.sh   Up      0.0.0.0:5900->5900/tcp
python         tail -f /dev/null         Up
selenium-hub   /opt/bin/entry_point.sh   Up      0.0.0.0:4444->4444/tcp
```

### 終了方法

```bash
$ docker-compose down
```

### サンプルスクリプトの実行

```bash
$ docker exec -it python /root/script/sample.py
```

実行すると Google にアクセスしてスクリーンショットを取得します。
script/images ディレクトリに画像ファイルが保存されます。

### VNC 接続によるデバッグ

`VNC`で接続するとブラウザの動きを確認しながらデバッグすることができます。Docker 環境の IP アドレスに VNC(デフォルトは 5900 番ポート)でアクセスした上で、サンプルスクリプトを実行してみてください。デフォルトのパスワードは"secret"です。

### Uni○s ログイン情報設定

```bash
docker-compose exec python bash
export LOGIN_ID=xxxxxxx
export LOGIN_PASSWORD=xxxxxxxxx
```
