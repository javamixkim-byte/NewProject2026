# NewProject2026
This is my first project using Codex

# 📊 [프로젝트 이름 입력 : Codex-DataViz]

> OpenAI Codex를 활용하여 자연어 명령만으로 데이터를 분석하고 시각화 차트를 자동으로 생성하는 파이썬 도구입니다.

## 📝 프로젝트 소개
이 프로젝트는 데이터 분석가나 비개발자가 복잡한 파이썬 코드(Pandas, Matplotlib 등)를 짜지 않아도, "7월 매출 추이를 꺾은선 그래프로 그려줘"와 같은 자연어 명령을 통해 데이터 분석 스크립트와 시각화 이미지를 자동으로 얻을 수 있도록 돕는 OpenAI Codex 기반 자동화 툴입니다.

## ✨ 주요 기능
- **자연어 기반 데이터 전처리**: 결측치 처리, 데이터 필터링, 정렬 명령을 파이썬 코드로 변환 및 실행
- **자동 차트 생성**: Matplotlib 및 Seaborn을 활용한 막대그래프, 꺾은선그래프, 산점도, 히트맵 등 자동 시각화
- **통계 요약 리포트**: 데이터셋(CSV/Excel)의 기초 통계 정보 분석 및 요약문 작성
- **코드 및 결과 저장**: 생성된 분석 소스 코드와 시각화 이미지(.png) 자동 저장

## 🛠️ 시작하기

### 1. 요구 사항
- Python 3.8 이상
- OpenAI API Key ([발급 받기](https://openai.com))

### 2. 설치 방법
리포지토리를 클론하고 필요한 패키지를 설치합니다.

```bash
# 리포지토리 클론
git clone https://github.com[사용자ID]/[리포지토리이름].git
cd [리포지토리이름]

# 가상환경 생성 및 활성화 (권장)
python -m venv venv
source venv/bin/activate  # Windows 환경: venv\Scripts\activate

# 의존성 패키지 설치 (데이터 분석 필수 라이브러리 포함)
pip install -r requirements.txt
```

### 3. 환경 변수 설정
프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 OpenAI API 키를 입력합니다.

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 💻 사용 방법

분석하고 싶은 CSV 또는 Excel 파일을 `data/` 폴더에 넣은 후 프로그램을 실행하고 자연어로 명령을 입력하세요.

```bash
python main.py
```

**💡 사용 예시 (Prompt):**
```text
🤖 파일 선택: data/sales_2026.csv
💬 명령 입력: "상위 5개 제품의 월별 판매량을 막대그래프(Bar chart)로 그려주고, 이미지로 저장해줘"
```

**🛠️ Codex가 생성하고 실행하는 예시 코드:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df = pd.read_csv('data/sales_2026.csv')

# Codex가 생성한 분석 및 시각화 로직 실행...
# (결과물로 'output_chart.png'가 자동 생성됩니다.)
```

## 🤝 기여 방법 (Contributing)
오픈소스 기여는 언제나 환영합니다! 
1. 이 리포지토리를 **Fork**합니다.
2. 새로운 기능 브랜치를 생성합니다 (`git checkout -b feature/AmazingFeature`).
3. 변경 사항을 **Commit**합니다 (`git commit -m 'Add some AmazingFeature'`).
4. 브랜치에 **Push**합니다 (`git push origin feature/AmazingFeature`).
5. **Pull Request**를 요청합니다.

## 📄 라이선스 (License)
이 프로젝트는 **MIT License**를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.
