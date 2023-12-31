from bs4 import BeautifulSoup
import requests
import threading
import cloudscraper
from os.path import basename
import os
import html5lib
from db import connection,try_sql_query,create_database,close_connection

database_name = "meow"

create_database(database_name)

proxies = {
    'http': 'http://127.0.0.1:2081',
    'https': 'http://127.0.0.1:2081',
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}


scraper = cloudscraper.create_scraper()


class Job:
    def __init__(self, title="Null", desc="Null", url="Null", img_url="Null", author="Null", views=0, downloads=0,
                img_id="Null", res="Null", lic="Null", cat="Null"):
        self.title = title
        self.desc = desc
        self.url = url
        self.img_url = img_url
        self.author = author
        self.views = views
        self.downloads = downloads
        self.img_id = img_id
        self.res = res
        self.lic = lic
        self.cat = cat

    def __str__(self):
        return "Cat : "+ self.cat +" | title : " + self.title + " | desc : " + self.desc + " | url : " + self.url + " | img url : " + self.img_url + " | author : " + self.author + " | views : " + self.views + " | downloads : " + self.downloads + " | img id : " + self.img_id + " | res : " + self.res + " | lic : " + self.lic


# Image
def download_image(lnk,img_id):
    filename = "{}.jpg".format(img_id)
    if not os.path.exists("static"):
        os.makedirs("static")
    filepath = os.path.join("static", filename)
    with open(filepath, "wb") as f:
        f.write(scraper.get(lnk, proxies=proxies, headers=headers).content)


# send requests through cloud scraper and parse it using html5lib
def req(req_url):
    r = scraper.get(url=req_url, proxies=proxies, headers=headers)
    return BeautifulSoup(r.content, "html5lib")


# Fetches all the categories
def get_cats():
    r = req("https://stocksnap.io/popular")
    cats = []
    for i in r.select(".popular-item ul"):
        for j in i.select("li a"):
            cats.append(j.text)
    return cats


# Gets image links from categories or Grid of images
def get_image_links(req_url):
    parsed_content = req(req_url)
    img_page_links = []
    for i in parsed_content.select(".photo-grid-item"):
        for j in i.select(".photo-grid-preview"):
            img_page_links.append("https://stocksnap.io" + j.get("href"))
    return img_page_links


# Makes the Search links to be used as a category page
def getSearchLinks():
    links = []
    for i in get_cats():
        links.append("https://stocksnap.io/search/" + i)
    return links


# Parses the image page
def get_image_data(req_url,cat):
    parsed_content = req(req_url)
    job = Job()
    job.url = req_url
    job.cat = cat
    job.img_id = req_url.split("-")[-1]
    for i in parsed_content.select(".photo-wrap .img-col"):
        for j in i.select("h1 > span"):
            job.title = j.text
        for j in i.select("figure > img"):
            job.img_url = j.get("src")
            job.desc = j.get("alt")
        for j in i.select(".icon-eye + span"):
            job.views = j.text
        for j in i.select(".icon-cloud-download + span"):
            job.downloads = j.text
        for j in i.select(".icon-frame + span"):
            job.res = j.text
        for j in i.select(".icon-info + span > a"):
            job.lic = j.text
        for j in i.select("a.author > span"):
            job.author = j.text
    return job

def do_job(job):
    db_connection = connection(database_name)
    try_sql_query(
        connection=db_connection,
        title=job.title,
        description=job.desc,
        url=job.url,
        img_url=job.img_url,
        author=job.author,
        views=job.views,
        downloads=job.downloads,
        license=job.lic,
        resolution=job.res,
        category=job.cat,
        img_id=job.img_id
        )
    download_image(job.img_url,job.img_id)
def get_all_images():
    images = []
    cats_link = getSearchLinks()
    for i in cats_link:
        cat = i.split("/")[-1]
        for j in get_image_links(i):
            # print(get_image_data(j,cat))
            job = get_image_data(j,cat)
            # To test with no multi threading uncomment the following line and comment the second and third line
            # do_job(job) 
            thread = threading.Thread(target=do_job,args=(job,))
            thread.start()

try:
    get_all_images()
except:
    print("something went wrong !")
finally:
    close_connection(database_name)