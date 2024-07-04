from exif import Image


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def read_image_location(image_path):
    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            lat_decimal = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
            lon_decimal = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
            coords = (lat_decimal, lon_decimal)
        except AttributeError:
            print ('No Coordinates')
    else:
        print ('The Image has no EXIF information')
        
    print(f"Lat/Lon: ({coords[0]:.4f}) / ({coords[1]:.4f})")

        
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
