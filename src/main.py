
from os import environ
from integrations.medium import Medium
import yaml
import json
import logging

logging.basicConfig(level=logging.INFO)

class Catalog:
    def __init__(self,fileCatalog):
        self.fileCatalog = fileCatalog
        access_token = environ.get('MEDIUM_TOKEN')
        self.medium_user = Medium(access_token)
    
    def getPostCatalog(self):
        yaml_file = open(self.fileCatalog)
        post_list = yaml.load(yaml_file, Loader=yaml.FullLoader)
        return post_list
    
    def postMedium(self,new_post):
        title = new_post["title"]
        logging.info(f"Postting new Article to Medium: {title} ",)
        post_return =  self.medium_user.post2Medium(new_post)
        url = post_return["data"]["url"]
        logging.info(f"Successfull {title}. Link: {url}")
        return post_return
    
    def getMediumTitles(self):
        logging.info("Getting Medium Posts")
        post_title_list = []
        postsMedium = self.medium_user.showPosts()["items"]
        for post in postsMedium:
            post_title_list.append(post["title"])
            
        return post_title_list 
    
    def formatMarkdownPost(self, title, content, tags,  status="draft"):
        new_post = {"title": title, "content": content}
        new_post["contentFormat"] = "markdown"
        new_post["tags"] = tags
        new_post["publishStatus"] = status
        return self.postMedium(new_post)

    def sendNewPosts(self):
        '''' Verify if is a new content by its title if so sends to Medium API. '''
        new_post_list = self.getPostCatalog()
        post_titles_list = self.getMediumTitles()
        #Post   
        for post_index in new_post_list:
            post = new_post_list[post_index]
            post_title = post["title"]
            if(post_title not in post_titles_list):
                post_content = open(post["content_file"], "r").read()
                catalog.formatMarkdownPost(post["title"], post_content, post["tags"], post["status"])
        
if __name__ == '__main__':
    fileCatalog = "./post_manager.yml"
    catalog = Catalog(fileCatalog)
    catalog.sendNewPosts()
     