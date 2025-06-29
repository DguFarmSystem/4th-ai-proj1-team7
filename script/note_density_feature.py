import os
import math
import pretty_midi

def main():
    directory_vevo_chord = "../dataset/vevo_chord/lab_gen_v2_norm/"
    directory_vevo_midi = "../dataset/vevo_midi/all/"
    output_dir = "../dataset/vevo_note_density/all_2/"
    os.makedirs(output_dir, exist_ok=True)  # <-- 🔧 디렉토리 자동 생성

    for filename in sorted(os.listdir(directory_vevo_chord)):
        chord_filepath = os.path.join(directory_vevo_chord, filename)
        print(chord_filepath)
        ct = 0
        with open(chord_filepath, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                line_arr = line.split(" ")
                if len(line_arr) > 1:
                    ct += 1

        fname = filename.split(".")[0]
        midipath = os.path.join(directory_vevo_midi, filename.replace("lab", "mid"))

        midi_data = pretty_midi.PrettyMIDI(midipath)
        total_time = midi_data.get_end_time()

        note_density_list = []
        for i in range(int(total_time) + 1):
            start_time = i
            end_time = i + 1
            total_notes = 0
            for instrument in midi_data.instruments:
                for note in instrument.notes:
                    if note.start < end_time and note.end > start_time:
                        total_notes += 1
            note_density = total_notes / float(end_time - start_time)
            note_density_list.append(note_density)

        fpathname = os.path.join(output_dir, fname + ".lab")
        with open(fpathname, 'w', encoding='utf-8') as f:
            for i in range(0, ct - 1):
                if i < len(note_density_list):
                    f.write(f"{i} {note_density_list[i]}\n")
                else:
                    f.write(f"{i} 0\n")

if __name__ == "__main__":
    main()
