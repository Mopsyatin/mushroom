from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from names import shampinion, lisichka, opyata, gruzd,borowik, podberez, podocin, ruzhik, satana,suroezka,maslenok,mizena,muhomor,pautinic,poganka,lepiota,lozhlisichka,lozhopenek,galerina,zhelchi

def Mushroom(image_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("image_path").convert("RGB")

    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    if class_name == "шампиньон":
        text = shampinion

    elif class_name == "лисичка обыкновенная":
        text = lisichka

    elif class_name == "опята": 
        text = opyata

    elif class_name == "груздь":
        text = gruzd

    elif class_name == "белый гриб (боровик)":
        text = borowik

    elif class_name == "подберёзовик":
        text = podberez

    elif class_name == "подосиновик":
        text = podocin

    elif class_name == "рыжик":
        text = ruzhik

    elif class_name == "сыроежка":
        text = suroezka

    elif class_name == "маслёнок":
        text = maslenok

    elif class_name == "мухомор":
        text = muhomor

    elif class_name == "бледная поганка":
        text = poganka

    elif class_name == "сатанинский гриб":
        text = satana

    elif class_name == "лепиота коричнево-красная":
        text = lepiota
    elif class_name == "галерина окаймлённая":
        text = galerina

    elif class_name == "паутинник красивейший":
        text = pautinic

    elif class_name == "желчный гриб":
        text = zhelchi

    elif class_name == "ложная лисичка":
        text = lozhlisichka

    elif class_name == "ложный опёнок":
        text = lozhopenek

    elif class_name == "мицена":
        text = mizena


    # Print prediction and confidence score
    print('''Памятка:
- собирать грибы следует вдали от дорог, магистралей, вне населенных мест, в экологически чистых районах. Собирать грибы лучше с восходом солнца, по росе;

— для сохранения свежести грибов необходимо собирать их в плетеную ивовую корзину. Не рекомендуется собирать в ведра, полиэтиленовые пакеты или мешки, так как в них нет доступа воздуха. Кроме того, в полиэтиленовых емкостях повышается температура, что приводит к порче грибов;

— нельзя собирать старые, переросшие, червивые и неизвестные грибы. Во время сбора нельзя пробовать грибы: употреблять их следует только после соответствующей термической обработки;

— нельзя брать грибы, имеющие утолщения у основания ножки. Чтобы не ошибиться в выборе грибов, необходимо их срезать с целой ножкой, чтобы дома еще раз проверить.;

— нельзя забывать, что некоторые съедобные грибы (опенок осенний, сыроежка) имеют ядовитых двойников.
          
- наше приложение точно не на сто  процентов и мы не несем ни какой ответственности за предоставленную информацию''')
    print("======================================================================================================================================================================================================================================================================================")
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    print("======================================================================================================================================================================================================================================================================================")
    print(text)