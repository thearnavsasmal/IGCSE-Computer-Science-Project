SlabColourChosen = ""
ConstSlabColourOptions = ["grey", "red", "green"]
SlabColourCustom = ""
SlabColourCheck = False
SlabColourCustomCheck = False
SlabDepthChosen = 0
ConstSlabDepthOptions = ["38", "45"]
SlabDepthCheck = False
ConstSlabShapeOptions = ["square", "rectangle", "round"]
SlabShapeChosen = ""
SlabSizeChosen = ""
SlabShapeCheck = False
SlabSizeCheck = False
SingleSlabVolume = 0
TotalSlabVolume = 0
GreySlabPrice = 0
FinalSlabPrice = 0
RequiredSlabCount = 0
RequiredSlabsTotal = 0

print("Please follow the instructions to make the slab that you require")
while True:
    print("Please choose a colour from the following:\nGrey\nRed\nGreen\nCustom")
    SlabColourChosen = input().lower()
    if SlabColourChosen in ConstSlabColourOptions:
        print(f"Slab colour set to {SlabColourChosen}")
        SlabColourCheck = True
        break
    elif SlabColourChosen == "custom":
        print("Please enter your custom colour")
        SlabColourCustom = input().lower()
        print(f"Custom slab colour set to {SlabColourCustom}")
        SlabColourCheck = True
        SlabColourCustomCheck = True
        break
    else:
        print("That is not a valid colour")

while True:
    print("Please choose one of the following depths for your slab (All measurements are in millimeters):\n38\n45")
    SlabDepthChosen = input()
    if SlabDepthChosen in ConstSlabDepthOptions:
        if SlabDepthChosen == "38":
            SlabDepthChosen = 38
            print(f"Slab depth has been set to {SlabDepthChosen}")
            SlabDepthCheck = True
            break
        elif SlabDepthChosen == "45":
            SlabDepthChosen = 45
            print(f"Slab depth has been set to {SlabDepthChosen}")
            SlabDepthCheck = True
            break
    else:
        print("That is not a valid depth")

while True:
    print("Please choose a slab shape from the following options:\nSquare\nRectangle\nRound")
    SlabShapeChosen = input().lower()
    if SlabShapeChosen in ConstSlabShapeOptions:
        if SlabShapeChosen == "square":
            SlabShapeCheck = True
            print("Please choose between one of the following sizes (All measurements are in millimeters):\nPress 'A' for 600x600\nPress 'B' for 450x450")
            SlabSizeChosen = input().lower()
            if SlabSizeChosen == "a":
                SlabSizeChosen = "600x600"
                print("Slab shape set to square\nSlab size set to 600mmx600mm")
                SlabSizeCheck = True
                break
            elif SlabSizeChosen == "b":
                SlabSizeChosen = "450x450"
                print("Slab shape set to square\nSlab size set to 450mmx450mm")
                SlabSizeCheck = True
                break
            else:
                print("That is not a valid size")

        elif SlabShapeChosen == "rectangle":
            SlabShapeCheck = True
            print("Please choose between one of the following sizes (All measurements are in millimeters):\nPress 'A' for 600x700\nPress 'B' for 600x450")
            SlabSizeChosen = input().lower()
            if SlabSizeChosen == "a":
                SlabSizeChosen = "600x700"
                print("Slab shape set to rectangle\nSlab size set to 600mmx700mm")
                SlabSizeCheck = True
                break
            elif SlabSizeChosen == "b":
                SlabSizeChosen = "600x450"
                SlabSizeCheck = True
                print("Slab shape set to rectangle\nSlab size set to 600mmx450mm")
                break
            else:
                print("That is not a valid size")

        elif SlabShapeChosen == "round":
            SlabShapeCheck = True
            print("Please choose between one of the following diameters (All measurements are in millimeters):\nPress 'A' for 300\nPress 'B' for 450")
            SlabSizeChosen = input().lower()
            if SlabSizeChosen == "a":
                SlabSizeChosen = "300"
                print("Slab shape set to round\nSlab diameter set to 300mm")
                SlabSizeCheck = True
                break
            elif SlabSizeChosen == "b":
                SlabSizeChosen = "450"
                print("Slab shape set to round\nSlab diameter set to 450mm")
                SlabSizeCheck = True
                break
            else:
                print("That is not a valid size")
    else:
        print("That is not a valid shape")

