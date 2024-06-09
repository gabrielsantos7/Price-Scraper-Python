from colorama import init, Fore

# Init colorama
init(autoreset=True)


def mandatory_input(prompt):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                user_input = input(f'\n{Fore.YELLOW}{prompt}').strip()
                if not user_input:
                    print(f'{Fore.RED}O campo é obrigatório. Por favor, tente novamente.')
                else:
                    return func(user_input, *args, **kwargs)
        return wrapper
    return decorator


def validated_input(prompt, valid_responses):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                user_input = input(f'\n{Fore.YELLOW}{prompt}').strip().lower()
                if user_input not in valid_responses:
                    print(f'{Fore.RED}Resposta inválida. Por favor, digite uma das seguintes opções: {
                          ", ".join(valid_responses)}.')
                else:
                    return func(user_input, *args, **kwargs)
        return wrapper
    return decorator
