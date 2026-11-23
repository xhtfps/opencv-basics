# OpenCV 图像处理基础

OpenCV + Python 图像处理的入门四课：图像 IO、绘图、基础处理、算术运算，每课一个可单独运行的脚本，配了示例图。

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
