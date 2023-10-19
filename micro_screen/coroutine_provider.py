class CoroutineProvider():
    def __init__(self) -> None:
        pass
    
    def launch(self, sleep_ms: int, work: function) -> int:
        pass
        
    def stop(self, coroutine_id):
        raise NotImplementedError