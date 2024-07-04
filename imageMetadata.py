from PIL import Image

def read_image_location(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img._getexif()
            # print(metadata)
            if metadata:
                print("Metadata found:")
                for tag, value in metadata.items():
                    print(tag, "-> ", value)
                    # tag_name = TAGS.get(tag, tag)
                    # print(f"{tag_name}: {value}")
            else:
                print("No metadata found.")
    except Exception as e:
        print(f"Error: {e}")
        
def read_image_pgp(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img._getexif()
            # print(metadata)
            if metadata:
                print("Metadata found:")
                for tag, value in metadata.items():
                    print(tag, "-> ", value)
                    # tag_name = TAGS.get(tag, tag)
                    # print(f"{tag_name}: {value}")
            else:
                print("No metadata found.")
    except Exception as e:
        print(f"Error: {e}")
