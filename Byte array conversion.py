#Put data class

#Original:

def PutData(self,s):
    split_string = list(s)
    string_length = len(s)
    array = []
    for i in range(0, string_length):
        pointer = ord(split_string[i])
        array.append(pointer)
    byte_array = bytearray(array)
    print(byte_array)
    #self.LCDs.write(byte_array)
    pass

def Skip():
    pass

#Change funtion into its own class
#Import s into put data class
#Return byte_array variable to write data

#(In Write data)

class PutData():
    def __init__(self, s):
        self.s = s
        
    def ConvertData(self):
        split_string = list(self.s)
        string_length = len(self.s)
        array = []
        for i in range(0, string_length):
            pointer = ord(split_string[i])
            array.append(pointer)
        byte_array = bytearray(array)
        print(byte_array)
        return self.s

class test():
    def __init__(self):
        self.s = "Hello"

    def GetData(self):
        print("Hi")
        print(self.s)
        putdata = PutData(self.s)
        message = putdata.ConvertData()
        print(message)

testing = test()
testing.GetData()
    
