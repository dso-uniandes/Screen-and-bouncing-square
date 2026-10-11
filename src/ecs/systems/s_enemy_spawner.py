import esper

from src.ecs.components.c_enemy_spawner import CEnemySpawner


def system_enemy_spawner(world: esper.World, delta_time: float):
    components = world.get_component(CEnemySpawner)

    c_spawner: CEnemySpawner
    for _, c_spawner in components:
        c_spawner.elapsed_time += delta_time

        for event in c_spawner.events:
            if event["triggered"]:
                continue

            if c_spawner.elapsed_time >= event["time"]:
                enemy_cfg = None

                for enemy in c_spawner.enemies:
                    if enemy["name"] == event["enemy_type"]:
                        enemy_cfg = enemy
                        break

                if enemy_cfg is not None:
                    print(f'Enemy found: {enemy_cfg["name"]}')
                    event["triggered"] = True