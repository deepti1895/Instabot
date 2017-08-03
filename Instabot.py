import requests
import urllib

token = '1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511'

def getSelfId():
    url = 'https://api.instagram.com/v1/users/self/?access_token=1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511'
    user_data = requests.get(url).json()
    if user_data['meta']['code'] == 200:
        if len(user_data['data']):
            print 'Username: %s' % (user_data['data']['username'])
            print 'UserId: %s' % (user_data['data']['id'])
            print 'No. of posts: %s' % (user_data['data']['counts']['media'])
            print 'profile picture: %s' % (user_data['data']['profile_picture'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'

    print user_data;
getSelfId();

user_name=raw_input("Please enter user name \n")
def getUserId(user_name):
    url = 'https://api.instagram.com/v1/users/search?q=%s&access_token=1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511' % (user_name)
    user_data = requests.get(url).json()
    user_name = user_data['data'][0]['username']
    user_id = user_data['data'][0]['id']
    if user_data['meta']['code'] == 200:
        if len(user_data['data'])==0:
            print("user not found")
        else:
            print "username:" +user_name
            print "id is:" +user_id
            return user_id
    else:
        print 'Status code other than 200 received!'



def users_post():
    user_id = getUserId(user_name)
    url = 'https://api.instagram.com/v1/users/%s/media/recent/?access_token=1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511' % (user_id)
    user_media = url
    user_media = requests.get(url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            print 'your media id is: %s' % (user_media ['data'][0]['id'])
            print 'your image is: %s' % (user_media ['data'][0]['images']['low_resolution']['url'])
            display_image = user_media ['data'][0]['images']['low_resolution']['url']
            ImageName='instaaa.jpg'
            urllib.urlretrieve(display_image,ImageName)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

    return user_media['data'][0]['id']



def likePost(media_id):
    url = 'https://api.instagram.com/v1/media/{0}/likes'.format(media_id)
    data = {'access_token':token}
    like_added= requests.post(url,data)
    like_added=like_added.json()
    if like_added['meta']['code'] == 200:
        print "Successfully added a new like!"
    else:
        print "Unable to add like. Try again!"
    print like_added


def post_comment(media_id):
    url = 'https://api.instagram.com/v1/media/{0}/comments'.format(media_id)
    data = {"access_token":token,
            "text":"Instabot"}
    make_comment = requests.post(url, data)
    make_comment = make_comment.json()
    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"
    print make_comment



choice=1
while choice!=3:
    user_choice = raw_input("What you want to do ? \n 1. Like a post \n 2. Comment a post \n 3. Download a post \n ")

    if(user_choice=='1'):
        media_id = users_post()
        likePost(media_id)
    elif(user_choice=='2'):
        media_id = users_post()
        post_comment(media_id)
    elif (user_choice == '3'):
        print "Wrong choice"















