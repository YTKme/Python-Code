"""
Thread Async IO
~~~~~~~~~~~~~~~

The ThreadAsyncIO module provide example(s) and comparison(s) for the
`threading` and the `asyncio` module.
"""

import requests
import threading
import timeit


WEBSITE_LIST = [
    'https://api.apis.guru/v2/specs/1forge.com/0.0.1/swagger.json',
    'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0',
    'https://api.apis.guru/v2/specs/1password.com/events/1.0.0/openapi.json',
    'https://api.apis.guru/v2/specs/1password.local/connect/1.5.7/openapi.json',
    'https://api.apis.guru/v2/specs/6-dot-authentiqio.appspot.com/6/openapi.json',
    'https://api.apis.guru/v2/specs/ably.io/platform/1.1.0/openapi.json',
    'https://api.apis.guru/v2/specs/ably.net/control/1.0.14/openapi.json',
    'https://api.apis.guru/v2/specs/abstractapi.com/geolocation/1.0.0/openapi.json',
    'https://api.apis.guru/v2/specs/adafruit.com/2.0.0/swagger.json',
    'https://api.apis.guru/v2/specs/adobe.com/aem/3.7.1-pre.0/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/AccountService/6/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalanceControlService/1/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalancePlatformConfigurationNotification-v1/1/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalancePlatformPaymentNotification-v1/1/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalancePlatformReportNotification-v1/1/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalancePlatformService/2/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BalancePlatformTransferNotification-v3/3/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/BinLookupService/54/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/CheckoutService/70/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/CheckoutUtilityService/1/openapi.json',
    'https://api.apis.guru/v2/specs/adyen.com/DataProtectionService/1/openapi.json',
]


def fetch_website_thread():
    """Fetch Website Thread"""

    # Create a list store the thread(s)
    thread_list = []

    # Loop through the WEBSITE_LIST
    for index, website in enumerate(WEBSITE_LIST):
        # Create thread
        thread = threading.Thread(
            target=fetch_worker, args=(f'W-{index}', website,))
        # Add thread to the thread_list
        thread_list.append(thread)
        # Start thread
        thread.start()


def fetch_worker(name: str, website: str):
    """Fetch Worker

    :param name: The name for the worker
    :type name: str
    :param website: The URL (Uniform Resource Locator) for the website
    :type website: str
    """

    print(f'Fetch Worker Website {name}: {website}')
    start = timeit.default_timer()
    response = requests.get(website)
    stop = timeit.default_timer()
    print(f'Fetch Worker Time {name}: {stop - start:.2f}')
