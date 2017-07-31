import requests
import urllib

token = '1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511'
def getUserId():
    url = 'https://api.instagram.com/v1/users/1961692708/?access_token=1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511'
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
getUserId();

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
    data = {'access_token':token,"text":"Instabot"}
    make_comment = requests.post(url, data)
    make_comment = make_comment.json()
    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"
    print make_comment


def users_post():
    url = 'https://api.instagram.com/v1/users/1961692708/media/recent/?access_token=1633692610.89dc0b7.795674d4ec8f41b4a4b7cad3d5fec511'
    user_media = url
    user_media = requests.get(url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            print 'your media id is: %s' % (user_media ['data'][0]['id'])
            print 'your image is: %s' % (user_media ['data'][0]['images']['low_resolution']['url'])
            display_image = user_media ['data'][0]['images']['low_resolution']['url']
            ImageName='instaaa.jpg'
            urllib.urlretrieve(display_image,ImageName)
            likePost(like_added['data'][0]['id'])
            post_comment(make_comment['data'][0]['id'])
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'

    else:
        print 'Status code other than 200 received!'

users_post();

















