import requests  # Для отправки HTTP-запросов
import json  # Для работы с JSON
import os  # Для работы с файлами

"""
def base(request):
    return render(request, 'films/base.html')

"""

# 🔑 ВАЖНО: Укажите ваш API-ключ (замените "YOUR_API_KEY" на ваш ключ)
API_KEY = "bf60be6"

# 🎬 Вводим название фильма
movie_title = input("Roman Holiday")

# 📌 Формируем URL запроса
api_url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

# 🔹 Отправляем GET-запрос
response = requests.get(api_url)

# 🔍 Проверяем, успешно ли прошёл запрос
if response.status_code == 200:
    data = response.json()  # Преобразуем JSON-ответ в словарь

    # Проверяем, найден ли фильм
    if data["Response"] == "True":
        print("\n🎥 Информация о фильме:")
        print(f"Название: {data['Title']}")
        print(f"Год: {data['Year']}")
        print(f"Жанр: {data['Genre']}")
        print(f"Режиссёр: {data['Director']}")
        print(f"Актёры: {data['Actors']}")
        print(f"IMDb рейтинг: {data['imdbRating']}")
        print(f"Постер: {data['Poster']}")

        # 📝 Сохранение данных в файл
        save_folder = "movies_data"
        os.makedirs(save_folder, exist_ok=True)  # Создаём папку, если её нет
        file_path = os.path.join(save_folder, f"{movie_title}.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"\n✅ Данные о фильме сохранены в файл: {file_path}")

        # 📥 Скачивание постера фильма
        if data["Poster"] != "N/A":
            poster_url = data["Poster"]
            poster_response = requests.get(poster_url)

            if poster_response.status_code == 200:
                poster_path = os.path.join(save_folder, f"{movie_title}.jpg")
                with open(poster_path, "wb") as img_file:
                    img_file.write(poster_response.content)
                print(f"🖼️ Постер фильма сохранён: {poster_path}")
            else:
                print("⚠️ Не удалось скачать постер.")

    else:
        print("❌ Фильм не найден. Попробуйте другое название.")

else:
    print(f"⚠️ Ошибка запроса: {response.status_code}")