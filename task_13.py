from enchant.checker import SpellChecker

SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
SYMBOL_LIST = list(SYMBOL)


class CeasarsCipher:
    def __init__(self):
        self.key = 0

    def get_key(self) -> int:
        return self.key

    def set_key(self, new_key: int) -> None:
        self.key = new_key

    def decrypt(self, message) -> str:
        self.set_key(0)
        while True:
            message_list = list(message)
            checker = SpellChecker('en_US')
            list_errors = []
            for i in range(len(message_list)):
                if SYMBOL.find(message_list[i]) - self.key < 0:
                    message_list[i] = SYMBOL_LIST[SYMBOL.find(message_list[i])
                                                  - self.key
                                                  + len(SYMBOL_LIST)]
                else:
                    message_list[i] = SYMBOL_LIST[SYMBOL.find(message_list[i])
                                                  - self.key]
            message_decrypted = ''.join(message_list)
            checker.set_text(message_decrypted)
            for err in checker:
                list_errors.append(err.word)
            if (len(list_errors) == 0 or len(list_errors) == 1) \
                    and len(list_errors) != len(message_decrypted.split(' ')):
                print(f'Расшифрованное сообщение: {message_decrypted}, '
                      f'ключ: {self.key}')
                break
            elif self.key == len(SYMBOL_LIST) - 1:
                print('Сообщение не было закодировано методом Цезаря')
                break
            else:
                self.key += 1
        return f'Расшифрованное сообщение: {message_decrypted}, ' \
               f'ключ: {self.key}'

    def encrypt(self, message: str, new_key) -> str:
        self.set_key(new_key)
        message_list = list(message)
        for i in range(len(message_list)):
            if SYMBOL.find(message_list[i]) + self.key > len(SYMBOL_LIST) - 1:
                message_list[i] = SYMBOL_LIST[SYMBOL.find(message_list[i])
                                              + self.key - len(SYMBOL_LIST)]
            else:
                message_list[i] = SYMBOL_LIST[SYMBOL.find(message_list[i])
                                              + self.key]
        return ''.join(message_list)


ceasar = CeasarsCipher()
message = 'The vacation was a success'
key = 3
message_encrypted = ceasar.encrypt(message, key)
print(message_encrypted)
ceasar.decrypt(message_encrypted)

