import subprocess
import re
import os
import ctypes

import winsound
import time

#### Config start ####

# Set Filename to Process | disabled to use "prompt ask for name"
# filename_with_extension = "P-KisaDanceByFire2.mp4"

# prompt ask for name
user_input_filename = input("Insert local video name, include extension .mp4: ")
filename_with_extension = user_input_filename

# Set the desired frames per second (FPS)
fps = 10  # Adjust the value as needed

# Set the desired colors to be used
colors = 256  # Adjust the colors

# Set the desired resizing dimensions (width, height) -1 means maintain ratio
# 320 portrait
# 640 landscape
resize = "320:-1"  # Adjust the values as needed

#### Config end ####

# Update the window title
ctypes.windll.kernel32.SetConsoleTitleW(f"Converting {filename_with_extension} to GIF")

working_video_dir = r"C:\\mp4-to-gif"

input_video_path = rf"{working_video_dir}\\{filename_with_extension}"

# Get the filename from the input video path
video_filename = os.path.basename(input_video_path)
video_filename_without_extension = os.path.splitext(video_filename)[0]

# Run FFmpeg command to get video duration
ffmpeg_command = f'ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{input_video_path}"'

# Get video duration
output = subprocess.check_output(ffmpeg_command, shell=True).decode("utf-8").strip()

# Convert the duration from float to int
duration_seconds = int(float(output))

# Set the desired GIF duration from video source (in seconds)
gif_duration = duration_seconds  # 18

print(video_filename_without_extension)

# Include fps and colors in the output filename
output_gif_path = rf"{working_video_dir}\{video_filename_without_extension}_{fps}fps_{colors}colors.gif"

# Use FFmpeg command to convert the video to GIF with resizing, FPS control, and quality adjustment
ffmpeg_command = f'ffmpeg -i "{input_video_path}" -t {gif_duration} -vf "scale={resize},split[s0][s1];[s0]format=pix_fmts=rgb24,scale=in_color_matrix=bt709:out_color_matrix=bt709[s2];[s2]palettegen=max_colors={colors}[p];[s1][p]paletteuse" -r {fps} "{output_gif_path}"'

# ffmpeg_command = f'ffmpeg -i "{input_video_path}" -t {gif_duration} -vf "scale={resize},split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse" -r {fps} "{output_gif_path}"'
# ffmpeg_command = f'ffmpeg -i "{input_video_path}" -t {gif_duration} -vf "scale={resize},split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -r {fps} -q:v {quality} "{output_gif_path}"'
# ffmpeg_command = f'ffmpeg -i "{input_video_path}" -t {gif_duration} -vf "scale={resize}" -r {fps} -q:v {quality} "{output_gif_path}"'

# Run the FFmpeg command
subprocess.call(ffmpeg_command, shell=True)

# Play the default system sound (beep)
# print("playing ding sound")
winsound.Beep(440, 500)  # Frequency of 440 Hz for 500 milliseconds

# Add a 1-second delay
time.sleep(1)

# Update the window title once the conversion is complete
ctypes.windll.kernel32.SetConsoleTitleW("Conversion complete!")


'''
import subprocess

input_video_path = r"C:\mp4-to-gif\KisaOllieLandscape.mp4"
output_gif_path = r"C:\mp4-to-gif\KisaOllieLandscape.gif"

# Set the desired GIF duration (in seconds)
gif_duration = 18

# Set the desired resizing dimensions (width, height)
resize = "640:-1"  # Adjust the values as needed

# Set the desired frames per second (FPS)
fps = 15  # Adjust the value as needed

# Use FFmpeg command to convert the video to GIF with resizing and FPS control
ffmpeg_command = f'ffmpeg -i "{input_video_path}" -t {gif_duration} -vf "scale={resize}" -r {fps} "{output_gif_path}"'

# Run the FFmpeg command
subprocess.call(ffmpeg_command, shell=True)
'''
