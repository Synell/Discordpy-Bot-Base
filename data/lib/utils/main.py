#----------------------------------------------------------------------

    # Functions
def bool_yes_no(b: bool = False):
    if b: return 'Oui'
    return 'Non'

def hex_to_rgb(hex: str = '#000000'):
    hex = hex.replace('#', '').replace('0x', '')
    if len(hex) != 6: return (0, 0, 0)
    return (int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:], 16))

def time_string(time: int|float, unit: str = 's') -> str:
    def time_double_digit(time: int) -> str:
        return f'{"0" * (2 - len(str(time)))}{time}'

    secs = int(time)
    totalSecs = secs
    mins = secs // 60
    total_mins = mins
    secs %= 60
    hours = mins // 60
    total_hours = hours
    mins %= 60
    days = hours // 24
    total_days = days
    hours %= 24
    weeks = days // 7
    total_weeks = weeks
    days %= 7
    months = weeks // 4
    total_months = months
    weeks %= 4
    years = months // 12
    total_years = years
    months %= 12

    match unit:
        case 's':
            return f'{totalSecs}s'
        case 'm':
            return f'{total_mins}m {time_double_digit(secs)}s'
        case 'h':
            return f'{total_hours}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
        case 'd':
            return f'{total_days}d {time_double_digit(hours)}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
        case 'w':
            return f'{total_weeks}w {time_double_digit(days)}d {time_double_digit(hours)}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
        case 'M':
            return f'{total_months}M {time_double_digit(weeks)}w {time_double_digit(days)}d {time_double_digit(hours)}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
        case 'y':
            return f'{total_years}y {time_double_digit(months)}M {time_double_digit(weeks)}w {time_double_digit(days)}d {time_double_digit(hours)}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
        case _:
            return f'{total_years}y {time_double_digit(months)}M {time_double_digit(weeks)}w {time_double_digit(days)}d {time_double_digit(hours)}h {time_double_digit(mins)}m {time_double_digit(secs)}s'
#----------------------------------------------------------------------
