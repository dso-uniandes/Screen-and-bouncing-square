class CEnemySpawner:
    def __init__(self, events: list, enemies: dict) -> None:
        self.events = []

        for event in events:
            self.events.append({
                "enemy_type": event["enemy_type"],
                "time": event["time"],
                "position": event["position"],
                "triggered": False
            })

        self.enemies = enemies
        self.elapsed_time = 0.0