from PIL import Image, ImageSequence

def extract_frames_at_intervals(gif_path, num_frames):
    """
    从GIF文件中提取均匀间隔的帧。
    
    :param gif_path: GIF文件的路径
    :param num_frames: 要提取的帧数
    :return: 帧列表
    """
    gif = Image.open(gif_path)
    total_frames = gif.n_frames
    interval = total_frames // num_frames
    frame_indices = [i * interval for i in range(num_frames)]
    
    # 添加最后一帧到图像上
    frame_indices.append(total_frames - 1) 
    frames = [frame.copy() for i, frame in enumerate(ImageSequence.Iterator(gif)) if i in frame_indices]
    return frames

def concatenate_frames(frames, interval):
    """
    将帧按照固定间隔拼接在一起。
    
    :param frames: 帧列表
    :param interval: 帧之间的间隔（像素）
    :return: 拼接后的图像
    """
    # 获取每一帧的宽度和高度
    width, height = frames[0].size
    
    # 计算拼接后图像的宽度和高度
    total_width = width * len(frames) + interval * (len(frames) - 1)
    total_height = height
    
    # 创建一个新的空白图像
    new_image = Image.new("RGBA", (total_width, total_height))
    
    # 将每一帧粘贴到新图像上
    x_offset = 0
    for frame in frames:
        new_image.paste(frame, (x_offset, 0))
        x_offset += width + interval
    
    return new_image

def main():
    gif_path = 'test.gif'  # 替换为你的GIF文件路径
    output_path = 'output.png'         # 输出文件路径
    num_frames = 10                     # 要提取的帧数
    interval = 10                      # 帧之间的间隔（像素）
    
    frames = extract_frames_at_intervals(gif_path, num_frames-1)
    concatenated_image = concatenate_frames(frames, interval)
    concatenated_image.save(output_path)
    print("Done")

if __name__ == "__main__":
    main()
