import urllib.request as ur
import json

gameid = input("Enter game id:c316b5c7-eebe-496f-b0b0-85381c174a62 ")
url = "https://play.kahoot.it/rest/kahoots/" + gameid
q = json.loads(ur.urlopen(url).read())["questions"]
colours_list = ["red", "blue", "yellow", "green"]

for index, slide in enumerate(q):
    if slide.get("type") == "quiz":
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"] == True:
                print("Question number: {}\n{}\n{}\n".format(
                    index + 1, slide["choices"][i].get("answer"), colours_list[i]))
