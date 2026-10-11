import esper
import pygame
import math
import random

from src.create.prefab_creator import create_square
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
                enemy_cfg = c_spawner.enemies.get(event["enemy_type"])

                if enemy_cfg is not None:
                    size = pygame.Vector2(
                        enemy_cfg["size"]["x"],
                        enemy_cfg["size"]["y"]
                    )

                    position = pygame.Vector2(
                        event["position"]["x"],
                        event["position"]["y"]
                    )

                    color = pygame.Color(
                        enemy_cfg["color"]["r"],
                        enemy_cfg["color"]["g"],
                        enemy_cfg["color"]["b"]
                    )

                    speed = random.uniform(
                        enemy_cfg["velocity_min"],
                        enemy_cfg["velocity_max"]
                    )

                    angle = random.uniform(0, 2 * math.pi)

                    velocity = pygame.Vector2(
                        math.cos(angle) * speed,
                        math.sin(angle) * speed
                    )

                    create_square(
                        world,
                        size,
                        position,
                        velocity,
                        color
                    )

                    event["triggered"] = True