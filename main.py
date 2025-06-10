import pyperclip

emoji_dict = {
    'A': '🍎', 'B': '🦇', 'C': '🐱', 'D': '🐶', 'E': '🐘',
    'F': '🐸', 'G': '🍇', 'H': '🏠', 'I': '🍦', 'J': '🕹️',
    'K': '🔑', 'L': '🦁', 'M': '🐭', 'N': '🥜', 'O': '🐙',
    'P': '🍕', 'Q': '👸', 'R': '🌹', 'S': '🐍', 'T': '🐅',
    'U': '☂️', 'V': '🎻', 'W': '🐋', 'X': '❌', 'Y': '🪀',
    'Z': '🦓', ' ': '⭐', '.': '🔴', '!': '💥', '?': '❓'
}

def encrypt_message(message):
    
    encrypted = ""
    for char in message.upper():
        emoji = emoji_dict.get(char, '⚪')  # ⚪ for unknown characters
        encrypted += emoji
    return encrypted

def main():
    print("🔐 EMOJI ENCRYPTER 🔐")
    print("-" * 30)
    
    while True:
        # Get message from user
        message = input("\nEnter message to encrypt (or 'quit' to exit): ")
        
        if message.lower() == 'quit':
            print("Goodbye! 👋")
            break
        
        # Encrypt the message
        encrypted = encrypt_message(message)
        
        # Copy to clipboard
        try:
            pyperclip.copy(encrypted)
            print(f"\nOriginal: {message}")
            print(f"Encrypted: {encrypted}")
            print("✅ Copied to clipboard!")
        except Exception as e:
            print(f"❌ Error copying to clipboard: {e}")
            print(f"Encrypted message: {encrypted}")

if __name__ == "__main__":
    main()
