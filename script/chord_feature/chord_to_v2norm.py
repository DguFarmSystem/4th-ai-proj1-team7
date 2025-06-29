from pathlib import Path
import re

# 반음 단위 이동용 음계 목록
NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F',
               'F#', 'G', 'G#', 'A', 'A#', 'B']
ENHARMONIC_MAP = {
    "A-": "G#", "B-": "A#", "D-": "C#", "E-": "D#", "G-": "F#",
    "C-": "B", "F-": "E",
}

def normalize_note(note):
    return ENHARMONIC_MAP.get(note, note)

def transpose_note(note, interval):
    note = normalize_note(note)
    base = re.match(r'[A-G]#?', note)
    if not base:
        return note
    root = base.group()
    idx = NOTES_SHARP.index(root)
    transposed = NOTES_SHARP[(idx + interval) % 12]
    return re.sub(root, transposed, note, count=1)

def get_transpose_interval(from_key, to_key):
    from_root = normalize_note(from_key.split()[0])
    to_root = to_key.split()[0]
    try:
        return NOTES_SHARP.index(to_root) - NOTES_SHARP.index(from_root)
    except:
        return None

def transpose_chord(chord, interval):
    m = re.match(r'^([A-G][#b-]?)(.*)', chord)
    if not m:
        return chord
    root, suffix = m.groups()
    root = normalize_note(root)
    if root not in NOTES_SHARP:
        return chord
    idx = NOTES_SHARP.index(root)
    new_root = NOTES_SHARP[(idx + interval) % 12]
    return new_root + suffix

def process_file(src_path, dst_path):
    with open(src_path, "r") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("key "):
        print(f"[건너뜀] 잘못된 형식: {src_path.name}")
        return

    key_line = lines[0].strip()
    key = key_line.replace("key ", "")
    key_mode = key.split()[1]

    if (key == "C major") or (key == "A minor"):
        dst_path.write_text("".join(lines))  # 복사만 수행
        print(f"[복사] {src_path.name} (이미 C/A)")
        return

    target_key = "C major" if key_mode == "major" else "A minor"
    interval = get_transpose_interval(key, target_key)
    if interval is None:
        print(f"[경고] 변환 실패: {src_path.name}")
        return

    transposed_lines = [f"key {target_key}\n"]
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) != 2:
            transposed_lines.append(line)
            continue
        sec, chord = parts
        transposed_chord = transpose_chord(chord, interval)
        transposed_lines.append(f"{sec} {transposed_chord}\n")

    with open(dst_path, "w") as f:
        f.writelines(transposed_lines)

    print(f"[변환 완료] {src_path.name} ({key} → {target_key})")

def main():
    src_dir = Path("../dataset/vevo_chord/lab_gen_v2")
    dst_dir = Path("../dataset/vevo_chord/lab_gen_v2_norm")
    dst_dir.mkdir(parents=True, exist_ok=True)

    for src_file in src_dir.glob("*.lab"):
        dst_file = dst_dir / src_file.name
        process_file(src_file, dst_file)

if __name__ == "__main__":
    main()
