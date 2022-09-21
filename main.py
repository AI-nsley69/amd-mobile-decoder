import sys

model = str(sys.argv[1])

if (len(model) != 5):
    raise Exception("Invalid Model! Requires 5 characters!")

if (not int(model[:3])):
    raise Exception("Invalid Model! Requires first 4 to be digits")

decode = [
    {
        '1': "Athlon Silver",
        '2': "Athlon Gold",
        '3': "Ryzen 3",
        '4': "Ryzen 3",
        '5': "Ryzen 5",
        '6': "Ryzen 5",
        '7': "Ryzen 7",
        '8': "Ryzen 7/9",
        '9': "Ryzen 9"
    },
    {
        '1': "Zen 1/+",
        '2': "Zen 2",
        '3': "Zen 3/+",
        '4': "Zen 4"
    },
    {
        '0': "Lower model within segment",
        '5': "Upper model within segment"
    },
    {
        'HX': "55W+ (Max Performance)",
        'HS': "~35W+ (Thin Gaming/Creator)",
        'U': "15-28W (Premium Ultrathin)",
        'C': "15-28W (Chromebook)",
        'e': "9W (Fanless U)"
    }
]

titles = ["Portfolio: ", "Market Segment: ", "Architecture: ", "Feature Isolation: ", "Form Factor/TDP: "]

decoded_name = "Model: " + model + "\n";

for i, c in enumerate(model):
    if (i == 0):
        decoded_name += titles[i] + str(int(c) + 2016) + "\n"
    else:
        decoded_name += titles[i] + decode[i-1][c] + "\n"

print(decoded_name)
