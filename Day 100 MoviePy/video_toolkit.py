from moviepy import VideoFileClip
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def video_information(video):
    print("\nVIDEO INFORMATION")
    print("-" * 35)
    print(f"Duration : {video.duration:.2f} seconds")
    print(f"Resolution : {video.w} x {video.h}")
    print(f"FPS : {video.fps}")


def extract_audio(video):
    if video.audio:
        audio_path = os.path.join(OUTPUT_DIR, "extracted_audio.mp3")
        video.audio.write_audiofile(audio_path)
        print("✅ Audio extracted successfully!")
    else:
        print("❌ This video has no audio.")


def create_thumbnail(video):
    thumbnail_path = os.path.join(OUTPUT_DIR, "thumbnail.png")
    video.save_frame(thumbnail_path, t=1)
    print("✅ Thumbnail created!")


def trim_video(video):
    end_time = min(10, video.duration)
    trimmed = video.subclipped(0, end_time)

    output = os.path.join(OUTPUT_DIR, "trimmed_video.mp4")
    trimmed.write_videofile(output, codec="libx264")

    print("✅ Trimmed video saved!")


def main():

    print("=" * 50)
    print("        VIDEO TOOLKIT")
    print("=" * 50)

    path = input("\nEnter video path: ").strip()

    if not os.path.exists(path):
        print("❌ File not found.")
        return

    video = VideoFileClip(path)

    video_information(video)
    create_thumbnail(video)
    extract_audio(video)
    trim_video(video)

    video.close()

    print("\n🎉 All tasks completed successfully!")


if __name__ == "__main__":
    main()