from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

MAX_LENGTH = 300  # limit long EXIF values

def extract_exif(file_path):
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()

        if not exif_data:
            return ["No EXIF data found."]

        output = []
        gps_info = {}

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)

            if tag_name == "GPSInfo":
                for t in value:
                    gps_tag = GPSTAGS.get(t, t)
                    gps_info[gps_tag] = value[t]
            else:
                clean = str(value)
                if isinstance(value, bytes):
                    try:
                        clean = value.decode('utf-8', errors='ignore').strip()
                    except:
                        clean = "<binary data>"
                if len(clean) > MAX_LENGTH:
                    clean = clean[:MAX_LENGTH] + "..."
                output.append(f"{tag_name}: {clean}")

        if gps_info:
            output.append("--- GPS Data ---")
            lat = convert_gps(gps_info.get("GPSLatitude"), gps_info.get("GPSLatitudeRef"))
            lon = convert_gps(gps_info.get("GPSLongitude"), gps_info.get("GPSLongitudeRef"))
            if lat and lon:
                output.append(f"Latitude: {lat}")
                output.append(f"Longitude: {lon}")
                output.append(f"Google Maps: https://maps.google.com/?q={lat},{lon}")

        return output

    except Exception as e:
        return [f"Error reading EXIF data: {e}"]

def convert_gps(value, ref):
    if not value or not ref:
        return None
    try:
        d, m, s = value
        decimal = float(d) + float(m) / 60 + float(s) / 3600
        if ref in ['S', 'W']:
            decimal = -decimal
        return round(decimal, 6)
    except:
        return None
