
from ast import While
from main import zoom
import json
import serial
import serial 
import time
import playsound
import os

arddata=serial.Serial('COM3',9600)
condition=True


def main():
    flag=0 
    a=zoom(Key='khaled',Sec='kkk')
    roaster=['Adnan Khan','khaled dawoud']
    print(type(a))
    play_one=True
    # b=a.createMeeting()

    # res = json.loads(b.text)
    # print(res.get('status'))
    # print(res.get('in_meeting'))
    # print(res.get('id'))

    b1=a.getStat()
    r = json.loads(b1.text)
    print(r.get('status'))
    print(r.get('in_meeting'))
    print(r.get('id'))
    print(r.get("start_url"))
    print(r.get("join_url"))
    a.getMeetingParticipants()

    
    while condition:
        
        b1=a.getStat()
        r = json.loads(b1.text)
        if r.get('status') == 'started':
            # H Lamp On and Lamp off
            c1=a.getMeetingParticipants()
            d=json.loads(c1.text)
            out_list=d.get('participants')
            a_key="user_name"
            if out_list:
                values_of_key=[a_dict[a_key] for a_dict in out_list]
                values_of_key = list(dict.fromkeys(values_of_key))

                answer=check_if_equal(roaster,values_of_key)
                if answer:
                    print("hi")
                    if play_one:
                        #audio_file = os.path.dirname(__file__) + '/start.mp3'
                        playsound.playsound('start.mp3')

                        play_one= False

                    arddata.write(b'K')

                else:
                    arddata.write(b'H')



            
        elif r.get('status') =='waiting':
            arddata.write(b'A') # Turn On the fan
            flag=0

            
def check_if_equal(list_1, list_2):
    """ Check if both the lists are of same length and if yes then compare
    sorted versions of both the list to check if both of them are equal
    i.e. contain similar elements with same frequency. """
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

            


        
if __name__ == '__main__':
    main()





