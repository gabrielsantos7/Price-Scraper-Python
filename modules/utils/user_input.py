from colorama import init, Fore

from .decorators import mandatory_input, validated_input

# Init colorama
init(autoreset=True)

@mandatory_input('Digite o nome do produto: ')
def get_product_name(product_name):
    return product_name

@validated_input('Deseja abrir o navegador? (sim/não): ', ['sim', 'não'])
def get_open_browser(open_browser):
    return open_browser == 'sim'

def get_user_inputs():
    product_name = get_product_name()
    brand = input(f'\n{Fore.YELLOW}Digite a marca (opcional, pressione Enter para pular): ').strip()
    store = input(f'\n{Fore.YELLOW}Digite o nome da loja (opcional, pressione Enter para pular): ').strip()
    open_browser = get_open_browser()

    return product_name, brand, store, open_browser
