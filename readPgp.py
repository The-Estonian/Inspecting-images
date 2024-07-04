

def read_image_pgp(image_path):
    with open(image_path, "rb") as file:
        datastream = file.read()
        print(datastream[datastream.find(b"-----BEGIN PGP PUBLIC KEY BLOCK-----"):-5].decode("utf-8"))
