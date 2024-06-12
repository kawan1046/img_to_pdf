from PIL import Image
import os

def image_to_pdf(image_path):
    # ファイルパスの前後の余分なクオートを削除（ドラッグアンドドロップ時に追加されることがある）
    image_path = image_path.strip('"')

    # 画像ファイルを開く
    image = Image.open(image_path)
    image = image.convert('RGB')  # PDF保存のためRGBに変換

    # PDFファイル名を決定（元の画像ファイル名に基づく）
    pdf_filename = os.path.splitext(image_path)[0] + '.pdf'

    # PDFとして保存
    image.save(pdf_filename)
    print(f"PDFファイルが作成されました: {pdf_filename}")

if __name__ == "__main__":
    print("画像ファイルをこのウィンドウにドラッグアンドドロップしてください。")
    image_path = input("ここにファイルパスをドロップ: ")
    image_to_pdf(image_path)
