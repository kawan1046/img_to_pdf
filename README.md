# Image to PDF Converter

このツールは、画像ファイルをPDFに変換するPythonスクリプトです。ユーザーは画像ファイルをコマンドラインウィンドウにドラッグアンドドロップすることで、簡単にPDFに変換できます。

## 特徴

- ドラッグアンドドロップで簡単に画像ファイルを指定できます。
- 変換されたPDFは、元の画像ファイル名を基に命名されます。

## 前提条件

このスクリプトを実行する前に、以下のソフトウェアがシステムにインストールされている必要があります：

- Python 3.6以上
- Pillowライブラリ

## インストール方法

### 1. Pythonのインストール

Pythonは[公式サイト](https://www.python.org/downloads/)からダウンロードしてインストールできます。

### 2. Pillowのインストール

Pillowライブラリは以下のコマンドを使用してインストールできます：

```bash
pip install pillow
```


## 使用方法

1. スクリプトをダウンロード後、任意のディレクトリに保存します。
2. コマンドプロンプトを開き、スクリプトが保存されているディレクトリに移動します。
3. スクリプトを実行するには以下のコマンドを入力します。

```python
python image_to_pdf.py
```


4. 表示されるメッセージに従って、変換したいPDFファイルをウィンドウにドラッグアンドドロップします。
5. 処理が完了すると、画像ファイルと同じディレクトリにPDFファイルが作成されます。

## ライセンス

このプロジェクトは[MITライセンス](https://opensource.org/licenses/MIT)のもとで公開されています。



## 貢献

プルリクエストはいつでも歓迎します。大きな変更を提案する場合は、まずissueを開いて議論してください。

