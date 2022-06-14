from os import environ
import requests
import json

class Medium:
    def __init__(self,access_token):
        self.BASE_URL = 'https://api.medium.com/v1'
        self.access_token = access_token
        self.headers = {
                'Authorization': 'Bearer ' + self.access_token,
                'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.my_info = self.getMyInfo()
        print("My info",self.my_info)
        #self.my_publications = self.getPublications()
        #print(json.dumps(self.my_publications, indent=4, sort_keys=True))
    
    def getMyInfo(self):
        info_url = self.BASE_URL + "/me"
        print(self.headers)
        response = requests.get(info_url, headers=self.headers)
        return json.loads(response.text)['data']
    
    
    def showPosts(self):
        url = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@' + self.my_info['username']
        response = requests.get(url)
        return json.loads(response.text)
        #return json.loads(response.text)['data']
    
    def getPublications(self):
        user_id = self.my_info['id']
        info_publication = self.BASE_URL + f'/users/{user_id}/publications'
        response = requests.get(info_publication, headers=self.headers)
        return json.loads(response.text)

    def post2Medium(self,post_content):
        user_id = self.my_info['id']
        url_post = self.BASE_URL + f"/users/{user_id}/posts"
        response = requests.post(url_post, headers=self.headers, data=post_content)
        print(response.text)
        return json.loads(response.text)

if __name__ == '__main__':
    access_token = environ.get('access_token')
    medium_user = Medium(access_token)
    new_post = {
                "title": "My react website",
                "contentFormat": "markdown",
                "content": "Link to my latest react project [Andre Web Page](http://frontend.andreyai.com) ",
                "canonicalUrl": "http://frontend.andreyai.com",
                "tags": ["tech","react","software_eng"],
                "publishStatus": "draft"
            }
    medium_user.post2Medium(new_post)
    #publications = medium_user.showPosts()
    #print(json.dumps(publications, indent=4, sort_keys=True))
    #publications = medium_user.getPublications()
    #print(json.dumps(publications, indent=4, sort_keys=True))
    