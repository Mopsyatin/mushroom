from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import colorama
from names import shampinion, lisichka, opyata, gruzd,borowik, podberez, podocin, ruzhik, satana,suroezka,maslenok,mizena,muhomor,pautinic,poganka,lepiota,lozhlisichka,lozhopenek,galerina,zhelchi

def Mushroom(image_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r", encoding="utf8").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image_path).convert("RGB")

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


    if class_name == class_names[0]:
        text = shampinion
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[1]:
        text = lisichka
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[2]: 
        text = opyata
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[3]:
        text = gruzd
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[4]:
        text = borowik
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[5]:
        text = podberez
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[6]:
        text = podocin
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[7]:
        text = ruzhik
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[8]:
        text = suroezka
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[9]:
        text = maslenok
        eat = 'СЪЕДОБНЫЙ'

    elif class_name == class_names[10]:
        text = muhomor
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[11]:
        text = poganka
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[12]:
        text = satana
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[13]:
        text = lepiota
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[14]:
        text = galerina
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[15]:
        text = pautinic
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[16]:
        text = zhelchi
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[17]:
        text = lozhlisichka
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[18]:
        text = lozhopenek
        eat = 'НЕ СЪЕДОБНЫЙ'

    elif class_name == class_names[19]:
        text = mizena
        eat = 'НЕ СЪЕДОБНЫЙ'


    # Print prediction and confidence score
    print('=============')
    print(colorama.Back.RED, 'ПАМЯТКА!!!:', colorama.Style.RESET_ALL)
    print('=============')
    print(colorama.Fore.BLACK)
    print(colorama.Back.WHITE + '''
- собирать грибы следует вдали от дорог, магистралей, вне населенных мест, в экологически чистых районах. Собирать грибы лучше с восходом солнца, по росе;

— для сохранения свежести грибов необходимо собирать их в плетеную ивовую корзину. Не рекомендуется собирать в ведра, полиэтиленовые пакеты или мешки, так как в них нет доступа воздуха. Кроме того, в полиэтиленовых емкостях повышается температура, что приводит к порче грибов;

— нельзя собирать старые, переросшие, червивые и неизвестные грибы. Во время сбора нельзя пробовать грибы: употреблять их следует только после соответствующей термической обработки;

— нельзя брать грибы, имеющие утолщения у основания ножки. Чтобы не ошибиться в выборе грибов, необходимо их срезать с целой ножкой, чтобы дома еще раз проверить.;

— нельзя забывать, что некоторые съедобные грибы (опенок осенний, сыроежка) имеют ядовитых двойников.
          
- наше приложение точно не на сто  процентов и мы не несем ни какой ответственности за предоставленную информацию''')
    print(colorama.Style.RESET_ALL)
    if eat == 'НЕ СЪЕДОБНЫЙ':
        print("=====================")
        print(colorama.Back.RED, 'ВАШ ГРИБ:', eat, colorama.Style.RESET_ALL)
        print("=====================")
        print("============================================================================================================")
        print(colorama.Back.WHITE, "Вид:", colorama.Back.RED, class_name[2:], end="", )
        print(colorama.Style.RESET_ALL)
        print(colorama.Back.WHITE, "Вероятность совпадения:", colorama.Back.RED, confidence_score, colorama.Style.RESET_ALL)
        print("============================================================================================================")
        print('================')
        print(colorama.Back.CYAN, 'ЭТО ИНТЕРЕСНО!', colorama.Style.RESET_ALL)
        print('================')
        print(colorama.Back.RED, text, colorama.Style.RESET_ALL)
    elif eat == 'СЪЕДОБНЫЙ':
        print("=====================")
        print(colorama.Back.LIGHTGREEN_EX, 'ВАШ ГРИБ:', eat, colorama.Style.RESET_ALL)
        print("=====================")
        print("============================================================================================================")
        print(colorama.Back.WHITE, "Вид:", colorama.Back.LIGHTGREEN_EX, class_name[2:], end="", )
        print(colorama.Style.RESET_ALL)
        print(colorama.Back.WHITE, "Вероятность совпадения:", colorama.Back.LIGHTGREEN_EX, confidence_score, colorama.Style.RESET_ALL)
        print("============================================================================================================")
        print('================')
        print(colorama.Back.CYAN, 'ЭТО ИНТЕРЕСНО!', colorama.Style.RESET_ALL)
        print('================')
        print(colorama.Back.LIGHTGREEN_EX, text, colorama.Style.RESET_ALL)