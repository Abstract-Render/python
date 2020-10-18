from math import ceil , pi
courseLengthYd=(float(input("Enter the course length")))
courseWidthYd = (float(input("Enter the course width")))
courseLengthft = courseLengthYd*3
courseWidthft = courseWidthYd*3

def calculateGreenAreas(Width):
     return ((((Width/2)/2)**2)*pi)*2
def calculateSandtrapVolume(Width):
    return (((((Width)/3)/2)**2)*1*pi)
def calculateTonsofSand(Width):
    return (calculateSandtrapVolume(courseWidthft)*100)/2000
def calculateBricks(widthFt):
    return (courseWidthft/3*pi)/2*3
def calculateBushes(widthFt):
    return ((2*courseWidthYd+2*courseLengthYd))-2
def calculateRoughsod(length,width):
    return (length*width) - calculateGreenAreas(courseWidthYd)-((((courseWidthYd/3)/2)**2)*pi)
def calculateMowingtimeMin(Yd):
    return (ceil((.5*calculateRoughsod(courseLengthYd,courseWidthYd)+1*calculateGreenAreas(courseWidthYd))/60))
print("Total square yards of rough sod: " + str(ceil(calculateRoughsod(courseLengthYd,courseWidthYd))))
print()
print("Total square yards of smooth sod: " + str(ceil(calculateGreenAreas(courseWidthYd))))
print("Tons of sand: " + str(ceil(calculateTonsofSand(courseWidthft))))
print("Number of retaining wall bricks: " + str(ceil(calculateBricks(courseWidthft))))
print("Number of bushes: " + str(ceil(calculateBushes(courseWidthft))))
print("Total Mowing Time (mins): " + str(ceil(calculateMowingtimeMin(courseWidthYd))))

