# mp3_spliter


# 1. 从youbube上下载音乐视频，MP4格式
推荐：

https://github.com/ErikZhou/YouPy

# 2. MP4格式转MP3格式 (支持mkv格式）

print('python mp4-to-mp3.py filename')


# 3. 利用ffmpeg分割MP3文件（Mac系统），根据静音间隔来分割歌曲


print('eg. python asplit.py 1_1.mp3 3 0.1')


输出结果：（文件1_1.mp3-out.sh）

ffmpeg -i 1_1.mp3 -ss 0 -to 349.5 -c copy -y 1_p01.mp3 &

ffmpeg -i 1_1.mp3 -ss 349.5 -to 685.5 -c copy -y 1_p02.mp3 &

ffmpeg -i 1_1.mp3 -ss 685.5 -to 934.5 -c copy -y 1_p03.mp3 &

ffmpeg -i 1_1.mp3 -ss 934.5 -to 1174.5 -c copy -y 1_p04.mp3 &

ffmpeg -i 1_1.mp3 -ss 1174.5 -to 1441.5 -c copy -y 1_p05.mp3 &

ffmpeg -i 1_1.mp3 -ss 1441.5 -to 1657.5 -c copy -y 1_p06.mp3 &

ffmpeg -i 1_1.mp3 -ss 1657.5 -to 1921.5 -c copy -y 1_p07.mp3 &

ffmpeg -i 1_1.mp3 -ss 1921.5 -to 2665.5 -c copy -y 1_p08.mp3 &

ffmpeg -i 1_1.mp3 -ss 2665.5 -to 2926.5 -c copy -y 1_p09.mp3 &

ffmpeg -i 1_1.mp3 -ss 2926.5 -to 3346.5 -c copy -y 1_p10.mp3 &

ffmpeg -i 1_1.mp3 -ss 3346.5 -to 3601.5 -c copy -y 1_p11.mp3 &

ffmpeg -i 1_1.mp3 -ss 3601.5 -to 3877.5 -c copy -y 1_p12.mp3 &

ffmpeg -i 1_1.mp3 -ss 3877.5 -to 4144.5 -c copy -y 1_p13.mp3 &

# 4. 从大MP3文件抽取单个MP3格式的歌曲
运行1_1.mp3-out.sh文件，最终结果如下：
1_p01.mp3
1_p02.mp3
1_p03.mp3
...
1_p12.mp3

# 5. 完整工作流启动代码
输入：同级目录下MP4文件列表

输出：分割好的MP3文件

python run.py

https://www.jianshu.com/p/e13a8efe4501
