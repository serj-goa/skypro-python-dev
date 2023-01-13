def run_calculator():
    while True:
        user_expression = input('Enter expression: ').lower().strip()

        if user_expression == 'stop':
            print('Program is closed. Good Bye!')
            break

        print(f'Answer: {eval(user_expression)}')


if __name__ == '__main__':
    run_calculator()
