# 🎵 Affective Multimodal Transformer model 기반 숏츠 배경음악 생성

## 📌 프로젝트 개요  
영상의 영상 및 음성 정보를 분석하여 분위기를 파악하고, 이에 어울리는 음악을 생성하는 AI 시스템을 개발하는 프로젝트입니다.

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

### Shorts 배경음악 생성 시스템 (Youtube Short BGM Generator)
- **입력**: BGM 없는 Shorts 영상  
- **출력**: 영상의 감정, 장면, 움직임 등의 특징을 분석하여 분위기를 파악하고, 해당 분위기에 어울리는 음악이 포함된 영상
- **활용 모델**: Affective Multimodal Transformer model 기반 Video2Music

## 📚 참고 자료 (References)  

### 🔍 논문 및 연구자료  
- https://arxiv.org/abs/2311.00968 (Video2Music: Suitable Music Generation from Videos using an Affective Multimodal Transformer mode) 
- https://joss.theoj.org/papers/10.21105/joss.03391 (omnizart)
- https://arxiv.org/abs/1907.02698 (A Bi-directional Transformer for Musical Chord Recognition)
- https://arxiv.org/abs/2103.00020 (Learning Transferable Visual Models From Natural Language Supervision)
  
### 📁 데이터셋  
- https://zenodo.org/records/10057093 (MuVi-Sync Dataset)
- YouTube Shorts 또는 자체 수집한 영상-음악 매칭 데이터셋  

### 🧪 오픈소스  
- https://github.com/AMAAI-Lab/Video2Music (Video2Music)
- https://github.com/gwinndr/MusicTransformer-Pytorch (MusicTransformer-Pytorch)
- https://github.com/Music-and-Culture-Technology-Lab/omnizart/tree/master (omnizart)
- https://github.com/jayg996/BTC-ISMIR19/tree/master (BTC-ISMIR19)
