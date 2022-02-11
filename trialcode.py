from json import dumps

from httplib2 import Http

import jenkins.model.Jenkins



def main():
    """Google Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAARM7dFAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=73W5Cltjjjv3IGdUv0MWoMP8eegMavqPu3HpAYTeL5I%3D'
    #bot_message = {'text' :'Hello from a Python script!'}
        
    bot_message = """ BUILD_USER= ${BUILD_USER}
                  BUILD_USER_ID =${BUILD_USER_ID}
                  BUILD_USER_EMAIL=${BUILD_USER_EMAIL}"
                  BUILD_NUMBER= ${BUILD_NUMBER}
    """    
    
        

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        #body=dumps(bot_message),
        body=bot_message
        
    )

    print(response)
 
 

if __name__ == '__main__':
    main()
    
    
 
