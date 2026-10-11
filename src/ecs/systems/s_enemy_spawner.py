import esper

from src.ecs.components.c_enemy_spawner import CEnemySpawner


def system_enemy_spawner(world: esper.World, delta_time: float):
    components = world.get_component(CEnemySpawner)

    c_spawner: CEnemySpawner
    for _, c_spawner in components:
        c_spawner.elapsed_time += delta_time