# fastAPI 勉強用サンプル

FastAPI 勉強用のサンプルプロジェクトです。

## 使い方

codespace を使う人
github から create codespace をおしてください

visual studio code を使う人
Dev Containers（拡張機能）入れた後に画面左下の矢印が向かい合っているマークを押し、コンテナで再度開くを押してください。

ターミナルに <br />
uvicorn main:app --host 0.0.0.0 --port 8000 --reload <br />
とうってください
![](./images/explanation1.png)

chrome などで URL に localhost:8000 と入力してください(codespace を用いていない人) <br />
codespace を使っている人は下の画像の赤線で囲んだ URL を ctr キーを押しながらクリックしてください。<br />
![](./images/explanation3.png)
次のような画面が出てきたら成功です！ <br />
![](./images/explanation2.png)

以下の URL で各種機能を見れます(codespace を用いていない人) <br />
自作 API のドキュメント: localhost:8000/docs <br />
PhpMyAdmin: localhost:80 <br />
