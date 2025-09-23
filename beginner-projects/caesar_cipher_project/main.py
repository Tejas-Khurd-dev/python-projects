import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    message = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            message += letter
        else:
            index = alphabet.index(letter)
            new_index = index + shift_amount
            new_index %= len(alphabet)
            message += alphabet[new_index]

    print(f"✅ {encode_or_decode}d message is: {message}")

should_restart = True
while should_restart:
    direction = input("👉 Type 'encode' 🔒 to encrypt, type 'decode' 🔓 to decrypt:\n").lower()
    text = input("📝 Type your message:\n").lower()
    key = (input("🔑 Type the key shift number:\n"))

    if not key.isdigit():
        print("⚠️ Enter a valid number for key!")
    else:
        key = int(key)

    if direction == "encode" or direction == "decode":
        caesar(original_text=text, shift_amount=key, encode_or_decode=direction)
    else:
        print("⚠️ Please enter 'encode' or 'decode'")

    choice = input("🔁 Do you want to run it again? Type 'y' for yes ✅ or 'n' for no ❌: ")

    if choice == "y":
        should_restart = True
    else:
        print("👋 Goodbye! Thanks for using Caesar Cipher 🔐")
        should_restart = False
