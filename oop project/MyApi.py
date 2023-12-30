import paralleldots
class ApiManager:
    def __init__(self):
        paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        sentiment = max(response['sentiment'], key=response['sentiment'].get)
        score = response['sentiment'][sentiment]

        return(f"Sentiment: {sentiment.capitalize()} with a score of {score}")

    def ner(self,text):
        response= paralleldots.ner(text)
        return response


    def emotion_analysis(self, text):
        response = paralleldots.emotion(text)
        if 'emotion' in response and response['emotion']:
            emotion = max(response['emotion'], key=response['emotion'].get)
            score = response['emotion'][emotion]
            return f"Emotion: {emotion.capitalize()} with a score of {score}"
        else:
            return "Unable to determine emotion. Please check your input or try again."

    def abuse_detection(self, text):
        try:
            response = paralleldots.abuse(text)
            if 'abusive' in response:
                abusive_score = response['abusive']
                return f"Abusive content detected with a score of {abusive_score}. Please refrain from using offensive language."
            else:
                # If abusive key is not present, return sentiment analysis result
                return self.sentiment_analysis(response)
        except Exception as e:
            print(f"Error during abuse detection: {e}")
            return "Unable to perform abuse detection at the moment."