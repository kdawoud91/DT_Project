from wsgiref import headers
import jwt
import requests
import json
from time import time


class zoom():

        def __init__(self,Key,Sec,meetingId=6567787215,userId='khaled.dawoud@mbzuai.ac.ae'):
                self.API_KEY = Key
                self.API_SEC = Sec
                # your zoom live meeting id, it is optional though
                self.meetingId = meetingId

                self.userId = userId
                self.meetingdetails= {
        "created_at": "2019-09-05T16:54:14Z",
        "duration": 60,
        "host_id": "AbcDefGHi",
        "id": 6567787215,
        "join_url": "https://zoom.us/j/1100000",
        "settings": {
        "alternative_hosts": "",
        "approval_type": 2,
        "audio": "both",
        "auto_recording": "local",
        "close_registration": False,
        "cn_meeting": False,
        "enforce_login": False,
        "enforce_login_domains": "",
        "global_dial_in_countries": [
          "US"
        ],
        "global_dial_in_numbers": [
          {
            "city": "New York",
            "country": "US",
            "country_name": "US",
            "number": "+1 1000200200",
            "type": "toll"
          },
          {
            "city": "San Jose",
            "country": "US",
            "country_name": "US",
            "number": "+1 6699006833",
            "type": "toll"
          },
          {
            "city": "San Jose",
            "country": "US",
            "country_name": "US",
            "number": "+1 408000000",
            "type": "toll"
          }
        ],
        "breakout_room": {
          "enable": False,
          "rooms": [
            {
              "name": "room1",
              "participants": [
                "james.user01@somemail1234.com",
                "james.user02@somemail1234.com"
              ]
            },
            {
              "name": "room2",
              "participants": [
                "james.user03@somemail1234.com"
              ]
            }
          ],
          "host_video": False,
          "in_meeting": True,
          "join_before_host": True,
          "mute_upon_entry": False,
          "participant_video": False,
          "registrants_confirmation_email": True,
          "use_pmi": False,
          "waiting_room": False,
          "watermark": True,
          "registrants_email_notification": True
        },
        "start_time": "2019-08-30T22:00:00Z",
        "start_url": "https://zoom.us/s/1100000?iIifQ.wfY2ldlb82SWo3TsR77lBiJjR53TNeFUiKbLyCvZZjw",
        "status": "waiting",
        "timezone": "America/New_York",
        "topic": "API Test",
        "type": 2,
        "uuid": "ng1MzyWNQaObxcf3+Gfm6A=="
        }
        }
                self.meetingdetails = {"topic": "The title of your zoom meeting",
                          "type": 2,
                          "start_time": "2019-06-14T10: 21: 57",
                          "duration": "45",
                          "timezone": "Europe/Madrid",
                          "agenda": "test",

                          "recurrence": {"type": 1,
                                         "repeat_interval": 1
                                         },
                          "settings": {"host_video": "true",
                                       "participant_video": "true",
                                       "join_before_host": "False",
                                       "mute_upon_entry": "False",
                                       "watermark": "true",
                                       "audio": "voip",
                                       "auto_recording": "cloud"
                                       }
                          }

        # create a function to generate a token using the pyjwt library
        def generateToken(self):
                API_KEY = 'bXma3X3lTDSMO88IS3UnjA'
                API_SEC = 'Si93k5jKOy2oHoT8ZaHZWKXpwoHw4CMt'
                token = jwt.encode(
                    # Create a payload of the token containing API Key & expiration time
                    {'iss': API_KEY, 'exp': time() + 5000},
                    # Secret used to generate token signature
                    API_SEC,
                    # Specify the hashing alg
                    algorithm='HS256'
                    # Convert token to utf-8
                )
                return 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IjhYQXc1aDhvUlNDWldnTG1oVV9MMmciLCJleHAiOjE3NjU1Njk1NDAsImlhdCI6MTY1MDUwNTYwNn0.WYJU2AJSvRMiXDJ8PIz5EAsMuBKtuc-0aw0zqQDludQ'
        # send a request with headers including a token

        #fetching zoom meeting info now of the user, i.e, YOU
        def getUsers(self):
                headers = {'authorization': 'Bearer %s' % self.generateToken(),
                          'content-type': 'application/json'}

                r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
                print("\n fetching zoom meeting info now of the user ... \n")
                print(r.text)


        #fetching zoom meeting participants of the live meeting

        def getMeetingParticipants(self):
                headers = {'authorization': 'Bearer %s' % self.generateToken(),
                          'content-type': 'application/json'}
                r = requests.get(
                    f'https://api.zoom.us/v2/metrics/meetings/{self.meetingId}/participants', headers=headers)
                print("\n fetching zoom meeting participants of the live meeting ... \n")

                # you need zoom premium subscription to get this detail, also it might not work as i haven't checked yet(coz i don't have zoom premium account)

                print(r.text)
                return r


        # this is the json data that you need to fill as per your requirement to create zoom meeting, look up here for documentation
        # https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate

        def createMeeting(self):
                headers = {'authorization': 'Bearer %s' % self.generateToken(),
                          'content-type': 'application/json'}
                r = requests.post(
                    f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(self.meetingdetails))

                print("\n creating zoom meeting ... \n")
                print(r.text)
                return r

        def getStat(self):
                headers = {'authorization': 'Bearer %s' % self.generateToken(),
                          'content-type': 'application/json'}

                r=requests.get(f'https://api.zoom.us/v2/meetings/{self.meetingId}', headers=headers,data=json.dumps(self.meetingdetails)) 
                #print(r.text) 
                return r


if __name__ == '__main__':

        c=zoom(Key='kdjfldkajf',Sec='dkjflkdja')
        c.getUsers()
              # getMeetingParticipants()
        c.createMeeting()
