import enchant

SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
SYMBOL_LIST = list(SYMBOL)


class CeasarsCipher:
    def __init__(self):
        self.key = 0

    def get_key(self) -> int:
        return self.key

    def set_key(self, new_key: int) -> None:
        self.key = new_key

    def decrypt(self, message) -> tuple[str, int]:
        self.set_key(0)
        while True:
            message_list = list(message)
            checker = enchant.Dict('en_US')
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
            message_decrypted_list = message_decrypted.split()
            for word in message_decrypted_list:
                if not checker.check(word):
                    list_errors.append(word)
            if (len(list_errors) == 0 or len(list_errors) == 1) and \
                    len(list_errors) != len(message_decrypted.split(' ')):
                break
            elif self.key == len(SYMBOL_LIST) - 1:
                print('Сообщение не было закодировано методом Цезаря')
                break
            else:
                self.key += 1
        return message_decrypted, self.key

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
        message_encrypted = ''.join(message_list)
        return message_encrypted


ceasar = CeasarsCipher()
message_for_encryption = 'The vacation was a success'
key = 3
message_encrypted = ceasar.encrypt(message_for_encryption, key)
print(f'Зашифрованное сообщение: {message_encrypted}')
print()

message_for_decryption = 'Wkh.ydfdwlrq.zdv.d.vxffhvv'
message_decrypted = ceasar.decrypt(message_for_decryption)
print(f'Расшифрованное сообщение: {message_decrypted[0]}, '
      f'ключ: {message_decrypted[1]}')
print()
foggoten_password = 'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D'
password = ceasar.decrypt(foggoten_password)
print(f'Расшифрованное сообщение: {password[0]}, ключ: {password[1]}')
file_path = input('Куда сохранить файл: ')
with open(file_path + '/ceasarcipher.txt', 'w', encoding='utf-8') as file:
    file.write(f'Расшифрованное сообщение: {message_decrypted[0]}, '
               f'ключ: {message_decrypted[1]}\n')
    file.write(f'Расшифрованное сообщение: {password[0]}, ключ: {password[1]}')
