import os
import subprocess
from pathlib import Path
import shutil

# 현재 디렉토리
cwd = Path.cwd()

# MIDI 파일 저장할 폴더 생성
output_dir = cwd / "vevo_midi"
output_dir.mkdir(exist_ok=True)

# 현재 폴더 내 모든 .wav 파일 반복
for wav_file in cwd.glob("*.wav"):
    print(f"변환 중: {wav_file.name}")
    
    # 예상되는 mid 파일명 (.wav → .mid)
    mid_file = wav_file.with_suffix(".mid")

    # 변환 실행
    subprocess.run([
        "omnizart", "music", "transcribe", str(wav_file)
    ])

    # 생성된 mid 파일을 vevo_midi 폴더로 이동
    if mid_file.exists():
        shutil.move(str(mid_file), output_dir / mid_file.name)
        print(f"→ 저장 완료: {output_dir / mid_file.name}")
    else:
        print(f"⚠️ 변환 실패 또는 파일 없음: {mid_file.name}")
