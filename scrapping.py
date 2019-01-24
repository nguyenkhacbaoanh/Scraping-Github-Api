import requests
from requests.packages.urllib3 import add_stderr_logger
# import urllib
from bs4 import BeautifulSoup
from urllib.error import HTTPError
# from urllib.request import urlopen
import re, random, datetime
random.seed(datetime.datetime.now())
# load variable environment
from dotenv import load_dotenv
load_dotenv()

add_stderr_logger()
url_base = "https://github.com/"
url_login = "https://github.com/login"
session = requests.Session()

per_session = session.post(url_login,
                           data={'login':id, 'password':'password'}, 
                           headers={"referer":url_base})
# critation of search infomation
key_search = ["repositories", "stars", "followers", "following"]
try:
   # information hors de boucle
   # soup = BeautifulSoup(session.get("https://github.com/supig").content, 'html.parser')
   # img = soup.find("img", {"class":"avatar width-full avatar-before-user-status"}).attrs["src"]
   # full_name = soup.find("span",{"class":"p-name vcard-fullname d-block overflow-hidden"})
   # acc_name = soup.find("span",{"class":"p-nickname vcard-username d-block"})
   # bio = soup.find("div", {"class":"p-note user-profile-bio mb-3"}).find("div").text
   # location = soup.find("li",{"itemprop":"homeLocation"}).find("span").text
   # # email = soup.find("li",{"itemprop":"email"}).find("a").text
   # information à cherche dans la boucle
   # --------------------------------------
   # Repositories:
   # params = {
   #    "tab": key_search[0]
   # }  
   # #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
   # soup = BeautifulSoup(session.get("https://github.com/supig", params=params).content, 'html.parser')
   # repo = soup.find("ul", {"data-filterable-for":"your-repos-filter"})
   # list_repo = repo.findAll("li",{"itemprop":"owns"})
   # # cherche les infos pour chaque repo:
   # repository = list()
   # used_lang = list()
   # for repo_ in list_repo:
   #    repository.append(repo_.find("a",{"itemprop":"name codeRepository"}).text.strip())
   #    try:
   #       used_lang.append(repo_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
   #    except:
   #       used_lang.append("Unknown")
   # # ---
   # # Pagination:
   # pa = soup.find("div",{"class":"pagination"})
   # # s'il y a un seul page, on n'a pas besoin des codes au-dessous
   # if pa != None:
   #    next_ = pa.findAll("a")
   #    # print(next_)
   #    for n in next_:
   #       # print(n.text)
   #       # print(n.attrs["href"])
   #       if n.text == "Next":
   #          soup_sub = BeautifulSoup(session.get(n.attrs["href"]).content, 'html.parser')
   #          repo = soup_sub.find("ul", {"data-filterable-for":"your-repos-filter"})
   #          list_repo = repo.findAll("li",{"itemprop":"owns"})
   #          for repo_ in list_repo:
   #             repository.append(repo_.find("a",{"itemprop":"name codeRepository"}).text.strip())
   #             try:
   #                used_lang.append(repo_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
   #             except:
   #                used_lang.append("Unknown")
   # print(repository)
   # print(used_lang)
   # --------------------------------------
   # Stars
   # params = {
   #    "tab": key_search[1]
   # }  
   # #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
   # star = BeautifulSoup(session.get("https://github.com/supig", params=params).content, 'html.parser')
   # list_stars = star.findAll("div",{"class":"col-12 d-block width-full py-4 border-bottom"})
   # # cherche les infos pour chaque repo:
   # repository_star = list()
   # used_lang_star = list()
   # for star_ in list_stars:
   #    repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
   #    try:
   #       used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
   #    except:
   #       used_lang_star.append("Unknown")
   # # ---
   # # Pagination:
   # pa = star.find("div",{"class":"pagination"})
   # # s'il y a un seul page, on n'a pas besoin des codes au-dessous
   # if pa != None:
   #    next_ = pa.findAll("a")
   #    # print(next_)
   #    for n in next_:
   #       # print(n.text)
   #       # print(n.attrs["href"])
   #       if n.text == "Next":
   #          star = BeautifulSoup(session.get(n.attrs["href"]).content, 'html.parser')
   #          # star = soup_sub.find("div", {"class":"d-lg-flex gutter-lg mt-4"})
   #          list_stars = star.findAll("div",{"class":"col-12 d-block width-full py-4 border-bottom"})
   #          for star_ in list_stars:
   #             repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
   #             try:
   #                used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
   #             except:
   #                used_lang_star.append("Unknown")
   # print(repository_star)
   # print(used_lang_star)
   # --------------------------------------
   # Followers
   params = {
      "tab": key_search[2]
   }  
   #it assumed that by now you are logged so we can now use .get and fetch any page of your choice
   follower = BeautifulSoup(session.get("https://github.com/supig", params=params).content, 'html.parser')
   list_followers = follower.findAll("div",{"class":"d-table table-fixed col-12 width-full py-4 border-bottom border-gray-light"})
   # cherche les infos pour chaque repo:
   followers = dict()
   for star_ in list_stars:
      repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
      try:
         used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
      except:
         used_lang_star.append("Unknown")
   # ---
   # Pagination:
   pa = star.find("div",{"class":"pagination"})
   # s'il y a un seul page, on n'a pas besoin des codes au-dessous
   if pa != None:
      next_ = pa.findAll("a")
      # print(next_)
      for n in next_:
         # print(n.text)
         # print(n.attrs["href"])
         if n.text == "Next":
            star = BeautifulSoup(session.get(n.attrs["href"]).content, 'html.parser')
            # star = soup_sub.find("div", {"class":"d-lg-flex gutter-lg mt-4"})
            list_stars = star.findAll("div",{"class":"col-12 d-block width-full py-4 border-bottom"})
            for star_ in list_stars:
               repository_star.append(star_.find("div",{"class":"d-inline-block mb-1"}).find("a").attrs["href"].lstrip("/"))
               try:
                  used_lang_star.append(star_.find("span",{"itemprop":"programmingLanguage"}).text.strip())
               except:
                  used_lang_star.append("Unknown")
   print(repository_star)
   print(used_lang_star)
except HTTPError as e:
   print(e)
