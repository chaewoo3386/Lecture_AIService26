import joblib
from konlpy.tag import Okt

def korean_tokenizer(text):
        my_tags = ['Noun', 'Adjective', 'Verb']
        my_stopwords = []
        return [word for word, tag in Okt().pos(text) if word not in my_stopwords and tag in my_tags]

class SentimentAnalyzer:
    def __init__(self, tokenizer, vectorizer_file, predict_model_file):
        self.__vectorizer = joblib.loadload(vectorizer_file)
        self.__predict_model = joblib.load(predict_model_file)
        self.__tokenizer = tokenizer

    def analyze_semtiment(self, review):
    # 특징 백터 추출
        self.__review_fv = vectorizer.transform([review])
        # 학습된 모델로 예측
        self.__pred = sa_model.predict(review_fv)
        # 예측값에 따라 결과를 생성하여 변환
        self.__result = '긍정' if pred[0] >= 0.5 else '부정'
        return result, pred[0]
