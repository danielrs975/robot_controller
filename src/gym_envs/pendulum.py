import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path
#Pooja BELURE added this library
import face_recognition
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path
#Pooja BELURE
from PIL import Image
import cv2
face_detector=cv2.CascadeClassifier('C:/Users/hp/Desktop/stage/haarcascade_frontalface_default.xml')
path = 'D:\\Stage\\Pendulum\\nature.png'
ncol=200
nrow=200
ncolreal=5
square_size=40
step_size=5
targetx= 16
targety=16
nA=4
#Pooja BELURE Global parameter for height and width of DLink camera
w = 0
h = 0
#nS= int( ncol/square_size*(ncol/square_size))
nS=int((ncol-square_size)/step_size)*int((nrow-square_size)/step_size)
#HA 14 Mars 2020 partie pour appeler un backend extÃ©rieur
import requests
import logging
import cv2
import dlib
from datetime import datetime
import time

host='192.168.0.20'
user='admin'
password='123456'
precision = [40,40]
trackingFace=0
first_frame=True
largeur_capture=ncol
hauteur_capture=nrow
def backendcontrol (s,a,r):
    newaction=a
    newreward=ra
    DlinkDCSCamera.camera_move()
    newreward=ra
    if newreward == 1:
        print("changed")
    else:
        print("unchanged")
    newstep =s
    return(newstep,newaction,newreward)

