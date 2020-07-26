def log_sleep(t, warn=False, action='to perform next action'):
    from time import sleep
    if not warn:
        for i in range(t, 0, -1):
            if i != 1:
                print(f'Now waiting {i} seconds {action}')
            else:
                print(f'Now waiting 1 second to {action}')
            sleep(1)
    else:
        #from clog import warning
        from console_log.clog import warning
        for i in range(t, 0, -1):
            if i != 1:
                warning(f'Now waiting {i} seconds {action}')
            else:
                warning(f'Now waiting 1 second {action}')
            sleep(1)


def partial_log_sleep(t, warn=False, action='to perform next action'):
    from time import sleep
    if not warn:
        print(f'Now waiting {t} seconds {action}')
        sleep(t-5)
        for i in range(5, 0, -1):
            if i != 1:
                print(f'Now waiting {i} seconds {action}')
            else:
                print(f'Now waiting 1 second {action}')
            sleep(1)
    else:
        #from clog import warning
        from console_log.clog import warning
        warning(f'Now waiting {t} seconds {action}')
        sleep(t-5)
        for i in range(5, 0, -1):
            if i != 1:
                warning(f'Now waiting {i} seconds {action}')
            else:
                warning(f'Now waiting 1 second {action}')
            sleep(1)
