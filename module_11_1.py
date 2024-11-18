# import multiprocessing as mp
# from PIL import Image
#
#
# def resize_image(image_paths, queue):
#     for image_path in image_paths:
#         image = Image.open(image_path)
#         image = image.resize((800, 600))
#         queue.put((image_path, image))
#
#
# def change_color(queue):
#     while True:
#         image_path, image = queue.get()
#         if image_path is None:  # Проверка на завершение
#             break
#         image = image.convert('L')
#         image.save(image_path)
#
#
# if __name__ == '__main__':
#     data = []
#     queue = mp.Queue()
#
#     for image in range(1, 10):
#         data.append(f'./img_{image}.jpg')
#
#
#     resize_process = mp.Process(target=resize_image, args=(data, queue))
#     change_process = mp.Process(target=change_color, args=(queue,))
#     resize_process.start()
#     change_process.start()
#     resize_process.join()
#
#     # Завершение процесса изменения цвета
#     queue.put((None, None))
#     change_process.join()

import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)

# from PIL import Image, TarIO
#
# fp = TarIO.TarIO("hopper.tar", "hopper.jpg")
# im = Image.open(fp)
