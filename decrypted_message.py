import string

#Change function name to decrypt
def decrypt(message,shift):
    alphabet = string.ascii_lowercase

    decrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            #Change to subtraction
            #new_position = (original_position - shift) % 26
            new_position = (original_position + shift) % 26
            decrypted_letter = alphabet[new_position]
            #حافظ عللى حالة الحرف
            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter

    #Change to print decrypted message
    print(f"\n\nHere is the original message\n****\n\n{decrypted_message}\n\n*****")

#تأخذ الرسالة من المستخدم وعدد حروف الانتقال
user_message = input("Enter a message: ")
shift_number = int(input("Enter a shift number: "))

#Change function call to decrypt
decrypt(user_message,shift_number)
