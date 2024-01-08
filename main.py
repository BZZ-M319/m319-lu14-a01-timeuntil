from datetime import datetime


def time_until():
    print('Would you like to know the time to a date or to a date and time?')
    print('1. date')
    print('2. date and time')
    choice = input('enter 1 or 2: ')
    if choice == '1':
        date = input('Enter a date in the format YYYY-MM-DD : ')
        date = datetime.strptime(date, '%Y-%m-%d')
    elif choice == '2':
        date = input('Enter a date in the format YYYY-MM-DD HH:MM:SS :')
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    now = datetime.now()
    time_until = date - now
    if time_until.days < 0:
        print('The ', date, ' passed for', time_until.days, 'days,'
              , time_until.seconds // 3600, 'hours,'
              , time_until.seconds // 60 % 60, 'minutes, and'
              , time_until.seconds % 60, 'seconds ')
    else:
        print('There are', time_until.days, 'days,'
              , time_until.seconds // 3600, 'hours,'
              , time_until.seconds // 60 % 60, 'minutes, and'
              , time_until.seconds % 60, 'seconds until', date)


if __name__ == '__main__':
    time_until()