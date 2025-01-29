class TimestampParser:
    @staticmethod
    def print_timestamp(timestamp) -> str:
        try:
            return timestamp.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None