import asyncio
from aiolimiter import AsyncLimiter
from time import time
from httpx import AsyncClient
from bs4 import BeautifulSoup
import pandas as pd
from django.conf import settings

COLUMNS = ["Course Name", "Course Provider", "First Instructor", "Course Description", "# of Students Enrolled",
           "# of Ratings", "Course URL"]
DF = pd.DataFrame(columns=COLUMNS)
FILENAME = ""


def set_category_url(category: str = 'data-science') -> None:
    global FILENAME
    FILENAME = f"{settings.MEDIA_ROOT}/files/{category}.csv"
    return f"https://www.coursera.org/browse/{category}"


async def scrape(url, course_name, course_provider, session, throttler):
    async with throttler:
        course_page = await session.get(url)
        page_soup = BeautifulSoup(course_page.content, "html.parser")
        if page_soup.find(attrs={"data-test": "ratings-count-without-asterisks"}):
            course_rating = \
                page_soup.find(attrs={"data-test": "ratings-count-without-asterisks"}).text.split(" ratings")[0]
        else:
            course_rating = ""

        if page_soup.find("div", class_="_1fpiay2"):
            course_participants = page_soup.find("div", class_="_1fpiay2").text.split(" already enrolled")[0]
        else:
            course_participants = ""

        if page_soup.find(attrs={"data-track-href": "#instructors"}).select_one("span"):
            first_instructor = page_soup.find(attrs={"data-track-href": "#instructors"}).select_one("span").text
            if "," in first_instructor:
                first_instructor = first_instructor.split(",")[0]
            elif "more" in first_instructor:
                first_instructor = first_instructor.split(" +")[0]
        else:
            first_instructor = ""

        if "professional-certificates" in url:
            course_description = page_soup.find("div", class_="cmlToHtml-content-container").text
            if page_soup.find("p", class_="cds-33 css-14d8ngk cds-35"):
                course_rating = page_soup.find("p", class_="cds-33 css-14d8ngk cds-35").text.split()[0]
                course_participants = page_soup.find("p", class_="cds-33 css-14d8ngk cds-35").text.split()[2]

        elif "specializations" in url:
            course_description = page_soup.find("div", class_="cmlToHtml-content-container").text
        else:
            course_description = page_soup.find("div", class_="m-t-1 description").text

        DF.loc[len(DF)] = [course_name, course_provider, first_instructor, course_description, course_participants,
                           course_rating, url]


async def run(category_name: str = "data-science"):
    _start = time()
    throttler = AsyncLimiter(max_rate=10,
                             time_period=1.5)  # 10 tasks/1.5, couldn't go faster 'cause I've been being blocked
    async with AsyncClient() as session:
        tasks = []
        category_page = await session.get(set_category_url(category_name))

        category_soup = BeautifulSoup(category_page.content, "html.parser")
        results = category_soup.find_all("div", class_="rc-Card productCard-card")
        for i in results:
            url_to_course = "https://www.coursera.org" + i.find("a", class_="CardText-link").get("href")
            course_name = i.find("a", class_="CardText-link").text
            course_provider = i.find("div", class_="rc-CardText productCard-subtitle css-1feobmm").text
            tasks.append(scrape(url_to_course, course_name, course_provider, session=session, throttler=throttler))
        results = await asyncio.gather(*tasks)
        # print(results)
    print(f"finished scraping in: {time() - _start:.1f} seconds")


def scrapper_main(category_name):
    asyncio.run(run(category_name))
    DF.to_csv(FILENAME)
