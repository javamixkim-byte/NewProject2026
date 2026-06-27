import os
import openai
from dotenv import load_dotenv

# 1. 환경 변수 로드 (.env 파일에서 API 키를 읽어옵니다)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("⚠️ .env 파일에 OPENAI_API_KEY가 설정되지 않았습니다.")

# OpenAI 클라이언트 초기화 (최신 openai>=1.0.0 버전 기준)
client = openai.OpenAI(api_key=api_key)

def generate_data_code(user_prompt, file_path="Data/sample.csv"):
    """
    사용자의 자연어 명령을 기반으로 데이터 분석 및 시각화 파이썬 코드를 생성합니다.
    """
    # 생성할 코드의 가이드라인을 시스템 프롬프트로 정의합니다.
    system_instruction = (
        "You are an expert Python data analyst. "
        "Generate ONLY executable Python code using pandas, matplotlib, or seaborn. "
        "Do not include markdown formatting like ```python or any explanations. "
        "Assume the data file is located at the given path. "
        "Always save the final visualization chart as 'output_chart.png'."
    )
    
    # Codex 계열 모델 대신 최신 고성능 모델(gpt-4o 등)을 활용합니다.
    user_instruction = f"File path: '{file_path}'\nCommand: {user_prompt}"
    
    print("\n🤖 AI가 데이터 분석 코드를 생성하는 중입니다...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # 최신 데이터 분석 지원 모델
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_instruction}
            ],
            temperature=0.2  # 정확한 코드 생성을 위해 낮게 설정
        )
        
        generated_code = response.choices[0].message.content.strip()
        return generated_code
        
    except Exception as e:
        print(f"❌ API 호출 중 오류 발생: {e}")
        return None

def execute_code(code_string):
    """
    생성된 파이썬 코드를 안전하게 실행합니다.
    """
    if not code_string:
        return
        
    print("\n⚙️ 생성된 코드를 실행합니다:")
    print("-" * 40)
    print(code_string)
    print("-" * 40)
    
    try:
        # 내장 함수 exec()를 사용하여 코드를 실행합니다.
        # 실제 서비스 운영 시에는 보안을 위해 샌드박스 환경을 권장합니다.
        exec(code_string, globals())
        print("\n✅ 분석 및 시각화가 성공적으로 완료되었습니다! ('output_chart.png' 확인)")
    except Exception as e:
        print(f"\n❌ 코드 실행 중 오류 발생: {e}")

if __name__ == "__main__":
    print("=== 📊 OpenAI 기반 데이터 분석 자동화 툴 ===")
    
    # 테스트용 파일 경로와 사용자 명령 예시
    csv_file = "Data/sample.csv" 
    prompt = "이 파일에서 매출(sales) 컬럼의 월별 추이를 꺾은선 그래프로 그리고 이미지로 저장해줘."
    
    # 1. 코드 생성
    ai_code = generate_data_code(prompt, file_path=csv_file)
    
    # 2. 코드 실행
    execute_code(ai_code)

