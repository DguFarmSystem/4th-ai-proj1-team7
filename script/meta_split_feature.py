import os
import random

# mp4 파일들이 있는 디렉토리 경로
vevo_dir = "../dataset/vevo"

# split 폴더 경로 (없으면 생성)
split_dir = "../dataset/vevo_meta/split/v2"
os.makedirs(split_dir, exist_ok=True)

# mp4 파일 목록 가져오기
all_files = [f for f in os.listdir(vevo_dir) if f.endswith(".mp4")]
all_ids = [os.path.splitext(f)[0] for f in all_files]  # 확장자 제거

# 무작위 셔플
random.shuffle(all_ids)

# 분할 비율
total = len(all_ids)
n_train = int(total * 0.6)
n_val = int(total * 0.3)
n_test = total - n_train - n_val

# 분할
train_ids = all_ids[:n_train]
val_ids = all_ids[n_train:n_train+n_val]
test_ids = all_ids[n_train+n_val:]

# 저장
with open(os.path.join(split_dir, "train.txt"), "w") as f:
    for id in train_ids:
        f.write(id + "\n")

with open(os.path.join(split_dir, "val.txt"), "w") as f:
    for id in val_ids:
        f.write(id + "\n")

with open(os.path.join(split_dir, "test.txt"), "w") as f:
    for id in test_ids:
        f.write(id + "\n")

print(f"총 {total}개 파일 중 → train: {n_train}, val: {n_val}, test: {n_test}")
