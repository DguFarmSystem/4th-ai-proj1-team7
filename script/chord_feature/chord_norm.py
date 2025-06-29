import os
from collections import Counter
from pathlib import Path

def parse_lab_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    chords = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            start, end, chord = float(parts[0]), float(parts[1]), parts[2]
            chords.append((start, end, chord))
    return chords

def convert_to_1sec_labels(chords, duration):
    one_sec_labels = []
    for sec in range(int(duration)):
        codes_in_sec = []
        for start, end, chord in chords:
            if start < sec + 1 and end > sec:
                overlap_start = max(start, sec)
                overlap_end = min(end, sec + 1)
                overlap_duration = overlap_end - overlap_start
                if overlap_duration > 0:
                    codes_in_sec.extend([chord] * int(overlap_duration * 100))  # 가중치 반영
        if codes_in_sec:
            most_common = Counter(codes_in_sec).most_common(1)[0][0]
        else:
            most_common = "N"
        one_sec_labels.append(most_common)
    return one_sec_labels

def process_all_lab_files():
    input_dir = Path("../dataset/vevo_chord/lab_gen")
    key_dir = Path("../dataset/vevo_chord/lab_key")
    output_dir = Path("../dataset/vevo_chord/lab_gen_v2")
    output_dir.mkdir(parents=True, exist_ok=True)

    lab_files = list(input_dir.glob("*.lab"))
    for lab_file in lab_files:
        key_file = key_dir / lab_file.name
        output_file = output_dir / lab_file.name

        if not key_file.exists():
            print(f"[경고] 키 파일 없음: {key_file}")
            continue

        chords = parse_lab_file(lab_file)
        if not chords:
            print(f"[경고] 빈 코드 파일: {lab_file}")
            continue

        total_duration = max(end for _, end, _ in chords)

        with open(key_file, "r") as f:
            key = f.readline().strip()

        one_sec_labels = convert_to_1sec_labels(chords, total_duration)

        with open(output_file, "w") as f:
            f.write(f"key {key}\n")
            for i, chord in enumerate(one_sec_labels):
                f.write(f"{i} {chord}\n")

        print(f"[완료] {lab_file.name} → {output_file}")

# 실행
if __name__ == "__main__":
    process_all_lab_files()
