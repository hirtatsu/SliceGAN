# SliceGAN 

以下の論文に使用されているSliceGANのコードです。二次元画像を教師データとして、GAN（敵対的生成ネットワーク）を用いて三次元構造を予測する。
[Kench, S., Cooper, S.J. Generating three-dimensional structures from a two-dimensional slice with generative adversarial network-based dimensionality expansion. Nat Mach Intell 3, 299–305 (2021).](https://www.nature.com/articles/s42256-021-00322-1)


### 準備
- Python3環境が構築していることが前提です。
- run_sliceganを開き、必要に応じて情報を編集します。特にプロジェクト名SliceGANは、等方性微細構造の単一の2Dトレーニング画像、または異方性微細構造の直角に撮影された3つの2D画像を必要とします。画像は、カラー、グレースケール、n相のいずれでも構いません。

To use SliceGAN open run_slicegan and edit information as requested. SliceGAN requires a single 2D training image of an isotropic microstructure, or three 2D images taken at perpendicular angles of an anisotropic microstructure. Images can be colour, grayscale or n-phase.

Use 'python run_slicegan 1' to train a new generator or 'python run_slicegan 0' to generate and save an example .tif file

### Development

If you are interested in trying new architectures, see the networks.py file

To adjust the training parameters or algorithm, see train.py

To add a new preprocessing method e.g for a different training datatype, see preproccessing.py.

### Results

![](images/SliceGAN_results.png)

### Versions

v1.1 release: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4399114.svg)](https://doi.org/10.5281/zenodo.4399114)

v1.0 release: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4319988.svg)](https://doi.org/10.5281/zenodo.4319988)

