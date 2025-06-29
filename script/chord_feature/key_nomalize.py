import os

# "-" 표기 기반의 flat → sharp 변환 매핑
flat_to_sharp_map = {
    "C-": "B",  "D-": "C#", "E-": "D#", "F-": "E",
    "G-": "F#", "A-": "G#", "B-": "A#"
}

def convert_dash_key_to_sharp(key_str):
    try:
        parts = key_str.strip().split()
        if len(parts) != 2:
            return key_str  # 예: "Unknown", "Error" 등은 그대로 유지

        tonic, mode = parts
        if tonic in flat_to_sharp_map:
            tonic = flat_to_sharp_map[tonic]
        return f"{tonic} {mode}"
    except:
        return key_str

# key 파일 경로
key_dir = '../dataset/vevo_chord/lab_key'

# 처리
for filename in os.listdir(key_dir):
    if filename.endswith('.lab'):
        file_path = os.path.join(key_dir, filename)
        with open(file_path, 'r') as f:
            key_line = f.readline().strip()

        new_key_line = convert_dash_key_to_sharp(key_line)

        with open(file_path, 'w') as f:
            f.write(new_key_line + '\n')

        print(f"{filename}: {key_line} → {new_key_line}")
