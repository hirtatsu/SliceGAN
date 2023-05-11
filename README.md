# SliceGAN 

以下の論文に使用されているSliceGANのコードです。二次元画像を教師データとして、GAN（敵対的生成ネットワーク）を用いて三次元構造を予測する。
[Kench, S., Cooper, S.J. Generating three-dimensional structures from a two-dimensional slice with generative adversarial network-based dimensionality expansion. Nat Mach Intell 3, 299–305 (2021).](https://www.nature.com/articles/s42256-021-00322-1)


### 準備
- Python3環境が構築していることが前提です。
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

### Development

If you are interested in trying new architectures, see the networks.py file

To adjust the training parameters or algorithm, see train.py

To add a new preprocessing method e.g for a different training datatype, see preproccessing.py.

### Results

![](images/SliceGAN_results.png)

### Versions

v1.1 release: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4399114.svg)](https://doi.org/10.5281/zenodo.4399114)

v1.0 release: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4319988.svg)](https://doi.org/10.5281/zenodo.4319988)

