from datetime import datetime
import sys


def convert_timestamp():
    """
    Converts a timestamp into a human readable date format

    >>> convert_timestamp(1601104029)
    09/26/2020 @ 7:07am (UTC)
    >>> convert_timestamp(1509923462)
    11/05/2017 @ 11:11pm (UTC)
    """
    ts = int(sys.argv[1])
    human_readable_time = '%m/%d/%Y @ %I:%M %p (UTC)'
    print(datetime.utcfromtimestamp(ts).strftime(human_readable_time))


if __name__ == '__main__':
    convert_timestamp()
