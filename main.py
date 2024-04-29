import json
from difflib import get_close_matches

def load_json(file):
    with open(file, 'r') as file:
        data = json.load(file)
    return data

def save_json(file, data):
    with open(file, 'w') as file:
        json.dump(data, file, indent=2)

def find_match(question, questions):
    matches = get_close_matches(question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question, data):
    for query in data["questions"]:
        if query["question"] == question:
            return query["question"]
    return None

def chat_bot():
    data = load_json('data.json')

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        match = find_match(user_input, [query["question"] for query in data["questions"]])

        if match:
            answer = get_answer(match, data)
            print(f"Bot: {answer}")

        else:
            print("Bot: I do not know the answer. Can you teach me?")
            new_answer = input("Type the answer or 'skip to skip")

            if new_answer.lower() != 'skip':
                data["questions"].append({"question": user_input, "answer": new_answer})
                save_json("data.json", data)
                print("Bot: Thank you for teaching me")

if __name__ == '__main__':
    chat_bot()