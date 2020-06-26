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
GreyConcreteCost = 0

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

while True:
    try:
        print("The cost of concrete is variable")
        print("Please enter the cost of 100000 millimeters cubed of grey concrete in dollars")
        GreyConcreteCost = float(input())
        break
    except:
        print("That is not a valid cost")
print(f"Grey concrete cost set to ${GreyConcreteCost}")

while True:
    print("Choose one of the following grades of concrete\n'A' for Basic\n'B' for Best")
    SlabGradeChosen = input().lower()
    if SlabGradeChosen == "a":
        SlabGradeChosen = "basic"
        print(f"Concrete grade set to: Basic")
        break
    elif SlabGradeChosen == "b":
        SlabGradeChosen = "best"
        print(f"Concrete grade set to: Best")
        break
    else:
        print("That is not a valid concrete grade")

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

if SlabGradeChosen == "basic":
    if SlabColourChosen == "grey":
        GreySlabPrice = (TotalSlabVolume/100000)*GreyConcreteCost
        FinalSlabPrice = GreySlabPrice
    elif SlabColourChosen == "red" or SlabColourChosen == "green":
        GreySlabPrice = ((TotalSlabVolume/100000)*GreyConcreteCost)
        FinalSlabPrice = ((10/100)*GreySlabPrice) + GreySlabPrice
    elif SlabColourCustomCheck == True:
        GreySlabPrice = ((TotalSlabVolume/100000)*GreyConcreteCost)
        FinalSlabPrice = 5 + ((15/100)*GreySlabPrice) + GreySlabPrice

elif SlabGradeChosen == "best":
    if SlabColourChosen == "grey":
        GreySlabPrice = (TotalSlabVolume/100000)*GreyConcreteCost
        FinalSlabPrice = ((7/100)*GreySlabPrice) + GreySlabPrice
    elif SlabColourChosen == "red" or SlabColourChosen == "green":
        GreySlabPrice = ((TotalSlabVolume/100000)*GreyConcreteCost)
        FinalSlabPrice = ((10/100)*GreySlabPrice) + GreySlabPrice
        FinalSlabPrice = ((7/100)*FinalSlabPrice) + FinalSlabPrice
    elif SlabColourCustomCheck == True:
        GreySlabPrice = ((TotalSlabVolume/100000)*GreyConcreteCost)
        FinalSlabPrice = 5 + ((15/100)*GreySlabPrice) + GreySlabPrice
        FinalSlabPrice = ((7/100)*FinalSlabPrice) + FinalSlabPrice

FinalSlabPrice = str(round(FinalSlabPrice, 2))

if SlabColourCheck == True and SlabDepthCheck == True and SlabShapeCheck == True and SlabSizeCheck == True:
    print(f"The options that you chose are:\nSlab Colour: {SlabColourChosen.capitalize()}\nSlab Depth: {SlabDepthChosen}\nSlab Shape: {SlabShapeChosen.capitalize()}\nSlab Size: {SlabSizeChosen}\nGrey Concrete Price: {GreyConcreteCost}\nSlab Grade = ")
    print(f"The price for your selection is ${FinalSlabPrice}")
