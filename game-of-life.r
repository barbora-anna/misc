isDead  <-    function(matrixOriginal, x, y) {
    NA %in% matrixOriginal[x, y]
}

howManyNeighbours   <-  function(matrixOriginal, x, y) {
    aliveCount  <-  0
    for (i in (-1):(1)){
        for (j in (-1):(1)) {
            if (i == 0 && j == 0)                next
            if (x + i < 1)                       next
            if (y + j < 1)                       next
            if (x + i > nrow(matrixOriginal))    next
            if (y + j > ncol(matrixOriginal))    next

            isdead  <-  isDead(matrixOriginal, x + i, y + j)

            if (isdead == FALSE) {
                aliveCount  <-  aliveCount + 1
            }
        }
    }

    return(aliveCount)
}

killCell    <-  function(matrixNew, x, y) {
    matrixNew[x,y]  <-  NA

    return(matrixNew)
}

birthCell   <-  function(matrixNew, x, y) {
    matrixNew[x, y]  <-  1

    return(matrixNew)
}

surviveCell <-  function(matrixOriginal, matrixNew, x, y) {
    matrixNew[x, y]  <- matrixOriginal[x, y] + 1

    return(matrixNew)
}

createNewMatrix <-  function(matrixOriginal) {
    matrixNew   <-  matrix( NA,
                            nrow = nrow(matrixOriginal),
                            ncol = ncol(matrixOriginal))
    return(matrixNew)
}

################################### LOOP

matrixWorldInception <- function(ncol, nrow, numberOfCells) {
    matrixOriginal   <-  matrix(NA, ncol, nrow)

    for (cell in 1:numberOfCells) {
        matrixOriginal  <-  birthCell(matrixOriginal, 
                                      sample(1:nrow, 1), 
                                      sample(1:ncol, 1)) 
    }

    return(matrixOriginal)
}

makeGeneration  <-  function(matrixOriginal) {
    matrixNew   <-  createNewMatrix(matrixOriginal)

    for (x in 1:nrow(matrixOriginal)) {
        for(y in 1:ncol(matrixOriginal)) {
            numberOfNeighbours  <-  howManyNeighbours(matrixOriginal, x, y)

            if (isDead(matrixOriginal, x, y) == FALSE) {
                if (numberOfNeighbours < 2) {
                    matrixNew   <-  killCell(matrixNew, x, y)
                }
                if (numberOfNeighbours == 2 || numberOfNeighbours == 3) {
                    matrixNew   <-  surviveCell(matrixOriginal, matrixNew, x, y)
                }
                if(numberOfNeighbours > 3) {
                    matrixNew   <-  killCell(matrixNew, x, y)
                }
            } else { 
                if(numberOfNeighbours == 3) {
                    matrixNew   <-  birthCell(matrixNew, x, y)
                }
            }
        }
    }

    return(matrixNew)
}

viewWorld   <-  function(matrix) {
    image(t(matrix), col = hcl.colors(30, "Purple-Yellow"))
    Sys.sleep(0.15)
    cat("living...")
}

comeAlive   <-  function(worldNcol, worldNrow, numberOfCells) {
    world   <-  matrixWorldInception(worldNcol, worldNrow, numberOfCells)

    while(TRUE) {
        viewWorld(world)
        world    <-  makeGeneration(world)
    }
}

settingsWorldNcol   = 15
settingsWorldNrow   = 15
settingsWorldNcells = 50

comeAlive(settingsWorldNcol, settingsWorldNrow, settingsWorldNcells)

# 80, 80, 900 work nice 
