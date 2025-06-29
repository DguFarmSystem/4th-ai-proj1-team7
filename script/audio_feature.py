import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_wav_path):
    try:
        clip = VideoFileClip(video_path)
        if clip.audio is None:
            print(f"[경고] 오디오가 없는 파일입니다: {video_path}")
            return
        clip.audio.write_audiofile(output_wav_path, codec='pcm_s16le')  # WAV 저장
        print(f"[완료] 추출됨: {output_wav_path}")
    except Exception as e:
        print(f"[에러] {video_path} 처리 중 오류 발생: {e}")

def main():
    input_dir = "../dataset/vevo"
    output_dir = "../dataset/vevo_audio/wav"

    os.makedirs(output_dir, exist_ok=True)

    for filename in sorted(os.listdir(input_dir)):
        if not filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            continue  # 비디오 파일이 아니면 건너뜀

        video_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_wav_path = os.path.join(output_dir, f"{base_name}.wav")

        extract_audio_from_video(video_path, output_wav_path)

if __name__ == "__main__":
    main()
