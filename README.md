# SliceGAN 

以下の論文に使用されているSliceGANのコードです。二次元画像を教師データとして、GAN（敵対的生成ネットワーク）を用いて三次元構造を予測する。
[Kench, S., Cooper, S.J. Generating three-dimensional structures from a two-dimensional slice with generative adversarial network-based dimensionality expansion. Nat Mach Intell 3, 299–305 (2021).](https://www.nature.com/articles/s42256-021-00322-1)


さらに、K. Sugiuraらにより解像度が向上する改良版が示されている。
[Sugiura K, Ogawa T, Adachi Y, Sun F, Suzuki A, Yamanaka A, Nakada N, Ishimoto T, Nakano T, Koizumi Y. Big-Volume SliceGAN for Improving a Synthetic 3D Microstructure Image of Additive-Manufactured TYPE 316L Steel. Journal of Imaging. 2023; 9(5):90. https://doi.org/10.3390/jimaging9050090](https://doi.org/10.3390/jimaging9050090)
- run_slicegan_128model.py



### 準備
- Python3環境が構築されていること。
- nvidia cuda toolkitとCUDA Deep Neural Network (cuDNN)がインストール済みであること。確認は以下。
```
nvidia-smi
nvcc -V

python3
>> import torch
>> torch.cuda.is_available()
TRUE
```
- Githubからローカルにクローンを持ってくる
```
git clone https://github.com/hirtatsu/SliceGAN.git
```
- SliceGANは、等方性微細構造の単一の2Dトレーニング画像、または異方性微細構造の直角に撮影された3つの2D画像を必要とします。画像は、カラー、グレースケール、n相のいずれでも構いません。
- run_sliceganを開き、必要に応じて情報を編集します。
  - プロジェクト名：
  ```
  Project_name = 'XXXXXXXXX'
  ```
  - 教師データのタイプ (colour, grayscale, three-phase or two-phase. n-phase materials must be segmented)
  ```
  image_type = 'nphase'
  ```
  - 教師データの相の数
  ```
  img_channels = 3
  ```
  - 教師データのデータタイプ(for colour/grayscale images, must be 'colour' / 'greyscale'. nphase can be, 'tif2D', 'png', 'jpg', tif3D, 'array')
  ```
  data_type = 'tif3D'
  ```
    - 教師データのディレクトリとファイル名：
  ```
  data_path = ['XXXXXXXXX/YYYYYY.tif']
  ```
- 新しいジェネレーターをトレーニングするには
```
python run_slicegan 1
```
- トレーニング後に画像を表示するには
```
python run_slicegan 0
```

### 開発

- 新しいアーキテクチャを試す場合は、networks.pyファイルを確認する。
- 学習パラメータやアルゴリズムを調整する場合は、train.pyを確認する。
- 新しい前処理方法（例えば、異なるトレーニングデータ型用）を追加する場合は、preproccessing.pyを確認する。

