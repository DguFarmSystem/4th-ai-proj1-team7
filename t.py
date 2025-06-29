import IPython
from video2music import Video2music
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "2"

input_video = "../videos/video_1.mp4"

input_primer = "C G Am F"
input_key = "C major"

video2music = Video2music()
output_filename = video2music.generate(input_video, input_primer, input_key)

IPython.display.Video(output_filename)