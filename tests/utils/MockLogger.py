class MockCalypsoLogger:
    def info(*args, **kwargs) -> None:
        pass

    def error(*args, **kwargs) -> None:
        pass

    def debug(*args, **kwargs) -> None:
        pass

    def write_to_request_log(*args, **kwargs) -> None:
        pass
