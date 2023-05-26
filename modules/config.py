import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='プログラムの説明')
    parser.add_argument('--image_model_name', type=str, default="microsoft/swinv2-base-patch4-window8-256", help='画像の特徴抽出モデル')
    parser.add_argument('--language_model_name', type=str, default="t5-large", help='言語の特徴抽出モデル')
    parser.add_argument('--transformer_model_name', type=str, default="t5-large", help='メインのモデル')
    parser.add_argument('--lr', type=float, default=0.001, help='学習率')
    parser.add_argument('--data_dir', type=str, default='/data/dataset/v-coco/coco/', help='データのディレクトリ')
    parser.add_argument('--batch_size', type=int, default=128, help='1GPUあたりのバッチサイズ')
    parser.add_argument('--num_epochs', type=int, default=100, help='エポック数')
    parser.add_argument('--max_source_length', type=int, default=256)
    parser.add_argument('--max_target_length', type=int, default=128)
    parser.add_argument('--result_dir', type=str, default='results', help='結果を保存するディレクトリ')
    args = parser.parse_args()
    return args