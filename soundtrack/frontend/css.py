
import base64
def get_css():
    with open('p6ucplA.jpeg', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    [class="css-ocqkz7 e1tzin5v4"]
        .css-1kyxreq {{
            display: flex;
            flex-flow: row wrap;
            row-gap: 1rem;
            justify-content: center !important;
        }}

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 {{
        background-color: #ffffff;
        color: #ffffff;
    }}

    </style>
    """
