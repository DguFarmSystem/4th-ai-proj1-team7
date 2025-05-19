# 🎵 Affective Multimodal Transformer model 기반 숏츠 배경음악 생성

## 📌 프로젝트 개요  
영상의 영상 및 음성 정보를 분석하여 분위기를 파악하고, 이에 어울리는 음악을 추천하거나 직접 생성하는 AI 시스템을 개발하는 프로젝트입니다.

## 👨‍💻 팀원 (Members)  

| 이름 | 학과 |
| --- | --- |
| 이제혁 | 컴퓨터공학전공 |
| 정해윤 | 산업시스템공학과 |
| 강병민 | 멀티미디어소프트웨어공학전공 |

## 🎯 프로젝트 동기 (Motivation)  
- YouTube Shorts, TikTok, Reels 등 숏폼 영상 플랫폼의 성장으로 배경음악(BGM)의 중요성이 증가함  
- 영상 제작자들이 음악 저작권, 선택의 어려움, 분위기 부조화 등의 문제를 겪고 있음  
- AI가 영상의 분위기를 분석하여 적절한 배경음악을 추천하거나 생성함으로써 제작자의 편의성을 높이고 영상 퀄리티를 향상 가능  
- 향후 AI 크리에이티브 도구로 확장 가능  

## 🔥 기대 결과물 (Expected Output)  

### ✅ 1차 버전: 음악 추천 시스템  
- **입력**: 영상(영상 + 음성 포함)  
- **출력**: 1~100번 라벨 중 가장 어울리는 음악 번호 추천  
- **기술 구성**: CNN + wav2vec2 기반 멀티모달 분류 모델  

### ✅ 2차 확장: 감정 기반 추천 고도화  
- 감정 및 상황 분석 모델 개선  
- 감정 라벨과 음악 라벨 간 유사도를 고려한 추천  

### ✅ 최종 목표: AI 음악 생성 시스템 (BGM Synthesizer)  
- **입력**: 영상 또는 감정 정보  
- **출력**: AI가 생성한 분위기 맞춤형 배경음악 (예: lo-fi, cheerful, sad 등)  
- **활용 모델**: MusicGen, Riffusion, MusicLM 등  

## 📚 참고 자료 (References)  

### 🔍 논문 및 연구자료  
- Multimodal Emotion Recognition using Audio and Video (arXiv)  
- Emotion-Aware Music Recommendation (ACM Transactions)  
- MusicGen: Simple and Controllable Music Generation (Meta AI)  
- CLIP + wav2vec2 based Multimodal Fusion (CMU-MOSEI Benchmark)  

### 📁 데이터셋  
- CREMA-D, RAVDESS (오디오 감정 인식)  
- YouTube Shorts 또는 자체 수집한 영상-음악 매칭 데이터셋  

### 🧪 오픈소스  
- [maelfabien/Multimodal-Emotion-Recognition](https://github.com/maelfabien/Multimodal-Emotion-Recognition)  
- [facebookresearch/audiocraft (MusicGen)](https://github.com/facebookresearch/audiocraft)  
- [aj-naik/Emotion-Music-Recommendation](https://github.com/aj-naik/Emotion-Music-Recommendation)  

## 📅 프로젝트 일정 (Agenda)  

| 일정 | 내용 | 비고 |
| --- | --- | --- |
| 1주차 | 프로젝트 목표 설정, 음악 번호 라벨링 및 데이터셋 구성 | 1~100 음악 번호 매칭 테이블 구축 |
| 2주차 | 멀티모달 감정 인식 및 추천 시스템 관련 이론 학습 | 영상/음성 특징 추출 및 fusion 방식 학습 |
| 3주차 | 영상 처리 (CNN, CLIP 등), 오디오 처리 (librosa, wav2vec2 등) 실습 | 데이터 전처리 및 라이브러리 학습 |
| 4주차 | 영상/오디오 특징 추출 및 결합, 멀티모달 분류 모델 설계 | early fusion 방식 설계 |
| 5주차 | 추천 모델 학습 및 평가 (1~100 음악 번호 분류) | accuracy, top-k accuracy 측정 |
| 6주차 | 추천 모델 성능 개선 | soft label 또는 cosine 유사도 고려 |
| 7주차 | MusicGen 기반 AI 음악 생성 모델 실습 및 구조 이해 | HuggingFace의 audiocraft 활용 |
| 8주차 | 감정 → 텍스트 프롬프트 → MusicGen으로 음악 생성 연결 | 예: "lofi sad piano" → 음악 생성 |
| 9주차 | 전체 파이프라인 통합, 데모 및 발표자료 제작 | 영상 입력 → 음악 추천/생성 → 결과 영상 출력 |
