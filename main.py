from datetime import datetime
from colorama import init, Fore

from modules.browser_manager import PriceSearchAutomation
from modules.spread_sheet import ExcelHandler
from modules.utils import get_user_inputs

from constants import *

# Init colorama
init(autoreset=True)


def main() -> None:
    product_name, brand, store, open_browser = get_user_inputs()
    query = ' '.join(filter(None, [product_name, brand, store]))
    print(f'\n{Fore.MAGENTA}Buscando por {query}...')

    browser_options = BROWSER_OPTIONS if open_browser else BROWSER_OPTIONS + \
        ('--headless',)
    automation = PriceSearchAutomation(*browser_options)
    products = None

    try:
        products = automation.search_product(query)
        print(f'\n{Fore.GREEN}Busca encerrada. {
              len(products)} itens encontrados.')
    except Exception:
        print(f'{Fore.RED}Ocorreu um erro interno. Não foi possível buscar produtos')
    finally:
        automation.close_browser()

    if products is not None and len(products) > 0:
        print(f'{Fore.GREEN}Iniciando etapa de transformação dos dados...')
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for product in products:
            product.append(current_datetime)

        excel_handler = ExcelHandler(
            SPREADSHEET_NAME, query if len(query) <= 25 else query[:25]
        )
        excel_handler.insert_header(SPREADSHEET_HEADERS)
        excel_handler.insert_data(products)
        excel_handler.save()
        print(f'{Fore.GREEN}Sucesso! Dados salvos na planilha "{
              query}" em {SPREADSHEET_NAME}')

    else:
        print(f'\n{Fore.RED}Não foram encontradas correspondências de sua pesquisa. Tente novamente usando outros termos.')


if __name__ == '__main__':
    main()
