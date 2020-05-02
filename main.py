dataLength = sum(1 for line in open('iris.data'))
allLines = []
classThreshold = [
    [
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ],
    [
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ],
    [
        [0,0],
        [0,0],
        [0,0],
        [0,0]
    ]
]
DataChange = [0,0,0]

with open('iris.data') as IRIS_DATA:
    lineNumber = 0
    while lineNumber < dataLength:
        ActualLine = IRIS_DATA.readline()
        ActualLineCleared = ActualLine.replace('\n','')
        ActualLine_inList = ActualLineCleared.split(",")

        ATTR_sepalLength = ActualLine_inList[0]
        ATTR_sepalWidth = ActualLine_inList[1]
        ATTR_petalLength = ActualLine_inList[2]
        ATTR_petalWidth = ActualLine_inList[3]
        ATTR_class = ActualLine_inList[4]
        ATTR_classINDEX = 0
        if ATTR_class == 'Iris-setosa':
            ATTR_classINDEX = 0
        elif ATTR_class == 'Iris-versicolor':
            ATTR_classINDEX = 1
        elif ATTR_class == 'Iris-virginica':
            ATTR_classINDEX = 2
        
        if DataChange[ATTR_classINDEX] == 0:
            classThreshold[ATTR_classINDEX][0] = [ATTR_sepalLength,ATTR_sepalLength]
            classThreshold[ATTR_classINDEX][1] = [ATTR_sepalWidth,ATTR_sepalWidth]
            classThreshold[ATTR_classINDEX][2] = [ATTR_petalLength,ATTR_petalLength]
            classThreshold[ATTR_classINDEX][3] = [ATTR_petalWidth,ATTR_petalWidth]
            DataChange[ATTR_classINDEX] = 1
        else:
            if classThreshold[ATTR_classINDEX][0][0] > ATTR_sepalLength:
                classThreshold[ATTR_classINDEX][0][0] = ATTR_sepalLength 
            if classThreshold[ATTR_classINDEX][0][1] < ATTR_sepalLength:
                classThreshold[ATTR_classINDEX][0][1] = ATTR_sepalLength 

            if classThreshold[ATTR_classINDEX][1][0] > ATTR_sepalWidth:
                classThreshold[ATTR_classINDEX][1][0] = ATTR_sepalWidth 
            if classThreshold[ATTR_classINDEX][1][1] < ATTR_sepalWidth:
                classThreshold[ATTR_classINDEX][1][1] = ATTR_sepalWidth 

            if classThreshold[ATTR_classINDEX][2][0] > ATTR_petalLength:
                classThreshold[ATTR_classINDEX][2][0] = ATTR_petalLength 
            if classThreshold[ATTR_classINDEX][2][1] < ATTR_petalLength:
                classThreshold[ATTR_classINDEX][2][1] = ATTR_petalLength 

            if classThreshold[ATTR_classINDEX][3][0] > ATTR_petalWidth:
                classThreshold[ATTR_classINDEX][3][0] = ATTR_petalWidth 
            if classThreshold[ATTR_classINDEX][3][1] < ATTR_petalWidth:
                classThreshold[ATTR_classINDEX][3][1] = ATTR_petalWidth       

        allLines.append(ActualLine_inList)
        lineNumber += 1  

for Treshold in classThreshold:
    print(Treshold)