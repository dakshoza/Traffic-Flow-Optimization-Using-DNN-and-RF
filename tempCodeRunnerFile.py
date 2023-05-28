use_pos = pygame.mouse.get_pos()
                for road in monitoredRoads:
                    if road.boundaries.collidepoint(mouse_pos):
                        road.update()