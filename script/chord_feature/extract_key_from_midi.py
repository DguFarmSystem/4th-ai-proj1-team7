import os
from music21 import converter, key

# 입력 및 출력 디렉토리
midi_dir = '../dataset/vevo_chord/lab_gen_midi'
key_dir = '../dataset/vevo_chord/lab_key'
os.makedirs(key_dir, exist_ok=True)

def extract_key_music21(midi_path):
    try:
        score = converter.parse(midi_path)
        k = score.analyze('key')
        return f"{k.tonic.name} {k.mode}"  # 예: "C major", "A minor"
    except Exception as e:
        print(f"⚠️ Error analyzing {midi_path}: {e}")
        return "Error"

for filename in os.listdir(midi_dir):
    if filename.endswith(".midi"):
        midi_path = os.path.join(midi_dir, filename)
        key_name = extract_key_music21(midi_path)

        base_name = os.path.splitext(filename)[0]
        key_file_path = os.path.join(key_dir, f"{base_name}.lab")
        with open(key_file_path, 'w') as f:
            f.write(f"{key_name}\n")

        print(f"✅ {filename} → {key_name}")
