import os

class FindTalentSettings:
    qa_env = os.environ["qa_env"]
    url = "http://{}.workmarket.com/login".format(qa_env)
    search_url = "https://{}.workmarket.com/search".format(qa_env)
    email = os.environ["email"]
    password = os.environ["password"]
