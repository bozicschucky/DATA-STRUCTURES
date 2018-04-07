class CaesarCipher:
    """ Class for doing encryption and decryption using a Ceaser cipher """

    def __init__(self,shift):
        """
        Construct Ceasar cipher using given integer shift for rotation.
        """
        encoder = [None]*26         #temp array for encrpytion
        decoder = [None]*26         #temp array for decryption
        for k in range(26):
            encoder[k]=chr((k+shift)%26 + ord('A'))
            decoder[k]=chr((k-shift)%26 + ord('A'))
        self._forward=''.join(encoder)      #will store as string
        self.backward=''.join(decoder)      #since fix

    def encrpyt(self,message):
        """ Return string  representing encrypted message. """
        return self._transform(message,self._forward)


    def decrpyt(self,secret):
        """ Return a decrpted message given encrypted message. """
        return self._transform(message,self._backward)

    def _transform(self,original,code):
        """
        utility to perform transformation based on given code string
        """
        msg = list(original)
        for k in xrange(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]-ord('A'))        #index from 0 to 25
                msg[k]=code[j]                  #replace this character
        return ''.join(msg)

if __name__ == '__main__':
    cipher=CaesarCipher(3)
    message="THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded=cipher.encrpyt(message)
    print('secret :', coded)
    answer=cipher.decrpted(coded)
    print("Message: ", answer)
