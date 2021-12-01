import requests


def get_answer(question):
    #r = requests.post('http://127.0.0.1:5000/api/question-answering', data = {'question': question})
    response_body = {
        'context': 'd. Retiro Parcial: El estudiante podrá solicitar el retiro de hasta dos (02) asignaturas, dentro del plazo que vence el último día útil de la quinta semana después del inicio de clases del periodo académico.',
        'answer': 'de hasta dos (02) asignaturas'
          }
    answer = response_body['context'].replace(response_body['answer'],'**'+response_body['answer']+'**') 
    return answer