final_x = 16
final_y= 16    #postions souhaitées de la cible
class DlinkDCSCamera(object):
    """DLINK DCS IP Camera Control."""

    DAY_NIGHT_AUTO = '0'
    DAY_NIGHT_MANUAL = '1'
    DAY_NIGHT_ALWAYS_DAY = '2'
    DAY_NIGHT_ALWAYS_NIGHT = '3'
    DAY_NIGHT_SCHEDULE = '4'

    DAY_NIGHT_LIGHT_SENSOR_LOW = '1'
    DAY_NIGHT_LIGHT_SENSOR_MEDIUM = '3'
    DAY_NIGHT_LIGHT_SENSOR_HIGH = '5'

    MOTION_DETECTION_ALWAYS = '0'
    MOTION_DETECTION_SCHEDULE = '1'

    SOUND_DETECTION_ALWAYS = '0'
    SOUND_DETECTION_SCHEDULE = '1'

    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 4
    WEDNESDAY = 8
    THURSDAY = 16
    FRIDAY = 32
    SATURDAY = 64

    FTP_MODE_ALWAYS = 0
    FTP_MODE_SCHEDULE = 1
    FTP_MODE_DETECTION = 2

    FRAMES_PER_SECOND = 0
    SECONDS_PER_FRAME = 1

    UPLOAD_FILE_MODE_OVERWRITE = 0
    UPLOAD_FILE_MODE_DATETIME = 1
    UPLOAD_FILE_MODE_SEQUENCE = 3

    UPLOAD_CREATE_FOLDER_OFF = 0
    UPLOAD_CREATE_FOLDER_HOURLY = 60
    UPLOAD_CREATE_FOLDER_DAILY = 1440

     
    largeur_capture=0
    hauteur_capture=0

    
    def __init__(self, host, user, password, port=80):
        """Initialize with the IP camera connection settings."""
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        #self.first_frame =first_frame
        self.trackingFace=trackingFace
        self.largeur_capture=largeur_capture
        self.hauteur_capture=hauteur_capture
        tracker = dlib.correlation_tracker()

    def send_command(self, cmd, params={}):
        """Send a control command to the IP camera."""
        _url = 'http://%s:%d/%s' % (self.host, self.port, cmd)
        r = requests.get(_url, auth=(self.user, self.password), params=params)
        log = logging.getLogger("DlinkDCSCamera.send_command")
        log.debug(r.request.url)
        return self.unmarshal_response(r.content.decode('utf-8'))

    def unmarshal_response(self, response):
        """Unmarshal the multiline key value pair response."""
        _obj = {}
        for line in response.splitlines():
            # ignore blank lines and xml <result> block
            if line != '' and not line.startswith('<'):
                _keyvalue = line.strip().split("=")
                _obj[_keyvalue[0]] = _keyvalue[1]
        return _obj

    def time_to_string(self, time):
        """Conert a datetime into the HH:MM:SS string format."""
        return datetime.strftime(time, '%H:%M:%S')

    # GETTERS

    def get_cgi_version(self):
        """Get IP Camera CGI version."""
        return self.send_command('cgiversion.cgi')

    def get_common_info(self):
        """Get IP Camera Information."""
        return self.send_command('common/info.cgi')

    def get_date_time(self):
        """Get IP Camera Data Time settings."""
        return self.send_command('datetime.cgi')

    def get_day_night(self):
        """Get the IP Camera Day Night Mode settings."""
        return self.send_command('daynight.cgi')

    def get_email(self):
        """Get the IP Camera Email notification settings."""
        return self.send_command('email.cgi')

    def get_iimage(self):
        """Get the IP Camera Image information."""
        return self.send_command('iimage.cgi')

    def get_image(self):
        """Get the IP Camera Image information."""
        return self.send_command('image.cgi')

    def get_inetwork(self):
        """Get the IP Camera Network information."""
        return self.send_command('inetwork.cgi')

    def get_isystem(self):
        """Get the IP Camera System information."""
        return self.send_command('isystem.cgi')

    def get_iwireless(self):
        """Get the IP Camera Wireless information."""
        return self.send_command('iwireless.cgi')

    def get_motion_detection(self):
        """Get the IP Camera Motion Detection settings."""
        return self.send_command('motion.cgi')

    def get_network(self):
        """Get the IP Camera Network settings."""
        return self.send_command('network.cgi')

    def get_ptz(self):
        """Get the IP Camera Network Pan Tilt Zoom."""
        return self.send_command('config/ptz_move.cgi')

    def get_ptz_presets(self):
        """Get the IP Camera Network Pan Tilt Zoom Preset List"""
        return self.send_command('config/ptz_preset_list.cgi')

    def get_sound_detection(self):
        """Get the IP Camera Sound Detection settings."""
        return self.send_command('sdbdetection.cgi')

    def get_stream_info(self):
        """Get the IP Camera Video stream info."""
        return self.send_command('config/stream_info.cgi')

    def get_upload(self):
        """Get the IP Camera FTP Upload settings."""
        return self.send_command('upload.cgi')

    def get_user(self):
        """Get the IP Camera user setttings."""
        return self.send_command('user.cgi')

    def get_user_list(self):
        """Get the list of IP Camera users."""
        return self.send_command('userlist.cgi')

    # SETTERS

    def set_day_night(self, mode):
        """
        Set the IP Camera Day Night Mode.
        mode -- one of DAY_NIGHT_AUTO, DAY_NIGHT_MANUAL, DAY_NIGHT_ALWAYS_DAY,
                DAY_NIGHT_ALWAYS_NIGHT, or DAY_NIGHT_SCHEDULE.
        """
        _params = {
            'DayNightMode': int(mode),
            'ConfigReboot': 'no',
        }
        return self.send_command('daynight.cgi', _params)

    def set_day_night_sensor(self, light_sensor_control):
        """
        Set the IP Camera Day Night light lensor control.
        light_sensor_control -- one of DAY_NIGHT_LIGHT_SENSOR_LOW,
                                DAY_NIGHT_LIGHT_SENSOR_MEDIUM
                                DAY_NIGHT_LIGHT_SENSOR_HIGH
        """
        _params = {
            'LightSensorControl': light_sensor_control,
            'ConfigReboot': 'no',
        }
        return self.send_command('daynight.cgi', _params)

    
    

    def set_motion_detection(self, enable):
        """Enable or Disable IP Camera Motion Detection."""
        _params = {
            'MotionDetectionEnable': ('1' if enable else '0'),
            'ConfigReboot': 'no',
        }
        return self.send_command('motion.cgi', _params)

    def set_motion_detection_sensitivity(self, sensitivity):
        """Set the IP Camera Motion Detection Sensitivity."""
        _params = {
            'MotionDetectionSensitivity': str(sensitivity),
            'ConfigReboot': 'no',
        }
        return self.send_command('motion.cgi', _params)

    def set_motion_detection_blockset(self, blockset):
        """
        Set the IP Camera Motion Detection Blockset mask.
        blockset -- a 5x5 bitmask of enabled motion capture cells e.g.
                    1111100000111110000011111
        """
        _params = {
            'MotionDetectionBlockSet': blockset,
            'ConfigReboot': 'no',
        }
        return self.send_command('motion.cgi', _params)

    def set_motion_detection_mode(self, mode):
        """
        Set the IP Camera Motion Detection mode.
        mode -- one of MOTION_DETECTION_ALWAYS or MOTION_DETECTION_SCHEDULE
        """
        _params = {
            'MotionDetectionScheduleMode': int(mode),
            'ConfigReboot': 'no',
        }
        return self.send_command('motion.cgi', _params)

    def set_motion_detection_schedule(self, schedule_days,
                                      schedule_start, schedule_stop):
        """
        Set the IP Camera Motion Detection Schedule.
        Effective when Motion Detection mode is MOTION_DETECTION_SCHEDULE
        schedule_days -- value representing scheduled days (1..127)
                         e.g. schedule_days = MONDAY + WEDNESDAY + FRIDAY
        schedule_start -- daily start time in the format 'HH:MM:SS'
        schedule_stop -- daily stop time in the format 'HH:MM:SS'
        """
        _params = {
            'MotionDetectionScheduleDay': int(schedule_days),
            'MotionDetectionScheduleTimeStart': schedule_start,
            'MotionDetectionScheduleTimeStop': schedule_stop,
            'ConfigReboot': 'no',
        }
        return self.send_command('motion.cgi', _params)


    def set_ptz(self, pan=167, tilt=25, zoom=0):
        """
        Set the IP Camera Pan Tilt Zoom location.
        pan -- 0 to 336 (default: 167)
        tile -- 0 to 106 (default: 25)
        zoom --
        """
        _params = {
            'p': int(pan),
            't': int(tilt),
            'z': int(zoom),
        }
        return self.send_command('config/ptz_move.cgi', _params)

    def set_ptz_move(self, x, y):
        """Move the IP Camera Pan Tilt Zoom location."""
        _params = {
            'command': 'set_relative_pos',
            'posX': int(x),
            'posY': int(y),
        }
        return self.send_command('cgi/ptdc.cgi', _params)

    def set_ptz_move_preset(self, preset):
        """Move the IP Camera to a Preset Pan Tilt Zoom location."""
        _params = {
            'PanTiltPresetPositionMove': preset,
        }
        return self.send_command('pantiltcontrol.cgi', _params)

    def set_sound_detection(self, enable):
        """Enable or Disable the IP Camera Sound Detection."""
        _params = {
            'SoundDetectionEnable': ('1' if enable else '0'),
            'ConfigReboot': 'no',
        }
    def set_sound_detection(self, enable):
        """Enable or Disable the IP Camera Sound Detection."""
        _params = {
            'SoundDetectionEnable': ('1' if enable else '0'),
            'ConfigReboot': 'no',
        }
        return self.send_command('sdbdetection.cgi', _params)

    def set_sound_detection_sensitivity(self, decibels):
        """
        Set the IP Camera Sound Detection sensitivity.
        decibels - the number of decibels required to trigger sound detection,
                   in the range 50..90
        """
        _params = {
            'SoundDetectionDB': str(decibels),
            'ConfigReboot': 'no',
        }
        return self.send_command('sdbdetection.cgi', _params)

    def set_sound_detection_mode(self, mode):
        """
        Set the IP Camera Sound Detection mode.
        mode -- one of SOUND_DETECTION_ALWAYS or SOUND_DETECTION_SCHEDULE
        """
        _params = {
            'SoundDetectionScheduleMode': int(mode),
            'ConfigReboot': 'no',
        }
        return self.send_command('sdbdetection.cgi', _params)

    def set_sound_detection_schedule(self, schedule_days,
                                     schedule_start, schedule_stop):
        """
        Set the IP Camera Sound Detection Schedule.
        Effective when Sound Detection mode is SOUND_DETECTION_SCHEDULE
        schedule_days -- value representing scheduled days (1..127)
                         e.g. schedule_days = MONDAY + WEDNESDAY + FRIDAY
        schedule_start -- daily start time in the format 'HH:MM:SS'
        schedule_stop -- daily stop time in the format 'HH:MM:SS'
        """
        _params = {
            'SoundDetectionScheduleDay': int(schedule_days),
            'SoundDetectionScheduleTimeStart': schedule_start,
            'SoundDetectionScheduleTimeStop': schedule_stop,
            'ConfigReboot': 'no',
        }
        return self.send_command('sdbdetection.cgi', _params)

    def set_upload_server(self, host, user, password, path='/',
                          passive=True, port=21):
        """
        Set the IP Camera FTP upload server settings.
        host -- FTP server hostname
        user -- FTP server user
        psasword -- FTP server password
        path -- FTP server upload path (default '/')
        passive -- Passive mode (deafault True)
        port -- FTP server port (default 21)
        """
        _params = {
            'FTPHostAddress': host,
            'FTPUserName': user,
            'FTPPassword': password,
            'FTPDirectoryPath': path,
            'FTPPortNumber': int(port),
            'FTPPassiveMode': ('1' if passive else '0'),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_image(self, enable):
        """Enable or Disable Image upload."""
        _params = {
            'FTPScheduleEnable': ('1' if enable else '0'),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_image_mode(self, mode):
        """
        Set the IP Camera image upload mode.
        mode -- one of FTP_MODE_ALWAYS, FTP_MODE_SCHEDULE, FTP_MODE_DETECTION
        """
        _params = {
            'FTPScheduleMode': int(mode),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_image_settings(self,
                                  filename='image',
                                  filename_mode=1,
                                  max_file_sequence_number=1024,
                                  create_subfolder_minutes=0,
                                  frequency_mode=0,
                                  frames_per_second=-1,
                                  seconds_per_frame=1):
        """
        Set the IP Camera upload image settings.
        filename -- base file name
        filename_mode -- UPLOAD_FILE_MODE_OVERWRITE, UPLOAD_FILE_MODE_DATETIME
                         or UPLOAD_FILE_MODE_SEQUENCE
        max_file_sequence_number -- maxamum sequence number if mode is
                                    UPLOAD_FILE_MODE_SEQUENCE
        create_subfolder_minutes -- create date/time subfolders
        frequency_mode -- FRAMES_PER_SECONDS or SECONDS_PER_FRAME
        frames_per_second -- frames (images) per second (1..3), use -1 for Auto
        seconds_per_frame -- seconds between frames
        """
        _params = {
            'FTPScheduleVideoFrequencyMode': int(frequency_mode),
            'FTPScheduleFramePerSecond': int(frames_per_second),
            'FTPScheduleSecondPerFrame': int(seconds_per_frame),
            'FTPScheduleBaseFileName': filename,
            'FTPScheduleFileMode': int(filename_mode),
            'FTPScheduleMaxFileSequenceNumber': int(max_file_sequence_number),
            'FTPCreateFolderInterval': int(create_subfolder_minutes),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_image_schedule(self,
                                  schedule_days=0,
                                  schedule_start='00:00:00',
                                  schedule_stop='00:00:00'):
        """
        Set the IP Camera upload image schedule.
        These settings are used if mode is FTP_MODE_SCHEDULE
        schedule_days -- value representing scheduled days (1..127)
                         e.g. schedule_days = MONDAY + WEDNESDAY + FRIDAY
        schedule_start -- daily start time in the format 'HH:MM:SS'
        schedule_stop -- daily end time in the format 'HH:MM:SS'
        """
        _params = {
            'FTPScheduleDay': schedule_days,
            'FTPScheduleTimeStart': schedule_start,
            'FTPScheduleTimeStop': schedule_stop,
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_video(self, enable):
        """Enable or Disable Video upload."""
        _params = {
            'FTPScheduleEnableVideo': ('1' if enable else '0'),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_video_settings(self, filename='video',
                                  file_limit_size=2048,
                                  file_limit_time=10):
        """
        Set the IP Camera upload video file settings.
        filename -- base file name
        file_limit_size -- video file size KBytes
                           (default is 2048, max is 3072 KBytes)
        file_limit_time -- video file lenght in seconds
                           (default is 10, max is 15 seconds)
        """
        _params = {
            'FTPScheduleBaseFileNameVideo': filename,
            'FTPScheduleVideoLimitSize': int(file_limit_size),
            'FTPScheduleVideoLimitTime': int(file_limit_time),
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_video_mode(self, mode):
        """
        Set the IP Camera upload video mode.
        mode -- one of FTP_MODE_ALWAYS, FTP_MODE_SCHEDULE, FTP_MODE_DETECTION
        """
        _params = {
            'FTPScheduleModeVideo': mode,
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    def set_upload_video_schedule(self, schedule_days=0,
                                  schedule_start='00:00:00',
                                  schedule_stop='00:00:00'):
        """
        Set the IP Camera upload video schedule.
        These settings are used if mode is FTP_MODE_SCHEDULE
        schedule_days -- value representing scheduled days (1..127)
                         e.g. schedule_days = MONDAY + WEDNESDAY + FRIDAY
        schedule_start -- daily start time in the format 'HH:MM:SS'
        schedule_stop -- daily end time in the format 'HH:MM:SS'
        """
        _params = {
            'FTPScheduleDayVideo': schedule_days,
            'FTPScheduleTimeStartVideo': schedule_start,
            'FTPScheduleTimeStopVideo': schedule_stop,
            'ConfigReboot': 'no',
        }
        return self.send_command('upload.cgi', _params)

    # HELPERS

    

    def disable_motion_detection(self):
        """Disable motion detection."""
        return self.set_motion_detection(False)

    def disable_sound_detection(self):
        """Disable sound detection."""
        return self.set_sound_detection(False)

    def disable_upload_image(self):
        """Disable image upload."""
        return self.set_upload_image(False)

    def disable_upload_video(self):
        """Disable video upload."""
        return self.set_upload_video(False)

    

    def enable_motion_detection(self):
        """Enable motion detection."""
        return self.set_motion_detection(True)

    def enable_sound_detection(self):
        """Enable sound detection."""
        return self.set_sound_detection(True)

    def enable_upload_image(self):
        """Enable image upload."""
        return self.set_upload_image(True)

    def enable_upload_video(self):
        """Enable video upload."""
        return self.set_upload_video(True)

    def camera_move_right(self):
        """Move the IP Camera Pan Tilt Zoom location."""
        _params = {
            'command': 'set_relative_pos',
            'posX': int(10),
            'posY': 0,
            
        }
        return self.send_command('cgi/ptdc.cgi', _params)

    def camera_move_left(self):
        """Move the IP Camera Pan Tilt Zoom location."""
        _params = {
            'command': 'set_relative_pos',
            'posX': int(-10),
            'posY': 0,
            
        }
        return self.send_command('cgi/ptdc.cgi', _params)
    # Pooja BELURE added the code for moving camera up and down.
    def camera_move_up(self):
        """Move the IP Camera Pan Tilt Zoom location."""
        _params = {
            'command': 'set_relative_pos',
            'posX': 0,
            'posY': int(10),
            
        }
        return self.send_command('cgi/ptdc.cgi', _params)
    # Pooja BELURE added the code for moving camera up and down.
    def camera_move_down(self):
        """Move the IP Camera Pan Tilt Zoom location."""
        _params = {
            'command': 'set_relative_pos',
            'posX': 0,
            'posY': int(-10),
            
        }
        return self.send_command('cgi/ptdc.cgi', _params)
# Global function for initializing camera #Pooja BELURE
camera = DlinkDCSCamera(host = host, user = user, password = password)      
def camera_initialization(camera):
        camera.set_ptz()
        #for testing qll the sequence , camera plus image detection
        camera.set_day_night(2)
        capture = cv2.VideoCapture('http://admin:123456@192.168.0.20:80/video/mjpg.cgi?profileid=1')
        largeur_capture=capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        hauteur_capture=capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        face_detector=cv2.CascadeClassifier('C:/Users/hp/Desktop/stage/haarcascade_frontalface_default.xml')
        precision = [40,40]
        face_move =  True
        print("face_detector",face_detector)
        capture = cv2.VideoCapture('http://admin:123456@192.168.0.20:80/video/mjpg.cgi?profileid=1')
        r, f = capture.read()
        image = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        cv2.imshow('image',image)
        #cv2.waitKey(0) # to wait infinitely an keyboard even to kill the image.
        cv2.destroyAllWindows()
        #camera.camera_move_right()
        return camera
camera=camera_initialization(camera)

# Another global routine to capture image and face detection to return face co-ordinates of the square. # Pooja BELURE
def capture_image_face_detect_dlink(camera) :
    top    = 0
    right  = 0
    bottom = 0
    left   = 0
    capture = cv2.VideoCapture('http://admin:123456@192.168.0.20:80/video/mjpg.cgi?profileid=1')
    r, frame = capture.read()
    w = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print("========frame.size============",frame.size,type(frame.size),w,h)
    #sqrWidth = np.ceil(np.sqrt(w*h)).astype(int)
    #frame_1 = cv2.resize(frame, (sqrWidth,sqrWidth), interpolation = cv2.INTER_AREA)
    #cv2.imwrite('D:\Stage\out.jpg',frame_1)
    #cv2.imshow("resized", frame)
    rgb_frame = frame[:, :, ::-1]
    #cv2.imshow("rgb_frame", rgb_frame)
    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    print(face_locations)
    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
    # Display the resulting image
    cv2.imshow('image', frame)

    # Hit 'q' on the keyboard to quit!
    cv2.waitKey(0)
    # Release handle to the webcam
    capture.release()
    cv2.destroyAllWindows()
    if right!=0 and bottom!=0 :
        return (left, top), (right, bottom),1,w,h
    else :
        return (0,0), (0,0),0,w,h

#Pooja BELURE: routine for the downscaling resolution of dlink camera
def downscale_Dlink(DlinkX,DlinkY,FaceX,FaceY,DlinkSqSize,StateX,StateY,NeuSqSize) :
    print("Inside downscale_dlink")
    print("DlinkX",DlinkX,"DlinkY",DlinkY,"FaceX",FaceX,"FaceY",FaceY,"DlinkSqSize",DlinkSqSize,"StateX",StateX,"StateY",StateY,"NeuSqSize",NeuSqSize)
    FaceX_D = (FaceX*StateX)/DlinkX
    FaceY_D = (FaceY*StateY)/DlinkY
    SqSize_D = (DlinkSqSize*NeuSqSize)/DlinkX
    print("FaceX_D:",FaceX_D,"FaceY_D:",FaceY_D,"SqSize_D",SqSize_D)
    return FaceX_D,FaceY_D,SqSize_D
        
class PendulumEnv(gym.Env):

    metadata = {

        'render.modes': ['human', 'rgb_array'],

        'video.frames_per_second': 30

    }
    position_x=10
    position_y=10
    ncol=ncol
    nrow=nrow
    step_size=step_size
    def __init__(self, g=10.0):

        self.max_speed = 8

        self.state = 0

        self.dt = .05

        # self.x = 0

        # self.y = 0

        self.l = 1.

        self.viewer = None
        
        self.reward_range = (0, 1)

        high = np.array([1., 1., self.max_speed], dtype=np.float32)
        P = {s : {a : [] for a in range(nA)} for s in range(nS)}
         

        self.observation_space = spaces.Box(

            low=-high,

            high=high,

            dtype=np.float32

        )



        self.seed()

    # def pos_to_state(self,row,col):
        #print("pos to state row",row,"col",col,row*(self.ncol-square_size)/step_size + col)
        # return int(row*(self.ncol-square_size)/step_size + col)
    def in_range(self,x,y,z):
        if x>y-z and x<y+z:  
            return(True)
        return(False)
    def pos_to_state(self,row,col):
        new_col=int(col/step_size)
        new_row=int(row/step_size)
        #print("pos to state row",row,"col",col,row*(self.ncol-square_size)/step_size + col)
        return int(new_row*((self.ncol-square_size)/step_size) + new_col)
    
    def state_to_pos(self):
        #print("stat to pos",self.state,"x", int(self.state // ((ncol-square_size)/step_size)), "y", int(self.state % ((ncol-square_size)/step_size)))
        return int(step_size*(self.state // ((ncol-square_size)/step_size))), int(step_size*(self.state % ((ncol-square_size)/step_size)))
        

    def seed(self, seed=None):

        self.np_random, seed = seeding.np_random(seed)

        return [seed]

    def target_reached(self,x,y):
        error=50
        if self.in_range(x ,final_x ,error) and self.in_range(y ,final_y ,error):
            return 1
        return 0
    
    # def step(self, u):
        # reward=0
        # done=0
        # x,y=self.state_to_pos()
        # if u==0 :   #right  
            # x = min(x+1,((ncol-square_size)/step_size-1))
        # if u==1 :    #left
            # x= max(x-1,0)
        # if u==2 : # up
            # y= max(y-1,0)
        # if u==3 :   #down  
            # y = min(y+1,(nrow-square_size)/step_size-1)
         
        # if self.target_reached(x,y)==1:
            # done=1
            # reward=1
            # print("target reached")
    
    def step(self, u, ext):
        reward=0
        done=0
        x,y=self.state_to_pos()
#------------- For no external device -------------------------------------#
        if ext==False :
            if u==0 :   #right
                #print("right......................")
                x = min(x+step_size,(ncol-square_size)-1)
            if u==1 :    #left
                x= max(x-step_size,0)
            if u==2 : # up
                y= max(y-step_size,0)
            if u==3 :   #down
                y = min(y+step_size,(nrow-square_size)-1)
         
            if self.target_reached(x,y)==1:
                done=1
                reward=1
                print("target reached")
#------------- For camera as a external device ----------------------------#               
        if ext==True :
            # Calling the Camera: Moving the camera:
                 
            if u==0 :   #Move camera right
                #print("right......................")
                print("Moving Camera Right")
                camera.camera_move_right()
            if u==1 :    #left
                print("Move camera left")
                camera.camera_move_left()
            if u==2 : # up
                #Move Camera Up
                print("Move camera Up")
                camera.camera_move_up()
            if u==3 :   #down
                #Move Camera Down
                print("Move camera Down")
                camera.camera_move_down()
            
            #If the face is recognized , give reward 1, done 1. 
            #Capture image
            (left, top), (right, bottom), ret,w,h= capture_image_face_detect_dlink(camera)
           
            #If face is not recognized, reward == 0, done == 1 (Good bye to episode :))
            if ret==0 :
                print("face is not detected")
                done=1
                reward=0
                #return self.state, reward, done, {}
            else :
                print("face is detected:",(left, top), (right, bottom))
               #Downscale the resolution
                DlinkSqSize=(left-right)*(top-bottom)
                x,y,size_D = downscale_Dlink(w,h,left,top,DlinkSqSize,32,32,1024)
                if self.target_reached(x,y)==1:
                    done=1
                    reward=1
                    #print("Face is recognized")
         
        self.state = self.pos_to_state(x,y)
        #print("step",x,y)
        return self.state, reward, done, {}



    def reset(self):

         

        #self.state = np.random.randint((ncol-square_size)*(nrow-square_size))
        self.state = np.random.randint(int((ncol-square_size)/step_size)*int((nrow-square_size)/step_size))

        self.last_u = None

        return int(self.state)



     

    def render(self, mode='human'):
        image = cv2.imread(path) 
        # Window name in which image is displayed 
        window_name = 'Image'
          
        # Start coordinate, here (5, 5) 
        # represents the top left corner of rectangle 
        x,y=self.state_to_pos()
        start_point = (x, y) 
        #print("step",x,y)
        # Ending coordinate, here (220, 220) 
        # represents the bottom right corner of rectangle 
        end_point = (x+32, y+32) 
          
        # Blue color in BGR 
        color = (255, 0, 0) 
          
        # Line thickness of 2 px 
        thickness = 2
        # Using cv2.rectangle() method 
        # Draw a rectangle with blue line borders of thickness of 2 px 
        image = cv2.rectangle(image, start_point, end_point, color, thickness) 
        #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, image)
        value=5
        #image = cv2.rectangle(image, (int(value),int(value)), end_point, color, thickness) 
        imgcpy=image.copy()
        img = cv2.resize(imgcpy,None,fx=0.5,fy=0.5) 
        cv2.imshow(window_name, image)
        # while True:
            # if cv2.waitKey(0) & 0xFF == ord('q'):
                # break
        # cv2.destroyAllWindows()
        cv2.waitKey(1)
        #cv2.destroyAllWindows()

        return 0



    def close(self):

        if self.viewer:

            self.viewer.close()

            self.viewer = None


# Intitialize Camera and get a global variable camera
# camera=camera_initialization(camera)


def angle_normalize(x):

    return (((x+np.pi) % (2*np.pi)) - np.pi)