if SlabSizeChosen == "600x600":
    SingleSlabVolume = (600*600)*SlabDepthChosen

elif SlabSizeChosen == "450x450":
    SingleSlabVolume = (450*450)*SlabDepthChosen

elif SlabSizeChosen == "600x700":
    SingleSlabVolume = (600*700)*SlabDepthChosen

elif SlabSizeChosen == "600x450":
    SingleSlabVolume = (600*450)*SlabDepthChosen

elif SlabSizeChosen == "300":
    SingleSlabVolume = (3.142*(150**2))*SlabDepthChosen

elif SlabSizeChosen == "450":
    SingleSlabVolume = (3.142*(225**2))*SlabDepthChosen

TotalSlabVolume = SingleSlabVolume*20

if SlabColourChosen == "grey":
    GreySlabPrice = (TotalSlabVolume/100000)*0.05
    FinalSlabPrice = GreySlabPrice
elif SlabColourChosen == "red" or SlabColourChosen == "green":
    GreySlabPrice = ((TotalSlabVolume/100000)*0.05)
    FinalSlabPrice = ((10/100)*GreySlabPrice) + GreySlabPrice
elif SlabColourCustomCheck == True:
    GreySlabPrice = ((TotalSlabVolume/100000)*0.05)
    FinalSlabPrice = 5 + ((15/100)*GreySlabPrice) + GreySlabPrice


if SlabColourCheck == True and SlabDepthCheck == True and SlabShapeCheck == True and SlabSizeCheck == True:
    print(f"The options that you chose are:\nSlab Colour: {SlabColourChosen.capitalize()}\nSlab Depth: {SlabDepthChosen}\nSlab Shape: {SlabShapeChosen.capitalize()}\nSlab Size: {SlabSizeChosen}")
    print(f"The price for 20 slabs of your selection is ${FinalSlabPrice}")



while True:
    print("\nHow many slabs do you require?\nSlabs are only available in batches of 20\nAll orders that are not multiples of 20(1 batch) will be rounded up to the next multiple of 20\nThe minimum order is 20 slabs and the maximum is 100 slabs")
    RequiredSlabs = int(input())

    if int(RequiredSlabs) < 20:
        print("The minimum order of slabs is 20")
        continue
    if int(RequiredSlabs) > 100:
        print("The maximum order of slabs is 100")
        continue
    else:
        if (RequiredSlabs % 20) == 0:
            RequiredSlabsTotal = (FinalSlabPrice/20) * RequiredSlabs
            print(f"Number of Slabs: {RequiredSlabs}\nTotal Price: {RequiredSlabsTotal}")
            break
        else:
            if RequiredSlabs > 20 and RequiredSlabs < 40:
                RequiredSlabs = 40
                print("The number of slabs has been rounded up to 40")

            if RequiredSlabs > 40 and RequiredSlabs < 60:
                RequiredSlabs = 60
                print("The number of slabs has been rounded up to 60")

            if RequiredSlabs > 60 and RequiredSlabs < 80:
                RequiredSlabs = 80
                print("The number of slabs has been rounded up to 40")

            elif RequiredSlabs > 80 and RequiredSlabs < 100:
                RequiredSlabs = 100
                print("The number of slabs has been rounded up to 100")

        RequiredSlabsTotal = (FinalSlabPrice/20) * RequiredSlabs
        print(f"Number of Slabs: {RequiredSlabs}\nTotal Price: {RequiredSlabsTotal}")
        break
