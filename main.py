import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import letters as lt
from PIL import Image, ImageDraw
from datetime import datetime


def get_height():
    height = input("Wie hoch ist die Kamera? (in cm) ")
    try:
        height = float(height)
    except:
        height = get_height()
    return height

def get_distance():
    distance = input("Wie weit ist die Kamera vom Text entfernt? (in cm) ")
    try:
        distance = float(distance)
    except:
        distance = get_distance()
    return distance

camera_pos = [0, 0, get_height()]
distance = get_distance()
space = 1

img = None

a4_size = (21.0, 29.7)

fig = plt.figure(figsize=(10, 5))

ax = fig.add_subplot(1, 3, 1, projection="3d")
ax.set_title("Projektion")
ax.scatter(camera_pos[0], camera_pos[1], camera_pos[2], c='red', s=10)

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title("Wort")
spacing_grid = 0.5 # This can be your user specified spacing.
minorLocator = MultipleLocator(spacing_grid)
# Set minor tick locations.
ax2.yaxis.set_minor_locator(minorLocator)
ax2.xaxis.set_minor_locator(minorLocator)
# Set grid to use minor tick locations.
ax2.grid(which = 'minor', linestyle = '--')
ax2.grid(linestyle = '--')

ax3 = fig.add_subplot(2, 2, 4)
ax3.set_title("Camcarpet")
spacing_grid = 0.5 # This can be your user specified spacing.
minorLocator = MultipleLocator(spacing_grid)
# Set minor tick locations.
ax3.yaxis.set_minor_locator(minorLocator)
ax3.xaxis.set_minor_locator(minorLocator)
# Set grid to use minor tick locations.
ax3.grid(which = 'minor', linestyle = '--')
ax3.grid(linestyle = '--')

def add_line(p1, p2, color): #p1 and p2 as p1=[1,6,3]
    points = []
    for coordinate in zip(p1,p2):
        points.append(np.array(list(coordinate)))
    ax.plot(points[0], points[1], points[2], color=color)

def add_line_2d(window, p1, p2, color):
    points = []
    for coordinate in zip(p1,p2):
        points.append(np.array(list(coordinate)))
    window.plot(points[0], points[1], color=color)



# points, lines = get_letter("t", 0, 0, 0)
# for line in lines:
#     print(points[line[0]])
#     print(line)
#     add_line(points[line[0]], points[line[1]])

word = input("Gib ein Wort ein!").lower()
total_length = 0
for letter in word:
    points, lines, length = lt.get_letter(letter, 0, 0, 0)
    total_length += length + space
total_length -= space

current_pos = [-total_length/2, distance, 0]

all_lines = []
all_letter_carpet_points_2d = []

for letter in word:
    points, lines, length = lt.get_letter(letter, current_pos[0], current_pos[1], current_pos[2])

    #3d rendering the letters and carpet
    current_pos[0] += length + space
    for line in lines:
        add_line(points[line[0]], points[line[1]], color="green")

    carpet_points = []
    for point in points:
        direction = list(np.subtract(np.array(point), np.array(camera_pos)))
        r = (0-camera_pos[2])/direction[2]
        new_point = list(np.add(np.array(camera_pos), np.multiply(r, np.array(direction))))
        carpet_points.append(new_point)

    for line in lines:
        add_line(carpet_points[line[0]], carpet_points[line[1]], color="red")

    #2d rendering the letters
    points_2d = points
    for point_2d in points_2d:
        del point_2d[1] #deleting y coord

    for line in lines:
        add_line_2d(ax2, points_2d[line[0]], points_2d[line[1]], color="green")

    #2d rendering carpet
    carpet_points_2d = carpet_points
    for carpet_point_2d in carpet_points_2d:
        del carpet_point_2d[2]
        carpet_point_2d[1] -= distance
        # coord = f"{round(carpet_point_2d[0], 1)}, {round(carpet_point_2d[1], 1)}"
        # ax3.annotate(coord, [carpet_point_2d[0], carpet_point_2d[1]])

    for line in lines:
        add_line_2d(ax3, carpet_points_2d[line[0]], carpet_points_2d[line[1]], color="red")

    all_letter_carpet_points_2d.append(carpet_points_2d)
    all_lines.append(lines)



#ax2.set_xlim([-total_length/2, total_length/2])
# if len(word) > 1:
#     ax2.set_ylim([0, total_length / 2])
#     ax3.set_ylim([0, total_length / 2])
# else:
#     ax2.set_xlim([-total_length/2 - 1, total_length/2 + 1])
#     ax3.set_xlim([-total_length / 2 - 1, total_length / 2 + 1])
#     ax2.set_ylim([0, total_length+1])
#     ax3.set_ylim([0, total_length+1])
def camcarpet_as_png():
    global img
    accepted = input("Möchtest du den Camcarpet auf A4? (j) Ja, (n) Nein ").lower()

    if accepted == "j":
        image_size = get_orientation()
        letter_scale = get_scale()
        scale = 100
        img = Image.new("RGB", (int(image_size[0] * scale), int(image_size[1] * scale)), "white")  # for output png
        draw = ImageDraw.Draw(img)
        min_x = min(point[0] for sublist in all_letter_carpet_points_2d for point in sublist)
        for sublist in all_letter_carpet_points_2d:
            for point in sublist:
                point[0] -= min_x
                point[0] *= letter_scale
                point[1] *= letter_scale
                point[1] = image_size[1] -point[1]
        for i, sublist in enumerate(all_lines):
            for line in sublist:
                draw.line([(all_letter_carpet_points_2d[i][line[0]][0] * scale, all_letter_carpet_points_2d[i][line[0]][1] * scale),
                           (all_letter_carpet_points_2d[i][line[1]][0] * scale, all_letter_carpet_points_2d[i][line[1]][1] * scale)], fill="black", width=10)
        draw.line([(-min_x * scale * letter_scale, image_size[1] * scale), (-min_x * scale * letter_scale, (image_size[1]-0.1) * scale)], fill="red", width=10)
        img.show()

        get_download()
    elif accepted == "n":
        print("continue")
    else:
        camcarpet_as_png()

def get_orientation():
    orientation = input("Welches Format? (h) Hochformat, (q) Querformat ").lower()
    if orientation == "h":
        image_size = (a4_size[0], a4_size[1])
    elif orientation == "q":
        image_size = (a4_size[1], a4_size[0])
    else:
        image_size = get_orientation()
    return image_size

def get_scale():
    scale = input("Welchen scale möchtest du? ").lower()
    try:
        scale = float(scale)
    except:
        get_scale()
    return scale

def get_download():
    download = input("Möchtest du das Bild speichern? (j) Ja, (n) Nein ").lower()
    if download == "j":
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        img.save(f"Image/camcarpet_{timestamp}.png")
    elif download == "n":
        print("continue")
    else:
        get_download()

ax2.set_xlim([-total_length/2 - 2.5, total_length/2 + 2.5])
ax2.set_ylim([0, total_length])

ax3.set_xlim([-total_length / 2 - 2.5-(total_length/4), total_length / 2 + 2.5+(total_length/4)])
ax3.set_ylim([0, total_length])

ax.set_xlim([-20, 20])
ax.set_ylim([0, 20])
ax.set_zlim([0, 40])

plt.show()

camcarpet_as_png()
