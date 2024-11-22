public_toilet = 'PB'

def home():
    private_toilet = 'PT'
    print(private_toilet)
    public_toilet = 'LPB'  # local variables have more preference as compare to public variables
    print(public_toilet)

home()