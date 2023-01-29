담당자 : 김태훈 (thkim@mnc.ai)


# 2021 NIPA 인공지능 놀이터

### Task19
[미들AI/시계열] 치매 예방을 위한 라이프로그 치매 분류 모델


## 상세 설명

### 과제 설명

실시간 수면/활동 라이프 로그 데이터 수집을 통한 인지능력 모니터링 과제

- 의의
  - 고령화 사회로의 진입 및 치매 발병률 증가에 따른 의료비 부담 증가로 인해 치매 환자의 조기진단과 치료가 중요한 과제로 부상
  - 치매는 초기에 진단이 이루어지지 않으면 발병 후 치료 및 회복이 어려워 예방과 조기 검진을 통한 선제적 관리가 유일한 대한안
  - 치매조기진단 예측 및 발병의 예방과 선제적 관리를 위한 AI 기술 필요

### 채점 방식

**Macro F1-Score**

Macro F1 = 1/6 * sum( F1 )  
  
F1-score: Pricision과 Recall의 조화평균  
F1 = (2 * Recall * Precision ) / ( Precision + Recall )

- Recall[재현율/민감도] : ( TP ) / ( TP + FN )
- Precision[정밀도] : ( TP ) / ( TP + FP )
  - TP : True로 예측하고 실제 값도 True
  - TN : False로 예측하고 실제 값도 False
  - FP : True로 예측하고 실제는 False
  - FN : False로 예측하고 실제는 True



## 데이터

### 데이터 설명

- 입출력
  - Input : 반지 형태의 데일리 수면/활동 데이터 수집기를 통해 5분 단위로 수집한 기본적인 삶의 패턴을 24시간 동안 라이프 로그 모니터링한 데이터
  - Output : 3가지 카테고리 중 1
    - CN : Cognitive Normal (인지기능 정상)
    - MCI : Mild Cognitive Impairment (경도 인지기능 장애)
    - Dem : Dementia (치매)

- 데이터셋 구성 : 272.3MB
  - train: 각각 ID와 input, ID와 label 정보를 담은 두 개의 csv 파일(train.csv, train_label.csv)
  - test: ID와 input 정보를 담은 1개의 csv 파일 (test.csv)

### 데이터 링크
- 데이터 다운로드 : [링크](https://aihub.or.kr/problem_contest/nipa-learning-platform)  
- AI hub 참고 데이터 : [치매 고위험군 웨어러블 라이프로그](https://aihub.or.kr/aidata/30749)