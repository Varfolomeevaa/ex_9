class MorseMsg:
    '''
    Class for morse messages
    '''
    morse_eng = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z'}
    morse_ru = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж', '--..': 'З',
                '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П',
                '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
                '----': 'Ш', '--.-': 'Щ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я'}
    vowels_eng = ['A', 'E', 'I', 'O', 'U', 'Y']
    vowels_ru = ['А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я']

    def __init__(self, ptr):
        '''
        method for initialization
        :param ptr: pater in morse
        '''
        self.ptr = ptr

    def eng_decode(self):
        '''
        method for decoding to english
        :return: pater in english
        '''
        letters = self.ptr.split()
        new_ptr = ''
        for i in range(len(letters)):
            new_ptr += MorseMsg.morse_eng[letters[i]]
        return new_ptr

    def ru_decode(self):
        '''
        method for decoding to russian
        :return: pater in russian
        '''
        letters = self.ptr.split()
        new_ptr = ''
        for i in range(len(letters)):
            new_ptr += MorseMsg.morse_ru[letters[i]]
        return new_ptr

    def get_vowels(self, lang):
        '''
         method for getting vowels
         :param lang: language
         :return: vowels
         '''
        letters = []
        if lang == 'ru':
            ptr = self.ru_decode()
            for i in range(len(ptr)):
                if ptr[i] in MorseMsg.vowels_ru:
                    letters.append(ptr[i])
        else:
            ptr = self.eng_decode()
            for i in range(len(ptr)):
                if ptr[i] in MorseMsg.vowels_eng:
                    letters.append(ptr[i])
        return letters

    def get_consonants(self, lang):
        '''
        method for getting consonants
        :param lang: language
        :return: consonants
        '''
        letters = []
        if lang == 'ru':
            ptr = self.ru_decode()
            for i in range(len(ptr)):
                if ptr[i] not in MorseMsg.vowels_ru:
                    letters.append(ptr[i])
        else:
            ptr = self.eng_decode()
            for i in range(len(ptr)):
                if ptr[i] not in MorseMsg.vowels_eng:
                    letters.append(ptr[i])
        return letters

    def __str__(self):
        '''
        method for string representation
        :return: string with a message
        '''
        return f'Закодированное сообщение: {self.ptr}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with a message
        '''
        return self.__str__()
