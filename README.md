# SliceGAN 

以下の論文に使用されているSliceGANのコードです。二次元画像を教師データとして、GAN（敵対的生成ネットワーク）を用いて三次元構造を予測する。
[Kench, S., Cooper, S.J. Generating three-dimensional structures from a two-dimensional slice with generative adversarial network-based dimensionality expansion. Nat Mach Intell 3, 299–305 (2021).](https://www.nature.com/articles/s42256-021-00322-1)


### 準備
- Python3環境が構築されていることが前提です。
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
- 例の.tifファイルを生成して保存するには
```
python run_slicegan 0
```

### 開発

- 新しいアーキテクチャを試すことに興味がある方は、networks.pyファイルをご覧ください。
- 学習パラメータやアルゴリズムを調整する場合は、train.pyを参照してください。
- 新しい前処理方法（例えば、異なるトレーニングデータ型用）を追加するには、preproccessing.pyを参照してください。

### 結果例

![](images/SliceGAN_results.png)

