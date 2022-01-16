# Reads txt file from the connection; default UTF-8 encoding
## Output: raw txt file content
readMyTextFile   <- function(path) {
  myFile <- readChar(path, 
                     file.info(path)$size, 
                     useBytes = FALSE)

  return(myFile)
}

# Splitter/tokenizer – splits text according to a given regex
## Input: raw text; Output: tokens
tokenizeMyText  <-  function(text, 
                             regex = "[^\\p{L}\\p{N}]+", 
                             makeLower = FALSE) {
  require(stringr)
  tokens   <- unlist(str_split(text, 
                               regex, 
                               simplify = FALSE))
  tokens   <- tokens[tokens != ""]

  if (makeLower) {
    tokens  <-  tolower(tokens)
  }

  return(tokens)
}

# Dataframer – takes a list of values and returns a freq. data frame
## Input: list of values; Output: freq data frame
getFreqDF        <-  function(data) {
  freqDataFrame  <-  data.frame(
                        sort(
                           table(data),
                                decreasing = TRUE),
                                stringsAsFactors = FALSE)

  return(freqDataFrame)
}

# Words-of-frequency finder – retrieves words of a given (n)
# max freq from a data frame
## Input: data frame; Output: words of given frequency (vector)
getWordsWithNFreq <-  function(df, freqColName = "Freq",
                                   wordsColName = "data",
                                   n = 1) {
  if(ncol(df) >= 2){
    wordsWithNFreq  <-  df[which(df[, freqColName] <= n), wordsColName]
    return(as.character(wordsWithNFreq))
  }

  wordsWithNFreq  <-  rownames(df[which(df[, 1] <= n), ])
  return(as.character(wordsWithNFreq))
}

# Splitter – splits tokens into a given number of groups
## Input: (reduced) tokens; Output: list of groups
splitTokens <-  function(tokens, nOfGroups = 2) {
  groups    <-  list()
  nOfGroupMembers  <- floor(length(tokens) / nOfGroups)

  from  <- 1
  to    <-  nOfGroupMembers
  for (i in 1:nOfGroups) {
    currentGroup  <-  tokens[from:to]
    groups[[i]]   <-  currentGroup

    from  <-  sum(lengths(groups)) + 1
    to    <-  from + nOfGroupMembers - 1
  }

  return(groups)
}

# Exports txt file
exportMyText  <- function(x, pathToFile) {
  write.table(x,
              file = pathToFile,
              quote = FALSE,
              row.names = FALSE,
              col.names = FALSE,
              fileEncoding = "UTF-8")
}

# List intersection – finds intersecting values in a list
## Input: list; Output: intersecting values
getListIntersect   <-  function(list) {
  intersectValues  <-  Reduce(intersect, list)

  return(intersectValues)
}

# Stuffs a vector with NAs to a given length
# Use to avoid errors with unequal lengths in cbind()/rbind()
## Input: vector and desired length; Output: NA-stuffed string
stuff     <-  function(vector, maxLength) {
  stuffedVector  <-  append(vector, 
                            rep(NA, 
                                maxLength - length(vector)))

  return(stuffedVector)
}

# Lists all txt files in a directory
## Input: path to directory; Output: files in txt format
listTxtFiles  <-  function(pathToDir) {
  txtFiles    <-  c()

  allFiles      <-  list.files(pathToDir)
  for (file in allFiles) {
    filePath    <-  file.path(pathToDir, file)
    if (!dir.exists(filePath)) {
      txtFiles  <-  append(txtFiles, file)
    }
  }

  return(txtFiles)
}
