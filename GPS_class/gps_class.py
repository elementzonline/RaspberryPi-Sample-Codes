import serial
import string


class gps():
    """
    --  Source code developed by Dhanish -- Elementz Engineers Guild Pvt Ltd
    --  Released under General Public Licence
    --  Checked using SkyTrack GPS
    """

    # This dict holds the global parsed data
    data = {}

    def __init__(self, ser):
        """
        :param ser: represents the serial object passed
        :return: None
        """
        self.ser = ser


    def toDecimalDegrees(self, ddmm):
        """
        Converts a string from ddmm.mmmm or dddmm.mmmm format
        to a float in dd.dddddd format
        """

        splitat = string.find(ddmm, '.') - 2
        return self._float(ddmm[:splitat]) + self._float(ddmm[splitat:]) / 60.0


    def _float(self, s):
        """
        Returns the float value of string s if it exists,
        or None if s is an empty string.
        """
        if s:
            return float(s)
        else:
            return None


    def _int(self, s):
        """
        Returns the int value of string s if it exists,
        or None if s is an empty string.
        """
        if s:
            return int(s)
        else:
            return None


    def calcCheckSum(self, line):
        """
        Returns the checksum as a one byte integer value.
        In this case the checksum is the XOR of everything after '$' and before '*'.
        """
        s = 0
        for c in line[1:-3]:
            s = s ^ ord(c)
        return s


    def parseRMC(self, fields):
        """
        Parses the Recommended Minimum Specific GNSS Data sentence fields.
        Stores the results in the global data dict.

        """

        # RMC has 12 fields
        assert len(fields) == 13

        # MsgId = fields[0]
        gps.data['UtcTime'] = fields[1]
        gps.data['RmcStatus'] = fields[2]
        gps.data['Latitude'] = self.toDecimalDegrees(fields[3])
        gps.data['NsIndicator'] = fields[4]
        gps.data['Longitude'] = self.toDecimalDegrees(fields[5])
        gps.data['EwIndicator'] = fields[6]
        gps.data['SpeedOverGround'] = self._float(fields[7])
        gps.data['CourseOverGround'] = self._float(fields[8])
        gps.data['Date'] = fields[9]
        gps.data['MagneticVariation'] = fields[10]
        gps.data['UnknownEmptyField'] = fields[11]
        gps.data['RmcMode'] = fields[11]

        # Attend to lat/lon plus/minus signs
        if gps.data['NsIndicator'] == 'S':
            gps.data['Latitude'] *= -1.0
        if gps.data['EwIndicator'] == 'W':
            gps.data['Longitude'] *= -1.0


    def parseLine(self, line):
        """
        Parses an NMEA sentence, sets fields in the global structure.
        Raises an AssertionError if the checksum does not validate.
        Returns the type of sentence that was parsed.
        """

        # Get rid of the \r\n if it exists
        line = line.rstrip()

        # Validate the sentence using the checksum
        assert self.calcCheckSum(line) == int(line[-2:], 16)

        # Pick the proper parsing function
        parseFunc = {
            "$GPRMC": self.parseRMC,
        }[line[:6]]

        # Call the parser with fields split and the tail chars removed.
        # The characters removed are the asterisk, the checksum (2 bytes) and \n\r.
        parseFunc(string.split(line[:-3], ','))

        # Return the type of sentence that was parsed
        return line[3:6]


    def getField(self, fieldname):
        """
        Returns the value of the named field.
        """
        return gps.data[fieldname]


    def readGPS(self):
        """
        Returns  GPS lattitude, longitude, date, time
        """
        gps_buf = ''

        while (gps_buf.find('$GPRMC') == -1):
            gps_buf = self.ser.readline()

        # print(gps_buf)
        self.parseLine(gps_buf)

        return gps.data['Latitude'], gps.data['Longitude'], gps.data['Date'], gps.data['UtcTime']


if __name__ == "__main__":

    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, timeout=None,
                        xonxoff=False, rtscts=False,
                        writeTimeout=None, dsrdtr=False,
                        interCharTimeout=None)

    gps_ser = gps(ser)
    while (True):
        print gps_ser.readGPS()


            
            
        