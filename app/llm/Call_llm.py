import requests


def make_guess(prompt):
    res = requests.post(url='http://ollama:11434/api/generate',
                        json={
                            'model': 'llama3.1',
                            'prompt': prompt,
                            'stream': False,
                        })
    return res.json()["response"]


if __name__ == '__main__':
    result = make_guess("Qual é a capital do Canada?")
    print(result)