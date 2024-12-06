# NLTK 설치
# pip install nltk

from nltk.tokenize import sent_tokenize


# 텍스트 파일 읽기
text = """
Python is an interpreted, high-level, general-purpose programming language.
Its design philosophy emphasizes code readability.
It is widely used in various domains such as web development, data analysis, and AI.
"""

# 문장을 토큰화
sentences = sent_tokenize(text)
print(sentences)

# 특정 크기로 청킹 (예: 2문장씩)
chunk_size = 1
chunks = [sentences[i:i + chunk_size] for i in range(0, len(sentences), chunk_size)]

# 결과 출력
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {' '.join(chunk)}")