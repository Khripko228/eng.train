import random

# Словарь английских слов и их переводов
words = {
    "apple": "яблоко",
    "house": "дом", 
    "cat": "кот",
    "dog": "собака",
    "book": "книга",
    "water": "вода",
    "sun": "солнце",
    "tree": "дерево",
    "car": "машина",
    "computer": "компьютер",
    "friend": "друг",
    "school": "школа",
    "mother": "мать",
    "father": "отец",
    "time": "время",
    "apple": "яблоко",
    "house": "дом",
    "cat": "кот", 
    "dog": "собака",
    "book": "книга",
    "water": "вода",
    "sun": "солнце",
    "tree": "дерево",
    "car": "машина",
    "computer": "компьютер",
    "friend": "друг",
    "school": "школа",
    "mother": "мать", 
    "father": "отец",
    "time": "время",
    "city": "город",
    "country": "страна",
    "language": "язык",
    "work": "работа",
    "day": "день",
    "night": "ночь",
    "food": "еда",
}

def main():
    print("=== ТРЕНАЖЕР АНГЛИЙСКИХ СЛОВ ===")
    print("Введите перевод слова. Для выхода введите 'exit'")
    
    score = 0
    total = 0
    
    # Создаем список слов для повторения
    word_list = list(words.items())
    random.shuffle(word_list)
    
    for english, correct_russian in word_list:
        print(f"\nСлово: {english}")
        answer = input("Перевод: ").strip().lower()
        
        if answer == "exit":
            break
        
        if answer == correct_russian:
            print("✅ Верно!")
            score += 1
        else:
            print(f"❌ Неверно. Правильно: {correct_russian}")
        
        total += 1
    
    print(f"\n=== РЕЗУЛЬТАТ ===")
    print(f"Правильных ответов: {score} из {total}")
    
    if total > 0:
        percent = (score / total) * 100
        print(f"Процент правильных: {percent:.1f}%")

if __name__ == "__main__":
    main()