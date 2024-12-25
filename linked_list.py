import pygame
import time

pygame.init()
w, h = 1200, 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Linked List Visualization")
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "green": (0, 255, 0),
    "light_green": (204, 255, 204),
    "blue": (0, 0, 255)
}

# the linked list
the_linked_list = {
    3: [9, "right"],
    9: [5, "right"],
    5: [1, "right"],
    1: [7, "right"],
    7: [11, "up"],
    11: [2, "up"],
    2: [8, "up"],
    8: [4, "left"],
    4: [12, "left"],
    12: [10, "down"],
    10: [6, "down"],
    6: [5, "down"]
}


def draw_linked_list(current_node1=None, current_node2=None, current_index=None):
    x, y = 200, 600
    for node, value in the_linked_list.items():
        # to highlight the current node
        if current_node1 == node:
            pygame.draw.rect(screen, colors["orange"], (x, y, 80, 80))
        if current_node2 == node:
            pygame.draw.rect(screen, colors["green"], (x, y, 80, 80))
        

        pygame.draw.rect(screen, colors["black"], (x, y, 80, 80), 5)
        if current_index == node:
            pygame.draw.rect(screen, colors["blue"], (x, y, 80, 80), 5)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node), True, colors["black"])
        screen.blit(text, (x + 30, y + 30))

        # the arrows to the next node
        if value[1] == "right":
            pygame.draw.line(screen, colors["black"], (x + 80, y + 40), (x + 120, y + 40), 5)
            pygame.draw.polygon(screen, colors["black"], [(x + 130, y + 40), (x + 110, y + 30), (x + 110, y + 50)])
            x += 130
        elif value[1] == "up":
            pygame.draw.line(screen, colors["black"], (x + 40, y), (x + 40, y - 40), 5)
            pygame.draw.polygon(screen, colors["black"], [(x + 40, y - 50), (x + 30, y - 30), (x + 50, y - 30)])
            y -= 130
        elif value[1] == "left":
            pygame.draw.line(screen, colors["black"], (x, y + 40), (x - 40, y + 40), 5)
            pygame.draw.polygon(screen, colors["black"], [(x - 60, y + 40), (x - 40, y + 30), (x - 40, y + 50)])
            x -= 135
        elif value[1] == "down":
            pygame.draw.line(screen, colors["black"], (x + 40, y + 80), (x + 40, y + 120), 5)
            pygame.draw.polygon(screen, colors["black"], [(x + 40, y + 130), (x + 30, y + 110), (x + 50, y + 110)])
            y += 130
    if current_node1 ==current_node2:
        print_true()


def the_algo():
    slow = 3  # the start node
    fast = the_linked_list[slow][0]  # the next node
    current_index = slow

    while True:
        yield slow, fast, current_index
        current_index = the_linked_list[current_index][0]  # update the current index
        slow = the_linked_list[slow][0]  # update the slow node
        fast = the_linked_list[the_linked_list[fast][0]][0]  # update the fast node
        

def print_true():
    pygame.draw.rect(screen, colors["light_green"], (100, 100, 700, 70), border_radius=10)
    pygame.draw.rect(screen, colors["green"], (100, 100, 700, 70), 6, border_radius=10)
    font = pygame.font.Font(None, 50)
    text = font.render("Yes, We found a circle in the linked list.", True, colors["black"])
    screen.blit(text, (150, 120))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()

def main():
    running = True
    algo = the_algo()  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        try:
            slow, fast, current_index = next(algo)
        except StopIteration:
            break

        screen.fill(colors["white"])
        font=pygame.font.Font(None,36)
        text=font.render("Is there a circle in the linked list?",True,colors["black"])
        screen.blit(text,(40,50))

        draw_linked_list(current_node1=slow, current_node2=fast, current_index=current_index)
        pygame.display.flip()
        time.sleep(1)  

    pygame.quit()


if __name__ == "__main__":
    main()
