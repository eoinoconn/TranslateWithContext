from PIL import Image
from transformers import pipeline

def classify(input, model="default"):
    """
    Method to classify input image
    """
    if model == "default":
        # Default transformers classifier. Assigns labels from imagenet 1000.
        classifier = pipeline(task="image-classification", device="cpu")
        return classifier(input)[0]
    else:
        raise NotImplementedError(f"Model {model} not implemented.")


image = Image.open("./docs/images/test_img.jpg")
print(classify(image))