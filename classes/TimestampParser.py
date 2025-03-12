import datetime


class TimestampParser:
    @staticmethod
    def print_timestamp(timestamp) -> str:
        try:
            return timestamp.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None
        
    @staticmethod
    def parse_timestamp_str(timestamp_str: str) -> datetime:
        try:
            return datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f%z")
        except ValueError:
            return datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S%z")
        except ValueError:
            return None