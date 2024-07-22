# GIF分割并拼接成图片
## 目的
将一个GIF图片均匀分割，可以指定分割的帧数，最后将帧拼接起来，可用于论文或者项目报告中！

## 环境配置

```
conda create -n gif_split python=3.8
pip install pillow
```

## 运行
自定义修改gif_split.py中的参数：

gif_path：将要提取帧的源文件名称

output_path：输出拼接的图片名称

num_frames：要均匀提取gif图片的帧数

interval：帧之间的间隔（像素）

```
python gif_split.py
```