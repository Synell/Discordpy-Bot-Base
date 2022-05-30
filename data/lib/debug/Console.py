#----------------------------------------------------------------------

    # Libraries
import colorama
colorama.init()
#----------------------------------------------------------------------

    # Class
class Console:
    def __new__(cls) -> None:
        return None

    def log(msg: str = ''):
        print(colorama.Fore.LIGHTBLACK_EX + '[LOG] ' + colorama.Fore.LIGHTBLACK_EX + str(msg) + colorama.Fore.RESET)

    def error(msg: str = ''):
        print(colorama.Fore.LIGHTRED_EX + '[ERROR] ' + colorama.Fore.LIGHTBLACK_EX + str(msg) + colorama.Fore.RESET)

    def warning(msg: str = ''):
        print(colorama.Fore.YELLOW + '[WARNING] ' + colorama.Fore.LIGHTBLACK_EX + str(msg) + colorama.Fore.RESET)

    def success(msg: str = ''):
        print(colorama.Fore.GREEN + '[SUCCESS] ' + colorama.Fore.LIGHTBLACK_EX + str(msg) + colorama.Fore.RESET)
#----------------------------------------------------------------------
