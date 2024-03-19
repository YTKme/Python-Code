"""
Argument Parse Alpha
~~~~~~~~~~~~~~~~~~~~

The ArgumentParseAlpha module provide example(s) for the `argparse`
module.
"""

import argparse
import asyncio


async def parse_argument():
    """Parse Argument

    :returns: the namespace with the parsed arguments
    :rtype: namespace
    """

    # Alpha Argument List
    alpha_argument_list = [
        # ((), {})
    ]

    # Alpha Argument Parser
    alpha_argument_parser = argparse.ArgumentParser(
        description=('Alpha Argument Parser')
    )

    # Add Alpha Argument List
    for argument in alpha_argument_list:
        alpha_argument_parser.add_argument(
            *argument[0],
            **argument[1],
        )

    subparser = alpha_argument_parser.add_subparsers(
        title='Subcommand(s)',
        description='Additional (sub)commmand(s) for Alpha Argument Parser.',
        dest='alpha_argument_subparser',
        help='Description',
        metavar='Option',
    )

    # Subparser Argument List
    subparser_argument_list = [
        (('-i', '--input'), {
            'action': 'store',
            'dest': 'subparser_input',
            'required': False,
            'help': 'Subparser Input.',
            'metavar': 'INPUT',
        }),
        (('-o', '--output'), {
            'action': 'store',
            'dest': 'subparser_output',
            'required': False,
            'help': 'Subparser Output.',
            'metavar': 'OUTPUT',
        })
    ]

    # Primary Argument List
    primary_argument_list = [
        (('-s', '--source'), {
            'action': 'store',
            'dest': 'primary_source',
            'required': False,
            'help': 'Primary Source.',
            'metavar': 'SOURCE',
        }),
        (('-d', '--destination'), {
            'action': 'store',
            'dest': 'primary_destination',
            'required': False,
            'help': 'Primary Destination.',
            'metavar': 'DESTINATION',
        })
    ]

    # Primary Subparser
    primary_argument_subparser = subparser.add_parser(
        'primary',
        help='Primary Argument Subparser For Alpha Argument Parser.'
    )

    # Secondary Subparser
    secondary_argument_subparser = subparser.add_parser(
        'secondary',
        help='Secondary Argument Subparser For Alpha Argument Parser.'
    )

    # Add Primary Argument List
    [primary_argument_subparser.add_argument(
        *argument[0], **argument[1]
    ) for argument in subparser_argument_list]
    [primary_argument_subparser.add_argument(
        *argument[0], **argument[1]
    ) for argument in primary_argument_list]

    # Add Secondary Argument List
    [secondary_argument_subparser.add_argument(
        *argument[0], **argument[1]
    ) for argument in subparser_argument_list]

    return alpha_argument_parser.parse_args()


async def main():
    """Main Function"""

    argument = await parse_argument()

    print(f'Argument: {argument}')


if __name__ == '__main__':
    asyncio.run(main())
