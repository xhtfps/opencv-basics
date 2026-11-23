<div align="center">

# OpenCV 图像处理基础

**四节课，四个能单独跑的脚本：IO、绘图、基础处理、算术运算**

![language](https://img.shields.io/badge/language-Python-3776ab?style=flat-square)
![stack](https://img.shields.io/badge/stack-OpenCV%204.x-5c3ee8?style=flat-square)
![license](https://img.shields.io/badge/license-see%20LICENSE-lightgrey?style=flat-square)
![last commit](https://img.shields.io/github/last-commit/xhtfps/opencv-basics?style=flat-square)

[快速开始](#3-快速开始与关键实现) · [常见问题](#4-常见问题) · [全部仓库索引](https://github.com/xhtfps/xhtfps)

</div>

## 入门要避开的四个坑

BGR/RGB 混用、`imshow` 不配 `waitKey`、中文路径读不出图、`cv2.add` 和 `numpy` 加法不是一回事——这四个坑几乎人人踩一遍。这里每节课对着一个坑设计，跑完就知道差别在哪。

## 亮点

- **每课一个独立脚本**：不用改路径、不用配工程，`python 01_图像IO操作.py` 直接看结果。
- **示例图随仓带**：`image/` 下的小图就是脚本用的那几张，跑起来不会找不到文件。
- **差异写进注释**：饱和截断 vs 模 256 溢出这类易混点，正文直接给对比方法。
- **只交付有价值的东西**：中间图、视频、IDE 目录都不入库。

## 结构

```mermaid
flowchart LR
  IO["01 图像 IO<br/>读写·色彩空间"] --> DRAW["02 绘图<br/>线·框·圆·文字"]
  DRAW --> PROC["03 基础处理<br/>阈值·滤波·边缘·形态学"]
  PROC --> MATH["04 算术运算<br/>加减·位运算·混合"]
```

## 1. 目录一览

| 文件 | 内容 |
| --- | --- |
| `01_图像IO操作.py` | 读写、显示、色彩空间转换 |
| `02_图像绘制图形.py` | 线/矩形/圆/多边形、文字 |
| `03_图像基础处理.py` | 阈值、滤波、边缘、形态学 |
| `04_图像的算术运算.py` | 加减乘、与或非、混合、位运算 |
| `image/` | 各脚本用到的示例图 |

## 2. 环境

| 项 | 要求 |
| --- | --- |
| Python | 3.9+（建议 conda 虚拟环境） |
| 依赖 | `pip install opencv-python numpy matplotlib` |
| 显示 | 本地桌面环境（`cv2.imshow` 在无头环境下不可用） |
| 中文路径 | Windows 下图片路径含中文时用 `cv2.imdecode` 读取 |

## 3. 快速开始与关键实现

```powershell
pip install opencv-python numpy matplotlib
python .\01_图像IO操作.py
```

关键点：

1. OpenCV 默认通道顺序是 **BGR**，matplotlib 是 RGB，混用会变“阿几色”。
2. `cv2.imshow` 后必须 `cv2.waitKey(0)`，否则窗口一闪而过。
3. 加法分 `cv2.add`（饱和截断）与 `numpy` 直接相加（模 256 溢出），对比时能看到明显差异。
4. 形态学操作记得先二值化，否者灰度图上效果很奇怪。

## 4. 常见问题

- **`cv2` 找不到**：装的是 `opencv-python-headless`（无 GUI），换装 `opencv-python`。
- **中文路径 `imread` 返回 None**：用 `cv2.imdecode(np.fromfile(path, np.uint8), cv2.IMREAD_COLOR)`。
- **图片全黑**：路径相对当前工作目录，先 `cd` 到脚本所在目录再跑。
- **颜色异常**：BGR/RGB 混用，显示前 `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`。

## 5. 维护说明

- 只交 `*.py` 与 `image/` 下的小图；跑出来的中间图、视频、`.vscode/` 不入库，见 [`EXCLUDED_FILES.md`](EXCLUDED_FILES.md)。
- 示例图部分来自开源素材，版权归原作者，仅作学习使用。
## 路线图

- [x] 四课脚本与示例图入库，均可独立运行
- [x] 中间产物与 IDE 目录清理
- [ ] 补一节「中文路径与无头环境」的最小可行写法
- [ ] 加一个把四课串起来的综合小作业

## 参与与反馈

- 遇到问题请走 [Issue 模板](.github/ISSUE_TEMPLATE)，附上脚本名与完整报错。
- 提 PR 前先读 [CONTRIBUTING.md](CONTRIBUTING.md)；安全问题按 [SECURITY.md](SECURITY.md) 私下反馈。
- 如果这个仓库帮你省过时间，点个 ⭐ 是最省事的支持。

## 许可证

本仓脚本见 [LICENSE](LICENSE)；示例图部分来自开源素材，版权归原作者。
