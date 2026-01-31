bot_name: str = 'Grand Central'
print(f'Hello! I\'m {bot_name}! How can I assist you today')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hi there! How can I help?')
    elif user_input in ['bye', 'see you', 'toodles']:
        print(f'{bot_name}: Good bye! Hack the planet!')
    elif user_input in ['+', 'add']:
        print(f'{bot_name}: Sure, lets add! Please enter two numbers')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Wrong! Use valid numbers!')
        print(f'{bot_name}: Bro what are you even doing? Try again but make sense this time')

    elif user_input in ['minus']:
        print(f'{bot_name}: Sure lets subtract!')
        try:
            num1: float = float(input('First number '))
            num2: float = float(input('Second number '))
            print(f'{bot_name}: The answer is {num1 - num2}')
        except ValueError:
            print(f'{bot_name}: Wrong!')
