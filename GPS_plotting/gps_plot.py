import serial
import pygmaps 
from time import sleep

import string


# This dict holds the global parsed data
data = {}


def toDecimalDegrees(ddmm):
    """
    Converts a string from ddmm.mmmm or dddmm.mmmm format
    to a float in dd.dddddd format
    """

    splitat = string.find(ddmm, '.') - 2
    return _float(ddmm[:splitat]) + _float(ddmm[splitat:]) / 60.0


def _float(s):
    """
    Returns the float value of string s if it exists,
    or None if s is an empty string.
    """
    if s:
        return float(s)
    else:
        return None


def _int(s):
    """
    Returns the int value of string s if it exists,
    or None if s is an empty string.
    """
    if s:
        return int(s)
    else:
        return None


def calcCheckSum(line):
    """
    Returns the checksum as a one byte integer value.
    In this case the checksum is the XOR of everything after '$' and before '*'.
    """
    s = 0
    for c in line[1:-3]:
        s = s ^ ord(c)
    return s





def parseRMC(fields):
    """
    Parses the Recommended Minimum Specific GNSS Data sentence fields.
    Stores the results in the global data dict.

    """

    # RMC has 12 fields
    assert len(fields) == 13

    # MsgId = fields[0]
    data['UtcTime'] = fields[1]
    data['RmcStatus'] = fields[2]
    data['Latitude'] = toDecimalDegrees(fields[3])
    data['NsIndicator'] = fields[4]
    data['Longitude'] = toDecimalDegrees(fields[5])
    data['EwIndicator'] = fields[6]
    data['SpeedOverGround'] = _float(fields[7])
    data['CourseOverGround'] = _float(fields[8])
    data['Date'] = fields[9]
    data['MagneticVariation'] = fields[10]
    data['UnknownEmptyField'] = fields[11]
    data['RmcMode'] = fields[11]

    # Attend to lat/lon plus/minus signs
    if data['NsIndicator'] == 'S':
        data['Latitude'] *= -1.0
    if data['EwIndicator'] == 'W':
        data['Longitude'] *= -1.0



def parseLine(line):
    """
    Parses an NMEA sentence, sets fields in the global structure.
    Raises an AssertionError if the checksum does not validate.
    Returns the type of sentence that was parsed.
    """

    # Get rid of the \r\n if it exists
    line = line.rstrip()

    # Validate the sentence using the checksum
    assert calcCheckSum(line) == int(line[-2:], 16)

    # Pick the proper parsing function
    parseFunc = {
        "$GPRMC": parseRMC,
        }[line[:6]]

    # Call the parser with fields split and the tail chars removed.
    # The characters removed are the asterisk, the checksum (2 bytes) and \n\r.
    parseFunc(string.split(line[:-3], ','))

    # Return the type of sentence that was parsed
    return line[3:6]


def getField(fieldname):
    """
    Returns the value of the named field.
    """
    return data[fieldname]

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS, 
                   parity=serial.PARITY_NONE, 
                   stopbits=serial.STOPBITS_ONE, timeout=None, 
                   xonxoff=False, rtscts=False, 
                   writeTimeout=None, dsrdtr=False, 
                   interCharTimeout=None)
path = []
j=0
while(True):
    sleep(5)
    i=0
    j=j+1
    #time_buffer = ''
    lat_buffer = ''
    long_buffer = ''
    gps_buf = ser.readline()
    #gps_buf = '$GPRMC,001225,A,0008.491,N,00076.942,E,12,25,251211,1.2,E,A*03'
    #gps_buf = '$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A'
    #gps_buf = '$GPRMC,092204.999,A,0829.4989,N,07656.6084,E,0.00,89.68,211200,,A*25'
    if(gps_buf.find('$GPRMC') != -1):
        #print(gps_buf)
        parseLine(gps_buf)
        print(data['Latitude'])
        print(data['Longitude'])        
        #path.append( (data['Latitude'],data['Longitude']+(j*0.001)))
        path.append( (data['Latitude'],data['Longitude']))
        location = path[:]
        mymap = pygmaps.maps(data['Latitude'], data['Longitude'], 15)
        mymap.addpoint(data['Latitude'], data['Longitude'], "#0000FF")
        mymap.addpath(location,"#00FF00")
        mymap.draw('./mymap.html')
            
            
        