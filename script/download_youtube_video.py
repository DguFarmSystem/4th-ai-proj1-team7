####base 환경###
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

def download_video(url, save_path, file_name):
    # 저장 경로가 없으면 생성
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 전체 파일 경로
    full_path = os.path.join(save_path, f"{file_name}.%(ext)s")

    # 비디오와 오디오 파일을 따로 저장
    command = [
        "yt-dlp", url,
        "-o", full_path,  # 확장자에 따라 저장
        #"-f", "bestvideo[height<=1080]+bestaudio/best",  # 비디오와 오디오를 각각 다운로드
        "-f", "bestvideo[ext=webm]+bestaudio[ext=webm]/best",  # 비디오와 오디오를 webm 형식으로 다운로드
        #"--keep-video",  # 병합하지 않고 각각 따로 저장
        "--recode-video", "mp4"
    ]

    # yt-dlp 실행
    subprocess.run(command)

def download_videos_multithread(link_list, save_path, max_workers=4):
    # 멀티스레드 풀 생성
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 각 링크를 병렬로 처리
        futures = []
        for i, url in enumerate(link_list):
            file_name = f"video_{i+1}"  # 각 파일에 순차적으로 이름 지정
            futures.append(executor.submit(download_video, url, save_path, file_name))

        # 모든 다운로드가 완료될 때까지 기다림
        for future in futures:
            future.result()  # 결과를 기다림 (예외 발생 시 처리)

# 유튜브 링크 리스트
link_list = [
]

# 저장 경로 지정
save_path = "./videos"

# 함수 호출
download_videos_multithread(link_list, save_path, max_workers=4)