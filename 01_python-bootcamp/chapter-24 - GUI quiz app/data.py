import requests
import html

response = requests.get('https://opentdb.com/api.php',params={
                            'amount': 10,
                            'type': 'boolean'})
response.raise_for_status()

results = response.json()['results']
question_data = [{'question': html.unescape(result['question']), 'correct_answer': html.unescape(result['correct_answer'])} for result in results]
