import json
from bs4 import BeautifulSoup
import csv
import asyncio
import aiohttp
import datetime


async def get_page_data(session, url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, "lxml")

        books_data = []

        for item in soup.select(".item_info"):
            book_title = item.select_one(".item-title span").text.strip()

            try:
                book_price = int(item.select_one(".price span.price_value").text.strip())
            except:
                book_price = "Нет цены"

            books_data.append(
                {
                    "book_title": book_title,
                    "book_price": book_price,
                }
            )

        return books_data


async def gather_data():
    async with aiohttp.ClientSession() as session:
        url = "https://bookling.ua/"
        books_data = await get_page_data(session, url)
        return books_data


def main():
    books_data = asyncio.run(gather_data())
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"books_{cur_time}_async.json", "w", encoding="utf-8") as file:
        json.dump(books_data, file, indent=4, ensure_ascii=False)

    with open(f"books_{cur_time}_async.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название книги",
                "Цена",
            )
        )

        for book in books_data:
            writer.writerow(
                (
                    book["book_title"],
                    book["book_price"],
                )
            )


if __name__ == "__main__":
    main()
