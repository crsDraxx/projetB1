class Twin:
    def __init__(self, key_left:str , key_right:str):
        self.__key_left = key_left
        self.__key_right = key_right
   

    def __cipher(self, message):
        clean_message = message.replace(' ', '').upper()
        ciphered_text= ""
        for j in clean_message:
            for i in self.__key_right:
                if i == j:
                    index = self.__key_right.index(i)
                    value = self.__key_left[index]
                    ciphered_text += value
                    #print(value)
                    self.__key_left = self.__key_left[index:]+self.__key_left[:index]
                    #print(self.__key_left)
                    self.__key_left = self.__key_left[0]+self.__key_left[2:14:]+self.__key_left[1]+self.__key_left[14:]
                    #print(self.__key_left)
                    self.__key_right = self.__key_right[index+1:]+self.__key_right[:index+1]
                    #print(self.__key_right)
                    self.__key_right = self.__key_right[:2]+self.__key_right[3:14:]+self.__key_right[2]+self.__key_right[14:]
                    #print(self.__key_right)
        print("le texte chiffré est :\n")
        print(ciphered_text, "\n")
        return ciphered_text
            

    def __uncipher(self, message):
        clean_message = message.replace('  ', '').upper()
        ciphered_text= ""
        for j in clean_message:
            for i in self.__key_left:
                if i == j:
                    index = self.__key_left.index(i)
                    value = self.__key_right[index]
                    ciphered_text += value
                    #print(value)
                    self.__key_left = self.__key_left[index:]+self.__key_left[:index]
                    #print(self.__key_left)
                    self.__key_left = self.__key_left[0]+self.__key_left[2:14:]+self.__key_left[1]+self.__key_left[14:]
                    #print(self.__key_left)
                    self.__key_right = self.__key_right[index+1:]+self.__key_right[:index+1]
                    #print(self.__key_right)
                    self.__key_right = self.__key_right[:2]+self.__key_right[3:14:]+self.__key_right[2]+self.__key_right[14:]
                    #print(self.__key_right)
        print("le texte déchiffré est :\n")
        print(ciphered_text,"\n")
        return ciphered_text

test_cipher = Twin("OAJTFYLQXCMPEDNVSBRUKHGWIZ","EWKFTYIQXUHPMABCNJRLDZSGVO")
test_cipher._Twin__cipher("SWAY")

test_uncipher = Twin("OAJTFYLQXCMPEDNVSBRUKHGWIZ","EWKFTYIQXUHPMABCNJRLDZSGVO")
test_uncipher._Twin__uncipher("GOPJ")

cipher_twin = Twin("ALZBHGUWIEFJCDYNMQRVKPTOXS","TWXLPRDZMNUGSAQKJHEBCIFYVO")
cipher_twin._Twin__uncipher("PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH")

cipherTwin = Twin("TWXLPRDZMNUGSAQKJHEBCIFYVO","OAJTFYLQXCMPEDNVSBRUKHGWIZ")
cipherTwin._Twin__cipher("Hani et Dalila aiment toutes les deux la Kpop")