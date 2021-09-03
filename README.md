# pixelamas

Pixelama is a Python-based tool that allows users to generate pixelated art using the Turtle library.

![Generated](https://github.com/shahnami/lame-lamas/blob/main/assets/collections/demo.svg?raw=true)

## Create your own

To create your own `ArtWork`, simply create your own configuration file within the `/configs` folder.
An example `ArtWork` is available under `/configs/llama.json` for inspiration.

1. Create a new configuration file, or copy the example file and rename it to what is suitable.

The configuration file must contain certain keys. A description of a new configuration for a `Monkey` class is provided below:

```
{
  "class": "Monkey", // This is the name of the class of your art, which is a subclass of ArtWork
  "assets": "assets/artwork/monkey/", // This is the path to the assets for your class, and needs to be created
  "configuration": {
    "rows": 37, // This is the recommended number of rows for your grid
    "cols": 37, // This is the recommended number of columns for your grid
    "pixel_size": 22, // This is the recommended pixel size
    "pen_size": 1, // This is the recommended pen size
    "primary": ["#FFFFFF"], // This is not used at the moment
    "secondary": ["#000000"], // This is not used at the moment
    "background": ["#000000", "red", "white", "#FF0000"], // List of colours to randomise from
    "properties": {
      "skin": { // Name of your first property, can be anything you want.
        "default": { // Recommended to have a default which basically stands for "none"
          "asset": "assets/artwork/monkey/skins/default.txt", // This can be empty if needs to draw nothing
          "odds": 0.85, // This is the odd of having the Default Skin property
          "layer": 0, // Each property is drawn layer by layer, starting from 0, as to not overlap unexpectedly
          "palette": { // Each property must have a palette definition
            "primary": { // You can name this anything you want
              "pixel": 1, // This is the pixel value on your grid. If the pixel is 1, it will draw whichever hex value is defined below
              "hex": ["#FFFFFF"] // This is the colour Turtle will draw when it detects a pixel value of 1
            },
            "secondary": { // You can name this anything you want, and is optional
              "pixel": 2,
              "hex": ["#EEEEEE"]
            },
            "tertiery": { // You can name this anything you want, and is optional
              "pixel": 3,
              "hex": ["#000000"]
            }
          }
        },
        "black": {
          "asset": "assets/artwork/monkey/skins/black.txt",
          "odds": 0.14,
          "layer": 0,
          "palette": {
            "primary": {
              "pixel": 1,
              "hex": ["#b2b2b2"]
            },
            "secondary": {
              "pixel": 2,
              "hex": ["#8E8E8E"]
            },
            "tertiery": {
              "pixel": 3,
              "hex": ["#000000"]
            }
          }
        }
      },
      "hat": {
        "default": {
          "asset": "",
          "odds": 0.95,
          "layer": 2,
          "palette": {
            "primary": {
              "pixel": 1,
              "hex": ["#FFFFFF"]
            }
          }
        },
        "homburg": {
          "asset": "assets/artwork/monkey/hats/homburg.txt",
          "odds": 0.05,
          "layer": 2,
          "palette": {
            "primary": {
              "pixel": 1,
              "hex": ["#000000", "#C19A6B", "#342415"]
            }
          }
        }
      },
      "optic": {
        "default": {
          "asset": "",
          "odds": 0.85,
          "layer": 4,
          "palette": {
            "primary": {
              "pixel": 1,
              "hex": ["#000000"]
            }
          }
        },
        "cool": {
          "asset": "assets/artwork/monkey/optics/cool.txt",
          "odds": 0.15,
          "layer": 4,
          "palette": {
            "primary": {
              "pixel": 1,
              "hex": ["#144EA9"]
            }
          }
        }
      }
    }
  }
}

```

2. Make sure to create a subclass of `ArtWork` in the `/models/artworks/` folder and add the import into `__init__.py`. This class should be the same as your configuration `class` value. In its most minimalistic form, the class would look as follows:

```
# /models/artworks/monkey.py

from models.artist import Artist
from models.artworks import ArtWork
from models.properties import Properties, Property


class Monkey(ArtWork): <---- name of class value from the configuration file

    def __init__(self, *, artist: Artist, properties: Properties):
        ArtWork.__init__(self, artist=artist, properties=properties)

```

```
# /models/artworks/__init__.py

from .artwork import ArtWork
from .llama import Llama
from .monkey import Monkey <----
```

3. Create the assets within the `/assets/artwork/monkey/` folder. Make sure to have the correct paths as defined in the configuration file.

4. An asset is draw by changing values in the grid of a a text file. This grid consists of 37 rows and columns. Each 0 is ignored, and each pixel value > 0 is drawn by the script. Whichever colour is drawn is defined in the configuration file under "pixel" and "hex".

```
0000000000000000000000000000000000000
0000000000000011000001100000000000000
0000000000000011000001100000000000000
0000000000000021000001200000000000000
0000000000000021000001200000000000000
0000000000000011111111100000000000000
0000000000000013111113100000000000000
0000000000000011133311100000000000000
0000000000000011133311100000000000000
0000000000000021113111200000000000000
0000000000000022111112200000000000000
0000000000000022222222200000000000000
0000000000000012222222100000000000000
0000000000000011222221100000000000000
0000000000000021122211200000000000000
0000000000000022112112200000000000000
0000000000000022211122200000000000000
0000000000000022211122200000000000000
0000000000000022221222200000000000000
0000000000000022222222200001120000000
0000000000000012222222111100112000000
0000000000000011222221111110112000000
0000000000000011122211111111120000000
0000000000000011112111111111100000000
0000000000000011111111111111100000000
0000000000000011111111111111100000000
0000000000000011111111111111000000000
0000000000000011111111111111000000000
0000000000000011111111111111000000000
0000000000000011111111111111000000000
0000000000000001100001120110000000000
0000000000000001100001120110000000000
0000000000000001100001120110000000000
0000000000000001100001130110000000000
0000000000000003300003300330000000000
0000000000000000000000000000000000000
0000000000000000000000000000000000000
```

5. The script will read each line sequentially from top to bottom, left to right. The above is an example of the entire art work. To add properties such as a optics, you will not be required to draw every column, simply the columns up until the property is fully drawn. For example, to draw optics on the llama above, the following text file is sufficient, as the skin is on layer 0, and the optics on layer 4, the skin will be drawn first, and the optics will overwrite any non-zero pixel value after.

```
0000000000000000000000000000000000000
0000000000000000000000000000000000000
0000000000000000000000000000000000000
0000000000000000000000000000000000000
0000000000000000000000000000000000000
0000000000000001111111000000000000000
0000000000000001100011000000000000000
```

6. If you decide to run a non-demo version, the image hashes will be stored in `/assets/hashes/hashes.txt` as to ensure each image is unique. If a hash exists, it will skip the generation of the image. To generate the images, you have the following options.

- `python3 main.py -c PATH_TO_CONFIGURATION_FILE` - runs the program for a given configuration
- `python3 main.py -c PATH_TO_CONFIGURATION_FILE -d` - runs a demo version which does not store the hash
- `python3 main.py -c PATH_TO_CONFIGURATION_FILE -o IMAGE_NAME` - saves the output under `/assets/collections/IMAGE_NAME`
