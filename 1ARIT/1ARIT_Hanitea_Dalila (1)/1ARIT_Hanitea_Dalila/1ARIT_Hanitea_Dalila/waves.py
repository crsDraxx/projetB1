class Wave:

    def __init__(self, n:int, offset:int):
        self.__n = n
        self.__offset = offset
        self.__direction = 1

    def __cipher(self, message:str):
        clean_message = message.replace(' ', '').upper()
        if self.__offset > self.__n :
            self.__offset -= self.__n
            self.__offset = self.__n - self.__offset-2
            self.__direction *= -1
        
        final_direction = self.__direction
        lines = []
        for _ in range(self.__n):
            lines.append('')

        cipher_offset = self.__offset
        for i in range(len(clean_message)):
            lines[cipher_offset] += clean_message[i]
            cipher_offset += self.__direction
            if cipher_offset == self.__n:
                self.__direction *= -1
                cipher_offset = self.__n - 2
            elif cipher_offset == -1:
                self.__direction *= -1
                cipher_offset = 1
        ciphered_text = ''.join(lines)
        print('Ciphered text : '+ciphered_text)
        self.__direction = final_direction
        self.__display_wave(ciphered_text)
        return ciphered_text

    def __uncipher(self, message:str):
        clean_message = message.replace(' ', '').upper()
        if self.__offset > self.__n :
            self.__offset -= self.__n
            self.__offset = self.__n - self.__offset-2
            self.__direction *= -1

        final_direction = self.__direction
        temp_offset = self.__offset
        temp_direction = self.__direction
        temp_lines = []

        for _ in range(self.__n):
            temp_lines.append('')

        for i in range(len(clean_message)):
            temp_lines[temp_offset] += clean_message[i]
            temp_offset += temp_direction
            if temp_offset == self.__n:
                temp_direction = -1
                temp_offset = self.__n - 2
            elif temp_offset == -1:
                temp_direction = 1
                temp_offset = 1


        counter = []
        for i in range(self.__n):
            counter.append(len(temp_lines[i]))
        
        lines = []
        current_index = 0
        counter_offset = self.__offset
        for i in counter:
            lines.append(clean_message[current_index:i+current_index])
            current_index += i
            counter_offset += self.__direction
        

        unciphered_text = ''
        uncipher_offset = self.__offset
        for i in range(len(clean_message)):
            unciphered_text += lines[uncipher_offset][0]
            lines[uncipher_offset] = lines[uncipher_offset][1:]
            uncipher_offset += self.__direction
            if uncipher_offset == self.__n:
                self.__direction *= -1
                uncipher_offset = self.__n - 2
            elif uncipher_offset == 0:
                self.__direction *= -1

        print('Unciphered text : '+unciphered_text)
        self.__direction = final_direction
        self.__display_wave(unciphered_text)
        return unciphered_text
    
    def __display_wave(self,message):
        clean_message = message.replace(' ', '').upper()
        lines = []

        for _ in range(self.__n):
            lines.append('')
        
        for char in clean_message:
            for i in range(self.__n):
                if self.__offset == i:
                    lines[i] += char
                else:
                    lines[i] += ' '
            self.__offset += self.__direction
            if self.__offset == self.__n:
                self.__direction *= -1
                self.__offset = self.__n - 2
            elif self.__offset == -1:
                self.__direction *= -1
                self.__offset = 1

        print("Vagues : \n")
        for line in lines:
            print(line)

test_cipher_wave = Wave(6,7)
test_cipher_wave._Wave__cipher("Did you ever wake up to find A day that broke up your mind")

test_uncipher_wave = Wave(6,7)
test_uncipher_wave._Wave__uncipher("YEDKNDOKUAAOEIDIUAPDYRUMDEWTNTBPRVROIHTYUEFAO")

cipher_wave = Wave(14, 7)
cipher_wave._Wave__cipher("Hani et Dalila aiment toutes les deux la Kpop")

cipher_wave = Wave(7, 8)
cipher_wave._Wave__uncipher('''HANHARYMTPTLAYNCIPSITTITNOWRIOEFHOAEALOWIDIIGTNOSATTNSDOATNSSOEGSHLEFTTAMTODAGGITHSGTIDYTGEETSSSTETMOILJINNWGSNIEEISNAISTKNUELIYSYENNAUAAEILGYLTMUGNMUOASOGRNBTENMGNSWFIRBAJIJMEIGHIOTR''')
