import os
from moviepy.editor import VideoFileClip

def video_to_audio_folder(input_folder, output_folder, allowed_extensions):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # this code loops through each file in the input folder
        for filename in os.listdir(input_folder):
            if any(filename.endswith(ext) for ext in allowed_extensions):
                video_path = os.path.join(input_folder, filename)
                audio_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp3")  # Output audio file path
                video_clip = VideoFileClip(video_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(audio_path)
                video_clip.close()
        print("All videos converted to audio successfully!")
    except Exception as e:
        print("Error:", e)

# file path:
input_folder = "E:/AMV songs"
output_folder = "E:/amv songs mp4"
allowed_extensions = [".mp4", ".avi", ".mov"] #these are the video file extensions supported for this code

video_to_audio_folder(input_folder, output_folder, allowed_extensions)